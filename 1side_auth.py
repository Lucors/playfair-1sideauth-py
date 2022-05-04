import sys
from playfair	import PlayfairCipher
from random 	import randint

# GUI
from PySide2.QtWidgets 	import QApplication, QWidget
from ui_control 		import Ui_ControlWidget
from ui_side 			import Ui_SideWidget


# Перемнная приложения
app = QApplication(sys.argv)
# Переменная виджета контроля 
cw = None
# Список всех сторон общения
sides = []


# Функции работы со списком сторон
def deleteSide(value_id):
	for i in range(len(sides)):
		if (sides[i].getID() == value_id):
			sides.pop(i)
			callSidesUpdates()
			return True
	return False

def addSide(side):
	if (len(sides) > 0):
		side.setID(sides[-1].getID()+1)
	sides.append(side)
	callSidesUpdates()
	side.show()

def callSidesUpdates():
	for i in range(len(sides)):
		sides[i].updateSidesCombo()
	cw.updateSidesList()

def sidesAsString():
	output = ""
	for i in range(len(sides)):
		if (i % 4 == 0):
			output += "\n"
		output += f"[{sides[i].getName()} #{sides[i].getID()}] " 
	return output


# Класс стороны общения
class SideWidget(QWidget, Ui_SideWidget):
	def __init__(self, name):
		super(SideWidget, self).__init__()
		self.setupUi(self)

		self.id = 0
		self.random = 0
		self.name_lbl.setText(name)
		self.pc = PlayfairCipher()
		self.key_apply_btn.clicked.connect(self.applyKeyword)
		self.auth_btn.clicked.connect(self.auth)

	def getName(self):
		return self.name_lbl.text()

	def getID(self):
		return self.id

	def getRandom(self):
		return int(self.rnd_value.text())

	def setID(self, value_id):
		self.id = value_id

	def setRandom(self):
		self.rnd_value.setText(str(randint(0, 999)))
		self.log(f"Задано случ. число: {self.rnd_value.text()}")

	def applyKeyword(self):
		if (not self.key_value.text()):
			return
		self.pc.setKeyword(self.key_value.text())
		self.log("Установлен новый ключ", True)

	def updateSidesCombo(self):
		self.sides_combo.clear()
		for side in sides:
			if (side.getID() == self.id):
				self.sides_combo.addItem("Текущий")
			else:
				self.sides_combo.addItem(f"{side.getName()} #{side.getID()}")
		self.log("Обновлен список сторон", True)

	def closeEvent(self, event):
		deleteSide(self.id)

	def log(self, txt, clear=False):
		if (not clear):
			txt = f"{self.log_lbl.text()}\n{txt}"
		self.log_lbl.setText(txt)

	def receive(self, rnd):
		self.log(f"Получен запрос сессии. r={rnd}", True)
		feedback = self.pc.encode(f"{rnd}{self.getName()}")
		self.log(f"Отвечаю: {feedback}")
		return feedback

	def auth(self):
		index_side = self.sides_combo.currentIndex()
		self.log(f"Установка сеанса с id = {index_side}", True)
		if (index_side > len(sides)):
			return self.log("Ошибка. Неверный index_side")
		side = sides[index_side]
		if (side.getID() == self.id):
			return self.log("Ошибка. Невалидная сторона")
		self.setRandom()

		self.log("Отправляю случ. число r")
		feedback = side.receive(self.getRandom())

		self.log(f"Получен ответ: {feedback}")
		feedback = self.pc.decode(feedback)
		self.log(f"Расшифр: {feedback}")
		feedback_rnd = ""
		feedback_name = ""
		for ch in feedback:
			if (ch.isdigit()):
				feedback_rnd += ch
			else:
				feedback_name += ch

		if (side.getName().upper() != feedback_name):
			return self.log("Ошибка. Имя не совпадает")
		if (self.getRandom() != int(feedback_rnd)):
			return self.log("Ошибка. Случ. число не совпадает")
		self.log("Успех!")


# Класс генератора сторон общения 
class ControlWidget(QWidget, Ui_ControlWidget):
	def __init__(self):
		super(ControlWidget, self).__init__()
		self.setupUi(self)

		self.add_side_btn.clicked.connect(self.addSide)

	def addSide(self):
		if (not self.side_name_editor.text()):
			return
		side = SideWidget(self.side_name_editor.text())
		addSide(side)

	def updateSidesList(self):
		self.sides_list.setText(sidesAsString())


cw = ControlWidget()
cw.show()
app.exec_()