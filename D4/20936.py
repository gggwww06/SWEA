# 20936. 상자 정렬하기

# 정렬 확인
# def is_sorted(list_l):
#     for a, b in enumerate(list_l):
#         if (a+1) != b:
#             return False
#     return True

def is_sorted(list_l):
    for a, b in enumerate(list_l[:-1]):
        if (a+1) != b:
            return a
    return False

T = int(input())

for _ in range(T):
    box_n = int(input())
    box_st = list(map(int, input().split())) + ['X']
    # print(box_st)

    index_x, index_i = 0, 0
    k = []
    # if is_sorted(box_st):
    #     # 첫 번째 숫자를 X로 이동 -> X
    #     if box_st[box_n] == 'X':
    #         box_st[0], box_st[box_n] = box_st[box_n], box_st[0]
    #         k.append(1)
    #     while is_sorted(box_st):  # 남은 index에 남은 숫자들 이동
    #         index_x = box_st.index('X')
    #         index_i = box_st.index(index_x + 1)
    #         box_st[index_x], box_st[index_i] = box_st[index_i], box_st[index_x]
    #         k.append(index_i + 1)
        # print(box_st)
    a = is_sorted(box_st)
    while a is not False:
        if box_st[box_n] == 'X':
            box_st[a], box_st[box_n] = box_st[box_n], box_st[a]
            k.append(a+1)
        else:  # 남은 index에 남은 숫자들 이동
            index_x = box_st.index('X')
            index_i = box_st.index(index_x + 1)
            box_st[index_x], box_st[index_i] = box_st[index_i], box_st[index_x]
            k.append(index_i + 1)
        a = is_sorted(box_st)

    print(len(k))
    print(" ".join(map(str, k)))
    # print(box_st)
