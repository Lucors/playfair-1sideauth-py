# Класс Шифровалишика по алгоритму Плейфейера
class PlayfairCipher():
	# Инициализатор класса шифровальщика Плейфейера
	def __init__(self, keyword="WATSON"):
		# Полный ключ шифрования (измененный алфавит)
		self.key 		= "" 
		# Ключ. слово для задания self.key (WATSON по умолч.)
		self.keyword 	= keyword
		# Алфавит шифрования
		self.alphabet 	= ("1234567890 "
							"ABCDEFGHIJKLMNOPQRSTUVWXYZ"
							"АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ")
		 # Кол.во строк матрицы шифрования
		self.rows 		= 7
		 # Кол.во столбцов
		self.columns 	= int(len(self.alphabet) / self.rows)
		self.setKeyword(self.keyword);

	# Метод возврата ключа (в виде матрицы)
	def getKey(self):
		return self.key

	# Метод возврата ключа
	def getKeyword(self):
		return self.keyword

	# Метод установки нового ключа
	def setKeyword(self, keyword):
		# Нужно привести ключ к ВЕРХНЕМУ регистру
		self.keyword = keyword.upper()
		prekey       = self.keyword + self.alphabet
		self.key     = ""

		# Нужно удалить все буквы повторяющиеся
		# и добавить все буквы алфавита, которых
		# еще не было в ключе
		for ch in prekey:
			if (ch in self.key):
				continue
			if (ch in self.alphabet):
				self.key += ch
		return self.key

	# Метод шифровки любой строки rawinput
	def encode(self, rawinput):
		# Приводим строку к верхн. регистру
		# и удаляем пробелы в начале и конце
		rawinput = rawinput.upper().strip()

		# Удаляем все буквы не из алфавита
		# Добавляем X между повторяющимися 
		# буквами и в конце строки, если
		# её длина нечёт.
		prepared_input = ""
		for i in range(len(rawinput)):
			ch = rawinput[i]
			if (not (ch in self.alphabet)):
				continue
			prepared_input += ch
			if (i+1 < len(rawinput)):
				if (ch == rawinput[i+1]):
					prepared_input += 'X'
		if (len(prepared_input) % 2 != 0):
			prepared_input += 'X'

		# В encoded будем хранить зашифрованные попарно буквы
		encoded = ""
		# Попарно берем две буквы из строки и сдвигаем 
			# из в матрице ключа по алгоритму Плейфейера
		# В нашем случае матрицы как таковой нет
			# используется просто ключевая строка
			# индексы в которой вычисляются так
			# будто это матрица
		for i in range(0, len(prepared_input), 2):
			try:
				iA = self.key.index(prepared_input[i])
				iB = self.key.index(prepared_input[i+1])
			except Exception:
				continue

			rowA = 	int(iA / self.columns)
			columnA = iA % self.columns
			rowB = 	int(iB / self.columns)
			columnB = iB % self.columns

			# Одна строка
			if (rowA == rowB):
				columnA = (columnA + 1) % self.columns
				rowA 	= (rowA % self.rows) * self.columns
				encoded += self.key[(rowA + columnA)]

				columnB = (columnB + 1) % self.columns
				rowB 	= (rowB % self.rows) * self.columns
				encoded += self.key[(rowB + columnB)]
				continue

			# Один столбец
			if (columnA == columnB):
				columnA = columnA % self.columns
				rowA 	= ((rowA + 1) % self.rows) * self.columns 
				encoded += self.key[(rowA + columnA)]

				columnB = columnB % self.columns
				rowB 	= ((rowB + 1) % self.rows) * self.columns 
				encoded += self.key[(rowB + columnB)]
				continue

			# Иначе
			encoded += self.key[(rowA*self.columns + columnB % self.columns)]
			encoded += self.key[(rowB*self.columns + columnA % self.columns)]

		# Возвращаем зашифрованное сообщение
		return encoded

	# Метод расшифровки rawinput
	# работает почти также как зашифр., просто правила сдвига букв иные
	def decode(self, rawinput):
		prepared_input = rawinput.upper()
		decoded = ""
		for i in range(0, len(prepared_input), 2):
			try:
				iA = self.key.index(prepared_input[i])
				iB = self.key.index(prepared_input[i+1])
			except Exception:
				continue

			rowA = 	int(iA / self.columns)
			columnA = iA % self.columns
			rowB = 	int(iB / self.columns)
			columnB = iB % self.columns

			# Одна строка
			if (rowA == rowB):
				if (columnA-1 < 0):
					columnA = self.columns
				if (columnB-1 < 0):
					columnB = self.columns
				decoded += self.key[(rowA * self.columns + (columnA-1) % self.columns)]
				decoded += self.key[(rowB * self.columns + (columnB-1) % self.columns)]
				continue
				
			# Один столбец
			if (columnA == columnB):
				if (rowA-1 < 0):
					rowA = self.rows
				if (rowB-1 < 0):
					rowB = self.rows

				columnA = columnA % self.columns
				rowA	= ((rowA - 1) % self.rows) * self.columns
				decoded += self.key[(rowA + columnA)]

				columnB = columnB % self.columns
				rowB	= ((rowB - 1) % self.rows) * self.columns
				decoded += self.key[(rowB + columnB)]
				continue

			# Иначе
			decoded += self.key[(rowA*self.columns + columnB % self.columns)]
			decoded += self.key[(rowB*self.columns + columnA % self.columns)]

		# Удаляем лишние разделители X 
		prepared_input 	= decoded
		decoded 		= ""
		for i in range(len(prepared_input)):
			if (prepared_input[i] == 'X'):
				if ((i-1 < 0) or (i+1 > len(prepared_input))):
					decoded += 'X'
					continue
				if (prepared_input[i-1] == prepared_input[i+1]):
					continue
			decoded += prepared_input[i]

		# Возвращаем расшифр. сообщение
		return decoded

# pc = PlayfairCipher()
# print(pc.encode("Привет, мир!"))
# a = pc.encode("Привет, мир!")
# print(pc.decode(a))