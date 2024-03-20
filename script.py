import mysql.connector

"""
Sql Connection Configuration
"""
config = {
    'host': 'localhost',
    'port': 4000,
    'user': 'maxscale',
    'password': 'shard',
}


def execute_query(cursor, query):
    rows = None
    try:
        cursor.execute(query)
        rows = cursor.fetchall()
    except e:
        print("Error: Cannot execute query")
    return rows


def prety_print(items, items_per_line):

    # Clean up
    items = [item[0] for item in items if item and item[0]]


    i = 0
    while i < len(items):
        string = " ".join(f"{str(item):10}" for item in items[i: i + items_per_line])
        i += 10
        print(string)
    

def task1(cursor):
    """
    print the largest zipcode in zipcodes_one
    """

    query = """
        SELECT MAX(Zipcode) AS Largest_Zipcode FROM zipcodes_one.zipcodes_one;
    """

    rows = execute_query(cursor, query)
    if rows and rows[-1]:
        print(f"The largest zipcode in zipcodes_one: {rows[-1][-1]}")
    else:
        print(f"The largest zipcode in zipcodes_one = Not Found")
    print()


def task2(cursor):
    """
        All zipcodes where state=KY (Kentucky).
    """
    query1 = """
        SELECT Zipcode FROM zipcodes_one.zipcodes_one WHERE State = 'KY'
    """
    query2 = """
        SELECT Zipcode FROM zipcodes_two.zipcodes_two WHERE State = 'KY'
    """

    rows = []
    rows = execute_query(cursor, query1)
    rows.extend(execute_query(cursor, query2))
    if rows:
        print(f"All zipcodes where state=KY, zipcodes count =  {len(rows)}")
        prety_print(rows, 5)
    print()

def task3(cursor):
    """
    print All zipcodes between 40000 and 41000
    """
    query1 = """
        SELECT Zipcode FROM zipcodes_one.zipcodes_one WHERE Zipcode BETWEEN 40000 AND 41000
    """
    query2 = """
        SELECT Zipcode FROM zipcodes_two.zipcodes_two WHERE Zipcode BETWEEN 40000 AND 41000
    """
    rows = []
    rows = execute_query(cursor, query1)
    rows.extend(execute_query(cursor, query2))
    if rows:
        print(f"All zipcodes between 40000 and 41000: zipcodes count = {len(rows)}")
        prety_print(rows, 5)
    print()

def task4(cursor):
    """
    The TotalWages column where state=PA (Pennsylvania)
    """
    query1 = """
        SELECT TotalWages FROM zipcodes_one.zipcodes_one WHERE State = 'PA'
    """
    query2 = """
        SELECT TotalWages FROM zipcodes_two.zipcodes_two WHERE State = 'PA'
    """
    rows = []
    rows = execute_query(cursor, query1)
    rows.extend(execute_query(cursor, query2))
    if rows:
        print(f"The TotalWages column where state=PA (Pennsylvania): TotalWagescount = {len(rows)}")
        prety_print(rows, 5)
    print()


def main():
    try:
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()
        task1(cursor)
        task2(cursor)
        task3(cursor)
        task4(cursor)
    except mysql.connector.Error as error:
        print(error)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

main()

