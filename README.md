# Python-36585-Aerolineas

## Deployment
Para instalar el proyecto y la aplicación en su máquina local, deberá realizar los siguientes pasos.
1. Instanciarse en la ubicación donde quiere ejecutarlo. (Por ejemplo, C:\Users\agugliuzza\CoderHouse\Python-36585).
    - cd CoderHouse
        - cd Python-36585

2. Ejecutar el siguiente script:
    - $ git clone https://github.com/agusgugliu/python-36585-Aerolineas.git

3. En Visual Studio Code, abrir la carpeta en donde clonamos el repositorio desde **File/Open Folder**

4. Abrir la Terminal Integrada de Visual Studio Code e instanciarnos en el proyecto de **Aerolineas**
    - cd Aerolineas

5. Ejecutar el comando para correr el servidor.
    - python manage.py runserver

6. Ingresar a http://127.0.0.1:8000/

7. Podrá seleccionar entre 3 íconos:
    - Aeropuertos:
        - permite visualizar aeropuertos
        - permite añadir aeropuertos
        - permite buscar aeropuertos por:
            - país
            - provincia
        - permite borrar aeropuertos
    - Aerolíneas
        - permite visualizar aerolíneas
        - permite añadir aerolíneas
        - permite buscar aerolíneas por:
            - país de bandera
            - alianza
        - permite borrar aerolíneas
    - Vuelos
        - permite visualizar vuelos
        - permite añadir vuelos
        - permite buscar vuelos por:
            - número de vuelo
            - aeropuerto de origen
            - aeropuerto de destino
        - permite borrar vuelos