import modulo_usuario
import modulo_contraseña

correcto=False
while correcto==False:
        nombre=input("Ingrese nombre de usuario: ")
        if modulo_usuario.validar_usuario(nombre) == True:
            print("Usuario creado exitosamente")
            correcto=True

while correcto==True:
    cont=input("Ingrese su Contraseña: ")
    if modulo_contraseña.clave(cont)==True:
        print("Contraseña creada exitosamente")
        correcto=False