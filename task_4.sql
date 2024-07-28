USE alx_book_store;

FROM
    INFORMATION_SCHEMA.COLUMNS
SELECT 
    COLUMN_NAME, 
    COLUMN_TYPE,  
    COLUMN_KEY,   
WHERE 
    TABLE_SCHEMA = 'alx_book_store', 
    TABLE_NAME = 'Books';
