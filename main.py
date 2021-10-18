from googleapiclient.discovery import build
from google.oauth2 import service_account
import json


def getLine(index):
    return sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range="Answers!A"+str(index)+":V"+str(index)).execute().get('values', [])[0]


def data():
    with open("data.json", 'r', encoding="utf-8") as f:
        data_people = json.load(f)
    data_people = {"people": []}
    i = 1
    try:
        while True:
            line = getLine(i)
            data_people["people"].append({"Пользователь": line[0], "Имя": line[1], "Фамилия": line[2],
                          "Адрес электронной почты": line[0], "Язык": "Russian, Русский",
                          "b2b логин": line[3], "ivi ID": "???",
                          "начисления": "(лучше убрать)", "Страна": line[4], "Регион РФ": line[5],
                          "Пол": "Невозможно определить",
                          "Возраст": line[6], "Этап обучения": line[7],
                          "Регистрация через гугл форму": True,
                          "Google аккаунт": line[8], "IOS аккаунт": line[9],
                          "Microsoft аккаунт": line[10],
                          "Xbox аккаунт": line[10], "Модель Smart TV": line[11], "Smart TV LG": "",
                          "Smart TV Sony": "",
                          "Smart TV Philips": "", "Модель Android TV": "", "Устройства": line[12],
                          "Создание пароля": True,
                          "Изменить пароль при следующем входе": True,
                          "Отправить пользователю информацию по учётной записи": True})
            i += 1
    except IndexError:
        print("la finito")
    with open("data.json", 'w', encoding="utf-8") as f:
        json.dump(data_people, f, ensure_ascii=False)


SERVICE_ACCOUNT_FILE = 'keys.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# The ID spreadsheet.
SAMPLE_SPREADSHEET_ID = '1e2dXIlmN_u6CcxyilSH2xKzkz0R6SJu7uoYhfuWnuzk'

service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range="Answers!A1:V3").execute()
values = result.get('values', [])

data()