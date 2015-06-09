def candy(cuts):
    if cuts % 2 == 0:
        print (cuts/2)**2
    else:
        print (cuts - 1)/2*(cuts + 1)/2

test_cases = int(raw_input().strip())

for _ in range(test_cases):
    k = int(raw_input().strip())
    candy(k)
