import sqlite3


con = sqlite3.connect("product_info_db")

c = conn.cursor():

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS product_info_db(id INTEGER, prodname TEXT, prodstatus TEXT, prodprice INTEGER,prodtype TEXT)')

    def data_Entry():
        c.execute("INSERT INTO product_info_db VALUES(90,'Nexon','Not Available',1000000,'Cars')")
        c.execute("INSERT INTO product_info_db VALUES(78,'Baggit','Available',3000,'Handbags')")
        c.execute("INSERT INTO product_info_db VALUES(12,'Libas','Not Available',1000,'Clothing')")
        c.execute("INSERT INTO product_info_db VALUES(34,'SSS','Available',2500,'Footwear')")
        c.execute("INSERT INTO product_info_db VALUES(56,'Tablet','Available',15000,'Gadget')")

        conn.commit()
        c.close()
        conn.close()
