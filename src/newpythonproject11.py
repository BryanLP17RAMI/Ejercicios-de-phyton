# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "BRIAN-FERNANDEZ"
__date__ = "$19/10/2015 05:06:45 PM$"

print 'Si desea entrar al menu de ARCHIVO ingresar la opcion 1'
print 'Si desea entrar al menu de BUSQUEDA ingresar la opcion 2'
print 'Si desea entrar al menu de SALIR ingresar la opcion 3'
a=input('Introduzca algunas de las opciones mencionadas=')
if a == 1 :
    print 'Bienvenido al menu de ARCHIVOS'
else:
    if a==2:
        print 'Bienvenido al menu de BUSQUEDA'
    else:
        if a==3:
            print 'Bienvenido al menu de SALIDA'
        else:
            print 'Ingrese una de las opciones validas mencionadas anteriormente'
