def is_nondigits(char):
    if char == " " or not char.isdigit():
        return True
    else:
        return False
def is_sign(char):
    if char == "+" or char == "-":
        return True
    else:
        return False
    

s = "+-22"

sign = True
integer = 0
num_started = False
INT_MAX = 2**31 - 1
INT_MIN = -2**31

for char in s:

    if is_sign(char):
        if num_started:
            break
        else:
            num_started = True
            if char == "-":
                sign = False
    
    elif char.isdigit():
        integer = (integer * 10) + int(char)
        num_started = True

    elif not num_started and char == " ":
        continue

    elif not num_started and is_nondigits(char):
        break

    elif num_started and is_nondigits(char) or char == " ":
        break

if sign == False:
    integer = 0 - integer

if integer > INT_MAX:
    integer = INT_MAX
elif integer < INT_MIN:
    integer = INT_MIN

print(integer)

#LEETCODE SOLUTION 
#class Solution:
#    def is_nondigits(self, char):
#        if char == " " or not char.isdigit():
#            return True
#        else:
#            return False
#    def is_sign(self, char):
#        if char == "+" or char == "-":
#            return True
#        else:
#            return False
#
#    def myAtoi(self, s: str) -> int:
#        sign = True
#        integer = 0
#        num_started = False
#        num_started = False
#        INT_MAX = 2**31 - 1
#        INT_MIN = -2**31
#
#        for char in s:
#
#            if self.is_sign(char):
#                if num_started:
#                    break
#                else:
#                    num_started = True
#                    if char == "-":
#                        sign = False
#            
#            elif char.isdigit():
#                integer = (integer * 10) + int(char)
#                num_started = True
#
#            elif not num_started and char == " ":
#                continue
#
#            elif not num_started and self.is_nondigits(char):
#                break
#
#            elif num_started and self.is_nondigits(char) or char == " ":
#                break
#
#        if sign == False:
#            integer = 0 - integer
#
#        if integer > INT_MAX:
#            return INT_MAX
#        elif integer < INT_MIN:
#            return INT_MIN
#
#        return integer
        
        