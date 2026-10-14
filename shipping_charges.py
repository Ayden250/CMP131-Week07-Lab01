#Ayden Suarez
#Lab 1
#CMP_131
#Week 7
miles_shipped=int(input("enter amount of miles: "))
package_weight= int(float("Enter a value of kilograms: "))
while(package_weight<0 or package_weight<20):
    print("Invalid")
while(miles_shipped>10 or miles_shipped<3000):
    print("Inavlid")
