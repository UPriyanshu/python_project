import tkinter as tk
from tkinter import messagebox


class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Modern Calculator")
        self.root.configure(bg="#f0f0f0")

        # Entry widget for display
        self.display = tk.Entry(
            root, width=20, font=("Arial", 24), bd=5, justify="right", bg="#ffffff"
        )
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Store the current calculation
        self.current = ""

        # Custom button style
        button_style = {
            "font": ("Arial", 18),
            "bd": 3,
            "width": 4,
            "height": 1,
            "relief": "raised",
        }

        # Button layout
        buttons = [
            ("7", 1, 0),
            ("8", 1, 1),
            ("9", 1, 2),
            ("/", 1, 3),
            ("4", 2, 0),
            ("5", 2, 1),
            ("6", 2, 2),
            ("*", 2, 3),
            ("1", 3, 0),
            ("2", 3, 1),
            ("3", 3, 2),
            ("-", 3, 3),
            ("0", 4, 0),
            ("C", 4, 1),
            ("=", 4, 2),
            ("+", 4, 3),
        ]

        # Create and place buttons
        for text, row, col in buttons:
            btn = tk.Button(
                root,
                text=text,
                command=lambda t=text: self.button_click(t),
                bg=(
                    "#e0e0e0"
                    if text.isdigit()
                    else (
                        "#ff9999"
                        if text == "C"
                        else "#99ff99" if text == "=" else "#99ccff"
                    )
                ),
                **button_style
            )
            btn.grid(row=row, column=col, padx=5, pady=5)

    def button_click(self, value):
        try:
            if value == "=":
                # Calculate result
                result = eval(self.current)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
                self.current = str(result)

            elif value == "C":
                # Clear display
                self.display.delete(0, tk.END)
                self.current = ""

            else:
                # Add to current calculation
                self.current += value
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, self.current)

        except Exception as e:
            messagebox.showerror("Error", "Invalid calculation!")
            self.display.delete(0, tk.END)
            self.current = ""


if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
