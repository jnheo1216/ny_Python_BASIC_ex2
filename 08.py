# 8. 어떤 회사에서 "compact" 차종을 가장 많이 생산하는지 알아보려고 합니다.
# 각 회사별 "compact" 차종 수를 내림차순으로 정렬해 출력하세요.
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


new_car_list_compact = [tmp for tmp in car_list if tmp.car_class == 'compact']
# 클래스만 잘하면 한줄로 조건에 맞는 리스트를 추려낼수있다
company_name = [tmp.manufacturer for tmp in new_car_list_compact]
company_name_set = set(company_name)
# 우리는 set을 통해서 index가 가능함
my_dict_company_compact = []
for i in company_name_set:
    circle_class = [tmp for tmp in new_car_list_compact if tmp.manufacturer == i]
    compact_count = len(circle_class)
    my_dict_company_compact.append((i, compact_count))
# set을 사용하여 튜플로 이루어진 리스트를 뽑아냈다
print(my_dict_company_compact)
s_my_dict_company_compact = reversed(sorted(my_dict_company_compact, key=lambda t : t[1]))
# 정렬법은 그냥 외우자 이렇게 쓰면 된다.
count = 1
for j in s_my_dict_company_compact:
    if count > 10:
        break
    else:
        print("compact 차종 개수 {}위 기업 : {} , {}".format(count, j[0], j[1]))
    count += 1


