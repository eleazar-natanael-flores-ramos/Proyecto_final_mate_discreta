import tkinter as tk
from tkinter import ttk

# ---- CLASE NODO ----
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

# ---- CLASE ÁRBOL BINARIO ----
class ArbolBinario:
    def __init__(self):
        self.raiz = Nodo("A")
        self.raiz.izquierdo = Nodo("B")
        self.raiz.derecho = Nodo("C")

        self.raiz.izquierdo.izquierdo = Nodo("D")
        self.raiz.izquierdo.derecho = Nodo("E")

        self.raiz.derecho.izquierdo = Nodo("F")
        self.raiz.derecho.derecho = Nodo("G")

        self.raiz.izquierdo.izquierdo.izquierdo = Nodo("H")
        self.raiz.izquierdo.izquierdo.derecho = Nodo("I")

        self.raiz.izquierdo.derecho.izquierdo = Nodo("J")
        self.raiz.izquierdo.derecho.derecho = Nodo("K")

        self.raiz.derecho.izquierdo.izquierdo = Nodo("L")
        self.raiz.derecho.izquierdo.derecho = Nodo("M")

        self.raiz.derecho.derecho.izquierdo = Nodo("N")
        self.raiz.derecho.derecho.derecho = Nodo("O")

    # ---- RECORRIDOS ----
    def preorden(self, nodo, recorrido):
        if nodo:
            recorrido.append(nodo.valor)
            self.preorden(nodo.izquierdo, recorrido)
            self.preorden(nodo.derecho, recorrido)
        return recorrido

    def inorden(self, nodo, recorrido):
        if nodo:
            self.inorden(nodo.izquierdo, recorrido)
            recorrido.append(nodo.valor)
            self.inorden(nodo.derecho, recorrido)
        return recorrido

    def postorden(self, nodo, recorrido):
        if nodo:
            self.postorden(nodo.izquierdo, recorrido)
            self.postorden(nodo.derecho, recorrido)
            recorrido.append(nodo.valor)
        return recorrido

# ---- INTERFAZ GRÁFICA ----
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Recorridos de Árbol Binario")
        self.root.geometry("800x600")
        self.root.config(bg="#eef2ff")

        self.arbol = ArbolBinario()

        ttk.Label(root, text="RECORRIDOS DE ÁRBOLES BINARIOS",
                  font=("Arial", 14, "bold")).pack(pady=10)

        frame_botones = ttk.Frame(root)
        frame_botones.pack(pady=5)

        ttk.Button(frame_botones, text="PreOrden", command=self.mostrar_preorden).grid(row=0, column=0, padx=10)
        ttk.Button(frame_botones, text="InOrden", command=self.mostrar_inorden).grid(row=0, column=1, padx=10)
        ttk.Button(frame_botones, text="PostOrden", command=self.mostrar_postorden).grid(row=0, column=2, padx=10)

        # Canvas para dibujar el árbol
        self.canvas = tk.Canvas(root, width=750, height=350, bg="white")
        self.canvas.pack(pady=10)

        # Cuadro para mostrar el recorrido
        self.texto_resultado = tk.Text(root, height=5, width=80, font=("Consolas", 12))
        self.texto_resultado.pack(pady=10)

        # Dibujar árbol al inicio
        self.dibujar_arbol(self.arbol.raiz, 375, 50, 180)

    # ---- DIBUJAR EL ÁRBOL ----
    def dibujar_arbol(self, nodo, x, y, distancia):
        if nodo is None:
            return

        radio = 20
        # Dibujar conexiones con hijos
        if nodo.izquierdo:
            self.canvas.create_line(x, y, x - distancia, y + 80, width=2)
            self.dibujar_arbol(nodo.izquierdo, x - distancia, y + 80, distancia / 2)
        if nodo.derecho:
            self.canvas.create_line(x, y, x + distancia, y + 80, width=2)
            self.dibujar_arbol(nodo.derecho, x + distancia, y + 80, distancia / 2)

        # Dibujar nodo (círculo)
        self.canvas.create_oval(x - radio, y - radio, x + radio, y + radio, fill="#9ad0f5", outline="black", width=2)
        self.canvas.create_text(x, y, text=nodo.valor, font=("Arial", 12, "bold"))

    # ---- MOSTRAR RECORRIDOS ----
    def mostrar_preorden(self):
        recorrido = self.arbol.preorden(self.arbol.raiz, [])
        self.mostrar_resultado("PREORDEN", recorrido)

    def mostrar_inorden(self):
        recorrido = self.arbol.inorden(self.arbol.raiz, [])
        self.mostrar_resultado("INORDEN", recorrido)

    def mostrar_postorden(self):
        recorrido = self.arbol.postorden(self.arbol.raiz, [])
        self.mostrar_resultado("POSTORDEN", recorrido)

    def mostrar_resultado(self, tipo, recorrido):
        self.texto_resultado.delete(1.0, tk.END)
        self.texto_resultado.insert(tk.END, f"Recorrido en {tipo}:\n")
        self.texto_resultado.insert(tk.END, " → ".join(recorrido))

# ---- EJECUTAR APP ----
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
