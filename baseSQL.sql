CREATE TABLE `rss_appid` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user` varchar(100) DEFAULT NULL COMMENT '使用者',
  `mobile` varchar(99) DEFAULT NULL,
  `appid` varchar(255) NOT NULL COMMENT 'APPID值',
  `appsercet` varchar(255) DEFAULT NULL,
  `create_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  PRIMARY KEY (`appid`,`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

CREATE TABLE `rss_users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `time` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email_unique` (`email`)
) ENGINE=MyISAM AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

CREATE TABLE `rss_subscribe` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL COMMENT '用户ID',
  `link` varchar(255) DEFAULT NULL COMMENT '订阅链接',
  `add_time` int(11) DEFAULT NULL COMMENT '添加时间',
  `last_update` int(11) DEFAULT NULL COMMENT '上次更新时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `防止用户订阅重复` (`user_id`,`link`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `rss_data` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `channel_id` int(11) DEFAULT NULL,
  `title` varchar(255) DEFAULT NULL,
  `desc` text,
  `link` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `防止用户订阅重复` (`channel_id`,`link`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
