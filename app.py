import spacy
import random
from googletrans import Translator
from IPython.display import clear_output

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Initialize Google Translator
translator = Translator()

# Questions and answers
questions = [
    "Your Question"
]

original_answers = [
    "Your Answer"
]

# Function to translate user's answer to English
def translate_to_english(answer, target_language):
    translation = translator.translate(answer, dest='en')
    return translation.text

# Function to initialize chatbot interaction
def chat_interaction():
    clear_output(wait=True)
    random_index = random.randint(0, len(questions)-1)
    current_question = questions[random_index]

    # Ask questions to the chatbot
    user_answer = input(f"Chatbot: {current_question}\nYour Answer: ")

    # Retrieve the original answer
    correct_answer = original_answers[random_index]

    # Answer comparison
    doc_user = nlp(user_answer)
    doc_correct = nlp(correct_answer)
    similarity = doc_user.similarity(doc_correct)

    # threshold for meaningfulness
    similarity_threshold = 0.2

    if similarity < similarity_threshold:
        print("Your answer is not very close to the correct one. Keep trying!")
    else:
        print("Great job! Your answer is similar to the correct answer.")
    
if __name__ == "__main__":
    chat_interaction()
