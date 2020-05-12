from guizero import App, Text, TextBox, PushButton, Slider, Picture

def say_my_name():
  welcome_message.value = my_name.value

def change_text_size(slider_value):
  welcome_message.size = slider_value

app = App("Hello world")

welcom_message = Text(app, text="Stella Lee", size=30, font="Arial", color="#87BAED")

my_name = TextBox(app, width=30, height=1.5)

update_text = PushButton(app, command=say_my_name, text="Display my name")

text_size = Slider(app, command=change_text_size, start=10, end=80)

puppy_img = Picture(app, image='puppy.gif')

app.display()
