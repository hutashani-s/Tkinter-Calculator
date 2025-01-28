import tkinter as tk

calculation = ""

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end") #deletes all text in the text area
    text_result.insert(1.0, calculation) #inserts the calculation in the text area

def evaluate_calculation():
    global calculation
    try:
        # if text_result.compare("end-1c", "==", "1.0") == False:
        #     clear_field()
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)

    except:
        clear_field()
        text_result.config(text = "error!")

def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")

root = tk.Tk()
root.title("Calculator")
root.config(padx=20, pady=20)
for child in root.winfo_children():
    child.grid_configure(padx=5, pady=5)


text_result = tk.Text(root, height=2, width=25, font=("Arial", 16))
text_result.grid(row=1, columnspan=4)

btn_bracket1 = tk.Button(root, text="(", command=lambda: add_to_calculation("("), width=5, font=("Arial", 14))
btn_bracket1.grid(row=2, column=0)
btn_bracket2 = tk.Button(root, text=")", command=lambda: add_to_calculation(")"), width=5, font=("Arial", 14))
btn_bracket2.grid(row=2, column=1)
btn_mod = tk.Button(root, text="%", command=lambda: add_to_calculation("%"), width=5, font=("Arial", 14))
btn_mod.grid(row=2, column=2)
btn_ce = tk.Button(root, text="CE", command=lambda: clear_field(), width=5, font=("Arial", 14))
btn_ce.grid(row=2, column=3)

btn_1 = tk.Button(root, text="1", command=lambda: add_to_calculation(1), width=5, font=("Arial", 14))
btn_1.grid(row=3, column=0)
btn_2 = tk.Button(root, text="2", command=lambda: add_to_calculation(2), width=5, font=("Arial", 14))
btn_2.grid(row=3, column=1)
btn_3 = tk.Button(root, text="3", command=lambda: add_to_calculation(3), width=5, font=("Arial", 14))
btn_3.grid(row=3, column=2)
btn_plus = tk.Button(root, text="+", command=lambda: add_to_calculation("+"), width=5, font=("Arial", 14))
btn_plus.grid(row=3, column=3)

btn_4 = tk.Button(root, text="4", command=lambda: add_to_calculation(4), width=5, font=("Arial", 14))
btn_4.grid(row=4, column=0)
btn_5 = tk.Button(root, text="5", command=lambda: add_to_calculation(5), width=5, font=("Arial", 14))
btn_5.grid(row=4, column=1)
btn_6 = tk.Button(root, text="6", command=lambda: add_to_calculation(6), width=5, font=("Arial", 14))
btn_6.grid(row=4, column=2)
btn_minus = tk.Button(root, text="-", command=lambda: add_to_calculation("-"), width=5, font=("Arial", 14))
btn_minus.grid(row=4, column=3)

btn_7 = tk.Button(root, text="7", command=lambda: add_to_calculation(7), width=5, font=("Arial", 14))
btn_7.grid(row=5, column=0)
btn_8 = tk.Button(root, text="8", command=lambda: add_to_calculation(8), width=5, font=("Arial", 14))
btn_8.grid(row=5, column=1)
btn_9 = tk.Button(root, text="9", command=lambda: add_to_calculation(9), width=5, font=("Arial", 14))
btn_9.grid(row=5, column=2)
btn_mul = tk.Button(root, text="x", command=lambda: add_to_calculation("*"), width=5, font=("Arial", 14))
btn_mul.grid(row=5, column=3)

btn_0 = tk.Button(root, text="0", command=lambda: add_to_calculation(0), width=5, font=("Arial", 14))
btn_0.grid(row=6, column=0)
btn_point = tk.Button(root, text=".", command=lambda: add_to_calculation("."), width=5, font=("Arial", 14))
btn_point.grid(row=6, column=1)
btn_equal = tk.Button(root, text="=", command=lambda: evaluate_calculation(), width=5, font=("Arial", 14))
btn_equal.grid(row=6, column=2)
btn_div = tk.Button(root, text="/", command=lambda: add_to_calculation("/"), width=5, font=("Arial", 14))
btn_div.grid(row=6, column=3)


root.mainloop()