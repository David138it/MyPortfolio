/*CREATE TABLE de13ma.gabn_dz2_brands (
id_brand SERIAL PRIMARY KEY,
title VARCHAR (255)
);*/
/*INSERT INTO de13ma.gabn_dz2_brands (title) VALUES 
('Nissan'),
('Chevrolet'),
('Datsun'),
('Hyundai'),
('Lada');*/
/*CREATE TABLE de13ma.gabn_dz2_transmittion_box (
id_box SERIAL PRIMARY KEY,
title VARCHAR (255)
);
INSERT INTO de13ma.gabn_dz2_transmittion_box (title) VALUES 
('Автомат'),
('Механика'),
('Вариатор');*/
/*CREATE TABLE de13ma.gabn_dz2_country_partner (
id_country SERIAL PRIMARY KEY,
title VARCHAR (255)
);
INSERT INTO de13ma.gabn_dz2_country_partner (title) VALUES 
('Russia'),
('Japane'),
('USA'),
('South Korea');*/
/*CREATE TABLE de13ma.gabn_dz2_clients (
id_client SERIAL PRIMARY KEY,
fio VARCHAR (255),
phone VARCHAR (255),
city VARCHAR (255)
);
INSERT INTO de13ma.gabn_dz2_clients 
(fio, phone, city) 
VALUES 
('David', '88886666000', 'Kutaisi'),
('Angelina', '88880000665', 'Irkutsk'),
('Leonid', '88886666111', 'Irkutsk');*/
/*CREATE TABLE de13ma.gabn_dz2_cars (
id_car SERIAL PRIMARY KEY,
id_brand INT REFERENCES de13ma.gabn_dz2_brands(id_brand),
model VARCHAR (255),
price NUMERIC,
releases TIMESTAMP,
id_box INT REFERENCES de13ma.gabn_dz2_transmittion_box(id_box),
id_country INT REFERENCES de13ma.gabn_dz2_country_partner(id_country)
);
INSERT INTO de13ma.gabn_dz2_cars (id_brand, model, price, releases, id_box, id_country) VALUES 
(1, 'Windgroad', 250000, '2006-09-12 12:12:12', 1, 2),
(2, 'Aveo', 450000, '2013-09-12 12:12:12', 3, 3),
(3, 'On-do', 300000, '2015-09-12 12:12:12', 2, 2),
(4, 'Solaris1', 750000, '2017-09-12 12:12:12', 1, 4),
(4, 'Solaris2', 900000, '2020-09-12 12:12:12', 1, 4),
(5, 'Vesta', 850000, '2021-09-12 12:12:12', 3, 1);*/
/*CREATE TABLE de13ma.gabn_dz2_sale (
id_sale SERIAL PRIMARY KEY,
id_car INT REFERENCES de13ma.gabn_dz2_cars(id_car),
id_client INT REFERENCES de13ma.gabn_dz2_clients(id_client),
dates TIMESTAMP
);
INSERT INTO de13ma.gabn_dz2_sale (id_car, id_client, dates) VALUES 
(1, 1, '2006-09-12 12:12:12'),
(2, 2, '2014-09-12 12:12:12'),
(3, 1, '2015-09-12 12:12:12'),
(4, 2, '2017-09-12 12:12:12'),
(5, 3, '2020-09-12 12:12:12'),
(6, 1, '2021-09-12 12:12:12');*/
SELECT * from de13ma.gabn_dz2_sale;