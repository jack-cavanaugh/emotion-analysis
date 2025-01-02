import spacy
import pandas as pd
import re

# SpaCy Initialize
nlp = spacy.load("en_core_web_lg")

# Preprocessing
def preprocess(doc):
    doc = nlp(doc)
    lem_doc = []

    for token in doc:
        lem_doc.append(token.lemma_)

    clean_doc = " ".join(lem_doc)
    clean_doc = re.sub(r'[^\w\s]', ' ', clean_doc)
    clean_doc = re.sub(r'\s+', ' ', clean_doc).strip()
    
    print("check")
    return(clean_doc)

# Check for Special Input
def quit_check(input):
    if input.lower().strip() == "help":
        print("*Temporary help screen*") # List all functions of Ed at future point
        return 
    elif input.lower().strip() == "quit":
        print("Ed: Thanks for chatting with me! See you again soon.")
        return # End all code

def introduction():
    print("Ed: Hello, my name is Ed! I'm an emotion detection chatbot.")
    print("Ed: What's your name?")
    username = input("User: ")
    username = preprocess(username)
    print(username)
    for token in username:
        p

def emotion_detection():
    pass

# Main Command
def main():
    print("Ed: Type STOP at any point to end our conversation. Type HELP to learn more about me.")
    introduction()


# Run Code
main()




# Vectorize and classify into pandas using SpaCy