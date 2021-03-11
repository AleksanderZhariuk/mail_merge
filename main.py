def replace_the_name(string, name):
    return string.replace('[name]', name)


def friend_list():
    with open('./Input/Names/invited_names.txt', 'r') as file:
        all_names = file.read()
        friends = all_names.split('\n')
        return friends


def writing_the_letter(name):
    with open('./Input/Letters/starting_letter.txt', 'r') as file:
        letter_blueprint = file.read()
        finish_letter = replace_the_name(letter_blueprint, name)

    with open(f'./Output/ReadyToSend/letter_for_{name}.txt', 'w') as file:
        file.write(finish_letter)


names = friend_list()

for friend in friend_list():
    writing_the_letter(friend)
