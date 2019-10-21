# coding: utf-8


class Solution(object):
    def search(self, nums, target):
        """
        这个题很迷。
        1.是对于旋转数组的定义：旋转数组是把一个有序数组的一部分放到后面去.23333
                             所以，tricky的是这样有两种情况：a.整个数组都是有序的;b.只有前半部分有序
        2.这个题很迷醉，所有边界条件几乎都是<=或>=，然后high和low的调整取值，都排除掉对应的就行。
          不然就会在else里面，死循环。大意是，例如nums[low] < target <= nums[mid]这个例子，只走到过target = nums[mid]这个case，
          但是在else包含的条件里面，是nums[low] >= target 或 nums[mid] < target 这个条件是在else里面，
          没有办法判断low = mid这个条件，是否在else里面走过，如果else-then的处理里面，假设low = mid条件没有走到过，则会一直走到这个分支。
          但实际上这个分支一定是走过的。 
          只有非常确定哪个分支一定走过了，才可以用这种。
        """
        res = -1
        if not nums:
            return res
        if len(nums) == 1 and target == nums[0]:
            return 0

        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) / 2
            if target == nums[mid]:
                return mid
            # 这块解释,看1.a.和1.b.
            if nums[mid] > nums[high]:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            elif nums[mid] <= nums[high]:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return res

if __name__ == '__main__':
    res = Solution().search([4, 5, 6, 7, 0, 1, 2], 0)
    print res