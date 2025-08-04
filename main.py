from zoho_auth import ZohoAuth
from zoho_sheet_client import ZohoSheetClient
from dotenv import load_dotenv
import os

load_dotenv()

auth = ZohoAuth(
    client_id=os.getenv("ZOHO_CLIENT_ID"),
    client_secret=os.getenv("ZOHO_CLIENT_SECRET"),
    refresh_token=os.getenv("ZOHO_REFRESH_TOKEN"),
    redirect_uri=os.getenv("ZOHO_REDIRECT_URI")
)

sheet = ZohoSheetClient(auth)
range = sheet.get_range_content(
    spreadsheet_id=os.getenv("ZOHO_SHEET_API_SPREADSHEET_ID"),
    worksheet_name="VPN",
    start_row=3,
    start_column=2,
    end_row=7,
    end_column=4
)
for row in range:
    print(row)
print("Range content retrieved successfully.")

csv_content = sheet.get_worksheet_csv(
    spreadsheet_id=os.getenv("ZOHO_SHEET_API_SPREADSHEET_ID"),
    worksheet_name="VPN"
)
with open("VPN.csv", "wb") as file:
    file.write(csv_content)
print("CSV file 'VPN.csv' created successfully.")


