#A python Simple calculator program without using Function
num1=float(input("enter the num1:"))
num2=float(input("enter the num2:"))

result={
    num1 + num2,
    num1 - num2,
    num1 * num2,
    num1 / num2,"error! Division by zero."
}
print("Result:",result)
