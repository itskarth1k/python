studentname=input("enter your name: ")
std=int(input("enter your std: "))
number_of_subjects=int(input("enter number of subjects:"))
english=float(input("enter your english mark:"))
maths=float(input("enter your maths mark:"))
chemistry=float(input("enter your chemistry mark:"))
physics=float(input("enter your physics mark:"))
computerscience=float(input("enter your computerscience mark :"))
totalmarks=english+maths+chemistry+physics+computerscience
print("total subject marks",totalmarks)
avg=totalmarks/number_of_subjects
print("The average of total marks",avg)