class Button:
    def __init__(self):
        self.press = False

    def press(self):
        self.press = True
        print("Button Pressed")

    def release(self):
        self.press = False
        print("Button Released")

class Forward(Button):
    def __init__(self):
        super().__init__()
        self.next = False

class Backward(Button):
    def __init__(self):
        super().__init__()
        self.previous = False


def start():
    button = Button()

    if input(f"There is a button. Press it? (Yes/No): ") == "Yes":
        Button.press()

    else:
        print(f"Nothing happened. Exiting...")

start()