
marks_dict = {}

for i in range(1, 9):
    roll_number = int(input(f"Enter roll number: "))
    marks = [int(x) for x in input(f"Enter three marks for roll {roll_number}: ").split()]
    marks_dict[roll_number] = marks

for roll, marks in marks_dict.items():
    total_marks = sum(marks)
    average_marks = total_marks / len(marks)
    print(f"Average marks of Roll {roll} is {average_marks:.2f}")
    