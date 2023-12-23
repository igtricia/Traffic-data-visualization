"""Dictionary related utility functions."""

__author__ = "730608965"

from csv import DictReader

"""Some helpful utility funtions for working with CSV data."""


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of csv into a table."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produces a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result 


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(dictnry: dict[str, list[str]], N: int) -> dict[str, list[str]]:
    """Produces a new column-based table with only the first N rows of data for each column."""
    result: dict[str, list[str]] = {}
    if N > len(dictnry):
        return dictnry
    for key in dictnry:
        list_1: list[str] = []
        counter: int = 0
        while counter < N:
            list_1.append(dictnry[key][counter])
            counter += 1
        result[key] = list_1     
    return result 


def select(dictnry: dict[str, list[str]], list_1: list[str]) -> dict[str, list[str]]:
    """Produces a new column-based table with only a specific subset of the original column."""
    result: dict[str, list[str]] = {}
    counter: int = 0
    while counter < len(list_1):
        result[list_1[counter]] = dictnry[list_1[counter]]
        counter += 1
    return result 


def concat(table_1: dict[str, list[str]], table_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produces a a new column based table with two column based tables."""
    result: dict[str, list[str]] = {}
    for key in table_1:
        result[key] = table_1[key]
    for key in table_2:
        if key in result:
            result[key] += table_2[key]
        else:
            result[key] = table_2[key]
    return result


def count(list_1: list[str]) -> dict[str, int]:
    """Counts the number of times a value has appeared in a list."""
    result: dict[str, int] = {}
    for item in list_1:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result 