#Reverse 
# Understand examples

# 123 → 321 ✅

# -123 → -321 ✅ (negative sign stays in front)

# 120 → 21 ✅ (leading zero drops after reversing)

class Solution:
    def reverse(self, x: int) -> int:
        int_max= 2**31 - 1
        int_min= 2**31

        rev=0
        sign= -1 if x<0 else 1
        x= abs(x)

        while x != 0:
            digit = x % 10
            x //=10
            if rev > int_max // 10 or (rev == int_max // 10 and digit > 7):
                return 0
            
            rev = rev * 10 + digit
        
        return sign * rev

