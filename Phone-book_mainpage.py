import Phone_book_module

print ()
#Verabils
c1 = Phone_book_module.p1
c2 = Phone_book_module.p2
c3 = Phone_book_module.p3
c4 = Phone_book_module.b1
c5 = Phone_book_module.b2

P1 = Phone_book_module.n1
P2 = Phone_book_module.n2
P3 = Phone_book_module.n3
P4 = Phone_book_module.n4
P5 = Phone_book_module.n5

Ad1 = Phone_book_module.ad1
Ad2 = Phone_book_module.ad2
Ad3 = Phone_book_module.ad3
Ad4 = Phone_book_module.ad4
Ad5 = Phone_book_module.ad5

#User Input: depending on what the people pick one of the lines will be used
lookup1 = (input("Who are you looking for "))

if lookup1 == "c1":
    print ("Here is your info", c1,P1,Ad1)
elif lookup1 == "c2":
    print ("Here is your info", c2,P2,Ad2)
elif lookup1 == "c3":
    print ("Here is your info", c3,P3,Ad3)
elif lookup1 == "c4":
    print ("Here is your info", c4,P4,Ad4)
elif lookup1 == "c5":
    print ("Here is your info", c5,P5,Ad5)
else:
    print("That contact does not exist")

print ("Thank you for using this PhoneBook")