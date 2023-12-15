# Dhruv Gargi - dg574 - 10th Nov 2023
class MyCalc:
    # Class MyCalc for basic calculator operations with memory feature

    ans = 0  # Default answer value

    def _is_float(self, val: str) -> bool:
        # Check if val can be converted to float
        try:
            float(val)
            return True
        except ValueError:
            return False

    def _is_int(self, val: str) -> bool:
        # Check if val can be converted to int
        try:
            int(val)
            return True
        except ValueError:
            return False

    def _as_number(self, val: str):
        # Convert string val to int or float
        val = str(val)  # Ensure val is a string
        if self._is_int(val):
            return int(val)
        elif self._is_float(val):
            return float(val)
        else:
            raise ValueError("Not a number")

    def add(self, num1: str, num2: str) -> float:
        # Add two numbers, using 'ans' as previous answer if specified
        if num1 == "ans":
            return self.add(self.ans, num2)
        else:
            num1, num2 = self._as_number(num1), self._as_number(num2)
            self.ans = num1 + num2
            return self.ans

    def sub(self, num1: str, num2: str) -> float:
        # Subtract num2 from num1, using 'ans' as num1 if specified
        if num1 == "ans":
            return self.sub(self.ans, num2)
        else:
            num1, num2 = self._as_number(num1), self._as_number(num2)
            self.ans = num1 - num2
            return self.ans

    def mult(self, num1: str, num2: str) -> float:
        # Multiply two numbers, using 'ans' as num1 if specified
        if num1 == "ans":
            return self.mult(self.ans, num2)
        else:
            num1, num2 = self._as_number(num1), self._as_number(num2)
            self.ans = num1 * num2
            return self.ans

    def div(self, num1: str, num2: str) -> float:
        # Divide num1 by num2, using 'ans' as num1 if specified
        if num1 == "ans":
            return self.div(self.ans, num2)
        else:
            num1, num2 = self._as_number(num1), self._as_number(num2)
            if num2 == 0:
                raise ZeroDivisionError("Can't divide by zero")
            self.ans = num1 / num2
            return self.ans

if __name__ == '__main__':
    calc = MyCalc()
    is_running = True
    while is_running:
        iSTR = input("What is your eq (To quit:q): ").strip()
        if iSTR in ("quit", "q"):
            print("Good Bye")
            is_running = False
        else:
            print("Your eq was " + str(iSTR)) # this print statment prints the same equation which was given by the user
            if "+" in iSTR: # this condition runs if there is a '+' symbol in the input equation
                nums = iSTR.split("+") # the equation is split using .split() method into 2 parts keeping '+' as the reference and stored in array called nums
                # line - 129 and 130
                # r is the output if the equation
                # nums has the 2 numbers using which the addition has to be performed. 
                # we are calling it individually from the array as num[0] and and num[1] and striping to remove the all the spaces in that string
                # the striped values in sent to the add function
                r = calc.add(nums[0].strip(), nums[1].strip()) 
                print("Result is " + str(r)) # printing the final result to the user
            # must be done before - check to hanlde negative values
            elif "/" in iSTR: # this condition runs if there is a '/' symbol in the input equation
                nums = iSTR.split("/") # the equation is split using .split() method into 2 parts keeping '/' as the reference and stored in array called nums
                # line - 139 and 140
                # r is the output if the equation
                # nums has the 2 numbers using which the division has to be performed. 
                # we are calling it individually from the array as num[0] and and num[1] and striping to remove the all the spaces in that string
                # the striped values in sent to the div function
                r = calc.div(nums[0].strip(), nums[1].strip()) 
                print("Result is " + str(r)) # printing the final result to the user
            elif "*" in iSTR or "x" in iSTR: # this condition runs if there is a 'x' or '*' symbol in the input equation
                nums = iSTR.split("*") if "*" in iSTR else iSTR.split("x") # the equation is split using .split() method into 2 parts keeping 'x' or '*' as the reference and stored in array called nums
                # line - 148 and 149
                # r is the output if the equation
                # nums has the 2 numbers using which the multiplication has to be performed. 
                # we are calling it individually from the array as num[0] and and num[1] and striping to remove the all the spaces in that string
                # the striped values in sent to the mult function
                r = calc.mult(nums[0].strip(), nums[1].strip())
                print("Result is " + str(r)) # printing the final result to the user
            # must be done last so negative numbers work
            elif "-" in iSTR: # this condition runs if there is a '-' symbol in the input equation
                iSTR = iSTR.replace(" ", "") # Removing all the white spaces from the string to remove complications while subtracting negative numbers. 
                if "--" in iSTR : # Here we are checking for if subtrahend is a negative number by checking if there is "--" in the string
                    nums = iSTR.split("--") # if the above condition passes then we are spliting the string using "--" as the refrence
                    nums[-1] = f"-{nums[-1]}" # since in the above line we removed the negative sign for the subtrahend, now we are adding it back again manually
                else:
                    nums = iSTR.rsplit("-",1) # the equation is split using .rsplit() method into 2 parts keeping '-' and length 1 as the reference and stored in array called nums
                # line - 158 and 159
                # r is the output if the equation
                # nums has the 2 numbers using which the subtraction has to be performed. 
                # we are calling it individually from the array as num[0] and and num[1] and striping to remove the all the spaces in that string
                # the striped values in sent to the sub function
                r = calc.sub(nums[0].strip(), nums[1].strip()) 
                print("Result is " + str(r)) # printing the final result to the user