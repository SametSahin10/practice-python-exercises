user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))
number_of_print = int(input("Enter the number to print the message for: "))
year_born = 2019 - user_age
after_100 = year_born + 100

print(number_of_print * "{}; in {}, you will turn 100 years old.\n"
      .format(user_name, after_100))
