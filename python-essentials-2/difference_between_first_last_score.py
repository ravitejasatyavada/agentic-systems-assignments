"""
Part 3: Difference Between First and Last Score
Create a class called StudentPerformance which does the following:

Takes a list of scores as input while creating the object.

Create a method called score_difference() which:

Finds the difference between the last score and the first score using indexing.
If the list is empty, handle it using exception handling and print:
No scores available to calculate difference
Example Input:

scores = [55, 65, 75, 85]
Output:

Difference between last and first score is: 30
"""


class StudentPerformance:
    def __init__(self, score_card):
        self.score_card = score_card

    def score_difference(self):
        score_list = self.score_card
        if len(score_list) < 1:
            raise Exception("No scores available to calculate difference")
        return score_list[-1] - score_list[0]


obj1 = StudentPerformance([55, 65, 75, 85])
print(f"Difference between last and first score is: {obj1.score_difference()}")

obj2 = StudentPerformance([85])
print(f"Difference between last and first score is: {obj2.score_difference()}")

obj3 = StudentPerformance([])
print(f"Difference between last and first score is: {obj3.score_difference()}")
