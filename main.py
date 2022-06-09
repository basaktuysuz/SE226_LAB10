import tkinter as tk

r = tk.Tk()
r.title("example")
r.geometry("500x500")


def READ():
    textBox.delete("1.0", tk.END)
    text_file = open("D:\\MarvelL.txt", 'r')
    stuff = text_file.read()
    textBox.insert(tk.END, stuff)
    text_file.close()


def CALCULATE():
    textBox.delete("1.0", tk.END)
    text_file = open("D:\\MarvelL.txt", 'r').read()
    text_file = text_file.split()
    freq = []

    for i in text_file:
        if i not in freq:
            freq.append(i)

    for i in range(0, len(freq)):
        str_ = (freq[i], '=', text_file.count(freq[i]))
        textBox.insert(tk.END, str_)
        textBox.insert(tk.END, "\n")


textBox = tk.Text(width=300, height=15, font=("helvetica", 16))
textBox.pack(pady=20)

button = tk.Button(text="READ", command=READ,font=("helvetica", 16))
button.pack()

button2 = tk.Button(text="CALCULATE",command=CALCULATE,font=("helvetica", 16))
button2.pack()

r.mainloop()
