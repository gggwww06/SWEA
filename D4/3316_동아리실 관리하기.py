# 3316. 동아리실 관리하기

T = int(input())
memberdict = {'A':1, 'B':2, 'C':4, 'D':8}

for tc in range(1, T + 1):
    chackim = input()
    members = [0] * 16
    members[1] = 1
    for n_mem in chackim:
        new_members = [0] * 16
        for b_mem in range(1, 16):  # 이전 경우의 수 목록
            if members[b_mem] == 0:
                continue
            for i in range(1, 16):  # 현재 경우의 수 목록
                if memberdict[n_mem] & i == 0:  # 필수 참가
                    continue
                if b_mem & i > 0:  # 겹치는 거 있음
                    new_members[i] += members[b_mem]
        members = new_members

    print(f'#{tc} {sum(members) % 1000000007}')
    
    
# 뭐가 다른거지
# 앞부분은 비슷한데 for문이 다름 메모리 제일 적고 제일 빠름
#
# for st in string:
#     today = bin_dict[st]  # 오늘의 책임자
#     for before, val in enumerate(b_arr):
#         if val != 0:
#             for x in range(16):
#                 # x와 before가 같고 today도 같은 경우
#                 if (x & before) and (x & today):
#                     t_arr[x] += val % 1000000007
#     b_arr = t_arr
#     ans = sum(t_arr) % 1000000007
#     t_arr = [0] * 16