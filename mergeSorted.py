def merge(nums1, m, nums2, n):
        
    if m == 0:  
        nums1[:] = nums2[:]
        return 1

    if n == 0:
        return 1

    i = m - 1  # Pointer for the last element in nums1's initialized part
    j = n - 1  # Pointer for the last element in nums2
    k = m + n - 1  # Pointer for the last position in nums1

    # Merge in reverse order
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1

    # If there are remaining elements in nums2, copy them
    while j >= 0:
        nums1[k] = nums2[j]
        k -= 1
        j -= 1




if __name__ == "__main__":
    nums1 = [4,5,6,0,0,0]
    m = 3
    nums2 = [1,2,3]
    n = 3

    merge(nums1,m,nums2,n)
    print(nums1)