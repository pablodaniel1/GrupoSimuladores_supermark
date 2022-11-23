BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "Clientes" (
	"Id de Cliente"	NUMERIC NOT NULL,
	"Nombre"	TEXT NOT NULL,
	"Apellido"	TEXT NOT NULL,
	"Domicilio"	TEXT NOT NULL,
	"Correo Electronico"	TEXT NOT NULL,
	"Telefono"	NUMERIC NOT NULL,
	PRIMARY KEY("Id de Cliente")
);
CREATE TABLE IF NOT EXISTS "Productos" (
	"Codigo de barras"	REAL NOT NULL,
	"Categoria"	TEXT NOT NULL,
	"Precio"	NUMERIC NOT NULL,
	"Cantidad"	NUMERIC NOT NULL,
	PRIMARY KEY("Codigo de barras")
);
CREATE TABLE IF NOT EXISTS "Carrito" (
	"Producto"	TEXT,
	"Cantidad"	INTEGER,
	"Precio"	INTEGER
);
CREATE TABLE IF NOT EXISTS "Lista de compras" (
	"Codigo de barras"	REAL NOT NULL,
	"Cantidad"	NUMERIC NOT NULL,
	"Producto"	TEXT NOT NULL,
	"Precio"	TEXT NOT NULL,
	PRIMARY KEY("Codigo de barras")
);
CREATE TABLE IF NOT EXISTS "Medios de pago" (
	"Tarjeta"	NUMERIC,
	"Efectivo"	NUMERIC,
	"Transferencia"	NUMERIC,
	"Deposito"	NUMERIC
);
COMMIT;
