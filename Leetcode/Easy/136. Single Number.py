from typing import List

"""
We can use three xor properties which are:
1 : num xor num = 0
2: xor is commutative meaning a ^ b = b ^ a or in other words the order of operands does not change the outcome.
3: num xor 0 = num

Because of property 2  we can think of the array as sorted pairs with one unique number for example: [1,1,4,4,5]

Because of property 1 we can xor go through the array and xor each number by it's neighbour which will get us 0.
And at the end we will arrive at 0 xor our number which is our number according to property 3.

"""


def singleNumber(nums: List[int]) -> int:
    output = 0
    for num in nums:
        output ^= num
    return output