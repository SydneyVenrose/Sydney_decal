#1. def computePower(x, y):
    # computePower returns x raised to the power y without using ** or pow
   # result = 1
    #for _ in range(y):
        #result = result * x  # You could also call dollproduct(x, result) if you want
   #return result 
#print(computePower(2, 3))

#2. def temperatureRange(readings):
    # Returns a tuple of (min_temp, max_temp)
    #return (min(readings), max(readings))
    #readings = [15, 14, 17, 20, 23, 28, 20]
    #print(temperatureRange(readings))  

#3. def isWeekend(day):
    # If day is 6 (Saturday) or 7 (Sunday), it's the weekend
   # return day == 6 or day == 7

# Example usage
#day = 6
#print(isWeekend(day))  # Output: True

#4. def fuel_efficiency(distance, fuel):
    #return distance / fuel

# Example usage
#distance = 70      # in miles
#fuel = 21.5        # in gallons
#print(fuel_efficiency(distance, fuel))  # Output: 3.26

#5 def decodeNumbers(n):
    #last_digit = n % 10              # Get the last digit
    #rest = n // 10                   # Remove the last digit
    #digits = 1

    # Count how many digits are in the 'rest'
    #temp = rest
    #while temp > 0:
        #temp = temp // 10
        #digits += 1

    #return last_digit * (10 ** digits) + rest

#6. def find_max_with_for_loops(nums):
   # max_val = nums[0]  # Start by assuming the first number is the biggest
    #$for num in nums:
        #if num > max_val:
            #max_val = num  # Found a new bigger number
    #return max_val

#7. def find_min_with_while_loop(nums):
   # i = 0
   #min_val = nums[0]
    #while i < len(nums):
       # if nums[i] < min_val:
           # min_val = nums[i]
       # i += 1
    #return min_val
# def find_max_with_while_loops(nums):
    #i = 0
    # max_val = nums[0]
   # while i < len(nums):
      #  if nums[i] > max_val:
           # max_val = nums[i]
       # i += 1
   # return max_val

#8. def vowel_and_consonant_count(text):
   # vowels = "aeiouAEIOU"
   # vowel_count = 0
   # consonant_count = 0

   # for char in text:
      #  if char.isalpha():  # Check if it's a letter (ignores punctuation/numbers)
          #  if char in vowels:
           #     vowel_count += 1
           # else:
            #    consonant_count += 1

   # return (vowel_count, consonant_count)
#9. def digital_root(num):
    # Step 1: Sum the digits
   # total = 0
    # n = num
   # while n > 0:
       # total += n % 10
       # n = n // 10

    # Step 2: Digital root (sum until 1 digit)
    # root = total
    # while root >= 10:
        # temp = 0
       #  while root > 0:
          #  temp += root % 10
         #   root = root // 10
      #  root = temp

   # return total, root