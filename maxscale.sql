CREATE USER 'maxscale'@'%' IDENTIFIED BY 'shard';
GRANT SELECT ON mysql.user TO 'maxscale'@'%';
GRANT SELECT ON mysql.db TO 'maxscale'@'%';
GRANT SELECT ON mysql.tables_priv TO 'maxscale'@'%';
GRANT SELECT ON mysql.columns_priv TO 'maxscale'@'%';
GRANT SELECT ON mysql.procs_priv TO 'maxscale'@'%';
GRANT SELECT ON mysql.proxies_priv TO 'maxscale'@'%';
GRANT SELECT ON mysql.roles_mapping TO 'maxscale'@'%';
GRANT SHOW DATABASES ON *.* TO 'maxscale'@'%';
GRANT SELECT ON mysql.* TO 'maxscale'@'%';
GRANT ALL PRIVILEGES ON zipcodes_one.* TO 'maxscale'@'%';
GRANT ALL PRIVILEGES ON zipcodes_two.* TO 'maxscale'@'%';

