def solution(inputArray):
    values = []
    for i in range(len(inputArray[0:-1])):
        new_max = inputArray[i]*inputArray[i+1]
        values.append(new_max)
    return max(values)