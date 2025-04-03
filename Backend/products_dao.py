from sql_connection import get_sql_connection

import mysql.connector

def get_all_products(connection): 

    cursor = connection.cursor()

    query = ("SELECT products.products_id, products.name, products.uom_id, products.price_per_unit, uom.uom_name FROM grocery_store.products INNER JOIN grocery_store.uom ON products.uom_id = uom.uom_id;")

    cursor.execute(query)
    
    response = []

    for (products_id,name,uom_id,price_per_unit,uom_name) in cursor:
        response.append(
            {
                'products_id':products_id,
                'name':name,
                'uom_id':uom_id,
                'price_per_unit': price_per_unit, 
                'uom_name': uom_name
            }
            
        )
    
    return response

def insert_new_product(connection,product):
    cursor = connection.cursor()
    query = ("insert into products(name,uom_id,price_per_unit) values(%s,%s,%s)")
    
    data = (product['product_name'],product['uom_id'],product['price_per_unit'])
    cursor.execute(query,data)
    
    connection.commit()
    return cursor.lastrowid 

def delete_product(connection,product_id):
    cursor = connection.cursor()
    query = ("DELETE FROM products where products_id = " + str(product_id))
    cursor.execute(query)
    connection.commit()
    
    
if __name__ == '__main__':
    connection = get_sql_connection()
    print(delete_product(connection,13))