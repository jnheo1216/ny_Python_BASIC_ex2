# 6. mpg 데이터의 class는 "suv", "compact" 등 자동차의 특징에 따라
# 일곱 종류로 분류한 변수입니다. 어떤 차종의 도시 연비가 높은지 비교하려 합니다.
# class별 cty 평균을 구하고 cty 평균이 높은 순으로 정렬해 출력하세요.

# set과 그걸 활용하여 순식간에 평균도 구해버리는 방법을 생각해보자

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

    def __repr__(self):
        return self.manufacturer + ", " + self.model \
               + "," + str(self.displ) + ", " + str(self.year) \
               + self.trans + ", " + self.drv \
               + str(self.cty) + ", " + str(self.hwy)


file = open("mpg.txt", "r")
car_list = list()

line = file.readline()  # 첫줄 메뉴표라서 빼준겨

while True:
    line = file.readline()
    if not line:
        break
    car_list.append(Car(line.strip()))

file.close()


def search_car_dict_and_avg(class_name):
    circle_class = [tmp.cty for tmp in car_list if tmp.car_class == class_name]
    return (class_name, round(sum(circle_class)/len(circle_class), 2))


print(car_list)


class_of_car = [tmp.car_class for tmp in car_list]
class_of_car_set = set(class_of_car)

my_dict_car = []
for k in class_of_car_set:
    my_dict_car.append(search_car_dict_and_avg(k))

print(my_dict_car)
s_my_dict_car = reversed(sorted(my_dict_car, key=lambda t : t[1]))
print(s_my_dict_car)

count = 1
for j in s_my_dict_car:
    if count > 5:
        break
    else:
        print("cty 평균 {}위 class : {} , {}".format(count, j[0], j[1]))
    count += 1


################################################################

