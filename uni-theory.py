def theory(n):
    a = n+1
    b = n-1

    print(n*n)
    print(a*b)
    print("")

    if a*b == n*n-1:
        return('pass')
    else:
        return('fail')

def test():
    for i in range(9999):
        
        if theory(i) == 'fail':
            print("FAIL")
            break
    
    print(f"Numbers 0 - {i} are ok!")

test()