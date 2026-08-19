from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView


class MDAI(App):

    def build(self):
        layout = BoxLayout(
            orientation="vertical",
            padding=10,
            spacing=10
        )

        titre = Label(
            text="MD AI 🤖",
            font_size=28,
            size_hint_y=None,
            height=60
        )

        layout.add_widget(titre)

        self.conversation = Label(
            text="MD AI : Bonjour Mamadou 👋\n\n",
            font_size=18,
            halign="left",
            valign="top",
            size_hint_y=None
        )

        self.conversation.bind(
            texture_size=self.conversation.setter("size")
        )

        scroll = ScrollView()
        scroll.add_widget(self.conversation)
        layout.add_widget(scroll)

        zone = BoxLayout(
            size_hint_y=None,
            height=55,
            spacing=5
        )

        self.champ = TextInput(
            hint_text="Écris à MD AI...",
            multiline=False,
            font_size=18
        )

        bouton = Button(
            text="Envoyer",
            size_hint_x=None,
            width=100
        )

        bouton.bind(on_press=self.envoyer)

        zone.add_widget(self.champ)
        zone.add_widget(bouton)

        layout.add_widget(zone)

        return layout

    def envoyer(self, instance):
        message = self.champ.text.strip()

        if message == "":
            return

        self.conversation.text += (
            "Toi : " + message + "\n"
            "MD AI : Je t'écoute 🤖💬\n\n"
        )

        self.champ.text = ""


MDAI().run()
