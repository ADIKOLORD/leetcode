# Number 1
"""

'''
82 . Удалить дубликаты из отсортированного списка II   42,8%     Середина
Given the head of a sorted linked list, delete all nodes that have duplicate numbers,
leaving only distinct numbers from the original list.
Return the linked list sorted as well.
Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]
Input: head = [1,1,1,2,3]
Output: [2,3]
'''
def delete_all_list(numbers, number):
    '''
    Если элемент в списке больше 1, то удаляет все похожие на него элементы, включая и себя.
    :param numbers: list
    :param number: Все типы данных
    :return: unical elements
    '''
    vrem = []
    for i in numbers:
        if i != number:
            vrem.append(i)
    return vrem

head = sorted(input('Text numbers: ').split())
print(head)
for i in head:
    if head.count(i) > 1:
        head = delete_all_list(head, i)
print(head)

"""

# Number 2
"""

'''

Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, 
and you may not use the same element twice.

You can return the answer in any order.
Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
'''
nums = [i for i in range(17)]
target = int(input('Text target: '))
output = []
for i in range(len(nums) - 1):
    vrem = []
    if nums[i] + nums[i + 1] == target:
        vrem.append(i)
        vrem.append(i + 1)
        output.append(vrem)
print(output)

"""

# Number 3
"""
'''
4. Median of Two Sorted Arrays     33.8%      Hard
Given two sorted arrays nums1 and nums2 of size m and n respectively, 
return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4,5,6] and median is (2 + 3) / 2 = 2.5.

'''

nums1 = [1, 2, 5]
nums2 = [3, 4]
mainlist = sorted(nums1 + nums2)

if len(mainlist) % 2 == 0:
    m = int(len(mainlist) / 2)
    res = (mainlist[m - 1] + mainlist[m]) / 2
    print(res)
else:
    m = int(len(mainlist) / 2)
    res = mainlist[m]
    print(res)
"""

# Number 4
"""

'''
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

'''

l1 = [2, 4, 3]
l2 = [5, 6, 4]
num1 = ''
num2 = ''
output = []
for i in reversed(l1):
    num1 += ''.join(str(i))
for j in reversed(l2):
    num2 += ''.join(str(j))
res = str(int(num1) + int(num2))
for k in res[::-1]:
    output.append(int(k))
print(output)
"""

# Number 5
'''
Given a string s, return the longest palindromic substring in s.

Example 1:

Input: s = "babad" 
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:

Input: s = "cbbd"
Output: "bb"

'''

s = "babad"
mainlist = []
for i in range(len(s)):
    a = s[i]
    b = (s[::-1])[i]
    if a == b:
        mainlist.append(a)
print(mainlist)

