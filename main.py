#Import required modules
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.menu import MDDropdownMenu
from kivy.metrics import dp
from api import send_data
import datetime

# UI
KV = '''
MDBoxLayout:
    orientation: 'vertical'
    padding: dp(10)
    spacing: dp(10)

    MDLabel:
        text: 'Date'
        theme_text_color: 'Primary'

    MDCard:
        size_hint_y: None
        height: dp(60)
        radius: [10,]
        elevation: 2
        MDTextField:
            id: date_input
            hint_text: 'YYYY-MM-DD'
            pos_hint: {'center_y': 0.5}

    MDLabel:
        text: 'Hour'
        theme_text_color: 'Primary'

    MDCard:
        size_hint_y: None
        height: dp(60)
        radius: [10,]
        elevation: 2
        MDTextField:
            id: hour_input
            hint_text: '0-23'
            pos_hint: {'center_y': 0.5}

    MDLabel:
        text: 'Minute'
        theme_text_color: 'Primary'

    MDCard:
        size_hint_y: None
        height: dp(60)
        radius: [10,]
        elevation: 2
        MDTextField:
            id: minute_input
            hint_text: '0-59'
            pos_hint: {'center_y': 0.5}

    MDLabel:
        text: 'Name'
        theme_text_color: 'Primary'

    MDCard:
        size_hint_y: None
        height: dp(60)
        radius: [10,]
        elevation: 2
        MDTextField:
            id: name_input
            hint_text: 'Name'
            pos_hint: {'center_y': 0.5}

    MDLabel:
        text: 'Surname (optional)'
        theme_text_color: 'Primary'

    MDCard:
        size_hint_y: None
        height: dp(60)
        radius: [10,]
        elevation: 2
        MDTextField:
            id: surname_input
            hint_text: 'Surname'
            pos_hint: {'center_y': 0.5}

    MDLabel:
        text: 'Sex'
        theme_text_color: 'Primary'

    MDCard:
        size_hint_y: None
        height: dp(60)
        radius: [10,]
        elevation: 2
        MDBoxLayout:
            padding: dp(10)
            MDDropDownItem:
                id: sex_input
                text: 'Select sex'
                on_release: app.menu.open()

    MDRaisedButton:
        text: 'Submit'
        pos_hint: {'center_x': 0.5}
        on_release: app.submit_data()

    MDLabel:
        id: result_label
        text: ''
        theme_text_color: 'Secondary'
'''


# Function to validate date format
def check_date_format(date_string, date_format="%Y-%m-%d"):
    try:
        datetime.datetime.strptime(date_string, date_format)
        return True
    except ValueError:
        return False


class MainApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def on_start(self):
        self.menu = MDDropdownMenu(
            caller=self.root.ids.sex_input,
            items=[
                {"viewclass": "OneLineListItem", "text": "male", "on_release": lambda x="male": self.set_item(x)},
                {"viewclass": "OneLineListItem", "text": "female", "on_release": lambda x="female": self.set_item(x)},
            ],
            width_mult=4,
        )

    def set_item(self, text_item):
        self.root.ids.sex_input.set_item(text_item)
        self.root.ids.sex_input.text = text_item
        self.menu.dismiss()

    def submit_data(self):
        date = self.root.ids.date_input.text
        hour = self.root.ids.hour_input.text
        minute = self.root.ids.minute_input.text
        name = self.root.ids.name_input.text
        surname = self.root.ids.surname_input.text
        sex = self.root.ids.sex_input.text

        # Validate inputs
        if self.validate_input(date, hour, minute, name, sex):
            # Send data to API
            try:
                response = send_data(date, hour, minute, name, surname, sex)
                self.show_dialog("Success", "Data sent successfully")
            except Exception as e:
                self.show_dialog("Error", f"Failed to send data: {str(e)}")

    # Function to validate inputs
    def validate_input(self, date, hour, minute, name, sex):
        if not check_date_format(date):
            self.show_dialog("Error", "Invalid date format. Please use YYYY-MM-DD.")
            return False
        if not hour.isdigit() or not (0 <= int(hour) <= 23):
            self.show_dialog("Error", "Invalid hour. Please enter a value between 0 and 23.")
            return False
        if not minute.isdigit() or not (0 <= int(minute) <= 59):
            self.show_dialog("Error", "Invalid minute. Please enter a value between 0 and 59.")
            return False
        if not name:
            self.show_dialog("Error", "Name cannot be empty.")
            return False
        if sex not in ["male", "female"]:
            self.show_dialog("Error", "Please select a valid sex.")
            return False
        return True

    def show_dialog(self, title, text):
        dialog = MDDialog(
            title=title,
            text=text,
            size_hint=(0.8, 0.3),
            buttons=[
                MDRaisedButton(
                    text="OK",
                    on_release=lambda x: dialog.dismiss()
                )
            ]
        )
        dialog.open()


if __name__ == '__main__':
    MainApp().run()
