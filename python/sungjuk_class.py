class Sungjuk:
	keys = "학번", "이름", "국어", "영어", "수학", "총점", "평균", "등급"
	rank_grade = dict(zip(tuple("수우미양가"), (90, 80, 70, 60, 0)))
	sz_ptr = "%-8s", "%-8s", "%-8d", "%-8d", "%-8d", "%-8d", "%-8.2f", "%-8s"

	def __init__(self):
		self._sid = ""
		self._name = ""
		self._kor = 0
		self._eng = 0
		self._mat = 0
		self._tot = 0
		self._avg = 0.0
		self._grade = ""

	def set_sid(self, sid):
		self._sid = sid
	def get_sid(self):
		return self._sid
	sid = property(get_sid, set_sid)
	def set_name(self, name):
		self._name = name
	def get_name(self):
		return self._name
	name = property(get_name, set_name)
	def set_kor(self, kor):
		self._kor = kor
	def get_kor(self):
		return self._kor
	kor = property(get_kor, set_kor)
	def set_eng(self, eng):
		self._eng = eng
	def get_eng(self):
		return self._eng
	eng = property(get_eng, set_eng)
	def set_mat(self, mat):
		self._mat = mat
	def get_mat(self):
		return self._mat
	mat = property(get_mat, set_mat)
	def set_tot(self, tot):
		self._tot = tot
	def get_tot(self):
		return self._tot
	tot = property(get_tot, set_tot)
	def set_avg(self, avg):
		self._avg = avg
	def get_avg(self):
		return self._avg
	avg = property(get_avg, set_avg)
	def set_grade(self, grade):
		self._grade = grade
	def get_grade(self):
		return self._grade
	grade = property(get_grade, set_grade)

	def values(self):
		return self.sid, self.name, self.kor, self.eng, self.mat, self.tot, self.avg, self.grade



	def input_sungjuk(self):
		self._sid = input("학번 입력 => ")
		self._name = input("이름 입력 => ")
		self._kor = int(input("국어 점수 입력 => "))
		self._eng = int(input("영어 점수 입력 -> "))
		self._mat = int(input("수학 점수 입력 => "))

	def proess_sungjuk(self):
		self._tot = self._kor + self._eng + self._mat
		self._avg = self._tot / 3

		if self._avg >= 90:
			self._grade = "수"
		elif self._avg >= 80:
			self._grade = "우"
		elif self._avg >= 70:
			self._grade = "미"
		elif self._avg >= 60:
			self._grade = "양"
		else:
			self._grade = "가"

	def output_sungjuk(self):
		print("%4s   %3s  %4d   %4d   %4d   %4d   %5.2f  %2s" % (self._id, self._name, self._kor, self._eng, self._mat, self._tot, self._avg, self._grade))

if __name__ == "__main__":
	obj = Sungjuk()
	obj.input_sungjuk()
	obj.proess_sungjuk()
	print("\n\t\t\t*** 성적관리 ***")
	print("======================================================")
	print("학번    이름    국어    영어    수학    총점    평균  등급")
	print("======================================================")
	obj.output_sungjuk()
	print("======================================================")
