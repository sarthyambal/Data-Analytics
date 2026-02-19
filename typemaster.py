import time
import random

sentences = [
    "The quick brown fox jumps over the lazy dog.", 
    "Typing is a skill that improves with practice.",
    "Python is a great programming language for beginners.",
]
def measure_accuracy (user_input, target_sentence):
    user_words = user_input.split()
    target_words = target_sentence.split()
    correct_words = sum(1 for u, t in zip(user_words, target_words) if u == t)
    accuracy = (correct_words / len(target_words)) * 100 if target_words else 0
    return accuracy


def typing_test():
    random_sentence = random.choice(sentences)
    print("Type the following sentence:")
    print(random_sentence)
    input("Press Enter to start...")
    start_time = time.time()
    user_input = input("\nSatart typing: ")
    end_time = time.time()
    time_taken = end_time - start_time
    time_taken_in_seconds = time_taken / 60
    word_count = len(random_sentence.split(" "))

    print("Results:")
    print(f"Time taken: {time_taken_in_seconds:.2f} seconds")
    print(f"Words typed: {word_count}")
    print(f"Words per minute: {word_count / time_taken_in_seconds * 60 if time_taken_in_seconds > 0 else 0:.2f}")
    accuracy = measure_accuracy(user_input, random_sentence)
    print(f"Accuracy: {accuracy:.2f}%")
typing_test()
