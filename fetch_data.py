
import os
import json

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

SPREADSHEETS_ID = "1Me6k8rA9vJZ1jrQlx_K8TV5nQ0I_nEuMVgqV5x3wqKo" # change this for after the /d/ 


def main():
    credentials = None
    if os.path.exists("token.json"):
        credentials = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())

        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            credentials = flow.run_local_server(port=0)

        with open("token.json", "w") as token:
            token.write(credentials.to_json())

    try:
        service = build("sheets", "v4", credentials=credentials)
        sheets = service.spreadsheets()

       
    # CHANGE THE ONE BELOW TO THE ATTENDANCE COLUMN E.G AM3:AM80  (ALWAYS 3 AND 80)
        result1 = sheets.values().get(spreadsheetId=SPREADSHEETS_ID, range="Sheet1!AH3:AH80").execute()
        # result variable has all the yes's
        attendance = result1.get("values", [])

        result2 = sheets.values().get(spreadsheetId=SPREADSHEETS_ID, range="Sheet1!C3:C80").execute()
        # result2 variable has all the SID's
        SIDS = result2.get("values")

        result3 = sheets.values().get(spreadsheetId=SPREADSHEETS_ID, range="Sheet1!A3").execute()
        # result3 variable has all the reference Y's
        reference_Y = result3.get("values")

        result4 = sheets.values().get(spreadsheetId=SPREADSHEETS_ID, range="Sheet1!D3:D80").execute()
        # result3 variable has all the reference Y's
        names = result4.get("values")
        
        all_SID = {}
        counter = 0
        for count in range(0,72):
            if attendance[count] == reference_Y[0]:
               counter = counter + 1
               all_SID[names[count][0]] = SIDS[count][0]
            
        print(f"The total number of kids that present :{counter}")
        
        # Custom format
        with open("output.txt", "w") as file:
            for key, value in all_SID.items():
                file.write(f"{key}, {value} \n")

        with open("output.json", "w") as file:
            json.dump(all_SID, file, indent=2)
        


        # Pick any SID using the above command init
        # All of the SIDS that have Yes are stored in this array.

    except HttpError as error:
        print(error)

if __name__ == "__main__":
    main()


# getting the sid of those who are yes
