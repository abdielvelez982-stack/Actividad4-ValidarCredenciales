
import tkinter as tk
import os
from dotenv import load_dotenv

# Cargar las variables de entorno
load_dotenv()


# Función 1: Capturar las credenciales
def capturar_credenciales():
    usuario = entrada_usuario.get()
    contrasena = entrada_contrasena.get()
    return usuario, contrasena


# Función 2: Validar las credenciales
def validar_credenciales():
    usuario, contrasena = capturar_credenciales()

    usuario_correcto = os.getenv("APP_USER")
    contrasena_correcta = os.getenv("APP_PASSWORD")

    if usuario == usuario_correcto and contrasena == contrasena_correcta:
        mostrar_mensaje("Acceso correcto", "green")
    else:
        mostrar_mensaje("Usuario o contraseña incorrectos", "red")


# Función 3: Mostrar el mensaje
def mostrar_mensaje(mensaje, color):
    etiqueta_resultado.config(text=mensaje, fg=color)


# Crear ventana
ventana = tk.Tk()
ventana.title("Inicio de sesión")
ventana.geometry("350x250")

# Usuario
tk.Label(ventana, text="Usuario:").pack(pady=5)
entrada_usuario = tk.Entry(ventana)
entrada_usuario.pack()

# Contraseña
tk.Label(ventana, text="Contraseña:").pack(pady=5)
entrada_contrasena = tk.Entry(ventana, show="*")
entrada_contrasena.pack()

# Botón
boton_ingresar = tk.Button(
    ventana,
    text="Ingresar",
    command=validar_credenciales
)
boton_ingresar.pack(pady=15)

# Resultado
etiqueta_resultado = tk.Label(ventana, text="")
etiqueta_resultado.pack()

ventana.mainloop()
