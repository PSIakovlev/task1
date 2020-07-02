def arithmetic(a,b,c):
	a=int(a)
	b=int(b)
	if c=="+":
		return a+b
	elif c=="-":
		return a-b
	elif c=="*":
		return a*b
	elif c=="/":
		return a/b
	else:
		return("Неизвестная операция")
def is_year_leap(year):
	year=int(year)
	return True if year%4==0 else False
def square(a):
	a=int(a)
	return (a*4, a*a, a*2**0.5)
def season(numberMonth):
	numberMonth=int(numberMonth)
	if numberMonth>0 and numberMonth<13:
		if numberMonth<3 or numberMonth == 12:
			return "Winter"
		elif numberMonth<6:
			return "Spring"
		elif numberMonth<9:
			return "Summer"
		else:
			return "Autumn"
	else:
		return "Смотри в инопланетном календаре"
def bank(a, years):
	if years>0:
		a = bank(a+a*0.1, years-1)
	return a
def is_prime(a):
    i=2;
    while i<=a/2:
        if a%i==0:
            return False
            break;
        else:
            return True
        i=i+1;
def date(day,month,year):
    if day<32 or month<13 or day>0 or month>0 or year>=0:
        if (day==31 and (month<8 and month%2!=0 or month>7 and month%2==0)) or (day==30 and month!=2) or (day == 29 and month == 2 and year%4==0) or day<29:
            return True
    return False
def XOR_cipher(a,b):
    return a^b
def XOR_uncipher(a,b):
    return a^b
#print(arithmetic(input("a="),input("b="),input("c=")))
#print(is_year_leap(input("Какой год?")))
#print(square(input("Сторона квадрата = ")))
#print(season(input("Номер месяца ")))
#print(bank(float(input("Вклад равен ")), int(input("На "))))
#print(is_prime(int(input("Введите число?"))))
#print(date(int(input("Введите число")), int(input("Введите номер месяца")), int(input("Введите год"))))
#print(XOR_cipher(int(input("Введите строку")), int(input("Введите ключ"))))
#print(XOR_uncipher(int(input("Введите зашифрованную строку")), int(input("Введите ключ"))))

#Простейшие арифметические операции (1)
#Написать функцию arithmetic, принимающую 3 аргумента: первые 2 - числа, третий - операция, которая должна быть произведена над ними. Если третий аргумент +, сложить их; если —, то вычесть; * — умножить; / — разделить (первое на второе). В остальных случаях вернуть строку "Неизвестная операция".

#Високосный год (2)
#Написать функцию is_year_leap, принимающую 1 аргумент — год, и возвращающую True, если год високосный, и False иначе.

#Квадрат (3)
#Написать функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения (с помощью кортежа): периметр квадрата, площадь квадрата и диагональ квадрата.

#Времена года (4)
#Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12), и возвращающую время года, которому этот месяц принадлежит (зима, весна, лето или осень).

#Банковский вклад (5)
#Пользователь делает вклад в размере a рублей сроком на years лет под 10% годовых (каждый год размер его вклада увеличивается на 10%. Эти деньги прибавляются к сумме вклада, и на них в следующем году тоже будут проценты).
#Написать функцию bank, принимающая аргументы a и years, и возвращающую сумму, которая будет на счету пользователя.

#Простые числа (6)
#Написать функцию is_prime, принимающую 1 аргумент — число от 0 до 1000, и возвращающую True, если оно простое, и False - иначе.

#Правильная дата (7)
#Написать функцию date, принимающую 3 аргумента — день, месяц и год. Вернуть True, если такая дата есть в нашем календаре, и False иначе.

#XOR-шифрование (8)
#Написать функцию XOR_cipher, принимающая 2 аргумента: строку, которую нужно зашифровать, и ключ шифрования, которая возвращает строку, зашифрованную путем применения функции XOR (^) над символами строки с ключом. Написать также функцию XOR_uncipher, которая по зашифрованной строке и ключу восстанавливает исходную строку.