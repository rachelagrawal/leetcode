class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Handle 32-bit signed integer overflow edge case
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
        
        # Determine sign of the result
        negative = (dividend < 0) != (divisor < 0)
        
        # Work with positive absolute values
        dvd = abs(dividend)
        dvs = abs(divisor)
        
        quotient = 0
        while dvd >= dvs:
            temp_dvs, multiple = dvs, 1
            while dvd >= (temp_dvs << 1):
                temp_dvs <<= 1
                multiple <<= 1
            dvd -= temp_dvs
            quotient += multiple
            
        # Apply sign
        if negative:
            quotient = -quotient
            
        # Clamp to 32-bit signed integer range [-2^31, 2^31 - 1]
        return max(-2147483648, min(quotient, 2147483647))
