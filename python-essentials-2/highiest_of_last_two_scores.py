"""
Part 2: Highest of Last Two Scores
Create a class called StudentScores which does the following:

Takes a list of scores as input while creating the object.

Create a method called highest_last_two() which:

Finds the highest score among the last two scores using negative indexing.
If the list has less than 2 scores, handle it using exception handling and print:
Not enough scores to find highest value
Example Input:

scores = [45, 67, 89, 72]
Output:

Highest score among last two is: 89
"""


class StudentScores:
    def __init__(self, score_list):
        self.score_list = score_list

    def highest_last_two(self):
        score_card = self.score_list
        if len(score_card) < 2:
            raise Exception("Not enough scores to find highest value")
        else:
            last1 = score_card[-1]
            last2 = score_card[-2]
            if last1 > last2:
                return last1
            else:
                return last2


score_obj1 = StudentScores([45, 67, 89, 72])
print(f"Highest score among last two is: {score_obj1.highest_last_two()}")

score_obj2 = StudentScores([72])
print(f"Highest score among last two is: {score_obj2.highest_last_two()}")
