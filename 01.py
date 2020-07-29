# 1. displ(배기량)이 4 이하인 자동차와 5 이상인 자동차 중
# 어떤 자동차의 hwy(고속도로 연비)가 평균적으로 더 높은지 확인하세요.

from operator import itemgetter

def my_read_txt(filename):  # 파일 이름을 받아오는 함수
    str = []  # 파일 내용을 넣을 리스트
    file = open(filename, 'r')  # 파일 읽기 오픈
    str = file.readlines()  # 싹 긁어오기
    for i in range(0, len(str)):  # 첫줄부터 막줄까지 돌려
         str[i] = str[i].strip().split(',')  # 각 문장에서 ,를 구분 기호로 사용
    return (str)  # 결과 반환
    file.close()  # 파일 닫기


file1 = my_read_txt('mpg.txt')
print(file1)
file1.pop(0)
print(file1)

car_list_new = []
for j in file1:
    if float(j[2]) < 4.01 or float(j[2]) > 5.0:
        car_list_new.append(j)
    else:
        pass
print(car_list_new)
print()
print()

sort_arry = []
for name in sorted(file1, key=itemgetter(8)):  # 이거하나면 정렬 개쉬움
    sort_arry.append(name)
sort_arry.reverse()

print("자동차 hwy연비 순으로(배기량4이하 5이상)")
for k in sort_arry:
    print(k)








print("hello world!")