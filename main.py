import tkinter as tk

fenetre = tk.Tk()
fenetre.title("MD AI 🤖")
fenetre.geometry("400x650")

titre = tk.Label(
    fenetre,
    text="MD AI 🤖",
    font=("Arial", 24, "bold")
)
titre.pack(pady=10)

conversation = tk.Text(
    fenetre,
    font=("Arial", 12),
    wrap="word"
)
conversation.pack(
    padx=10,
    pady=10,
    fill="both",
    expand=True
)

zone = tk.Frame(fenetre)
zone.pack(fill="x", padx=10, pady=10)

champ = tk.Entry(
    zone,
    font=("Arial", 14)
)
champ.pack(
    side="left",
    fill="x",
    expand=True
)

def envoyer(event=None):
    message = champ.get().strip()

    if message == "":
        return

    conversation.insert(
        tk.END,
        "Toi : " + message + "\n"
    )

    conversation.insert(
        tk.END,
        "MD AI : Je t'écoute 🤖💬\n\n"
    )

    champ.delete(0, tk.END)

bouton = tk.Button(
    zone,
    text="Envoyer",
    font=("Arial", 12),
    command=envoyer
)
bouton.pack(side="right", padx=(5, 0))

champ.bind("<Return>", envoyer)

fenetre.mainloop()
        
