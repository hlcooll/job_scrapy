CREATE TABLE `python_job` (
  `id` int(20) NOT NULL AUTO_INCREMENT,
  `position` varchar(30) DEFAULT NULL COMMENT '职位',
  `salary` varchar(20) DEFAULT NULL COMMENT '薪水',
  `t_company` varchar(30) DEFAULT NULL COMMENT '公司',
  `address` varchar(50) DEFAULT NULL COMMENT '地址',
  `touch` varchar(30) DEFAULT NULL COMMENT '联系方式',
  `url` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=152 DEFAULT CHARSET=utf8
