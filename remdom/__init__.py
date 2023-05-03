
table = [25421, 6436,463,473,24,2,37,3854,94,62,545151,515,15126,327,3487,4568,6,4563,47,4358,35,2,35,43,7,548,457,45]
resolver = [612,42,236,84,23,6,124,362,652,23]
seed = 172
nms = []





def initiate(seed):
    res = 0
    result = []
    for number in str(seed):
        res += resolver[int(number)]

    for i in str(res):
        result.append(int(i))
    er = []
    for i in result:
        nh = i
        while i > len(str(seed))-1:
            i = i - len(str(seed))-1
            
        nh += int(str(seed)[i])
        er.append(nh)
    
    return er

def generate(seed):
    nae = initiate(seed)
    result = 0
    for number in nae:
        result += table[number]
    final = 0
    for nmb in str(result):
        final += int(nmb)
    
    shifter = 0
    for seed_nmb in str(seed):
        shifter += final + int(seed_nmb)
    
    for i in range(10):
        for number in str(shifter):
            number = int(number)
            r = table.pop(number)
            table.append(r)

    if len(str(final)) == 1:
        return final
    return int(str(final)[len(str(final))-1])

        
def rnd(seed, decimals):
    result = []
    result_string = ''
    counter = 0

    # Normal counter should be equal to number of decimals, that is the most random number
    # Abnormal counter is when counter is higher than the number of decimals by 2 or 3 and number of decimals is lower than 6

    for i in range(decimals):
        nm = generate(seed)
        result.append(nm)
        counter += result.count(nm)
        
    if counter == decimals:
        pass
    else:
        return "Not random enough"
        


    if result[0] == 0:
        result.pop(0)
        result.append(0)
    


    for number in result:
        result_string += str(number)

    return int(result_string)


def random(seed, decimals):
    number = "Not random enough"
    while number == "Not random enough":
        number = rnd(seed, decimals)
        seed += 1

    return number


