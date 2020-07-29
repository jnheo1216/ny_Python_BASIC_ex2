# 5. mpg 데이터는 연비를 나타내는 변수가 2개입니다.
# 두 변수를 각각 활용하는 대신 하나의 통합 연비 변수를 만들어 사용하려 합니다.
# 평균 연비 변수는 두 연비(고속도로와 도시)의 평균을 이용합니다.
# 회사별로 "suv" 자동차의 평균 연비를 구한후 내림차순으로 정렬한 후 1~5위까지 데이터를 출력하세요.

from operator import itemgetter
import operator

class Car(object):
    def __init__(self, car_data):
        car_data = car_data.split(",")
        self.manufacturer = car_data[0]
        self.model = car_data[1]
        self.displ = float(car_data[2])
        self.year = int(car_data[3])
        self.cyl = int(car_data[4])
        self.trans = car_data[5]
        self.drv = car_data[6]
        self.cty = int(car_data[7])
        self.hwy = int(car_data[8])
        self.fl = car_data[9]
        self.car_class = car_data[10]
        self.avg_cty_hwy = (int(car_data[7]) + int(car_data[8])) / 2

    def __repr__(self):
        return self.manufacturer + ", " + self.model \
               + "," + str(self.displ) + ", " + str(self.year) \
               + self.trans + ", " + self.drv \
               + str(self.cty) + ", " + str(self.hwy)


def my_read_txt(filename):  # 파일 이름을 받아오는 함수
    str = []  # 파일 내용을 넣을 리스트
    file = open(filename, 'r')  # 파일 읽기 오픈
    str = file.readlines()  # 싹 긁어오기
    for i in range(0, len(str)):  # 첫줄부터 막줄까지 돌려
         str[i] = str[i].strip().split(',')  # 각 문장에서 ,를 구분 기호로 사용
    return (str)  # 결과 반환
    file.close()  # 파일 닫기


def get_list_avg(list):
    if not list:
        return 0
    else:
        sum = 0.0
        count = 0.0
        for i in list:
            sum += float(i[-1])
            count += 1.0
        return round(sum / count, 2)


file1 = my_read_txt('mpg.txt')
file1.pop(0)
print(file1)
print()
print()

count = 0
new_car_list_avg = []
for j in file1:
    if j[10] == 'suv':
        hwy_cty_avg = (float(j[7]) + float(j[8]))/2
        j.append(hwy_cty_avg)
        new_car_list_avg.append(j)
    else:
        pass

# for nn in new_car_list_avg:
#     print(nn)

car_list_chevrolet = []
car_list_ford = []
car_list_honda = []
car_list_audi = []
car_list_dodge = []
car_list_hyundai = []
car_list_jeep = []
car_list_land_rover = []
car_list_lincoln = []
car_list_mercury = []
car_list_nissan = []
car_list_pontiac = []
car_list_subaru = []
car_list_toyota = []
car_list_volkswagen = []

for k in new_car_list_avg:
    if k[0] == 'chevrolet':
        car_list_chevrolet.append(k)
    elif k[0] == 'ford':
        car_list_ford.append(k)
    elif k[0] == 'honda':
        car_list_honda.append(k)
    elif k[0] == 'audi':
        car_list_audi.append(k)
    elif k[0] == 'dodge':
        car_list_dodge.append(k)
    elif k[0] == 'hyundai':
        car_list_hyundai.append(k)
    elif k[0] == 'jeep':
        car_list_jeep.append(k)
    elif k[0] == 'land rover':
        car_list_land_rover.append(k)
    elif k[0] == 'lincoln':
        car_list_lincoln.append(k)
    elif k[0] == 'mercury':
        car_list_mercury.append(k)
    elif k[0] == 'nissan':
        car_list_nissan.append(k)
    elif k[0] == 'pontiac':
        car_list_pontiac.append(k)
    elif k[0] == 'subaru':
        car_list_subaru.append(k)
    elif k[0] == 'toyota':
        car_list_toyota.append(k)
    elif k[0] == 'volkswagen':
        car_list_volkswagen.append(k)
    else:
        pass

dict_car = {}
dict_car['chevrolet'] = get_list_avg(car_list_chevrolet)
dict_car['ford'] = get_list_avg(car_list_ford)
dict_car['honda'] = get_list_avg(car_list_honda)
dict_car['audi'] = get_list_avg(car_list_audi)
dict_car['dodge'] = get_list_avg(car_list_dodge)
dict_car['hyundai'] = get_list_avg(car_list_hyundai)
dict_car['jeep'] = get_list_avg(car_list_jeep)
dict_car['land rover'] = get_list_avg(car_list_land_rover)
dict_car['lincoln'] = get_list_avg(car_list_lincoln)
dict_car['mercury'] = get_list_avg(car_list_mercury)
dict_car['nissan'] = get_list_avg(car_list_nissan)
dict_car['pontiac'] = get_list_avg(car_list_pontiac)
dict_car['subaru'] = get_list_avg(car_list_subaru)
dict_car['toyota'] = get_list_avg(car_list_toyota)
dict_car['volkswagen'] = get_list_avg(car_list_volkswagen)
print(dict_car)
# dict 전용 정렬법
s_dict_car = sorted(dict_car.items(), key=operator.itemgetter(1), reverse=True)
print(s_dict_car)

count = 1
for k in s_dict_car:
    if count > 5:
        break
    else:
        print("suv 연비 {}위 : {} , {}".format(count, k[0], k[1]))
    count += 1

##################################################################

file2 = open("mpg.txt", "r")
car_list = list()

line = file2.readline()  # 첫줄 메뉴표라서 빼준겨

while True:
    line = file2.readline()
    if not line:
        break
    car_list.append(Car(line.strip()))

file2.close()



new_car_list_suv = [tmp for tmp in car_list if tmp.car_class == 'suv']

company_name = [tmp.manufacturer for tmp in new_car_list_suv]
company_name_set = set(company_name)

my_dict_company = []
for i in company_name_set:
    circle_class = [tmp.avg_cty_hwy for tmp in new_car_list_suv if tmp.manufacturer == i]
    avg = round(sum(circle_class) / len(circle_class), 2)
    my_dict_company.append((i, avg))

print(my_dict_company)
s_my_dict_company = reversed(sorted(my_dict_company, key=lambda t : t[1]))

count = 1
for j in s_my_dict_company:
    if count > 5:
        break
    else:
        print("suv 통합 연비 {}위 기업 : {} , {}".format(count, j[0], j[1]))
    count += 1

