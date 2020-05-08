CREATE TABLE `student_tb` (
    `sno` int(11) NOT NULL,
    `name` char(10) DEFAULT NULL,
    `det` char(20) DEFAULT NULL,
    `addr` char(80) DEFAULT NULL,
    `tel` char(20) DEFAULT NULL,
    PRIMARY KEY (`sno`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

show tables;