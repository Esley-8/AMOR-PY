import tkinter as tk
import random

class PoemaVisual(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Poema para el Preciosote 💞")
        self.geometry("650x500")
        self.config(bg="white")

        # Poema personalizado
        poema = (
            "Preciso, Er mi guapo esto es para ti"
            "Eres esa brisa que acaricia mi alma"
            "y lel ucero que guía mi caminar,"
            "tu voz calma tormentas internas"
            "y tu risa ilumina mi pensar"
            "Desde la luna llena al cielo estrellado,"
            "mi amor por ti no deja de brillar,"
            "porque tú eres mi paz, mi refugio,"
            "mi lugar seguro en este mar."
            "mi niño de cristal,"
            "no hay otro como tú en la creación."
            "Mi niño hermoso, mi poesía viva,"
            "te llevo eterno en mi corazón."
        )

        texto = tk.Label(self, text=poema, font=("Georgia", 13, "italic"), fg="medium violet red",
                         bg="white", justify="center", wraplength=600)
        texto.pack(pady=20)

        self.canvas = tk.Canvas(self, width=650, height=300, bg="white", highlightthickness=0)
        self.canvas.pack()

        self.hearts = []
        self.animar_corazones()

    def crear_corazon(self):
        x = random.randint(50, 600)
        tamaño = random.randint(14, 26)
        corazon = self.canvas.create_text(x, 290, text="💖", font=("Helvetica", tamaño))
        self.hearts.append((corazon, tamaño))

    def animar_corazones(self):
        if random.random() < 0.45:
            self.crear_corazon()

        for corazon, tamaño in self.hearts:
            self.canvas.move(corazon, 0, -2)
            coords = self.canvas.coords(corazon)
            if coords[1] < -30:
                self.canvas.delete(corazon)
                self.hearts.remove((corazon, tamaño))

        self.after(50, self.animar_corazones)

if __name__ == "__main__":
    app = PoemaVisual()
    app.mainloop()
