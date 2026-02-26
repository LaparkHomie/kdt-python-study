lst = []
flag = False
total = 0

inputdct = ("제품코드", "제품명", "수량", "단가", "판매금액")

while True:
	dct = []
	for i in range(0, 4):
		szText = input(inputdct[i] + " 입력 => ")
		if szText == "exit":
			flag = True
			break
		dct.append(szText)
	if flag == True:
		break

	dct[2] = int(dct[2])
	dct[3] = int(dct[3])
	dct.append(dct[2] * dct[3])
	lst.append(dct)
	total += dct[4]
	print()

print("\t" * 3 + "*** 제품관리 ***")
print("=" * 40)
print("    ".join(inputdct))
print("=" * 40)
for dct in lst:
	print("%4s       %4s   %4d    %4d    %6d" % tuple(dct))
print("=" * 40)
print("\t" * 3 + "총 판매금액 = %7d" % total)


# lst = []
# flag = False
# total = 0
#
# inputdct = dict(zip(("code", "name", "count", "price"), ("제품코드", "제품명", "수량", "단가")))
#
# while True:
# 	dct = {}
# 	for K, V in inputdct.items():
# 		dct[K] = input(V + " 입력 => ")
# 		if dct[K] == "exit":
# 			flag = True
# 			break
# 	if flag == True:
# 		break
#
# 	dct["count"] = int(dct["count"])
# 	dct["price"] = int(dct["price"])
# 	dct["value"] = dct["count"] * dct["price"]
# 	lst.append(dct)
# 	total += dct["value"]
# 	print()
# inputdct["total"] = "판매금액"
#
# print("\t" * 3 + "*** 제품관리 ***")
# print("=" * 40)
# print("    ".join(inputdct.values()))
# print("=" * 40)
# for dct in lst:
# 	print("%4s       %4s   %4d    %4d    %6d" % tuple(dct.values()))
# print("=" * 40)
# print("\t" * 3 + "총 판매금액 = %7d" % total)
