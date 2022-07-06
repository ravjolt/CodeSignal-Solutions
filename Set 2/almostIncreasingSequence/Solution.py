def solution(sequence):
    removed=0
    output = True
    prev_max = maxim = float('-infinity')
    for s in sequence:
        if s > maxim:
            prev_max = maxim
            maxim=s
        elif s > prev_max:
            removed +=1
            maxim = s
        else:
            removed+=1
        if removed > 1:
            output = False
    return output