import sqlite3

def create_table():
    """Create the GroceryDB table"""
    conn = sqlite3.connect("GroceryDB.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS
                    GroceryDB (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    general_name TEXT NOT NULL, count_products INTEGER
                    NOT NULL, ingred_FPro REAL NOT NULL, avg_FPro_products
                    REAL NOT NULL, avg_distance_root REAL NOT NULL,
                    ingred_normalization_term REAL NOT NULL, semantic_tree_name
                    TEXT NOT NULL, semantic_tree_node TEXT NOT NULL)""")
    cursor.execute("PRAGMA table_info(GroceryDB);")
    results = cursor.fetchall()
    column_names = [result[1] for result in results]
    print(column_names)
    conn.commit()
    conn.close()


def create(general_name, count_products,
            ingred_FPro, avg_FPro_products,
              avg_distance_root, ingred_normalization_term,
                semantic_tree_name, semantic_tree_node):
    """Insert a new item into the GroceryDB table"""
    conn = sqlite3.connect("GroceryDB.db")
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM GroceryDB")
    id = cursor.fetchone()[0] + 1
    cursor.execute("""INSERT INTO GroceryDB (id, general_name, count_products,
                    ingred_FPro, avg_FPro_products, avg_distance_root, 
                   ingred_normalization_term, semantic_tree_name,
                    semantic_tree_node) VALUES (?, ?, ?, ?, ?, ?, ?, ?,
                    ?)""", (id, general_name, count_products, ingred_FPro,
                             avg_FPro_products, avg_distance_root,
                               ingred_normalization_term, semantic_tree_name,
                                 semantic_tree_node))
    conn.commit()
    conn.close()


def read():
    """Query the database for all rows of the GroceryDB table"""
    conn = sqlite3.connect("GroceryDB.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM GroceryDB")
    rows = cursor.fetchall()
    conn.close()

    for row in rows:
        print(row)


def update(id, general_name,
            count_products, ingred_FPro,
              avg_FPro_products, avg_distance_root,
                ingred_normalization_term, semantic_tree_name,
                  semantic_tree_node):
    """Update an item in the GroceryDB table"""
    conn = sqlite3.connect("GroceryDB.db")
    cursor = conn.cursor()
    cursor.execute("""UPDATE GroceryDB SET general_name=?,
                    count_products=?, ingred_FPro=?,
                    avg_FPro_products=?, avg_distance_root=?,
                    ingred_normalization_term=?, semantic_tree_name=?,
                    semantic_tree_node=? WHERE id=?""",
                      (general_name, count_products,
                        ingred_FPro, avg_FPro_products,
                          avg_distance_root, ingred_normalization_term,
                            semantic_tree_name, semantic_tree_node, id))
    conn.commit()
    conn.close()

def delete(id):
    """Delete an item from the GroceryDB table"""
    conn = sqlite3.connect("GroceryDB.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM GroceryDB WHERE id=?", (id,))
    deleted_rows = cursor.rowcount
    conn.commit()
    conn.close()
    return deleted_rows

def get_database_dimensions():
    """Get the number of rows and columns in the GroceryDB table"""
    conn = sqlite3.connect("GroceryDB.db")
    cursor = conn.cursor()
    cursor.execute("""SELECT COUNT(*) AS num_rows, COUNT(*) * (SELECT COUNT(*)
                    FROM pragma_table_info('GroceryDB'))
                    AS num_cols FROM GroceryDB""")
    result = cursor.fetchone()
    conn.close()
    if result:
        return result
    else:
        return None


if __name__ == "__main__":
    create_table()
    create_table()
    create("Eggs", 10, 0.5, 0.2, 0.1, 0.3, "Tree1", "Node1")
    last_id = get_database_dimensions()[0]
    update(last_id, "Eggs", 20, 0.5, 0.2, 0.1, 0.3, "Tree1", "Node1")
    delete(last_id)
    read()