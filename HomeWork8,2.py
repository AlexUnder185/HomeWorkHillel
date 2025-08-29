def is_palindrome(text):
    some_name = ''.join(ch.lower() for ch in text if ch.isalnum())
    return some_name == some_name[::-1]


assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")
