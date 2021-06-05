'''
국, 영, 수 과목의 점수를 입력받아서
평균점수를 통해 A-F 학점을 출력하시오.
'''

class Grade(object):
    def __init__(self, kor, eng, math):
        self.kor = kor
        self.eng = eng
        self.math = math

    def sum(self):
        return self.kor + self.eng + self.math  # kor, eng, math 처럼 ()이 없는 것은 속성, 프로퍼티라고함.

    def avg(self):
        return self.sum() / 3

    def get_grade(self):
        score = int(self.avg())

        if score >= 90:
            grade = 'A'
        elif score >= 80:
            grade = 'B'
        elif score >= 70:
            grade = 'C'
        elif score >= 60:
            grade = 'D'
        elif score >= 50:
            grade = 'E'
        else:
            grade = 'F'
        return grade

    @staticmethod
    def main(1):
        while 1:
            menu = input('0-종료 1-학점')
            if menu == '0':
                break
            elif menu == '1':
                kor = int(input('국어점수 : '))
                eng = int(input('영어점수 : '))
                math = int(input('수학점수 : '))
                grade = Grade(kor, eng, math)
                print(f' 국어 {grade.kor}점, 영어 {grade.eng}점, 수학 {grade.math}점 \n=> 학점 : {grade.get_grade()}')
            else:
                input('메뉴선택 오류')

Grade.main()