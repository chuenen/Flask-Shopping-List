CREATE TABLE `product` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `stock_pcs` INT UNSIGNED NOT NULL,
  `price` INT UNSIGNED NOT NULL,
  `shop_id` VARCHAR(2) NOT NULL,
  `vip` ENUM('false', 'true') NOT NULL,
  `disabled` ENUM('false', 'true') NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE `order` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `product_id` INT UNSIGNED NOT NULL,
  `customer_id` VARCHAR(20) NOT NULL,
  `qty` INT UNSIGNED NOT NULL,
  `disabled` ENUM('false', 'true') NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

INSERT INTO `product` (id, stock_pcs, price, shop_id, vip, disabled) VALUES
  (1, 6, 150, 'um', 'false', 'false'),
  (2, 10, 110, 'ms', 'false', 'false'),
  (3, 20, 900, 'ps', 'false', 'false'),
  (4, 2, 1899, 'ps', 'true', 'false'),
  (5, 8, 35, 'ms', 'false', 'false'),
  (6, 5, 60, 'um', 'false', 'false'),
  (7, 5, 800, 'ps', 'true', 'false');
