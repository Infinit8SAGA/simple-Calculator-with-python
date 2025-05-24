
class CalculatorEngine:
    """هسته منطقی ماشین حساب بدون وابستگی به UI"""

    def __init__(self):
        self.reset()

    def reset(self):
        self.current_input = "0"
        self.stored_value = None
        self.current_operator = None
        self.reset_input = False

    def input_digit(self, digit):
        if self.reset_input:
            self.current_input = "0"
            self.reset_input = False

        if self.current_input == "0":
            self.current_input = digit
        else:
            self.current_input += digit

    def input_decimal(self):
        if self.reset_input:
            self.current_input = "0"
            self.reset_input = False

        if "." not in self.current_input:
            self.current_input += "."

    def set_operator(self, operator):
        try:
            if self.current_operator and not self.reset_input:
                self.calculate()

            self.stored_value = float(self.current_input)
            self.current_operator = operator
            self.reset_input = True
            return True
        except ValueError:
            self.reset()
            return False

    def calculate(self):
        if self.current_operator and self.stored_value is not None:
            try:
                current_value = float(self.current_input)
                result = self._perform_calculation(current_value)

                if isinstance(result, str):
                    return result  # خطا

                self.current_input = self._format_result(result)
                self.stored_value = None
                self.current_operator = None
                self.reset_input = True
                return None
            except Exception as e:
                self.reset()
                return str(e)
        return None

    def _perform_calculation(self, current_value):
        if self.current_operator == "+":
            return self.stored_value + current_value
        elif self.current_operator == "-":
            return self.stored_value - current_value
        elif self.current_operator == "*":
            return self.stored_value * current_value
        elif self.current_operator == "/":
            if current_value == 0:
                return "division by zero"
            return self.stored_value / current_value
        return None

    def _format_result(self, result):
        if isinstance(result, float) and result.is_integer():
            return str(int(result))
        return str(result)

    def get_current_display(self):
        return self.current_input