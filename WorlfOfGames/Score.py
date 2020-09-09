import Utils



def add_score(difficulty):
    try:
        with open(Utils.SCORES_FILE_NAME, "r") as file:
            current_score = int(file.read())
            try:
                with open(Utils.SCORES_FILE_NAME, 'w') as file:
                    file.write(str(current_score + (difficulty * 3) + 5))
            except:
                raise Exception('Could not write to  Scores.txt')
    except:
        print('Could not open Scores.txt. Creating new one.')
        try:
            with open(Utils.SCORES_FILE_NAME, 'w') as file:
                file.write(str((difficulty * 3) + 5))
        except:
                raise Exception('Could not write to  Scores.txt')


# Updates scores file with zero value in case that  game was lost and no file was created yet.
# Helps to show zero value on scores site instead of showing error message.
def create_zero_score():
    try:            # try to open and read scores file.
        with open(Utils.SCORES_FILE_NAME, "r") as file:
            current_score = int(file.read())
    except:         # if not succeeded to open and read scores file:
        print('Could not open Scores.txt. Creating new one with zero value.')
        try:        # if not succeeded to open and read scores file, try to open new file and write zero score
            with open(Utils.SCORES_FILE_NAME, 'w') as file:
                file.write("0")
        except:     # If not succeeded to write to the file the new score, will be shown on the scores site.
                print('Could not write to Scores.txt.')
