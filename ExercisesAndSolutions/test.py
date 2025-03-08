var = 10
for i in range(10):
    for j in range(2, 10, 1):
        print(f'var ilk for: {var}')
        if var % 2 == 0:
            print(f'********************************if var: {var}')
            continue
            print(f'continue: {var}')
            var += 1
    var+=1
    print(f'var for :+1: {var}')
else:
    var+=1
    print(f'var else +1: {var}')
print(var)