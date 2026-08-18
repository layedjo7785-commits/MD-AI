from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


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
            text="MD AI : Bonjour Mamadou 👋\nJe suis prêt à discuter avec toi.",
            font_size=18,
            halign="left",
            valign="top"
        )
        layout.add_widget(self.conversation)

        zone = BoxLayout(
            size_hint_y=None,
            height=55,
            spacing=5
        )

        self.champ = TextInput(
            hint_text="Écris ton message...",
            multiline=False,
            font_size=18
        )
        zone.add_widget(self.champ)

        bouton = Button(
            text="Envoyer",
            font_size=16,
            size_hint_x=None,
            width=100
        )
        bouton.bind(on_press=self.envoyer)
        zone.add_widget(bouton)

        layout.add_widget(zone)

        return layout

    def envoyer(self, instance):
        message = self.champ.text.strip()

        if not message:
            return

        reponse = self.repondre(message)

        self.conversation.text += (
            "\n\nToi : " + message +
            "\nMD AI : " + reponse
        )

        self.champ.text = ""

    def repondre(self, message):
        texte = message.lower()

        if "bonjour" in texte or "salut" in texte:
            return "Bonjour 👋 Je suis MD AI !"

        if "comment tu vas" in texte:
            return "Je vais très bien 🤖 Et toi ?"

        if "ton nom" in texte or "qui es-tu" in texte:
            return "Je suis MD AI, ton assistant personnel 🤖."

        if "couleur" in texte:
            return "Ta couleur préférée est le bleu 💙."

        return "Je t'écoute. Dis-moi quelque chose ! 💬"


if __name__ == "__main__":
    MDAI().run()
