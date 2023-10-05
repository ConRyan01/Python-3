def solution(text, ending):
    result = None
    for i in range(len(ending) - 1,-1,-1):
        j = len(text)-1
        if ending[i] == text[j]:
            print(ending[i],text[j])
            result = True
            
        else:
            print(ending[i],text[j])
            result = False
            
        j-=1
    return result

print(solution('xmhaomjsakpiqxqilhj','qlqilhj'))