num = input("단을 입력하시오 => ")

print(" ** " + num + "단 **")

num = int(num)

for i in range(1, 10):
	print("%d * %d = %d" % (num, i, num * i))
