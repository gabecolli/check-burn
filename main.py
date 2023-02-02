# #list of all dse contracts. this will contain dictionaries. customer being key and the value will be another dictionary with the following keys: hours_remaining, start_date, end_date
# dse_contracts = []

# #get user input for how many hours in a contract and who the customer is then add to list dse_contracts
# def get_contract_data():
#     while True:
#         hours_remaining = input("How many hours are remaining in the contract? ")
#         customer = input("Who is the customer? ")
#         start_date = input("What is the start date? Please use the following format: YYYY-MM-DD ")
#         end_date = input("What is the end date? Please use the following format: YYYY-MM-DD ")
#         dse_contracts.append({"customer": customer, "hours_remaining": hours_remaining, "start_date": start_date, "end_date": end_date})
#         if input("Do you have another contract? (y/n) ") == "n":
#             break


import datetime
import holidays

def calculate_difference(start_date, end_date):
    start = datetime.datetime.strptime(start_date, '%Y-%m-%d')
    end = datetime.datetime.strptime(end_date, '%Y-%m-%d')
    diff = end - start
    months = diff.days // 30
    weeks = (diff.days % 30) // 7
    days = (diff.days % 30) % 7
    formatted_dates = [start + datetime.timedelta(days=x) for x in range(diff.days + 1)]
    formatted_dates = [date.strftime("%m-%d-%Y") for date in formatted_dates]
    federal_holidays = 0
    all_holidays = holidays.US()
    for date in formatted_dates:
        if all_holidays.get(date):
            print(date)
            federal_holidays += 1
    return months, weeks, days, federal_holidays

start_date = "2023-01-01"
end_date = "2023-02-02"
months, weeks, days, federal_holidays = calculate_difference(start_date, end_date)
print("Months:", months)
print("Weeks:", weeks)
print("Days:", days)
print("Federal Holidays:", federal_holidays)
