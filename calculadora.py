import tkinter as tk


def formatear_resultado(valor):
    """Devuelve el valor como entero si no tiene decimales, o como flotante si los tiene."""
    return int(valor) if valor == int(valor) else round(valor, 2)


def sumar():
    try:
        res = float(entrada1.get()) + float(entrada2.get())
        resultado_label.config(text=f"Resultado: {formatear_resultado(res)}")
    except ValueError:
        resultado_label.config(text="Error: entrada inválida")


def restar():
    try:
        res = float(entrada1.get()) - float(entrada2.get())
        resultado_label.config(text=f"Resultado: {formatear_resultado(res)}")
    except ValueError:
        resultado_label.config(text="Error: entrada inválida")


def dividir():
    try:
        num2 = float(entrada2.get())
        if num2 == 0:
            resultado_label.config(text="Error: división por 0")
        else:
            res = float(entrada1.get()) / num2
            resultado_label.config(text=f"Resultado: {formatear_resultado(res)}")
    except ValueError:
        resultado_label.config(text="Error: entrada inválida")


# Crear ventana principal
ventana = tk.Tk()
ventana.title("Calculadora simple")
ventana.geometry("300x300")
ventana.resizable(False, False)

# Widgets
tk.Label(ventana, text="Número 1").pack()
entrada1 = tk.Entry(ventana)
entrada1.pack()

tk.Label(ventana, text="Número 2").pack()
entrada2 = tk.Entry(ventana)
entrada2.pack()

tk.Button(ventana, text="Sumar", command=sumar).pack(pady=5)
tk.Button(ventana, text="Restar", command=restar).pack(pady=5)
tk.Button(ventana, text="Dividir", command=dividir).pack(pady=5)

resultado_label = tk.Label(ventana, text="Resultado:", font=("Arial", 14))
resultado_label.pack(pady=10)

ventana.mainloop()