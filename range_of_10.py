def range_sum_cal():
    s = int(input("decide the start of the range "))
    f = int(input("decide the end of the range "))
    if f>s:
        for i in range(s,f):
            current = i
            if current == 0:
                previous = 0
            else:
                previous = i-1
            sum = current + previous
            print("current number= ",current , "previous number =",previous , "sum =",sum)
    else:
        print("the range syntax is wrong")
range_sum_cal()