import requests
import shutil
from zoho_auth import ZohoAuth

class ZohoSheetClient:
    def __init__(self, auth: ZohoAuth):
        self.auth = auth
        self.base_url = "https://sheet.zoho.com/api/v2"


    # Retrieves content from a specified range in a worksheet using the content API
    def get_range_content(self, spreadsheet_id, worksheet_name, start_row, start_column, end_row, end_column):
        token = self.auth.get_token()
        url = f"{self.base_url}/{spreadsheet_id}"
        headers = {
            "Authorization": f"Zoho-oauthtoken {token}",
            "Content-type": "application/x-www-form-urlencoded"
        }
        data = {
            "method": "range.content.get",
            "worksheet_name": worksheet_name,
            "start_row": start_row,
            "start_column": start_column,
            "end_row": end_row,
            "end_column": end_column
        }
        resp = requests.post(url, headers=headers, data=data)
        resp.raise_for_status()
        return resp.json()["range_details"]
    
    # Downloads a worksheet as a CSV file Using the content API
    def get_worksheet_csv(self, spreadsheet_id, worksheet_name):
        token = self.auth.get_token()
        url = f"{self.base_url}/{spreadsheet_id}"
        headers = {
            "Authorization": f"Zoho-oauthtoken {token}",
            "Content-type": "application/x-www-form-urlencoded"
        }
        data = {
            "method": "workbook.download",
            "worksheet_name": worksheet_name,
            "format": "csv"
        }
        resp = requests.post(url, headers=headers, data=data)
        resp.raise_for_status()
        #with open(f"{worksheet_name}.csv", "wb") as file:
        return resp.content  # Return the CSV content directly
    
    
    

