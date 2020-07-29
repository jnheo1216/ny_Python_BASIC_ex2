# 4. "audi"에서 생산한 자동차 중에 어떤 자동차 모델의 hwy(고속도로 연비)가
# 높은지 알아보려고 한다. "audi"에서 생산한 자동차 중 hwy가 1~5위에 해당하는
# 자동차의 데이터를 출력하세요.

from operator import itemgetter

class Car(object):
    def __init__(self, car_list):
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
    def __repr__(self):  # 이걸 안하면  프린트하면 메모리값을 줌
        return self.manufacturer


def my_read_txt(filename):  # 파일 이름을 받아오는 함수
    str = []  # 파일 내용을 넣을 리스트
    file = open(filename, 'r')  # 파일 읽기 오픈
    str = file.readlines()  # 싹 긁어오기
    for i in range(0, len(str)):  # 첫줄부터 막줄까지 돌려
         str[i] = str[i].strip().split(',')  # 각 문장에서 ,를 구분 기호로 사용
    return (str)  # 결과 반환
    file.close()  # 파일 닫기

file1 = my_read_txt('mpg.txt')
file1.pop(0)
print(file1)
print()
print()

car_list_audi = []
for j in file1:
    if j[0] == 'audi':
        car_list_audi.append(j)
    else:
        pass

sort_arry = []
for name in sorted(file1, key=itemgetter(8)):  # 이거하나면 정렬 개쉬움
    sort_arry.append(name)
sort_arry.reverse()

count = 1
for k in sort_arry:
    if count > 5:
        break
    else:
        print("아우디 고속도로 연비 {}위 : {} {}년식 {}. 연비 : {}".format(count, k[1], k[3], k[5], k[8]))
    count += 1



