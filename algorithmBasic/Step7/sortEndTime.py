# 모듈 호출
from random import randint
import time


# 배열에 10,000개의 정수를 삽입
array = []
for _ in range(10000):
    # 1부터 100사이의 랜덤한 정수
    array.append(randint(1, 100))


# 선택 정렬 프로그램 성능 측정
start_time = time.time()

# 선택정렬 소스코드
for i in range(len(array)):
    min_index = i  # 가장 작은 원소의 인덱스
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]

# 측정 종료
end_time = time.time()
print('선택 정렬 성능 시간 측정 :', end_time - start_time)


# 배열 초기화(무작위 데이터로)
array = []
for _ in range(10000):
    # 1부터 100사이의 랜덤한 정수
    array.append(randint(1, 100))

# 기본 정렬 프로그램 성능 측정
start_time = time.time()

# 기본 정렬 라이브러리 사용
array.sort()

# 측정 종료
end_time = time.time()
print('기본 정렬 라이브러리 성능 시간 측정:', end_time - start_time)