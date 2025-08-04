# # utils.py
# import gspread
# from google.oauth2.service_account import Credentials

# def push_to_google_sheet(data_list):
#     """
#     Appends a list of data to the first sheet of your Google Spreadsheet.
#     Example: data_list = [1, 'John Doe', 'john@example.com', 85]
#     """
#     # Define the scope
#     scope = ["https://www.googleapis.com/auth/spreadsheets"]

#     # Load credentials
#     creds = Credentials.from_service_account_file(
#         "djangoseet-3d24e8c79dad.json",  # path to your JSON file
#         scopes=scope
#     )

#     # Authorize the client
#     client = gspread.authorize(creds)

#     # Open the spreadsheet (use your actual Sheet ID)
#     sheet = client.open_by_key("1FH61b4xU6av8QJVii4bF3APjrdILHFUwpnv4nzwVipg").sheet1

#     # Append the data as a new row
#     sheet.append_row(data_list)
#     sheet2 = client.open_by_key("1FH61b4xU6av8QJVii4bF3APjrdILHFUwpnv4nzwVipg").sheet2
#     sheet2.append_row(data_list)




# def push_to_google_sheet_student(data_list):
#     """
#     Appends a list of data to the first sheet of your Google Spreadsheet.
#     Example: data_list = [1, 'John Doe', 'john@example.com', 85]
#     """
#     # Define the scope
#     scope = ["https://www.googleapis.com/auth/spreadsheets"]

#     # Load credentials
#     creds = Credentials.from_service_account_file(
#         "djangoseet-3d24e8c79dad.json",  # path to your JSON file
#         scopes=scope
#     )

#     # Authorize the client
#     client = gspread.authorize(creds)

#     # Open the spreadsheet (use your actual Sheet ID)
#     # sheet = client.open_by_key("1FH61b4xU6av8QJVii4bF3APjrdILHFUwpnv4nzwVipg").sheet1

#     # # Append the data as a new row
#     # sheet.append_row(data_list)
#     spreadsheet = client.open_by_key("1FH61b4xU6av8QJVii4bF3APjrdILHFUwpnv4nzwVipg")

#     # Access Sheet2 by name (recommended)
#     sheet = spreadsheet.worksheet("Sheet2")
#     sheet.append_row(data_list)


# def push_to_google_sheet_addence(data_list):
#     """
#     Appends a list of data to the first sheet of your Google Spreadsheet.
#     Example: data_list = [1, 'John Doe', 'john@example.com', 85]
#     """
#     # Define the scope
#     scope = ["https://www.googleapis.com/auth/spreadsheets"]

#     # Load credentials
#     creds = Credentials.from_service_account_file(
#         "djangoseet-3d24e8c79dad.json",  # path to your JSON file
#         scopes=scope
#     )

#     # Authorize the client
#     client = gspread.authorize(creds)

#     # Open the spreadsheet (use your actual Sheet ID)
#     # sheet = client.open_by_key("1FH61b4xU6av8QJVii4bF3APjrdILHFUwpnv4nzwVipg").sheet1

#     # # Append the data as a new row
#     # sheet.append_row(data_list)
#     spreadsheet = client.open_by_key("1FH61b4xU6av8QJVii4bF3APjrdILHFUwpnv4nzwVipg")

#     # Access Sheet2 by name (recommended)
#     sheet = spreadsheet.worksheet("Sheet3")
#     sheet.append_row(data_list)
import os
import json
import gspread
from google.oauth2.service_account import Credentials

# Common function to load credentials from .env
def get_gspread_client():
    scope = ["https://www.googleapis.com/auth/spreadsheets"]
    creds_info = json.loads(os.getenv("GOOGLE_CREDENTIALS"))
    creds = Credentials.from_service_account_info(creds_info, scopes=scope)
    return gspread.authorize(creds)


def push_to_google_sheet(data_list):
    client = get_gspread_client()
    sheet = client.open_by_key("1FH61b4xU6av8QJVii4bF3APjrdILHFUwpnv4nzwVipg").sheet1
    sheet.append_row(data_list)

    sheet2 = client.open_by_key("1FH61b4xU6av8QJVii4bF3APjrdILHFUwpnv4nzwVipg").worksheet("Sheet2")
    sheet2.append_row(data_list)


def push_to_google_sheet_student(data_list):
    client = get_gspread_client()
    sheet = client.open_by_key("1FH61b4xU6av8QJVii4bF3APjrdILHFUwpnv4nzwVipg").worksheet("Sheet2")
    sheet.append_row(data_list)


def push_to_google_sheet_addence(data_list):
    client = get_gspread_client()
    sheet = client.open_by_key("1FH61b4xU6av8QJVii4bF3APjrdILHFUwpnv4nzwVipg").worksheet("Sheet3")
    sheet.append_row(data_list)
