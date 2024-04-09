# -*- coding:utf-8 -*-
"""
作者：Zhakx
日期：2024年04月09日
"""

# Leetcode 1 两数之和

# 时间 48 ms 击败 65.18%

# 内存 17.7 MB 击败 5.11%
import bisect as b
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        nums = sorted(zip(nums, range(n))) # O(nlogn)

        # 以下部分时间复杂度为：O(nlogn)
        for i in range(n):
            t = target - nums[i][0]
            j = b.bisect_left(nums, (t, ), i + 1, n)
            if j < n and nums[j][0] == t:
                return [nums[i][1], nums[j][1]]

        return []


def main():
    solution = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    print(solution.twoSum(nums, target))


if __name__ == "__main__":
    main()
