def is_palindrome(s):
   
  
    cleaned = ''.join(filter(str.isalnum, s)).lower()
    return cleaned == cleaned[::-1]

# Run the program
if __name__ == "__main__":
   

    # Example usage of is_palindrome
    test_string = input("\nEnter a string to check for palindrome: ")
    if is_palindrome(test_string):
        print(f"'{test_string}' is a palindrome.")
    else:
        print(f"'{test_string}' is not a palindrome.")
