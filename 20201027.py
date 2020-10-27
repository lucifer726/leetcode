def removeDuplicates(nums):
    a = 0
    b = 1
    while b < len(nums):
        if nums[b] == nums[a]:
            b += 1
        else:
            a += 1
            nums[a] = nums[b]
    return nums[:a+1]


if __name__ == '__main__':
    print(removeDuplicates([1, 1, 2, 3, 3, 4, 5, 5]))
