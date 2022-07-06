def solution(statues):
    statues.sort()
    y = 0
    for i in range(len(statues)-1):
        if statues[i+1] - statues[i]:
            y = y + statues[i+1] - statues[i] -1
    return (y)