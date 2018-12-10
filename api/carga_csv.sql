use api;
delete clicluster;
load data infile '/home/osboxes/api/clicluster.csv' 
into table clicluster 
fields terminated by ',' 
lines terminated by '\n' 
ignore 1 rows;
delete deucluster;
load data local infile '/home/osboxes/api/deucluster.csv'
into table deucluster 
fields terminated by ',' 
lines terminated by '\n' 
ignore 1 rows;
delete morahistorica;
load data local infile '/home/osboxes/api/morahistorica.csv' 
into table morahistorica 
fields terminated by ',' 
lines terminated by '\n' 
ignore 0 rows;
