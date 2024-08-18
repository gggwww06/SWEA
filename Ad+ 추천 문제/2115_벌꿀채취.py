# 2115. [모의 SW 역량테스트] 벌꿀채취

T = int(input())  # 테스트 케이스 수
for tc in range(1, T + 1):
    N, M, C = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    res = []

    for i in range(N):
        im = 0
        for j in range(N-M+1):
            h = arr[i][j:j+M]
            h.sort(reverse=True)
            for l in range(M):
                cnt = mm = 0
                for k in h[l:]:
                    if k+cnt > C:
                        continue
                    else:
                        cnt += k
                        mm += k*k
                im = max(im, mm)
        res.append(im)
    res.sort(reverse=True)

    print(f'#{tc} {sum(res[:2])}')
