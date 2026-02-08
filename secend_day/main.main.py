key = input().strip()
q = int(input().strip())

guesses = []
for _ in range(q):
    guesses.append(input().strip())

game_over = False


def resolver(key: str, guess: str) -> str:
    if len(guess) != len(key):
        return "Invalid Length"

    n = len(key)
    result = [""] * n
    used_key = [False] * n
    used_guess = [False] * n

    for i in range(n):
        if guess[i] == key[i]:
            result[i] = "G"
            used_key[i] = True
            used_guess[i] = True

    for i in range(n):
        if not used_guess[i]:
            for j in range(n):
                if not used_key[j] and guess[i] == key[j]:
                    result[i] = "Y"
                    used_key[j] = True
                    break
            else:
                result[i] = "R"

    return "".join(result)


for guess_word in guesses:
    if game_over:
        print("Game Over")
        continue

    if len(guess_word) != len(key):
        print("Invalid Length")
        continue

    result = resolver(key, guess_word)
    print(result)

    if result == "G" * len(key):
        game_over = True
