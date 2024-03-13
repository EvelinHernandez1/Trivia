import random

class Question:
    def __init__(self, question, options, correct_answer):
        self.question = question
        self.options = options
        self.correct_answer = correct_answer
    #creación de comprensión de listas con condiciones y enumerate
    def display_question(self):
        print(self.question)
        formatted_options = [f"{i + 1}. {option}" for i, option in enumerate(self.options)]
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
                user_answer = input("Enter your answer (1-4): ")
                if user_answer.isdigit() and 1 <= int(user_answer) <= len(question.options):
                    user_answer = int(user_answer) - 1 # asignasión multiple: En esta sección, la entrada del usuario se convierte a un entero y luego se resta 1, todo en una sola línea, utilizando la asignación múltiple. Esto permite que user_answer se actualice con el valor correcto de la respuesta del usuario en un solo paso.
                    break
                print("Please enter a valid option number.")
            if question.check_answer(user_answer):
                print("Correct!")
                self.score += 1
            else:
                print("Incorrect!")
            print()
        
        print(f"Your final score is: {self.score}/{len(self.questions)}")

        # Creación de compresión de diccionario
        correct_answers_dict = {question.question: question.options[question.correct_answer] for question in self.questions}
        print("\nCorrect Answers:")
        # Implementación de zip para iterar sobre las claves y valores del diccionario
        for question, answer in zip(correct_answers_dict.keys(), correct_answers_dict.values()):
            print(f"{question}: {answer}")

# Iniciar el juego de trivia
game = TriviaGame()
game.play()
