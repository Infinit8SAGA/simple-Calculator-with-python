import tkinter as tk
from tkinter import font as tkfont
from core import CalculatorEngine


class CalculatorUI:
    """رابط کاربری گرافیکی"""

    def __init__(self, root):
        self.engine = CalculatorEngine()
        self.root = root
        self._setup_ui()

    def _setup_ui(self):
        self.root.title("Calculator")
        self.root.geometry("350x500")

        # نمایشگر
        self.display_var = tk.StringVar()
        self.display_var.set(self.engine.get_current_display())

        display = tk.Label(
            self.root,
            textvariable=self.display_var,
            font=tkfont.Font(size=24),
            anchor="e",
            bg="#f0f0f0",
            padx=20,
            pady=10
        )
        display.pack(fill="x", padx=10, pady=10)

        # دکمه‌ها
        buttons_frame = tk.Frame(self.root)
        buttons_frame.pack(expand=True, fill="both", padx=10, pady=10)

        buttons = [
            ("7", 0, 0), ("8", 0, 1), ("9", 0, 2), ("/", 0, 3),
            ("4", 1, 0), ("5", 1, 1), ("6", 1, 2), ("*", 1, 3),
            ("1", 2, 0), ("2", 2, 1), ("3", 2, 2), ("-", 2, 3),
            ("0", 3, 0), (".", 3, 1), ("C", 3, 2), ("+", 3, 3),
            ("=", 4, 0, 4)
        ]

        for button in buttons:
            text, row, col = button[:3]
            colspan = button[3] if len(button) > 3 else 1

            btn = tk.Button(
                buttons_frame,
                text=text,
                font=tkfont.Font(size=14),
                command=lambda t=text: self._on_button_click(t)
            )
            btn.grid(
                row=row,
                column=col,
                columnspan=colspan,
                sticky="nsew",
                padx=2,
                pady=2
            )

        # تنظیم اندازه‌گیری
        for i in range(5):
            buttons_frame.rowconfigure(i, weight=1)
        for i in range(4):
            buttons_frame.columnconfigure(i, weight=1)

    def _on_button_click(self, button_text):
        if button_text.isdigit():
            self.engine.input_digit(button_text)
        elif button_text == ".":
            self.engine.input_decimal()
        elif button_text == "C":
            self.engine.reset()
        elif button_text in "+-*/":
            if not self.engine.set_operator(button_text):
                self._show_error("invalid operator")
        elif button_text == "=":
            error = self.engine.calculate()
            if error:
                self._show_error(error)

        self._update_display()

    def _update_display(self):
        self.display_var.set(self.engine.get_current_display())

    def _show_error(self, message):
        self.display_var.set(f"error: {message}")
        self.root.after(2000, self._update_display)


def run():
    root = tk.Tk()
    app = CalculatorUI(root)
    root.mainloop()


if __name__ == "__main__":
    run()