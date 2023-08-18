from tkinter import *
import random

def roll_dice():
    num_dice = int(entry.get())
    dice = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    results = [random.choice(dice) for _ in range(num_dice)]
    total = sum([ord(result) - ord('\u2680') + 1 for result in results])
    result_label.config(text=' '.join(results) + f'\n {total}', font=("Ariel", 60))
    result_label.pack()
    play_again_button.pack()
    roll_button.pack_forget()


def play_again():
    result_label.pack_forget()
    play_again_button.pack_forget()
    roll_button.pack()
    num_dice_label.pack()
    entry.pack()
    entry.delete(0, END)

root = Tk()
root.geometry("1000x500")
root.title("DICE ROLLER")

num_dice_label = Label(root, text="Enter the number of Dice:", font=("Ariel", 18))
num_dice_label.pack(pady=5)

entry = Entry(root, width=40, font=('Arial 12'))
entry.pack(pady=5)

roll_button = Button(root, text="Roll the Dice!", foreground='blue', font=("Ariel", 12), height=2, command=roll_dice)
roll_button.pack(pady=5)

result_label = Label(root, font=("Ariel", 18))

play_again_button = Button(root, text="Play Again", foreground='green', font=("Ariel", 12), height=2, command=play_again)

root.mainloop()