def validar_usuario(nombre_usuario):

     longitud=len(nombre_usuario)
     x=nombre_usuario.isalnum()

     if x== False:
         print("El nombre de usuario puede contener solo letras y números")

     if longitud < 6:
         print("El nombre de usuario debe contener al menos 6 caracteres")

     if longitud > 12:
         print("El nombre de usuario no puede contener más de 12 caracteres")

     if longitud >5 and longitud <13 and x ==True:
        return True