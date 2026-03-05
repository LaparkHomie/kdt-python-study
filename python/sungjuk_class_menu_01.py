from sungjuk_class import Sungjuk

# DATA_PATH = "sungjuk_data.csv"
sz_title = "입력", "출력", "조회", "수정", "삭제", "종료"
keys = "학번", "이름", "국어", "영어", "수학", "총점", "평균", "등급"
sz_ptr = "%-8s", "%-8s", "%-8d", "%-8d", "%-8d", "%-8d", "%-8.2f", "%-8s"
loop_ptr = 61

lst = []

def menu_title():
	print("*** 성적관리 ***")
	for i in range(len(sz_title) - 1):
		print("%d. 성적정보 %s" % (i + 1, sz_title[i]))
	print("%d. 프로그램 %s" % (6, sz_title[5]))
	print()

def input_sungjuk():
	obj = Sungjuk()
	obj.input_sungjuk()
	obj.proess_sungjuk()
	lst.append(obj)

	print("\n성적 입력 성공!!!\n")

def print_sungjuk():
	if len(lst) == 0:
		print("\n출력할 데이터가 없음!!!\n")
		return

	print(" " * 20 + "*** 성적표 ***")
	print("=" * loop_ptr)
	print(*keys, sep="     ")
	print("=" * loop_ptr)
	tot_avg = 0
	for obj in lst:
		#dct.update(dict(zip(keys[2:6], map(int, map(dct.get, keys[2:6])))))
		#dct["평균"] = float(dct["평균"])
		print("".join(sz_ptr) % obj.values())
		tot_avg += obj.avg
	print("=" * loop_ptr)
	print("학생수: %d, 전체 평균: %.2f" % (len(lst), tot_avg / len(lst)))

def search_sungjuk():
	pass
def update_sungjuk():
	pass
def delete_sungjuk():
	pass

if __name__ == "__main__":
	while True:
		menu_title()
		menu = int(input("메뉴를 선택하세요(1~6) => "))
		if menu == 1:
			input_sungjuk()
		elif menu == 2:
			print_sungjuk()
		elif menu == 3:
			search_sungjuk()
		elif menu == 4:
			update_sungjuk()
		elif menu == 5:
			delete_sungjuk()
		elif menu == 6:
			print("\n프로그램 종료!!\n")
			break
		else:
			print("\n메뉴를 다시 입력하세요!!\n")
