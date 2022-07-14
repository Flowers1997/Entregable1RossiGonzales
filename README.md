
Entregable
# Entregable1RossiGonzales
Readme-instrucciones de uso del Entregable1RossiGonzalez :

#Primero debemos poner a correr el sevidor;  al abrir este archivo con VSC en consola escribiremos: python manage.py runserver

#Este comando nos dara un link de acceso a nuestro servidor http://127.0.0.1:8000 , y a acederemos a la primer vista de inicio escribiendo /App1/ en el link ---> http://127.0.0.1:8000/App1/

#En la vista inicio usted podra ver distintos botones como Cocineros, Mozos y Lava Platos, que lo redireccionaran a las distintas vistas, o tambien puede acceder a ellas usando los siguientes links:

http://127.0.0.1:8000/App1/cocineros/
http://127.0.0.1:8000/App1/mozos/
http://127.0.0.1:8000/App1/lavaplatos/

En cada una de estas vistas antes mencionadas usted podra encontrar un formulario que le permitira ingresar un empleado completando los datos de Nombre, Apellido, antiguedad en la empresa y fecha de nacimiento

#Utilizando el boton Buscar Mozo, o el link http://127.0.0.1:8000/App1/busquedaMozos/ , usted accedera a un formulario que le permitira buscar a un mozo en la base de datos ingresando el apellido, puede probar buscando Rossi, Gonzales o Miramontes

Caracteristicas del entregable:
nuestro proyecto cuenta con herencia html en 4 archivos html que heredan del archivo padre.html una plantilla con Bootstrap y otros dos archivos html como son busquedaMozos y resultadoBusqueda que usan una plantilla creada a partir del signo "!"
