# 7. 어떤 회사 자동차의 hwy(고속도로 연비)가 가장 높은지 알아보려 합니다.
# hwy(고속도로 연비) 평균이 가장 높은 회사 세 곳을 출력하세요.
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


def search_car_dict_hwy_avg(company_name):
    circle_class = [tmp.hwy for tmp in car_list if tmp.manufacturer == company_name]
    return (company_name, round(sum(circle_class)/len(circle_class), 2))


company_of_car = [tmp.manufacturer for tmp in car_list]
company_of_car_set = set(company_of_car)

my_dict_company = []
for i in company_of_car_set:
    my_dict_company.append(search_car_dict_hwy_avg(i))

print(my_dict_company)
s_my_dict_company = reversed(sorted(my_dict_company, key=lambda t : t[1]))

count = 1
for j in s_my_dict_company:
    if count > 5:
        break
    else:
        print("hwy 평균 {}위 기업 : {} , {}".format(count, j[0], j[1]))
    count += 1
