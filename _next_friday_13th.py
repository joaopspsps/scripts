#!/usr/bin/env python3
# Find the next ocurrence of Friday 13th.

from datetime import datetime
from itertools import count


def main() -> None:
    today = datetime.today()
    cur_month = today.month
    cur_year = today.year

    for year in count(cur_year):
        for month in range(cur_month, 12 + 1):
            if datetime(year, month, 13).weekday() == 5:
                print(f"{year}-{month}-13")
                return


if __name__ == "__main__":
    main()
