list = []

running = True

while running:
 print("1.Create")
 print("2.Read")
 print("3.Update")
 print("4.Delete")
 print("5.Exit")

 print("\n Please enter a number: ", end="")
 ans = int(input())

 if ans == 1:
     print("Enter a name please: ", end="")
     y = input()
     list.append(y)
     continue

 elif ans == 2:
     print(list)
     continue

 elif ans == 3:
     print("please enter a valid index: ", end="")
     y = int(input())

     print(list[y] + " is selected, now enter a new name: ", end="")

     z = input()
     list[y] = z
     print("Update successful!")
     continue
 elif ans == 4:
     print(list)
     print("please type which name do you want to delete: ", end="")
     y = input()
     list.remove(y)

     print("Delete successful!")
     continue

 elif ans == 5:
     print("Exit the system? Y/N: ", end="")
     x =  input()

     if x == "Y":
         running = False

     else:
      continue
 break


