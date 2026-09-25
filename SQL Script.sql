/*
 	Create Table
 	--------------
 	Create Table Table_Name (
 		col_name datatype constraint,
 		col_name datatype constraint
 		
 		id integer primary key autoincrement,
 		name text not null unique,
 		type text not null check (type in ('type1', 'type2', 'type3'))
 	);
 	
 	autoincrement -> SQLite, MySQL, PosGres SQL
 */
-- Customer Table
Create Table Customers (
	customer_id integer primary key autoincrement,
	customer_name text not null,
	email text not null unique,
	phone text not null unique,
	address text not null,
	customer_type text not null CHECK (customer_type  in (
											'Regular', 'Non-Regular', 'VIP'
										))
);


/*
 * Insert Data
 * --------------
 * Insert into Table_Name (col1, col2, col3, col4) values (val1, val2, val3, val4);
 *
 * Multiple Insertion
 * ----------------------
 * Insert into Table_Name (col1, col2, col3, col4) values
 * (val1, val2, val3, val4),
 * (val1, val2, val3, val4),
 * (val1, val2, val3, val4);
 */


/*
 * Insert, Update, Delete -> change data in database
 * ----------------------------------------------------
 * Commit -> Permanent Change, 
 * Rollback -> Undo Changes - Only for temporary changes, 
 * SavePoint (Checkpoint) -> Permanent Change in Memory
 * 
 * 
 * Nepal Bank
 * 	- start savepoint
 * 	- Each 15 Minutes -> Commit
 * 	- stop savepoint
 */

-- Insert
Insert into Customers (customer_name, email, phone, address, customer_type)
values ('Shyam', 'shyam@gmail.com', '1234567890', 'Kathmandu', 'VIP');


select * from Customers;

select * from Staffs;

select * from orders;


/*
 * Update Table Data
 * ------------------
 * Update Table_Name set col_name = value where pk=value;
 */

Update Orders set order_status = 'Processing' where order_id = 3;

/*
 * Delete Data
 * ----------------
 * Delete
 * 	- Remove singe data or Multiple data.
 * 	- It does not reset structure.
 * 		- Delete from table_name where pk = value;
 * 
 * Truncate
 * 	- Removes all data and reset structure.
 *  - Data cannot be recovered even if it is not committed.
 * 
 * Remove Structure
 * -------------------
 * Drop 
 */

delete from orders;

/*
 * Basic Analysis
 * ----------------- 
 * 1. Where -> Used for data filter.
 * 2. And -> used to extract data of numeric range.
 * 3. OR
 * 4. Between
 * 5. In
 * 6. Like
 */

--select * from table_name where col_name = 'value';

select * from orders where order_status = 'Pending';
























