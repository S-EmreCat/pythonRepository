class Question:
    def __init__(self,text,choices,answer):
        self.text = text
        self.choices = choices
        self.answer = answer
        
    def checkAnswer(self,answer):
        if answer not in self.choices:
            raise Exception("hatalı seçim")
        return self.answer == answer
    


class QuizApp:
    def __init__(self, questions):
        self.questions = questions
        self.questionIndex = 0
        self.score = 0
        
    
    def getQuestion(self):
        return self.questions[self.questionIndex]
    
    def displayQuestion(self):
        question = self.getQuestion()
        print(f'Soru {self.questionIndex+1}: {question.text}')
        for i in question.choices:
            print(f'- {i}')
        
        answer = input("cevap giriniz: ")
        if question.checkAnswer(answer):
            self.score += 1
            print("Tebrikler bildiniz...")
            
        self.questionIndex += 1 
        self.loadQuestion()
        
    def loadQuestion(self):
        if len(self.questions) == self.questionIndex:
            self.displayScore()
        else: 
            self.displayProgress()
            self.displayQuestion()
    
    def displayScore(self):
        point = 100 / len(self.questions)
        totalScore = round(self.score * point)
        print(f'Toplam {len(self.questions)} sorudan {self.score} tanesini bildniz')
        print(f'Toplam puan: {totalScore}')
    
    def displayProgress(self):
        totalQuestion = len(self.questions)
        questionNumber = self.questionIndex + 1
        print(f'toplam {totalQuestion} sorudan {questionNumber}. sorudasınz'.center(100,"*"))
        
q1 = Question("en iyi programlama dili hangisidir?",["python","c#","java","dart"],"python")
q2 = Question("en popüler programlama dili hangisidir?",["python","java","c#","dart"],"python")
q3 = Question("en çok kazandıran programlama dili hangisidir?",["python","java","dart","c#"],"python")

questions = [q1,q2,q3]

quiz  = QuizApp(questions=questions)
print(quiz.loadQuestion())
