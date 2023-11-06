# """
# ETL-Query script
# """

# from mylib.extract import extract
# from mylib.transform_load import load
# from mylib.query import query

# # Extract
# print("Extracting data...")
# extract()

# # Transform and load
# print("Transforming data...")
# load()

# # Query
# print("Querying data...")
# query()

# """
# ETL-Query script
# """

import argparse
from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import query
from mylib.CRUD import get_database_dimensions
from mylib.CRUD import create
from mylib.CRUD import read
from mylib.CRUD import update
from mylib.CRUD import delete


def main(args):
    # Extract
    print("Extracting data...")
    extract()

    # Transform and load
    print("Transforming data...")
    load()

    # CRUD, Create an entry
    # Update the entry
    # Delete the entry
    # Read the database
    create("Eggs", 10, 0.5, 0.2, 0.1, 0.3, "Tree1", "Node1")
    last_id = get_database_dimensions()[0]
    update(last_id, "Eggs", 20, 0.5, 0.2, 0.1, 0.3, "Tree1", "Node1")
    delete(last_id)
    read() 
    # Query
    if args.query:
        print("Querying data...")
        query()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ETL-Query script")
    parser.add_argument("--query", action="store_true", help="query the database")
    args = parser.parse_args()
    main(args)