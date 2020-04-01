# Modulo-SXE-2-EVAL
Modulo 2ªEvalucion

Este modulo trata de recrear un videoclub con un sitema de alquielr de peliculas. Estas peliculas podremos añadirlas nosotros mismo al igual que los datos del director de ellas. Consta de 3 modelos diferentes.

### Modelo VideoclubDirectores

Este modelo es el encargado de manejar los datos de los directores de las peliculas. Consta de 6 atributos principales.

- partner_id: al al tener herencia con el modelo res.partner en este atributo nos saldrán los nombres ya creados para este campo los cuales estan en el modelo padr.
- nombre: en este campo se indica simplemente el nombre del director.
- fecha_nacimiento: en este campo de tipo Date, indicamos la fecha en el la que nació el director.
- foto: es un campo de tipo Bnary que guardará una foto del director.
- edad: este campo es un campo calculado el cual mediante el metodo calcular__edad comprobará cuantos alos tiene el director en funcion de la fecha de nacimiento que hayamos introducido. Si la fecha es superior a la fecha del dia en el que se crea o igual al propio dia saltará un aviso y no dejara crear al director.
- retirado: en un campo de tipo char en el que se indica con si o no si el director está retirado o no.

Por otra parte el state es el estado en el que se encuentra ell director el cual puede ser activo, retirado o fallecido. Por defecto el estado será activo.

Tendremos las opciones de vistar form y tree.

Ademas en este modelo tendramos un menu con botones en los que podrémos cambiar el estado de un director a disponible si esta retirado, a retirado si esta disponible o a fallecido si esta disponible o retirado.

### Modelo VideoclubPeliculas

Este modelo manejara los datos de las péliculas las cuales se pueden alquilar en el videoclub. En este caso existen 4 atributos:

- titulo: como su nombre indica es el título de la película el cuál será requerido para poder creara.
- genero: en este indicaremos de que genero es la película.
- horas: un campo integer en el que indicaremos cuantas horas dura la pelicula.
- directores: en este campo podremos introducir el director de la pélicula tomando como ejermplos los directores creados en el modelo directores. Si no hay niguno podremos crear uno directamente desde esta pantalla.

Este modelo tenemos la opcion de vistar tree, kanban y form.

### Modelo VideoclubAlquiler

Por último tenemos este modelo de alquiler el cual como su nombre indica llevara los alquileres de las peliculas en el videoclub. Consta simplemente de 3 atributos:

- nombre_pelicula: en este indicaremos el nombre de la pelicula que queramos alquilar tomando los datos introducidos en el modelo donde guardamos los datos de las peliculas.
- fecha_alquiler: es la fecha en la alquilamos la pelicula que for defecto esta la fecha actual en la que esteamos creando el alquiler.
- fecha_devolucion: es la fecha en la que se deberá devolver la pelicula, esta no puede ser inferior o igual a la fecha de alquiler ya que nos saltará un aviso de que es erroneo y que como mínimo podemos alquilarla 1 día.

En este modelo tendremos las vists form, tree y calendar en modo calendario para visualizar mejor las fechas.