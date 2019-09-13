def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    midpoint = len(lst) //2
    left, right = merge_sort(lst[:midpoint]), merge_sort(lst[midpoint:])
    return merge(left, right)

def merge(left, right):
    result = []
    left_point = right_point = 0
    while left_point < len(left) and right_point < len(right):
        if left[left_point] < right[right_point]:
            result.append(left[left_point])
            left_point += 1
        else:
            result.append(right[right_point])
            right_point += 1

    result.extend(left[left_point:])
    result.extend(right[right_point:])
    return result


emoney = [1, 6, 3, 7, 8, 9, 4, 2, 0]
print(emoney, merge_sort(emoney))
