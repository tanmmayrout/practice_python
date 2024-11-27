#Practice for functions 27th November
#Program to accept values and find the average and then grade

def find_percentage(n1,n2,n3,n4):
    total= n1+n2+n3+n4
    result=(total/400)*100

    return result

def grade_compute(average_marks):
    if average_marks>=90:
        grade = 'A'
    elif average_marks>=80:
        grade = 'B'
    elif average_marks>=70:
        grade = 'C'
    elif average_marks>=60:
        grade = 'D'
    elif average_marks>=50:
        grade = 'E'
    else:
        grade = 'F'
    return grade


no1=(int(input("Enter your English marks ")))
no2=(int(input("Enter your Maths marks ")))
no3=(int(input("Enter your Science marks ")))
no4=(int(input("Enter your SST marks ")))

total_percentage= find_percentage(no1,no2,no3,no4)

print("Your Percentage is",total_percentage)

Your_grade=grade_compute(total_percentage)

print("Your grade is ", Your_grade)

