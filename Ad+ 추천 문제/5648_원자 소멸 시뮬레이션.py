# 5648. [모의 SW 역량테스트] 원자 소멸 시뮬레이션

# 3개 이상 충돌은 구현 불가, 내려가는 거랑 올라가는 거 구현 불가
# T = int(input())  # 테스트 케이스 수
# for tc in range(1, T + 1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     res = 0
# 
#     for x1, y1, d1, k1 in arr:
#         qs = []
#         qd = []
#         for x2, y2, d2, k2 in arr:
#             if d1 == 0 and x2 == x1 and y2 > y1:  # 상 : 같은 세로선, 위쪽
#                 if d2 == 0:  # 같은 방향
#                     qs.append(y2)
#                 elif d2 == 1:  # 다른 방향
#                     qd.append(y2)
#             elif d1 == 1 and x2 == x1 and y2 < y1:  # 하 : 같은 세로선, 아래쪽
#                 if d2 == 1:  # 같은 방향
#                     qs.append(y2)
#                 elif d2 == 0:  # 다른 방향
#                     qd.append(y2)
#             elif d1 == 2 and y2 == y1 and x2 < x1:  # 좌 : 같은 가로선, 왼쪽
#                 if d2 == 2:  # 같은 방향
#                     qs.append(x2)
#                 elif d2 == 3:  # 다른 방향
#                     qd.append(x2)
#             elif d1 == 3 and y2 == y1 and x2 > x1:  # 우 : 같은 가로선, 오른쪽
#                 if d2 == 3:  # 같은 방향
#                     qs.append(x2)
#                 elif d2 == 2:  # 다른 방향
#                     qd.append(x2)
#         qs.sort()
#         qd.sort()
#         for i in qd:
#             if qs:
#                 if d1 == 0 or d1 == 3:
#                     if qs[0] < i:
#                         qs.pop(0)
#                     else:
#                         res += k1
#                         break
#                 else:
#                     if qs[-1] > i:
#                         qs.pop(-1)
#                     else:
#                         res += k1
#                         break
#             else:
#                 res += k1
#                 break
# 
#     print(f'#{tc} {res}')

# map 그리기
T = int(input())  # 테스트 케이스 수
for tc in range(1, T + 1):
    N = int(input())
    arr = []
    for _ in range(N):
        x, y, d, k = map(int, input().split())
        arr.append([x*2, y*2, d, k])
    res = 0

    while arr:
        a_len = len(arr)
        a_del = [] # 지울 원자 목록
        for i in range(a_len):  # 남은 원자 이동
            if arr[i][2] == 0:  # 상
                arr[i][1] += 1
                if arr[i][1] > 2000:
                    a_del.append(i)
            elif arr[i][2] == 1:  # 하
                arr[i][1] -= 1
                if arr[i][1] < -2000:
                    a_del.append(i)
            elif arr[i][2] == 2:  # 좌
                arr[i][0] -= 1
                if arr[i][0] < -2000:
                    a_del.append(i)
            else:  # 우
                arr[i][0] += 1
                if arr[i][0] > 2000:
                    a_del.append(i)

        for i in range(a_len-1):    # 원자 충돌 확인
            q = []
            for j in range(i+1, a_len):
                if arr[i][0] == arr[j][0] and arr[i][1] == arr[j][1] and j not in a_del:
                    q.append(arr[j][3])
                    a_del.append(j)
            if q:
                a_del.append(i)
                q.append(arr[i][3])
                res += sum(q)

        a_del.sort(reverse=True)
        for i in a_del: # 지우기
            arr.pop(i)

    print(f'#{tc} {res}')