
# Creating a table
Create table FeatureGroupInstance (
		featgrp_id integer PRIMARY KEY, 
		window int, T date, 
		Symbol varchar );
Create table Feature (
		feat_id integer PRIMARY KEY,
		name varchar, 
		group varchar);
Create table FeatureValue (
		Primary key (id), 
		value decimal, 
		value_id integer PRIMARY KEY,
    	feat_id integer REFERENCES Feature (feat_id), 
    	featgrp_id integer REFERENCES FeatureGroupInstance (featgrp_id), 

    );

# Inserting data
INSERT INTO products (product_no, name, price) VALUES
    (1, 'Cheese', 9.99),
    (2, 'Bread', 1.99),
    (3, 'Milk', 2.99);


# Update
UPDATE COMPANY SET SALARY = 15000 WHERE ID = 3;


