-- To run: Ctrl + Shift + Q

DELETE FROM AppAerolineas_aeropuertos;
DELETE FROM  sqlite_sequence where name='AppAerolineas_aeropuertos';


DELETE FROM AppAerolineas_aerolineas;
UPDATE AppAerolineas_aerolineas SET nombre = UPPER(nombre);
DELETE FROM  sqlite_sequence where name='AppAerolineas_aerolineas';


DELETE FROM AppAerolineas_vuelos;
DELETE FROM  sqlite_sequence where name='AppAerolineas_vuelos';