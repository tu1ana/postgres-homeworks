-- Подключиться к БД Northwind и сделать следующие изменения:
-- 1. Добавить ограничение на поле unit_price таблицы products (цена должна быть больше 0)
ALTER TABLE products ADD CONSTRAINT chk_products_unit_price CHECK (unit_price > 0);

-- 2. Добавить ограничение, что поле discontinued таблицы products может содержать только значения 0 или 1
ALTER TABLE products ADD CONSTRAINT chk_products_discontinued CHECK (discontinued IN (0, 1));

-- 3. Создать новую таблицу, содержащую все продукты, снятые с продажи (discontinued = 1)
SELECT * INTO discontinued_products FROM products WHERE discontinued = 1;

-- 4. Удалить из products товары, снятые с продажи (discontinued = 1)
-- Для 4-го пункта может потребоваться удаление ограничения, связанного с foreign_key. Подумайте, как это можно решить, чтобы связь с таблицей order_details все же осталась.

--solution 1 (not the best one as it deletes the relationship 'products - order_details')
ALTER TABLE order_details drop CONSTRAINT fk_order_details_products;
DELETE FROM products WHERE discontinued = 1;

DELETE FROM order_details
WHERE product_id NOT IN (SELECT product_id FROM products); -- deleting product_ids from order_details which are no longer in products

ALTER TABLE order_details ADD CONSTRAINT fk_order_details_products FOREIGN KEY(product_id) REFERENCES products(product_id) --relationship renewed

--solution 2 (a better one - foreign keys intact)
DELETE FROM order_details
WHERE product_id IN (SELECT product_id FROM products where discontinued = 1);

DELETE FROM products WHERE discontinued = 1;


--alter table order_details add column product_name varchar(40)
--update order_details set product_name = (
--	select product_name from products
--	where products.product_id = order_details.product_id
--)
--alter table products add constraint products_unique_name unique (product_name)
--ALTER TABLE order_details add CONSTRAINT fk_order_details_product_name FOREIGN KEY(product_name) REFERENCES products(product_name)
--ALTER TABLE order_details drop CONSTRAINT fk_order_details_product_name

--ALTER TABLE order_details add CONSTRAINT fk_order_details_products FOREIGN KEY(product_id) REFERENCES products(product_id)

