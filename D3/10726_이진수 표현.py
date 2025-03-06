# 10726. 이진수 표현

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    res = 'OFF'
    chk = 2 ** N - 1
    if chk & M == chk:
        res = 'ON'

    print(f'#{tc} {res}')


# chk를 ** 말고 <<으로 구하기
# 메모리나 시간은 또이또이
#
# lastNBit = (1 << N) - 1         # 111...1 (길이 N)
#     if lastNBit == (M & lastNBit):
#         print(f'#{test_case} ON')
#     else:
#         print(f'#{test_case} OFF')

# format으로 2진수 문자열로 바꿔서 하면 훨씬 빠르고 메모리 감소
#
# if ('0'*N + format(M, 'b'))[-N:] == '1'*N:
#         oout.append(f'#{q} ON')
#     else: oout.append(f'#{q} OFF')