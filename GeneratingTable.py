import random
import requests
import csv

def write_data(file_name, data):
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data[0])
        for row in data[1:]:
            writer.writerow(row)

def generate_ids(data_len):
    id = [str(random.randint(0, 99999)) for _ in range(data_len)]
    return id
    
def generate_salary(data_len):
    salary = [str(random.randint(100000, 999999)) for _ in range(data_len)]
    return salary

def generate_month(data_len):
    months = [str(random.randint(1, 12)) for _ in range(data_len)]
    return months
    
def generate_users(data_len):
    # https://randomuser.me/api/?results=10
    url = "https://randomuser.me/api/"
    params = {'results': data_len}
    response = requests.get(url, params=params)
    data = response.json()
    result = list(map(lambda x: x['name']['title'] + '.' + ' ' + x['name']['first'] + ' ' + x['name']['last'], data['results']))
    return result  
    
data_len = 15    
titles = ['id', 'salary', 'month', 'name']
merged = zip(generate_ids(data_len), generate_salary(data_len), generate_month(data_len), generate_users(data_len))    
result = [titles] + list(merged)
write_data('data.csv', result)