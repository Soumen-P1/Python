a = int(input("enter number "))

match a:
    case 1:
        print("Case is 1")
    case 2:
        print("Case is 2")
    case 13:
        print("Case is 13")
    case _:
        print("no case is found")
