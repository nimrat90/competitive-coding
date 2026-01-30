def product_except_self():
    print("--- Problem 2: Product of Array Except Self ---")
   
    user_input = input("Enter numbers separated by space (e.g., 1 2 3 4): ")
    try:
        nums = [int(x) for x in user_input.split()]
    except ValueError:
        print("Invalid input.")
        return

    length = len(nums)
    answer = [1] * length
    
    prefix = 1
    for i in range(length):
        answer[i] = prefix
        prefix *= nums[i]
    suffix = 1
    for i in range(length - 1, -1, -1):
        answer[i] *= suffix
        suffix *= nums[i]
        
    print(f"\nOriginal Array: {nums}")
    print(f"Result Array:   {answer}")

if __name__ == "__main__":
    product_except_self()