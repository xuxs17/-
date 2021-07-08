import random

def get_result(a):
    num = 2**len(a)
    result = []

    while len(result) < num:
        mid = []
        for i in range(len(a)):
            mid.append(''.join(random.sample(a[i], 1)))
        random_str = '|'.join(i for i in mid)

        if random_str not in result:
            result.append(random_str)
            print(result[-1])

# 使用时更改a中的维度数值即可
a = [['访问来源', '整体'], ['阅读频次','整体'], ['平台', '整体'], ['月龄', '整体'], ['阅读来源', '整体']]
get_result(a)
