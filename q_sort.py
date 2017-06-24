# coding=utf-8
# http://blog.csdn.net/morewindows/article/details/6684558
num_list = [4, 1, 2, 5, 123, 123, 1]


def q_sort(num_list, start, end):
    if start < end:
        x = num_list[start]
        i = start
        j = end
        while i < j:
            while i < j and num_list[j] >= x:
                j -= 1
            if i < j:
                num_list[i] = num_list[j]
                i += 1
            while i < j and num_list[i] <= x:
                i += 1
            if i < j:
                num_list[j] = num_list[i]
                j -= 1
        num_list[i] = x
        q_sort(num_list, start, i - 1)
        q_sort(num_list, i + 1, end)


q_sort(num_list, 0, len(num_list) - 1)

print num_list
