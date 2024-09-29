import unittest


class MyTestCase(unittest.TestCase):
    # 二分搜索
    def test_search(self, nums: List[int], target: int) -> int:
        if len(nums) <= 0:
            return -1
        left_index, right_index = 0, len(nums) - 1

        while left_index <= right_index:
            middle = left_index + (right_index - left_index)//2
            if target < nums[middle]:
                right_index = middle - 1
            elif target > nums[middle]:
                left_index = middle + 1
            else:
                return middle
        return -1





if __name__ == '__main__':
    unittest.main()
