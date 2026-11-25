from calculator import Calculator


class CalculatorService:

    def __init__(self):
        self.calculator = Calculator()

    def calculate(self, operation, a, b):
        operations = {
            "add": self.calculator.add,
            "subtract": self.calculator.subtract,
            "multiply": self.calculator.multiply,
            "divide": self.calculator.divide
        }

        if operation not in operations:
            raise ValueError("Unsupported operation")

        return operations[operation](a, b)
