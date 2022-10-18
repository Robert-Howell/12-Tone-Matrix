
import random


def matrix_maker(starting_number):

    note_list_r0 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    random.shuffle(note_list_r0)
    note_list_r0.remove(starting_number)
    note_list_r0.insert(0, starting_number)

    note_list_reverse = []

    for note in range(0, 11):
        note_list_reverse.append(note_list_r0[note + 1] - note_list_r0[note])

    note_list_inverse = [note_list_r0[0]]

    for notes in range(0, 11):
        if (note_list_inverse[notes] - note_list_reverse[notes]) == 0:
            note_list_inverse.append((note_list_inverse[notes] - note_list_reverse[notes]) + 12)
        elif (note_list_inverse[notes] - note_list_reverse[notes]) > 12:
            note_list_inverse.append((note_list_inverse[notes] - note_list_reverse[notes]) - 12)
        elif (note_list_inverse[notes] - note_list_reverse[notes]) < 0:
            note_list_inverse.append((note_list_inverse[notes] - note_list_reverse[notes]) + 12)
        else:
            note_list_inverse.append(note_list_inverse[notes] - note_list_reverse[notes])

    final_list = [note_list_r0]

    for value in range(1, 12):
        new_list = []
        new_list.clear()
        new_list = [note_list_inverse[value]]
        for i in range(0, 11):
            if (new_list[i] + note_list_reverse[i]) == 0:
                new_list.append((new_list[i] + note_list_reverse[i]) + 12)
            elif (new_list[i] + note_list_reverse[i]) > 12:
                new_list.append((new_list[i] + note_list_reverse[i]) - 12)
            elif (new_list[i] + note_list_reverse[i]) < 0:
                new_list.append((new_list[i] + note_list_reverse[i]) + 12)
            else:
                new_list.append(new_list[i] + note_list_reverse[i])
            if len(new_list) == 12:
                final_list.append(new_list)

    [print(i) for i in final_list]


matrix_maker(int(input("What number between 1 and 12 do you want to start with?")))
