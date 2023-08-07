import json
from difflib import get_close_matches

def load_knowledge_base(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        data: dict = json.load(file)
    return data

def save(file_path: str, data: dict):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

def find_best_match(user_question: str, questions: list[str]) -> str | None:
    matches: list = get_close_matches(user_question, questions, n=1, cutoff=0.6)
    return matches[0] if matches else None

def get_answer(question: str, knowledge_base: dict) -> str | None:
    for q in knowledge_base["questions"]:
        if q["question"] == question:
            return q["answer"]

def chat_bot():
    knowledge_base: dict = load_knowledge_base("knowledge_base.json")
    while True:
        user_input: str = input("You: ")
        if user_input.lower() == "quit":
            print("Bye Bye 👋")
            break
        best_match: str | None = find_best_match(user_input, [q["question"] for q in knowledge_base["questions"]])

        if best_match:
            answer: str = get_answer(best_match, knowledge_base)
            print(f"Bot:{answer}")
        else:
            print("Bot: I am not willing to answer until you explain it")
            new_answer: str = input("Master teach me or else type SKIP:")
            if new_answer.lower()=="skip":
                print("Bot: I thought you are cool ask me something I know?")
            if new_answer.lower()=="yo":
                print("Bot: Orewa Monkey D Luffy")
            if new_answer.lower()=="":
                print("Bot :Try again")
                pass
            elif new_answer.lower() != "skip":
                knowledge_base["questions"].append({"question": user_input, "answer": new_answer})
                save("knowledge_base.json", knowledge_base)
                print("Bot: Arigato I learnt something new")

chat_bot()