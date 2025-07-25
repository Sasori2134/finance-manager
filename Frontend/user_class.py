import requests
import json
from pprint import pprint
from datetime import datetime

class User:
    def __init__(self,access_token,refresh_token, endpoint='http://127.0.0.1:8000/'):
        self.access_token = access_token
        self.refresh_token = refresh_token
        self.endpoint = endpoint
        self.refresh_access_token_endpoint = 'api/token/refresh/'
        self.page = 1
    
    def add_transaction(self,category,itemname,price,transaction_type):
        response = requests.post(f'{self.endpoint}add_transaction', json={'category' : category, 'itemname' : itemname, 'price' : price, 'transaction_type' : transaction_type}, headers = {'Authorization' : f'Bearer {self.access_token}'})
        if response.status_code == 401:
            response = requests.post(f'{self.endpoint}{self.refresh_access_token_endpoint}', json=({'refresh' : self.refresh_token}))
            self.access_token = response.json().get('access')
            response = requests.post(f'{self.endpoint}add_transaction', json={'category' : category, 'itemname' : itemname, 'price' : price, 'transaction_type' : transaction_type}, headers = {'Authorization' : f'Bearer {self.access_token}'})
        return response.json()
    
    def delete_transaction(self,pk):
        response = requests.delete(f'{self.endpoint}delete_transaction/{pk}',headers = {'Authorization' : f'Bearer {self.access_token}'})
        if response.status_code == 401:
            response = requests.post(f'{self.endpoint}{self.refresh_access_token_endpoint}', json=({'refresh' : self.refresh_token}))
            self.access_token = response.json().get('access')
            response = requests.delete(f'{self.endpoint}delete_transaction/{pk}',headers = {'Authorization' : f'Bearer {self.access_token}'})

        return response.status_code

    def filter_expenses(self,from_date = None,to_date = None,category = None,transaction_type = None):
        if self.page != 1:
            response = requests.get(f'{self.endpoint}expenses', params={'page' : self.page,'from_date' : from_date, 'to_date' : to_date, 'category' : category, 'transaction_type' : transaction_type},headers = {'Authorization' : f'Bearer {self.access_token}'})
            self.page += 1
        else:
            response = requests.get(f'{self.endpoint}expenses', params={'from_date' : from_date, 'to_date' : to_date, 'category' : category, 'transaction_type' : transaction_type}, headers = {'Authorization' : f'Bearer {self.access_token}'})
            self.page += 1
        if response.status_code == 401:
            response = requests.post(f'{self.endpoint}{self.refresh_access_token_endpoint}', json=({'refresh' : self.refresh_token}))
            self.access_token = response.json().get('access')
            if self.page != 1:
                response = requests.get(f'{self.endpoint}expenses', params={'page' : self.page, 'from_date' : from_date, 'to_date' : to_date, 'category' : category, 'transaction_type' : transaction_type},headers = {'Authorization' : f'Bearer {self.access_token}'})
            else:
                response = requests.get(f'{self.endpoint}expenses', params={'from_date' : from_date, 'to_date' : to_date, 'category' : category, 'transaction_type' : transaction_type}, headers = {'Authorization' : f'Bearer {self.access_token}'})
        return response.json()


    def add_budget(self,budget,category):
        response = requests.post(f'{self.endpoint}add_budget', json={'budget' : budget, 'category' : category}, headers = {'Authorization' : f'Bearer {self.access_token}'})
        if response.status_code == 401:
            response = requests.post(f'{self.endpoint}{self.refresh_access_token_endpoint}', json=({'refresh' : self.refresh_token}))
            self.access_token = response.json().get('access')
            response = requests.post(f'{self.endpoint}add_budget', json={'budget' : budget, 'category' : category}, headers = {'Authorization' : f'Bearer {self.access_token}'})
        return response.json()

    def delete_budget(self,pk):
        response = requests.delete(f'{self.endpoint}delete_budget/{pk}', headers = {'Authorization' : f'Bearer {self.access_token}'})
        if response.status_code == 401:
            response = requests.post(f'{self.endpoint}{self.refresh_access_token_endpoint}', json=({'refresh' : self.refresh_token}))
            self.access_token = response.json().get('access')
            response = requests.delete(f'{self.endpoint}delete_budget/{pk}', headers = {'Authorization' : f'Bearer {self.access_token}'})
        return response.status_code

    def get_budget(self):
        response = requests.get(f'{self.endpoint}get_budget', headers = {'Authorization' : f'Bearer {self.access_token}'})
        if response.status_code == 401:
            response = requests.post(f'{self.endpoint}{self.refresh_access_token_endpoint}', json=({'refresh' : self.refresh_token}))
            self.access_token = response.json().get('access')
            response = requests.get(f'{self.endpoint}get_budget', headers = {'Authorization' : f'Bearer {self.access_token}'})
        return response.json()

    def create_recurring_bills(self,category,price,date):
        response = requests.post(f'{self.endpoint}/recurring_bills', json={'category' : category, 'price' : price, 'date' : date}, headers = {'Authorization' : f'Bearer {self.access_token}'})
        if response.status_code == 401:
            response = requests.post(f'{self.endpoint}{self.refresh_access_token_endpoint}', json=({'refresh' : self.refresh_token}))
            self.access_token = response.json().get('access')
            response = requests.post(f'{self.endpoint}/recurring_bills', json={'category' : category, 'price' : price, 'date' : date}, headers = {'Authorization' : f'Bearer {self.access_token}'})

        return response.json()

    def get_recurring_bills(self):
        response = requests.get(f'{self.endpoint}/get_recurring_bills', headers = {'Authorization' : f'Bearer {self.access_token}'})
        if response.status_code == 401:
            response = requests.post(f'{self.endpoint}{self.refresh_access_token_endpoint}', json=({'refresh' : self.refresh_token}))
            self.access_token = response.json().get('access')
            response = requests.get(f'{self.endpoint}/get_recurring_bills', headers = {'Authorization' : f'Bearer {self.access_token}'})
        return response.json()

    def delete_recurring_bills(self,pk):
        response = requests.delete(f'{self.endpoint}delete_recurring_bills/{pk}', headers = {'Authorization' : f'Bearer {self.access_token}'})
        if response.status_code == 401:
            response = requests.post(f'{self.endpoint}{self.refresh_access_token_endpoint}', json=({'refresh' : self.refresh_token}))
            self.access_token = response.json().get('access')
            response = requests.delete(f'{self.endpoint}delete_recurring_bills/{pk}', headers = {'Authorization' : f'Bearer {self.access_token}'})
        return response.status_code

    def dashboard(self):
        check_recurring_bills = requests.post(f'{self.endpoint}check_recurring_bills', headers = {'Authorization' : f'Bearer {self.access_token}'})
        if check_recurring_bills.status_code == 401:
            response = requests.post(f'{self.endpoint}{self.refresh_access_token_endpoint}', json=({'refresh' : self.refresh_token}))
            self.access_token = response.json().get('access')
            check_recurring_bills = requests.post(f'{self.endpoint}check_recurring_bills', headers = {'Authorization' : f'Bearer {self.access_token}'})
        monthly_average = requests.get(f'{self.endpoint}dashboard/monthly_average', headers = {'Authorization' : f'Bearer {self.access_token}'})
        monthly_data = requests.get(f'{self.endpoint}dashboard/monthly_data', headers = {'Authorization' : f'Bearer {self.access_token}'})
        stats = requests.get(f'{self.endpoint}dashboard/total_stats', headers = {'Authorization' : f'Bearer {self.access_token}'})
        recent_transactions = requests.get(f'{self.endpoint}dashboard/recent_transactions', headers = {'Authorization' : f'Bearer {self.access_token}'})
        piechart = requests.get(f'{self.endpoint}dashboard/data_for_piechart_total', headers = {'Authorization' : f'Bearer {self.access_token}'})
        return {'monthly_average' : monthly_average.json(), 'monthly_data' : monthly_data.json(), 'total_stats' : stats.json(), 'recent_transactions' : recent_transactions.json(), 'piechart' : piechart.json()}

    def analytics(self,days):
        analytics_data = requests.get(f'{self.endpoint}analytics/analytics_data',params={'days' : days},headers = {'Authorization' : f'Bearer {self.access_token}'})
        if analytics_data.status_code == 401:
            response = requests.post(f'{self.endpoint}{self.refresh_access_token_endpoint}', json=({'refresh' : self.refresh_token}))
            self.access_token = response.json().get('access').json()
            analytics_data = requests.get(f'{self.endpoint}analytics/analytics_data',params={'days' : days},headers = {'Authorization' : f'Bearer {self.access_token}'})
        stats = requests.get(f'{self.endpoint}analytics/analytics_stats', params={'days' : days}, headers = {'Authorization' : f'Bearer {self.access_token}'})
        piechart = requests.get(f'{self.endpoint}analytics/data_for_piechart_analytics', params={'days' : days}, headers = {'Authorization' : f'Bearer {self.access_token}'})
        if analytics_data.status_code == 400:
            return {'message' : 'Invalid Data Type Expected A Number'}
        return {'analytics_data' : analytics_data.json(), 'stats' : stats.json(), 'piechart' : piechart.json()}

    def log_out(self):
        response = requests.post(f'{self.endpoint}api/log_out', json = {'refresh' : self.refresh_token}, headers = {'Authorization' : f'Bearer {self.access_token}'})
        if response.status_code == 401:
            response = requests.post(f'{self.endpoint}{self.refresh_access_token_endpoint}', json=({'refresh' : self.refresh_token}))
            self.access_token = response.json().get('access').json()
            response = requests.post(f'{self.endpoint}api/log_out', json = {'refresh' : self.refresh_token}, headers = {'Authorization' : f'Bearer {self.access_token}'})
        return response.status_code

