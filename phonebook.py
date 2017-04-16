phone_book = dict()
size = input("Enter the size of phone book : ")
print("**** Loading phone book with user data *** ")
for i in range(0, size):
    name = raw_input("Enter name: ")
    number = input("Enter number: ")
    phone_book.update({name:number})

print phone_book

print " *** Searching in phone book ***"

search = raw_input("Enter the search String : ")
print("Name : %s  and Number : %s" %(search,phone_book.get(search,"Not Found")))



search = raw_input("Enter the search String : ")
print("Name : %s  and Number : %s" %(search,phone_book.get(search,"Not Found")))
