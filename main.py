import csv

class Client:
    def __init__(self, name, sex, age, device, browser, bill, region):
        self.name = name.strip()
        self.sex = sex.strip()
        self.age = self.parse_age(age)
        self.device = device.strip()
        self.browser = browser.strip()
        self.bill = self.parse_bill(bill)
        self.region = region.strip()

    def parse_age(self, age):
        try:
            return int(age)
        except ValueError:
            return 'неизвестно'

    def parse_bill(self, bill):
        try:
            return int(bill)
        except ValueError:
            return 'неизвестно'

    def generate_description(self):
        sex_description = 'женского' if self.sex.lower() == 'female' else 'мужского'
        devices = {
            'mobile': 'мобильного',
            'tablet': 'планшетного(мобильного)',
            'desktop': 'настольного'
        }
        device_type = devices.get(self.device.lower(), self.device)
        return (f"Пользователь {self.name} {sex_description} пола, {self.age} лет "
                f"совершила покупку на {self.bill} у.е. с {device_type} "
                f"браузера {self.browser}. Регион, из которого совершалась покупка: "
                f"{self.region}.")

def load_csv(filepath):
    with open(filepath, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        data = []
        for row in reader:
            data.append(row)
    return data

def parse_client(data_row):
    client = Client(
        name=data_row.get('name', ''),
        sex=data_row.get('sex', ''),
        age=data_row.get('age', ''),
        device=data_row.get('device_type', ''),
        browser=data_row.get('browser', ''),
        bill=data_row.get('bill', ''),
        region=data_row.get('region', '')
    )
    return client

def write_output(descriptions, output_filepath):
    with open(output_filepath, mode='w', encoding='utf-8') as file:
        for description in descriptions:
            file.write(description + '\n')

input_csv = 'web_clients_correct.csv'
output_txt = 'descriptions.txt'
data = load_csv(input_csv)
descriptions = []
for row in data:
    client = parse_client(row)
    description = client.generate_description()
    descriptions.append(description)
write_output(descriptions, output_txt)