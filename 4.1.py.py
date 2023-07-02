def strr(s):
    for sym in set(s):
        counter=0
        for sem in s :
            if sym==sem:
                counter+=1
        print(sym, counter)
strr("xhxchcbchchhchchc")