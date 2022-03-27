def plusMinus(arr: list):
    n = len(arr)
    pos = 0
    neg = 0
    zero = 0
    for i in arr:
        if i > 0 :
            pos+=1
        elif i < 0 :
            neg+=1
        else:
            zero+=1
    print("{:.6f}".format(pos/n))
    print("{:.6f}".format(neg/n))
    print("{:.6f}".format(zero/n))
    return None

if __name__ == "__main__":
    plusMinus([-4,3,-9,0,4,1])
    plusMinus([1,1,0,-1,-1])