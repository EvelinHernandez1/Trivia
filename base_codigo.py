import random

class Question:
    def __init__(self, question, options, correct_answer):
        self.question = question
        self.options = options
        self.correct_answer = correct_answer
    #creación de comprensión de listas con condiciones y enumerate
    def display_question(self):
        print(self.question)
        formatted_options = [f"{i + 1}. {option}" for i, option in enumerate(self.options) if i + 1 in range(1, 5)]
        print('\n'.join(formatted_options))

    def check_answer(self, user_answer):
        return user_answer == self.correct_answer

class TriviaGame:
    def __init__(self):
        self.questions = [
            Question("What is not a principle of animation?", ["Anticipation", "Staging", "Squash and enlarging", "Arc"], 2),
            Question("which is not a 3D software?", ["Krita", "Zbrush", "Maya", "Blender"], 0),
            Question("What is a design element?", ["Segmentation", "Landscape", "Point", "Translation"], 2),
            Question("Which geometry is preferred for 3D environments?", ["N-gon", "Quad", "Triangle", "Circle"], 1),
            Question("What is the complementary of purple?", ["Red", "Pink", "Yellow", "Orange"], 2)
        ]
        self.score = 0

    def play(self):
        random.shuffle(self.questions)
        for question in self.questions:
            question.display_question()
            while True:
                try:
                    user_answer = int(input("Enter your answer (1-4): ")) - 1
                    if user_answer not in range(0, 4):
                        raise ValueError("Please enter a number between 1 and 4.")
                    break
                except ValueError as e:
                    print(e)
            if question.check_answer(user_answer):
                print("Correct!")
                self.score += 1
            else:
                print("Incorrect!")
            print()
        
        print(f"Your final score is: {self.score}/{len(self.questions)}")

# Iniciar el juego de trivia
game = TriviaGame()
game.play()
