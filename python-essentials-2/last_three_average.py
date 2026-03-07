""""
Part 1: Last Three Average
Create a class called StudentMarks which does the following:

Takes a list of marks as input while creating the object.
Create a method called last_three_avg() which:
Finds the average of the last three marks using negative indexing. If the list has less than 3 marks, handle it using exception handling and print:
Not enough marks to calculate average
Example Input:

marks = [50, 60, 70, 80, 90]
Output:

Average of last 3 marks is: 80.0
"""


class StudentMarks:

    def __init__(self, student_marks: List):
        self.student_marks = student_marks

    def last_three_avg(self):
        marks_list = self.student_marks
        if len(marks_list) < 3:
            raise Exception("Not enough marks to calculate average")
        else:
            return (marks_list[-1] + marks_list[-2] + marks_list[-3])/3


marks = StudentMarks([50, 60, 70, 80, 90])
print(f"Average of last 3 marks is: {marks.last_three_avg()}")

marks1 = StudentMarks([80, 90])
print(f"Average of last 3 marks is: {marks1.last_three_avg()}")
