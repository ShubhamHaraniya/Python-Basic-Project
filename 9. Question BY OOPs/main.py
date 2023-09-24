from que_bank import question_data
class Question:
    def __init__(self,text,answer):
        self.que= text
        self.ans = answer
Que_Num = 0
True_Answer = 0
for questions in question_data:
    Que_Num += 1
    text_main = questions["text"]
    ans_main = questions["answer"]
    new_que = Question(text_main,ans_main)
    input_ans = input(f"{Que_Num}].{new_que.que}? ").lower()
    if input_ans == new_que.ans.lower():
        True_Answer += 1
print(f"YOUR TOTAL SCORE : {True_Answer} out of {Que_Num}")