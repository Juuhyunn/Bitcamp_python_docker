def int_to_bin(a : int):
    return bin(a)

def bin_to_str(a) -> []:
    ls = []
    [ls.append(str(a)[i]) for i in range(len(str(a)))]
    del ls[0:2]
    print('2진수 표현 : ' + ''.join(ls))
    return ls

def list_to_chuck(ls : []) -> []:
    # print(f'변환 전 : {ls}')
    for i,j in enumerate(ls):
        if j == '1':
            ls[i] = '0'
        elif j == '0':
            ls[i] = '00'
    return ls

def make_chuck(ls : []) -> []:
    result = []
    ls.append('가짜값')
    # print(f'척 값 만들기 전 : {ls}')
    n = 1
    for i, j in enumerate(ls):
        if i == len(ls)-1:
            pass
        elif j != ls[i+1]:
            result.append(str(f'{j} {"0"*n} '))
            n = 1
        elif j == ls[i+1]:
            n += 1
    return result

def chuck_to_str(ls: []) -> str:
    return ''.join(ls)

if __name__ == '__main__':
    print(chuck_to_str(make_chuck(list_to_chuck(bin_to_str(int_to_bin(int(input('Input Int'))))))))