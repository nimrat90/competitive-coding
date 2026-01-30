def find_median_sorted_arrays():
    print("--- Problem 3: Median of Two Sorted Arrays ---")
  
    print("Note: Please enter the arrays in SORTED order (e.g., 1 3 5).")
    try:
        input1 = input("Enter first sorted array: ")
        nums1 = [int(x) for x in input1.split()]
        
        input2 = input("Enter second sorted array: ")
        nums2 = [int(x) for x in input2.split()]
    except ValueError:
        print("Invalid input. Please enter integers.")
        return
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
        
    m, n = len(nums1), len(nums2)
    low, high = 0, m
    median = 0.0

    while low <= high:
        partitionX = (low + high) // 2
        partitionY = (m + n + 1) // 2 - partitionX
       
        maxLeftX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
        minRightX = float('inf') if partitionX == m else nums1[partitionX]
        
        maxLeftY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
        minRightY = float('inf') if partitionY == n else nums2[partitionY]
        
        if maxLeftX <= minRightY and maxLeftY <= minRightX:
        
            if (m + n) % 2 == 0:
                median = (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2
            else:
                median = max(maxLeftX, maxLeftY)
            break
        elif maxLeftX > minRightY:
            high = partitionX - 1
        else:
            low = partitionX + 1
            
    print(f"\nMerged Array (Conceptual): {sorted(nums1 + nums2)}")
    print(f"Calculated Median: {median}")

if __name__ == "__main__":
    find_median_sorted_arrays()