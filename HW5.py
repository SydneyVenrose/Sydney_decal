# HW5 - Review
# Answering questions as Judy

# 1. You have been plopped into this directory system. What command will tell you what your working directory is?
# Command: pwd

# 2. The command tells you ∼/python_decal/judy_decal. What command with list all the files in your current working directory?
# Command: ls

# 3. Brianna just sent out an announcement that there was a typo on homework.py. 
# So you need to pull the updates. What commands will let you move to the correct repository and pull the latest changes?
# Commands:
# cd ~/python_decal/judy_decal
# git pull origin main

# 4. How would you move this new homework.py to your personal repository homework directory?
# Command: mv homework.py ~/python_decal/judy_decal/homework/

# 5. You want to see the contents of the homework.py in your terminal from your personal repository. 
# What command(s) will let you do this?
# Command: cat homework.py

# 6. You want to edit the contents of the homework.py in your terminal from your personal repository. 
# What command will let you do this?
# Command: nano homework.py

# 7. You have finished the homework. What commands will allow you to save the changes and push from your local repository to your remote repository?
# Commands:
# git add homework.py
# git commit -m "Finished homework"
# git push origin main

# 8. Oh no! Git gave you the following error. What commands should you call to resolve this error and push your homework properly? What does the error mean? 
# Error: ! [rejected] main -> main (fetch first)
# Hint: Updates were rejected because the remote contains work that you do not have locally. 
# Solution:
# git pull origin main
# git push origin main
# The error means that there are changes in the remote repository that you don't have locally. You need to pull those changes before pushing your own.

# 9. What absolute path will allow you to move to Recents/?
# Command: cd /Users/judy/Recents/

# HW3 Review: Data Types + Functions + Conditionals + Loops

# 2.1 Data Types
#def checkDataType(input):
   # return str(type(input).__name__)

# Test cases
#print(checkDataType(3.14))  # 'float'
#print(checkDataType(True))  # 'bool'


# 2.2 Conditionals
#def evenOrOdd(num):
    #if num % 2 == 0:
      #  return "Even"
   # else:
   #     return "Odd"

# Test cases
#print(evenOrOdd(7))  # 'Odd'
#print(evenOrOdd(10))  # 'Even'


# 3 Loops
#def sumWithLoop(numbers):
    #total = 0
    #for number in numbers:
       # total += number
   # return total

# Test case
#numbers = [1, 2, 3, 4, 5]
#print(sumWithLoop(numbers))  # 15
