# N = int(input())

# for i in range(N):
    # A, B = input().strip().split(' ')

    # if(len(B) > len(A)):
        # print('nao encaixa')
    # else:
        # A = A[(len(A) - len(B)):]
        # print('encaixa' if A == B else 'nao encaixa')




# N = int(input())

# while(N > 0):
    # # A = int(input())
    # # B = int(input())
    # A, B = input().strip().split(' ')
    # if int(A) >= int(B) and (int(A) - int(B))%10 == 0:
        # print("encaixa")
    # else:
        # print("nao encaixa")
    # N -=1

qte = int(input())

for i in range(qte):
    A, B = list(map(str,input().split()))
    if A[-len(B):] == B:
        print ("encaixa")
    else:
        print("nao encaixa")