from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import sys

global SCOPES,url,WRITE_FILE_ID
SCOPES = "https://www.googleapis.com/auth/spreadsheets"
WRITE_FILE_ID = '1Kw5QL1EjtCS2ugMKpahZdFQM2zmDj1-O6SQ6col8rpU'
url = sys.argv[1]

def oauth_verify() :
    store = file.Storage('token.json')
    creds = store.get()

    if not creds or creds.invalid :
        flow = client.flow_from_clientsecrets('client_id.json', SCOPES)
        creds = tools.run_flow(flow, store)

    service = build('sheets', 'v4', http=creds.authorize(Http()))
    return service

def getTitle(auth,id) :
    result = auth.spreadsheets().get(spreadsheetId=id).execute()
    title = result.get('properties').get('title')
    r = auth.spreadsheets().values().get(spreadsheetId=id,range="A1:A").execute()
    dates = r.get('values',[])
    title = title + " " + dates[1][0]
    return title

def getEmails(auth,id) :
    result = auth.spreadsheets().values().get(spreadsheetId=id,range="B2:B").execute()
    return result

def getNames(auth,id) :
    result = auth.spreadsheets().values().get(spreadsheetId=id,range="C2:C").execute()
    return result

def writeAttendees(auth,name_range,email_range) :
    names = name_range.get('values',[])
    emails = email_range.get('values',[])
    body_names = {'values' : names }
    name_result = auth.spreadsheets().values().update(spreadsheetId=WRITE_FILE_ID,
                                                      range='B2:B',
                                                      valueInputOption='RAW',
                                                      body=body_names).execute()

    body_emails = {'values' : emails }
    email_result = auth.spreadsheets().values().update(spreadsheetId=WRITE_FILE_ID,
                                                       range='C2:C',
                                                       valueInputOption='RAW',
                                                       body=body_emails).execute()
def updateAttendance(auth,event) :
    value_range = auth.spreadsheets().values().get(spreadsheetId=WRITE_FILE_ID,range='B2:Z').execute()
    values = value_range.get('values',[])
    for person in values :
        person.append(event)
    body = {'values': values}
    result = auth.spreadsheets().values().update(spreadsheetId=WRITE_FILE_ID,range='B2:Z',valueInputOption='RAW',body=body).execute()

def getId(url) :
    start = url.find('d/')
    end = url.find('/edit')
    id = url[start+2:end]
    return id

def main() :
    id = getId(url)
    auth = oauth_verify()
    title = getTitle(auth,id)
    email_range = getEmails(auth,id)
    name_range = getNames(auth,id)
    writeAttendees(auth,name_range,email_range)
    updateAttendance(auth,title)
    print("done")

if __name__ == "__main__" :
    main()
