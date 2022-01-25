PI = 3.14
r = float(input("Enter the radius of a circle:"))
area = PI * r * r
print("Area of a circle = %.2f" %area)
fn= input("Enter Filename: ")

f = fn.split(".")

print ("Extension of the file is : " + f[-1])
