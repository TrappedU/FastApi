CREATE TABLE `scrapper` (
  `id` int NOT NULL AUTO_INCREMENT,
  `url` varchar(256) NOT NULL,
  `status` varchar(256) NOT NULL,
  'result' json,
  `created_at` DATETIME,
  `last_modified_date` DATETIME,
  `last_modified_by` char(60) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
);