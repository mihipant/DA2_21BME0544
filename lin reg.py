def lin_reg():
    global a, b
    b= ((n*xy_sum) - ((x_sum)*(y_sum)))/((n*x2_sum)-((x_sum)*(x_sum)))
    a= (((y_sum)*(x2_sum)) - ((x_sum)*(xy_sum)))/(((n*x2_sum)- ((x_sum)*(x_sum))))

x_sum=0
y_sum=0
xy_sum=0
x2_sum=0

n= int(input("Enter number of known values: "))
i=1
while i <= n:
    x= int(input("Enter the altitude of living: "))
    y= int(input("Enter value of temperature recorded: "))
    xy= x*y
    x2= x*x
    x_sum += x
    y_sum += y
    xy_sum += xy
    x2_sum += x2
    i+=1

x_val= int(input("Enter the Altitude for which temperature needs to be calculated: "))

lin_reg()
y_val= a + b*x_val

print("Value of temperature for given value of altitude: ", y_val)
