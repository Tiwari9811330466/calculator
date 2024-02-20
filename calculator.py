import tkinter as tk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")

        self.result_var = tk.StringVar()
        self.result_var.set("0")

        self.entry = tk.Entry(root, textvariable=self.result_var, font=("Helvetica", 20), justify=tk.RIGHT)
        self.entry.grid(row=0, column=0, columnspan=4)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            tk.Button(root, text=button, width=5, height=2, command=lambda btn=button: self.on_button_click(btn)).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def on_button_click(self, button):
        current_text = self.result_var.get()

        if button == "=":
            try:
                result = eval(current_text)
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set("Error")
        else:
            if current_text == "0" or current_text == "Error":
                self.result_var.set(button)
            else:
                self.result_var.set(current_text + button)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
