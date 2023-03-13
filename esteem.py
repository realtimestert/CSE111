#Program for the Rosenburg self-esteem scale
#Survey that contains 10 statements.

def main():
    print()
    print("This program is an implementation of the Rosenberg")
    print("Self-Esteem Scale. This program will show you ten")
    print("statements that you could possibly apply to yourself.")
    print("Please rate how much you agree with each of the")
    print("statements by responding with one of these four letters:")
    print()
    print("D means you strongly disagree with the statement.")
    print("d means you disagree with the statement.")
    print("a means you agree with the statement.")
    print("A means you strongly agree with the statement.")

    score = 0

    print("1. I feel that I am a person of worth, at least on an equal plane with others.")
    q1 = input("Enter D, d, a, or A: ")
    score += positive_score(q1) 

    print("I feel that I have a number of good qualities.")
    q2 = input("Enter D, d, a, or A: ")
    score += positive_score(q2)

    print("All in all, I am inclined to feel that I am a failure.")
    q3 = input("Enter D, d, a, or A: ")
    score += negative_score(q3)

    print("I am able to do things as well as most other people.")
    q4 = input("Enter D, d, a, or A: ")
    score += positive_score(q4)

    print("I feel I do not have much to be proud of.")
    q5 = input("Enter D, d, a, or A: ")
    score += negative_score(q5)

    print("I take a positive attitude toward myself.")
    q6 = input("Enter D, d, a, or A: ")
    score += positive_score(q6)

    print("On the whole, I am satisfied with myself.")
    q7 = input("Enter D, d, a, or A: ")
    score += positive_score(q7)

    print("I wish I could have more respect for myself.")
    q8 = input("Enter D, d, a, or A: ")
    score += negative_score(q8)

    print("I certainly feel useless at times.")
    q9 = input("Enter D, d, a, or A: ")
    score += negative_score(q9)

    print("At times I think I am no good at all.")
    q10 = input("Enter D, d, a, or A: ")
    score += negative_score(q10)

    print(f"Your score is {score}")
    print("A score below 15 may indicate problematic low self-esteem.")

def positive_score(answer):
    if answer == "D":
        score = 0
    elif answer == "d":
        score = 1
    elif answer == "a":
        score = 2
    elif answer == "A":
        score = 3
    return score
    
def negative_score(answer):
    if answer == "D":
        score = 3
    elif answer == "d":
        score = 2
    elif answer == "a":
        score = 1
    elif answer == "A":
        score = 0
    return score

if __name__ == "__main__":  
    main()