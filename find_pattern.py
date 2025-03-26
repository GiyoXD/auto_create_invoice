import re

def find_header_row(sheet, row_range, column_range, pattern):

    """
    Finds the row number containing the header based on a pattern,
    assuming the workbook and sheet are already open.

    Args:
        sheet: The openpyxl sheet object.
        row_range: The number of rows to search (starting from row 1).
        column_range: The number of columns to search (starting from column 1).
        pattern: A string or regular expression to search for in the cells.

    Returns:
        The row number (1-indexed) containing the header, or None if the pattern is not found.
    """
    try:
        for row in range(1, row_range + 1):  # openpyxl rows are 1-indexed
            for col in range(1, column_range + 1):  # openpyxl columns are 1-indexed
                cell = sheet.cell(row=row, column=col)
                if cell.value is not None:
                    cell_value = str(cell.value)
                    if re.search(pattern, cell_value, re.IGNORECASE):
                        return row  # Return the row number (1-indexed)


        return None  # Pattern not found

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def cell_not_empty(cell_value, chars_to_find, case_sensitive=False):
  if cell_value is None:
    return False
  cell_value = str(cell_value)
  if case_sensitive:
    for char in chars_to_find:
      if char in cell_value:
        return True
  else:
    cell_value_lower = cell_value.lower()
    for char in chars_to_find:
      if char.lower() in cell_value_lower:
        return True
  return False

def match_data(to_match_value, expected_values):
    for value in expected_values:
        if cell_not_empty(to_match_value, value):
            return value  # or to_match_value, depending on what you need to return
    return None

def found_formula(value):
    return value.startswith("=")

def found_empty_and_count_them():
   print()
# Todo this will find and count how many of the empty row are.
                                


def storing_value(ws):
    letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    header_map = {
        "订单号": [],
        "item": [],
        "desc": [],
        "pcs": [],
        "net": [],
        "gross": [],
        "unit": [],
        "cbm": [],
        "inv_no": [],
        "inv_date": [],
    }

    header_row = find_header_row(ws, 20, 20, "订单号")
    if header_row == None:
       print("header not found")
       return 


    for i in range(1, 26):
        field_index = letter[i]
        if ws[field_index+str(header_row)].value in header_map.keys():
           head_index = field_index+str(header_row) 
           start_store_field(head_index)
            
def start_store_field(head_index):
    row = head_index[1:]
    column = head_index[0]
    
    # store first row
    


    


