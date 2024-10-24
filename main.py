from datetime import datetime
from application.db import people as pl
from application import salary as slr

if __name__ == '__main__':
    print(datetime.now())
    pl.get_employees()
    slr.calculate_salary()
