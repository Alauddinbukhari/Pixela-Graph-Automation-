import requests
import datetime

# Get current date and time
todays_date = datetime.datetime.now()

# Set username and token for authentication
USERNAME = ""
TOKEN = ""

# Set API endpoint URL for pixela service
pixela_endpoint = "https://pixe.la/v1/users"

# Define parameters for creating a new user (commented out)
# user_params = {
#     "token": "",
#     "username": "",
#     "agreeTermsOfService": "",
#     "notMinor": "",
#     "thanksCode": ""
# }

# Send POST request to create new user and print response to console (commented out)
# response = requests.post(pixela_endpoint, json=user_params)
# print(response.text)

# Set API endpoint URL for graphs
graphs_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

# Define parameters for creating a new graph (commented out)
# graph_configuration = {
#     "id": "mygraph02",
#     "name": "Coding Graph",
#     "unit": "minutes",
#     "type": "float",
#     "color": "ajisai"
# }

# Send POST request to create new graph and print response to console (commented out)
# response = requests.post(graphs_endpoint, headers={"X-USER-TOKEN": TOKEN}, json=graph_configuration)
# print(response.text)

# Define dictionary with quantity of minutes (data for graph) for today's date
minutes_details = {
    "quantity": "90.00",
    # Alternatively, you can use today.strftime() to format the date in YYYYMMDD format
    "date": todays_date.strftime("%Y%m%d")
}

# Send POST request to add data (minutes) to graph and print response to console
# response = requests.post(f"{graphs_endpoint}/mygraph02", headers={"X-USER-TOKEN": TOKEN}, json=minutes_details)
# print(response.text)

# Send DELETE request to remove data (minutes) from graph for specific date and print response to console
response = requests.delete(f"{graphs_endpoint}/mygraph02/{todays_date.strftime('%Y%m%d')}", headers={"X-USER-TOKEN": TOKEN})
print(response.text)
