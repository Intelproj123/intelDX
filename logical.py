# logicValOne = bool(input("첫 번째 논리값 입력 : "))  # 잘못된 방법
# logicValTwo = bool(input("두 번째 논리값 입력 : "))  # 잘못된 방법
# logicValOne = True
# logicValTwo = False

# bool 함수는 빈문자열을 False로, 아무 문자나 있으면 True로 반환한다.
logicValOne = bool(input("빈문자열은 False 아니면 True"))
logicValTwo = bool(input("빈문자열은 False 아니면 True"))

print("logicValOne = {} not LogicValOne = {}".format(logicValOne, (not logicValOne)))
print("{} and {} = {}".format(logicValOne, logicValTwo, (logicValOne and logicValTwo)))
print("{} or {} = {}".format(logicValOne, logicValTwo, (logicValOne or logicValTwo)))

# 논리 연산자는 논리값과 논리값을 연산해서 논리값을 리턴하는 연산자
# 입력은 True 혹은 False로 해야 함


