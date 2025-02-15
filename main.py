# main.py
from app.ai.enums.topic import Topic
from app.ai.questionGenerator import QuestionGenerator

if __name__ == "__main__":
    # Initialize the question generator
    print("Loading models")
    genAi = QuestionGenerator()

    # Generate questions
    print("Generating questions......")
    questions = genAi.generateQuestions(6, Topic.Business, "12-15", None)
    print("Finished generating questions!")

    # Write questions to a CSV file
    csvHeader = ['question', 'choiceA', 'choiceB', 'choiceC', 'choiceD', 'answer']
    file = open("static/output.csv", "w")
    file.write(",".join(csvHeader) + '\n')
    for question in questions:
        file.write(",".join(question.__dict__.values()) + '\n')
    file.close()