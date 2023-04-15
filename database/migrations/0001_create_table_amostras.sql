use heroku_25b7ace0ee7f569;

drop table amostras;

create table amostras (
	id int primary key auto_increment,
	mp10 decimal not null,
	mp25 decimal not null,
	o3 decimal not null,
	co decimal not null,
	no2 decimal not null,
	so2 decimal not null
) DEFAULT CHARSET = utf8mb4;

alter table amostras auto_increment = 1;