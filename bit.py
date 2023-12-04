from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label

class NumberConversionApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        self.input_info = TextInput(hint_text='Enter number and number system (e.g., 10101 binary)', multiline=False)
        self.layout.add_widget(self.input_info)

        self.convert_button = Button(text='Convert', on_press=self.convert_number)
        self.layout.add_widget(self.convert_button)

        self.output_label = Label(text='')
        self.layout.add_widget(self.output_label)

        return self.layout

    def convert_number(self, instance):
        input_info = self.input_info.text.strip().split()

        if len(input_info) == 2:
            input_number_str, input_choice = input_info
            decimal_number = self.convert_to_decimal(input_number_str, input_choice.lower())

            if decimal_number is not None:
                self.display_output(decimal_number)
            else:
                self.output_label.text = 'Invalid input'
        else:
            self.output_label.text = 'Invalid input format. Please enter both number and number system.'

    def convert_to_decimal(self, input_number_str, input_choice):
        base = {'binary': 2, 'octal': 8, 'decimal': 10, 'hexadecimal': 16}

        try:
            return int(input_number_str, base[input_choice])
        except ValueError:
            return None  # Handle the case of an invalid input

    def display_output(self, decimal_number):
        binary_number = bin(decimal_number)[2:]
        octal_number = oct(decimal_number)[2:]
        hexadecimal_number = hex(decimal_number)[2:].upper()

        self.output_label.text = (
            f'Decimal: {decimal_number}\n'
            f'Binary: {binary_number}\n'
            f'Octal: {octal_number}\n'
            f'Hexadecimal: {hexadecimal_number}'
        )

if __name__ == '__main__':
    NumberConversionApp().run()
