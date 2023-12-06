# djangoWebApp

Aplicacion que permite:

# 1 Cargar autos a la BBDD mediante formulario.

La siguiente función `cars_view` es una vista de Django diseñada para manejar la operación de agregar un nuevo auto a la base de datos. La vista verifica el método de la solicitud (GET o POST) para determinar cómo debe procesarse.

Si la solicitud es un método GET, significa que el usuario está accediendo a la página para agregar un auto y se renderiza un formulario vacío utilizando la clase `AutoFormulario`. El formulario se pasa como contexto a la plantilla "consesionario/add_car.html", donde el usuario puede ingresar la información del auto.

Si la solicitud es un método POST, significa que el usuario ha enviado el formulario con la información del nuevo auto. En este caso, se instancia un objeto `AutoFormulario` utilizando los datos de la solicitud y se verifica si el formulario es válido. Si es válido, se extraen los datos limpios del formulario y se crea un nuevo objeto `Auto` con la información del auto.

# 2 Cargar Sucursales a la BBDD mediante formulario.

La función garages_view es una vista de Django para agregar nuevas sucursales al sistema. Verifica si la solicitud es de tipo GET, en cuyo caso renderiza un formulario vacío con SucursalFormulario en la plantilla "consesionario/add_garage.html". Si la solicitud es de tipo POST, instancia un objeto SucursalFormulario con los datos de la solicitud, verifica la validez del formulario y, si es válido, crea un nuevo objeto Sucursal con la información proporcionada.

# 3 Cargar Clientes a la BBDD mediante formulario 

La función customers_view en Django gestiona la adición de nuevos clientes al sistema. Cuando la solicitud es GET, se muestra un formulario vacío (ClienteFormulario) en la plantilla "consesionario/add_customer.html". Si la solicitud es POST (cuando se envía el formulario), se valida el formulario, y si es válido, se crea un nuevo objeto Cliente con los datos proporcionados.

# 4 Muestra todos los datos en tablas desde la BBDD