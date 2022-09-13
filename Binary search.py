try:
    def binarySearch():
        a = []
        num = int(input("Enter the number of elements in list: "))
        for i in range(num):
            number = int(input("Enter a number: "))
            a.append(number)
        mn = 0
        mx = len(a)
        mid = c = 0
        n = int(input("Enter the number you wish to search: "))
        print("The list you entered is: " + str(a))
        while(mn <= mx):
            mid = int((mn+mx)/2)
            if(n == a[mid]):
                c += 1
                print("Number found at " + str(mid + 1))
                break
            elif(n > a[mid]):
                mn = mid + 1
            elif(n < a[mid]):
                mx = mid - 1
    
        if(c == 0):
            print("Number not found")

    binarySearch()
    
except ValueError:
    print("Enter a number and not a string")
except IndexError:
    print("You cannot have zero elements in a list")
except:
    print("Enter correctly")