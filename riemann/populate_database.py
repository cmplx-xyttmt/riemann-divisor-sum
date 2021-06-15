'''A simple cli to populate the database.'''
import time
from riemann.database import DivisorDb
from riemann.divisor import compute_riemann_divisor_sums
from riemann.sqlite_database import SqliteDivisorDb


def populate_db(db: DivisorDb, batch_size: int = 250000) -> None:
    '''Populate the db in batches.
    Write the computed divisor sums to the database after each batch.
    '''
    largest_n = db.summarize().largest_computed_n 
    if largest_n is None:
        starting_n = 5041
    else:
        starting_n = largest_n.n + 1
    while True:
        ending_n = starting_n + batch_size
        start = time.time()
        db.upsert(compute_riemann_divisor_sums(starting_n, ending_n))
        end = time.time()
        print(f"Computed [{starting_n}, {ending_n}] in {end - start} seconds")
        starting_n = ending_n + 1


if __name__ == "__main__":
    import sys
    db = SqliteDivisorDb(database_path=sys.argv[1])
    try:
        populate_db(db)
    except KeyboardInterrupt:
        print("Stopping and printing stats...")
    finally:
        best_witness = db.summarize().largest_witness_value
        print(f"Best witness: {best_witness}")
