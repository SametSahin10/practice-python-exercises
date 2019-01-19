user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))
year_born = 2019 - user_age
after_100 = year_born + 100

print("{}; in {}, you will turn 100 years old.".format(user_name, after_100))
