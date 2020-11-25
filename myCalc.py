import sys 

from PyQt5.QtWidgets import QApplication,QDialog
from PyQt5.QtGui import QIcon

from myCalc_UI import Ui_Dialog

class Calculator(QDialog,Ui_Dialog):
    first_number = None # Holds first number entered.
    calculating = False # Calculate state/flag.
    typing_second_num = False # Typing the second number state/flag.

    def __init__(self):
        super(Calculator,self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('calc.png'))
        self.prep_buttons()
        self.show()

    def prep_buttons(self):
        """ Prepare buttons signal and slots."""

        # Connect digit presses method on button that have digits.
        self.pushButton_0.clicked.connect(self.digit_pressed)
        self.pushButton_1.clicked.connect(self.digit_pressed)
        self.pushButton_2.clicked.connect(self.digit_pressed)
        self.pushButton_3.clicked.connect(self.digit_pressed)
        self.pushButton_4.clicked.connect(self.digit_pressed)
        self.pushButton_5.clicked.connect(self.digit_pressed)
        self.pushButton_6.clicked.connect(self.digit_pressed)
        self.pushButton_7.clicked.connect(self.digit_pressed)
        self.pushButton_8.clicked.connect(self.digit_pressed)
        self.pushButton_9.clicked.connect(self.digit_pressed)
            
        # Connect clear button with clear method.
        self.pushButtonClear.clicked.connect(self.clear)

        # Connect decimal point button with point method.
        self.pushButton_point.clicked.connect(self.point)

        # Connect unary operators to unary_op_pressed.
        self.pushButton_plusMinus.clicked.connect(self.unary_op_pressed)
        self.pushButton_percent.clicked.connect(self.unary_op_pressed)

        # Connect binary operators to binary_op_pressed method.
        self.pushButton_plus.clicked.connect(self.binary_op_pressed)
        self.pushButton_multiply.clicked.connect(self.binary_op_pressed)
        self.pushButton_minus.clicked.connect(self.binary_op_pressed)
        self.pushButton_divide.clicked.connect(self.binary_op_pressed)

        # Connect equals operator to equal_pressed method.
        self.pushButton_equal.clicked.connect(self.equal_pressed)


    def clear(self): 
        """ Set all state to non-active state (initial state)""" 
        # Set main label to zero.
        self.main_label.setText('0')
        self.sub_label.clear()
        self.pushButton_plus.setChecked(False)
        self.pushButton_multiply.setChecked(False)
        self.pushButton_divide.setChecked(False)
        self.pushButton_minus.setChecked(False)
        self.typing_second_num = False 
        self.first_num = None 

    def point(self): 
        """ Add decimal point to main label if none existed."""
        if '.' not in self.main_label.text(): 
            self.main_label.setText(self.main_label.text() + '.')

            if self.typing_second_num: 
                self.sub_label.setText(self.sub_label.text() + '.')

    def digit_pressed(self): 
        """ Set main label by the button(digit) sender. """
        # Get the button(digit) sender.
        button = self.sender()

        if ((self.pushButton_plus.isChecked() or self.pushButton_minus.isChecked() or 
                self.pushButton_divide.isChecked() or self.pushButton_multiply.isChecked()) 
                    and not(self.typing_second_num)): 
                    # Check if some binary operator is active(pressed) and if typing a second number state is not active.

            self.typing_second_num = True # Set typing a second number to active(True).
            new_label  = button.text() # Set new label to second number.

            # Set sub label text immediately by fist digit of second number.
            self.sub_label.setText(f'{self.sub_label.text()} {new_label}')       
        else: 
            if ('.' in self.main_label.text() and button.text == '0'): 
                # if the number entered contains necessary zeros and contains a decimal point.

                # Set the new label with formatting ('.15' - didn't remove necessary zeros).
                new_label = format(float(self.main_label.text() + button.text()), '.15')
            else: 
                # Setup new label with formatting('.15g' - removes unnecessary zeros).
                new_label = format(float(self.main_label.text() + button.text()),'.15g')

                if self.typing_second_num: # Check if typing a second number is active. 
                    # Add the new digit entered to the current text @ sub label.
                    self.sub_label.setText(self.sub_label.text() + button.text())

        # Set main label with the new label.
        self.main_label.setText(new_label)
        

    def unary_op_pressed(self): 
        """ Perform unary operations ('+/-' , '%') on main label."""
        if self.main_label.text() != '0': 
            # Get the unary operator.
            button = self.sender()

            # Convert str number from main label to float.
            number_label = float(self.main_label.text())

            if button.text() == '+/-': 
                number_label *= -1 
            else: #button.text() = '%'
                number_label *= 0.01
    
            # Format number_label ('.15g' - removes unnecessary zeros.)
            new_label = format(number_label,'.15g')

            # Set main label to new number_label(operated)
            self.main_label.setText(new_label)

            if self.sub_label.text(): # Check if sub label contains non-empty text.
                subL_list = self.sub_label.text().split() # Convert sub label text to list. 
                subL_list[2] = f'({new_label})' # Access element @ index 2 and change to new label.
                self.sub_label.setText(' '.join(subL_list)) # Set sub label to new sub label(operated).


    def binary_op_pressed(self): 
        """ Sets binary operator button and calculation state to active."""

        # Get binary operator. 
        button = self.sender()

        # Set sub label text with current main label text plus the binary operator symbol.
        self.sub_label.setText(f'{self.main_label.text()} {button.text()}') 

        # Set button to active state.
        button.setChecked(True)

        # Get current number @ main label.
        self.first_num = float(self.main_label.text())

        # Set calculate state active.
        self.calculating = True 

        
    def equal_pressed(self): 
        """ Perform binary operations (+, -, *, /) when equals(=) button is pressed."""

        if self.calculating: # Check if calcuting state is active.

            self.sub_label.setText(self.sub_label.text() + ' =') # Add equal symbol to sub label text.

            second_number = float(self.main_label.text()) # Get second number.

            if self.pushButton_plus.isChecked(): # Check if plus button is pressed.

                self.pushButton_plus.setChecked(False) # Set plus button to non-active state.
                result = self.first_num + second_number # Store sum of two numbers to result.

            if self.pushButton_minus.isChecked(): # Checked if minus button is pressed.

                self.pushButton_minus.setChecked(False) # Set minus button to non-active state.
                result = self.first_num - second_number # Store difference of two numbers to result.

            if self.pushButton_multiply.isChecked(): # Checked if multiply button is pressed.

                self.pushButton_multiply.setChecked(False) # Set multiply button to non-active state.
                result = self.first_num * second_number # Store product of two numbers to result.

            if self.pushButton_divide.isChecked():  # Checked if division button is pressed.

                self.pushButton_divide.setChecked(False) # Set  division button to non-active state.
                result = self.first_num / second_number # Store product of two numbers to result.


            self.typing_second_num = False # Set typing second number to non-active state.

            self.main_label.setText(format(result, '.15g')) # Set the main label to result with formatting.

            self.calculating = False # Set calculate to non-active state.


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myCalc = Calculator()
    sys.exit(app.exec_())

