first = int(input("첫 번째 정수 : "))
second = int(input("두 번째 정수 : "))

print("{} << {} = {}".format(first, second, (first << second)))
print("{} >> {} = {}".format(first, second, (first >> second)))

# shift 연산은 곱하기 2의 몇 승 혹은 나누기 2의 몇 승과 같다
# 입력을 8과 2로 해 보세요!!

# 출력 결과
# 8 << 2 = 32
# 8 >> 2 = 2
