import numpy as np
import pandas as pd

# def solution(A):
#     # if all neg, return 1
#     if max(A) < 1:
#         return 1
#     # has positive values
#     else:
#         A = np.array(A)
#         num = np.arange(1, max(A))
#         print(num)
#         A1 = np.sort(A)
#         print(A1)
#         for i in num:
#             find = 0
#             for j in A1:
#                 if i == j:p
#                     find += 1
#                     break
#             if find == 0:
#                 return i


# def solution(A):
#     # if all neg, return 1
#     if max(A) < 1:
#         return 1
#     # has positive values
#     else:
#         A = [x for x in A if x > 0]
#         A = sorted(A)
#         for i in range(max(A)):
#             find = 0
#             for j in A:
#                 if i + 1 == j:
#                     find += 1
#                     break
#             if find == 0:
#                 return i + 1
#         return max(A) + 1


# def solution(A):
#     m = max(A)
#     if m <= 0:
#         return 1
#     possible = set(e for e in range(1, m + 2)) - set(A)
#     return min(possible)


def solution(A):
    B = [x for x in A if x > 0]
    B = sorted(B)
    if 1 not in B:
        return 1
    for i in range(0, len(B) - 1):
        if B[i + 1] - B[i] > 1:
            return B[i] + 1
    return max(B) + 1


A = [-1, -3]
A = [1, 3, 6, 4, 1, 2]
print(solution(A))