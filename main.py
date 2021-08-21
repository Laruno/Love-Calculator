# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1 = name1.lower()
name2 = name2.lower()

total_name = name1 + name2
Total_True = total_name.count('t') + total_name.count('r')+ total_name.count('u') + total_name.count('e')

Total_Love = total_name.count('l') + total_name.count('o')+ total_name.count('v') + total_name.count('e')

Love_scores = (Total_True * 10) + Total_Love

if Love_scores < 10 or Love_scores > 90:
  print(f"Your score is {Love_scores}, you go together like coke and mentos. ")
elif Love_scores > 40 and Love_scores < 50:
  print(f"Your score is {Love_scores}, you are alright together.")
else:
  print(f"Your score is {Love_scores}")

