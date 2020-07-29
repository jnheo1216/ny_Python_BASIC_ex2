# 2. 자동차 제조 회사에 따라 도시 연비가 다른지 알아보려고 한다.
# "audi"와 "toyota" 중 어느 manufacturer(제조회사)의 cty(도시 연비)가
# 평균적으로 더 높은지 확인하세요.

from operator import itemgetter


def my_read_txt(filename):  # 파일 이름을 받아오는 함수
    str = []  # 파일 내용을 넣을 리스트
    file = open(filename, 'r')  # 파일 읽기 오픈
    str = file.readlines()  # 싹 긁어오기
    for i in range(0, len(str)):  # 첫줄부터 막줄까지 돌려
         str[i] = str[i].strip().split(',')  # 각 문장에서 ,를 구분 기호로 사용
    return (str)  # 결과 반환
    file.close()  # 파일 닫기


def get_list_cty_avg(list):
    sum = 0.0
    count = 0.0
    for i in list:
        sum += float(i[7])
        count += 1.0
    return sum / count

file1 = my_read_txt('mpg.txt')
file1.pop(0)
print(file1)
print()
print()


car_list_audi = []
car_list_toyota = []
for j in file1:
    if j[0] == 'audi':
        car_list_audi.append(j)
    elif j[0] == 'toyota':
        car_list_toyota.append(j)
    else:
        pass
# print(car_list_audi)
# print(car_list_toyota)

avg_audi = get_list_cty_avg(car_list_toyota)
avg_toyota = get_list_cty_avg(car_list_audi)

print(avg_audi)
print(avg_toyota)

if avg_audi > avg_toyota:
    print("아우디가 평균 {}으로 더 연비 좋음 ".format(round(avg_audi, 2)))
elif avg_audi < avg_toyota:
    print("도요타가 평균 {}으로 더 연비 좋음".format(round(avg_toyota, 2)))
else:
    print("연비가 평균 {}으로 똑같네".format(round(avg_audi, 2)))