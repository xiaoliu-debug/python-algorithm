"""二分查找（Binary Search）

思路回顾：
1. 前提：列表 arr 必须已经排好序（从小到大）。
2. 维护一个搜索区间 [left, right]，一开始覆盖整个列表。
3. 每次取区间中间位置 mid，比较 arr[mid] 与 target：
   - arr[mid] == target -> 找到，返回 mid
   - arr[mid] <  target -> 目标在右半边，left  = mid + 1
   - arr[mid] >  target -> 目标在左半边，right = mid - 1
4. 区间不断缩小，直到 left > right（区间为空）说明没找到，返回 -1。
"""


def binary_search(arr, target):
    """在已排序列表 arr 中查找 target，返回其下标；找不到返回 -1。"""
    left, right = 0, len(arr) - 1

    while left <= right:              # 空①：循环条件
        mid = (left + right) // 2     # 空②：中点怎么算
        if arr[mid] == target:
            return mid                # 空③：找到了返回下标
        elif arr[mid] < target:
            left = mid + 1            # 空④：目标在右边，left 右移
        else:
            right = mid - 1           # 空⑤：目标在左边，right 左移

    return -1                         # 没找到，兜底返回


if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9, 11, 13]
    print(binary_search(arr, 7))    # 期望输出: 3
    print(binary_search(arr, 8))    # 期望输出: -1
    print(binary_search(arr, 1))    # 期望输出: 0
    print(binary_search(arr, 13))   # 期望输出: 6
