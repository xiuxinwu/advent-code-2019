import math
#part1
# list = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,13,1,19,1,19,9,23,1,5,23,27,1,27,9,31,
# 1,6,31,35,2,35,9,39,1,39,6,43,2,9,43,47,1,47,6,51,2,51,9,55,1,5,55,59,2,59,6,63,
# 1,9,63,67,1,67,10,71,1,71,13,75,2,13,75,79,1,6,79,83,2,9,83,87,1,87,6,91,2,10,91,
# 95,2,13,95,99,1,9,99,103,1,5,103,107,2,9,107,111,1,111,5,115,1,115,5,119,1,10,119,
# 123,1,13,123,127,1,2,127,131,1,131,13,0,99,2,14,0,0]


# list = [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,13,1,19,1,19,9,23,1,5,23,27,1,27,9,31,
# 1,6,31,35,2,35,9,39,1,39,6,43,2,9,43,47,1,47,6,51,2,51,9,55,1,5,55,59,2,59,6,63,
# 1,9,63,67,1,67,10,71,1,71,13,75,2,13,75,79,1,6,79,83,2,9,83,87,1,87,6,91,2,10,91,
# 95,2,13,95,99,1,9,99,103,1,5,103,107,2,9,107,111,1,111,5,115,1,115,5,119,1,10,119,
# 123,1,13,123,127,1,2,127,131,1,131,13,0,99,2,14,0,0]
# #list = [1,9,10,3,2,3,11,0,99,30,40,50]
#
# length = len(list)
# i = 0
# #for i,x in enumerate(list):
# while i < length:
#     value0 = list[i]
#     print("value0:" + str(value0))
#     if value0 == 99:
#         break
#     value1 = list[list[i+1]]
#     print("value1:" + str(value1))
#     value2 = list[list[i+2]]
#     print("value2:" + str(value2))
#     value3 = list[i+3]
#     print("value3:" + str(value3))
#     if value0 ==1:
#         result = value1 + value2
#     if value0 ==2:
#         result = value1 * value2
#     list[value3] = result
#     i = i + 4
# print(list[0])
# print(list)

#part2

def calculate(num1,num2,list):
    list[1]=num1
    list[2]=num2
    length = len(list)
    i = 0
    #for i,x in enumerate(list):
    while i < length:
        value0 = list[i]
        #print("value0:" + str(value0))
        if value0 == 99:
            break
        value1 = list[list[i+1]]
        #print("value1:" + str(value1))
        value2 = list[list[i+2]]
        #print("value2:" + str(value2))
        value3 = list[i+3]
        #print("value3:" + str(value3))
        if value0 ==1:
            result = value1 + value2
        elif value0 ==2:
            result = value1 * value2
        else :
            break
        list[value3] = result
        i = i + 4
    return list[0]

# print(calculate(79,12,list))
GOAL = 19690720
for k in range(100):
    for j in range(100):
        # リストを毎回初期化しないと行けない
        list = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,13,1,19,1,19,9,23,1,5,23,27,1,27,9,31,
        1,6,31,35,2,35,9,39,1,39,6,43,2,9,43,47,1,47,6,51,2,51,9,55,1,5,55,59,2,59,6,63,
        1,9,63,67,1,67,10,71,1,71,13,75,2,13,75,79,1,6,79,83,2,9,83,87,1,87,6,91,2,10,
        91,95,2,13,95,99,1,9,99,103,1,5,103,107,2,9,107,111,1,111,5,115,1,115,5,119,1,
        10,119,123,1,13,123,127,1,2,127,131,1,131,13,0,99,2,14,0,0]
        result = calculate(k , j , list)
        if result == GOAL:
            print(100 * k + j)
            break
