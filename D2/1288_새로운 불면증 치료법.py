# 1288. 새로운 불면증 치료법

T = int(input())

for tc in range(T):
    N = int(input())
    numlst = [0]*10
    cnt = 1
    while True:
        num = str(N * cnt)
        for i in num:
            n = int(i)
            if numlst[n] == 0:
                numlst[n] = 1
            if sum(numlst) == 10:
                break
        else:
            cnt += 1
            continue
        break
    print(f'#{tc+1} {N*cnt}')

# list말고 set으로 해서 add하는 게 더 빠름

# 비트연산-or(|), shift(<<)를 사용하면 조금 더 빠르고 메모리가 많이 절약됨
#
# T = int(input())
# total = (1 << 10) - 1
#
# for tc in range(T):
#     N = int(input())
#     visited = 0
#     cnt = 0
#     while True:
#         cnt += 1
#         strNum = str(N * cnt)
#         for c in strNum:
#             num = int(c)
#             visited |= (1 << num)
#
#         if visited == total:
#             break
#     print(f'#{tc + 1} {N * cnt}')