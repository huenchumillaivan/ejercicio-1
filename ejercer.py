print("Usted ah ingresado a nombre de usuario")
usuario = input("ingrese su nombre: ")
edad = (int(input("ingrese su edad: ")))

if len(usuario) > 5 and len(usuario) < 15 and usuario[0].isalpha() and usuario.isalnum():
    print("nombre de usuario valido")
    print(f"bienvenido gracias por ingresar don/dama {usuario}")
    print(f"su edad es: {edad}")
elif len(usuario) <= 5 or len(usuario) >= 15:
    print("Error: la longitud debe estar entre 6 y 14 caracter. :D")
else:
    print("Error: El usuario debe ser alfanumerico y comenzar con una letra.")    