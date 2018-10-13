CREATE DATABASE `ebay_log`

CREATE TABLE `log_item` (
`corr_id` VARCHAR(256) NOT NULL,
`timestamp` DATE NOT NULL,
`url_api` VARCHAR(256) NULL,
`node_id` VARCHAR(256) NULL,
`ri` VARCHAR(256) NULL,
`parent_ri` VARCHAR(256) NULL,
INDEX `key` (`corr_id`),
INDEX `time_index` (`timestamp`)
)
COLLATE='utf8_general_ci'
;