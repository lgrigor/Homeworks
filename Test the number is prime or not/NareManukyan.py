
def get_prime_number(num):
   if num > 1:
       for n in range(2, num):
           if num % n == 0:
               print(num, "is not a prime number")
               return False
     
   else:
      return True
   print(num, "is a prime number")

get_prime_number(int(input("Enter a number: ")))


