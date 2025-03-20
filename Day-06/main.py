num = int(input("Enter An Integer: "))

binary_num = bin(num)[2:]
if binary_num == binary_num[::-1]:
    print(f"Binary: {binary_num}")
    print("Output: Palindrome ✅")
else:
    print(f"Binary: {binary_num}")
    print("Output: Not a Palindrome ❌")
