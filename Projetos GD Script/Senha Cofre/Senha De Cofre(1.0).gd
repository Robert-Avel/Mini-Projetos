extends ColorRect

var password:String = "123"
var counter:int = 0
@onready var screen:Label = $"password/password number"
@onready var numbers:ColorRect = $numbers
@onready var delt_button:Button = $Delt/Button
@onready var enter_button:Button = $Enter/EnterButton

func _ready():
	for display in numbers.get_children():
		var button = display.get_child(1)
		#envia button como argumento para a função _number_pressed
		button.pressed.connect(_number_pressed.bind(button))
	delt_button.pressed.connect(_delt_pressed)
	enter_button.pressed.connect(_enter_pressed)
func _enter_pressed():
	if password != screen.text:
		screen.text = "Wrong"
		#get_tree() pega o tempo do jogo
		#create_timer cria um timer de 3 segundos e após isso da timeout
		await get_tree().create_timer(3.0).timeout
		screen.text = ""
		counter = 0
	else:
		screen.text = "Finish"
		await get_tree().create_timer(3.0).timeout
		$"../ColorRect".visible = true
func _delt_pressed():
	counter -= 1
	# acreen.text vai ser igual a ela mesma menos o ultimo indice
	#o substr vai subtrair o texto dede o inicio dele q é 0 até o maximo de caracteres
	#e vai subtrair apenas 1
	screen.text = screen.text.substr(0,screen.text.length()-1)
func _number_pressed(button):
	if counter < 7:
		var char_numbers = len(button.name)
		screen.text += str(button.name)[char_numbers-1]
		counter += 1