s = "dvdf"

def solution(s):
    starting_index = 0
    #current index
    found_unique = []

    for i in range(starting_index,len(s)-1):
        if s[i] not in found_unique:
            found_unique.append(s[i])
            #print (found_unique)
    #print (len(found_unique))

    starting_index = len(found_unique)-1
    #print (starting_index)
    
    found_in_loop = []
    for i in range(starting_index,len(s)):
        if s[i] not in found_in_loop:
            found_in_loop.append(s[i])
        #print (found_in_loop)
    
    starting_index = len(found_in_loop)-1
    found_in_loop_2 =[]

    for i in range(starting_index, len(s)):
        if s[i] not in found_in_loop_2 :
            found_in_loop_2.append(s[i])
        #print (found_in_loop_2)

# ... continue until loop n = len(s)

    return max(len(found_in_loop_2),len(found_in_loop), len(found_unique)) # max of all loop n
#print (solution(s))

def solution_2(*args):
    lengths = []

    for start in range(len(s)):
        found = []

        for i in range (start, len(s)):
            if s[i] not in found:
                found.append(s[i])
        lengths.append(len(found))

    return max(lengths)

#print (solution_2(s))


def solution_3(s):
    left = 0
    seen = set()
    max_length = 0

    for right in range (len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left +=1

        seen.add(s[right])
        max_length = max(max_length, right - left + 1) 
    return max_length

print (solution_3(s))
