def three_sum(nums):
    nums.sort()
    triplets = []

    for i, a in enumerate(nums):
        if a > 0:
            break
        if i>0 and a == nums[i-1]:
            continue
        l, r = i+1, len(nums) - 1
        while l < r:
            total = a + nums[l] + nums[r]
            if total > 0:
                r-=1
            elif total < 0:
                l+=1
            else:
                triplets.append([a, nums[l], nums[r]])
                l+=1
                r-=1
                while nums[l] == nums[l-1] and l<r:
                    l+=1
    print(triplets)
    return triplets

# three_sum([-1,0,1,2,-1,-4])

def trap(height):
    n = len(height)
    if n <= 2:
        return 0
    left_max = [0] * n
    right_max = [0] * n
    left_max[0] = height[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i-1], height[i])

    right_max[n-1] = height[n-1]
    for i in range(n-2, -1, -1):
        right_max[i] = max(right_max[i+1], height[i])
    trapped_water = 0
    for i in range(n):
        trapped_water += min(left_max[i], right_max[i]) - height[i]
    print(left_max)
    print(right_max)
    print(trapped_water)
    return trapped_water

# trap([0,1,0,2,1,0,1,3,2,1,2,1])

def maxProfit(prices):
    profit = 0
    lowest = prices[0]

    for price in prices[1:]:
        if price < lowest:
            lowest = price
        if price - lowest > profit:
            profit = price - lowest
    print(profit)
    return profit

# maxProfit([7, 4, 2, 3, 1, 6, 4, 11])


def lengthOfLongestSubstring(s):
    if not s:
        return 0
    
    char_set = set()
    max_length = 0
    left = 0

    for right in range(len(s)):
        print(char_set)
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        print(char_set)
        print('xxx')
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)

    print(max_length)

lengthOfLongestSubstring("pwwkewslkhjg")
