import random;

word_list = ["ardvark", "baboon", "camel"];

chosen_word = random.choice(word_list);
print(f"Pssst, the solution is {chosen_word}");

display = [];
word_len = len(chosen_word);
for _ in range(word_len):
    display += "_";
print(display);

end_of_game = False;


while not end_of_game:
    guess = input("Guess a letter: ").lower();
    for position in range(word_len):
        letter = chosen_word[position];
        # print(f"current postion: {position} \n current letter: {letter} \n Gusseed letter: {guess}");
        if letter == guess:
            display[position] = letter;
    print(display);

    if "_" not in display:
        end_of_game = True;
        print("You Win!");