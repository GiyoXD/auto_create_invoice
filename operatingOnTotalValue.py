import pandas as pd

def foundEmpty(current_row, field, ws, table_n, pcsField):
    if value:
        store(ws[field+str(current_row)], field, table_n)
    else:
        totalValue = ws[field+str(current_row-1)].value

        pcs_starting_row = current_row - 1
        counting_distribute_row = 1
        while ws[field+str(current_row)].value == False:
            counting_distribute_row++

        totalPCS = 0
        for i in range(counting_distribute_row):
            totalPCS += ws[pcsField+str(pcs_starting_row)].value
            pcs_starting_row++

        distributed_values = []
        
        pcs_starting_row = current_row - 1
        for i in range(counting_distribute_row):
            pcs = ws[field+str(pcs_starting_row)].value
            distributed_value = totalValue * (pcs / totalPCS)
            distributed_values.append(distributed_values)
        store(distributed_values, field, table_n)


def distributing_on_field(startR, field, tableNo):








def find_field(fieldnameValue, ws, row_search_limit=10):
    """
    Finds the (row, column) index of a specific value in a given worksheet.

    Parameters:
        fieldnameValue (str/int/float): The value to search for.
        ws (Worksheet): The worksheet object to search within.
        row_search_limit (int): The maximum number of rows to search for the header row (default: 10).

    Returns:
        tuple: (row, column) index of the value if found, otherwise None.
    """
    # Step 1: Find the header row within the specified row_search_limit
    header_row = None
    header_row_index = None
    for row in ws.iter_rows(min_row=1, max_row=row_search_limit, values_only=True):
        if fieldnameValue in row:  # Check if the fieldnameValue exists in this row
            header_row = row
            header_row_index = row[0].row  # Get the row index of the header row
            break

    if not header_row:
        return None  # Header row not found within the search limit

    # Step 2: Map field names to their column indices
    field_to_column = {field: idx + 1 for idx, field in enumerate(header_row) if field is not None}

    # Step 3: Check if the fieldnameValue exists in the header row
    if fieldnameValue not in field_to_column:
        return None  # Field not found in headers

    # Step 4: Return the (row, column) index of the header
    return (header_row_index, field_to_column[fieldnameValue])
        

