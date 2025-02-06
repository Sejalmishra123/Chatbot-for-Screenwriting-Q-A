import spacy
import random
from googletrans import Translator

# Load spaCy model for NLP processing
nlp = spacy.load("en_core_web_sm")

# Initialize Google Translator for multilingual support
translator = Translator()

# Placeholder for user-defined questions and answers
questions = [
    "Your Question"
]

original_answers = [
    "Your Answer"
]

# Function to translate user's answer to English (if needed)
def translate_to_english(answer):
    try:
        translation = translator.translate(answer, dest='en')
        return translation.text
    except Exception as e:
        print(f"Translation Error: {e}")
        return answer  # If translation fails, return the original answer

# Function to calculate similarity between user answer and correct answer
def check_similarity(user_answer, correct_answer):
    doc_user = nlp(user_answer)
    doc_correct = nlp(correct_answer)
    return doc_user.similarity(doc_correct)

# Chatbot interaction function
def chat_interaction():
    # Randomly pick a question from the list
    random_index = random.randint(0, len(questions) - 1)
    current_question = questions[random_index]

    # Ask the question
    user_answer = input(f"Chatbot: {current_question}\nYour Answer: ")

    # Translate if required
    translated_answer = translate_to_english(user_answer)

    # Retrieve the correct answer
    correct_answer = original_answers[random_index]

    # Calculate similarity
    similarity = check_similarity(translated_answer, correct_answer)

    # Define similarity threshold
    similarity_threshold = 0.3

    if similarity < similarity_threshold:
        print("\nChatbot: Your answer is not very close to the correct one. Try again!")
    else:
        print("\nChatbot: Great job! Your answer is similar to the correct one.")

# Run chatbot
if __name__ == "__main__":
    chat_interaction()
