from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

global SCOPES
SCOPES = "https://www.googleapis.com/auth/spreadsheets"

def oauth_verify() :
    store = file.Storage('token.json')
    creds = store.get()

    if not creds or creds.invalid :
        flow = client.flow_from_clientsecrets('client_id.json', SCOPES)
        creds = tools.run_flow(flow, store)

    service = build('sheets', 'v4', http=creds.authorize(Http()))
    return service

def getEmails(auth) :
    ATTENDENCE_SHEET_ID = "1xhMQ6JUQnof1dvfPpA3KXqq1FFp3YKH5t06-pwfaT78"
    result = auth.spreadsheets().values().get(spreadsheetId=ATTENDENCE_SHEET_ID,range="B2:B70").execute()
    values = result.get('values', [])
    return values

def getNames(auth) :
    ATTENDENCE_SHEET_ID = "1xhMQ6JUQnof1dvfPpA3KXqq1FFp3YKH5t06-pwfaT78"
    result = auth.spreadsheets().values().get(spreadsheetId=ATTENDENCE_SHEET_ID,range="C2:C70").execute()
    values = result.get('values', [])
    return values

def writeBatch(auth) :
    WRITE_FILE_ID = "1Kw5QL1EjtCS2ugMKpahZdFQM2zmDj1-O6SQ6col8rpU"
    result = auth.spreadsheets().values().batchUpdate(spreadsheetId=WRITE_FILE_ID, range)
    

def main() :
    auth = oauth_verify()
    emails = getEmails(auth)
    names = getNames(auth)


if __name__ == "__main__" :
    main()
