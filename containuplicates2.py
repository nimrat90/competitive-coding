def contains_nearby_duplicate():
    print("--- Problem 1: Contains Duplicate II ---")
    user_input = input("Enter numbers separated by space (e.g., 1 2 3 1): ")
    try:
        nums = [int(x) for x in user_input.split()]
    except ValueError:
        print("Invalid input. Please enter integers only.")
        return
    try:
        k = int(input("Enter the distance k (e.g., 3): "))
    except ValueError:
        print("Invalid input. k must be an integer.")
        return

    index_map = {}
    found = False
    
    print(f"\nChecking array: {nums} with k={k}...")
    
    for i, num in enumerate(nums):
        if num in index_map and abs(i - index_map[num]) <= k:
            print(f"-> Found duplicate '{num}' at indices {index_map[num]} and {i} (distance {abs(i - index_map[num])})")
            found = True
            break
        
        index_map[num] = i
    
    print(f"\nResult: {found}")

if __name__ == "__main__":
    contains_nearby_duplicate()