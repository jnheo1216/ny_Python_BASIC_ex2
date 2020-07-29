# 3. "chevrolet", "ford", "honda" 자동차의 고속도로 연비 평균을 알아보려고 한다.
# 이 회사들의 데이터를 추출한 후 hwy(고속도로 연비) 평균을 구하세요.

from operator import itemgetter

class Car(object):
    def __init__(self, car_list):
        car_list = car_list.split(",")
        self.manufacturer = car_list[0]
        self.model = car_list[1]
        self.displ = car_list[2]
        self.year = car_list[3]
        self.cyl = car_list[4]
        self.trans = car_list[5]
        self.drv = car_list[6]
        self.cty = car_list[7]
        self.hwy = car_list[8]
        self.fl = car_list[9]
        self.clas = car_list[10]



def my_read_txt(filename):  # 파일 이름을 받아오는 함수
    str = []  # 파일 내용을 넣을 리스트
    file = open(filename, 'r')  # 파일 읽기 오픈
    str = file.readlines()  # 싹 긁어오기
    for i in range(0, len(str)):  # 첫줄부터 막줄까지 돌려
         str[i] = str[i].strip().split(',')  # 각 문장에서 ,를 구분 기호로 사용
    return (str)  # 결과 반환
    file.close()  # 파일 닫기


def get_list_hwy_avg(list):
    sum = 0.0
    count = 0.0
    for i in list:
        sum += float(i[8])
        count += 1.0
    return round(sum / count, 2)

file1 = my_read_txt('mpg.txt')
file1.pop(0)
print(file1)
print()
print()

car_list_chevrolet = []
car_list_ford = []
car_list_honda = []

for j in file1:
    if j[0] == 'chevrolet':
        car_list_chevrolet.append(j)
    elif j[0] == 'ford':
        car_list_ford.append(j)
    elif j[0] == 'honda':
        car_list_honda.append(j)
    else:
        pass

avg_hwy_chevrolet = get_list_hwy_avg(car_list_chevrolet)
avg_hwy_ford = get_list_hwy_avg(car_list_ford)
avg_hwy_honda = get_list_hwy_avg(car_list_honda)

print("chevrolet 고속도로 연비 평균 : {}".format(avg_hwy_chevrolet))
print("ford 고속도로 연비 평균 : {}".format(avg_hwy_ford))
print("honda 고속도로 연비 평균 : {}".format(avg_hwy_honda))