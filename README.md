
# Pixela Graph Automation
This script uses the **requests** and **datetime** libraries in Python to automate the process of adding and removing data to a graph on the Pixela service


## Prerequisites
Before running this script, you will need to have the following:
+ A Pixela account, which you can create at [Pixela](https://pixe.la/)
+ Your Pixela username and token for authentication
+ Python 3 installed on your machine
+ The requests and datetime libraries installed for Python
## Installation

To install the requests and datetime libraries, use the following command in your terminal:

```bash
  pip install requests datetime

```
    
## Usage/Examples
Clone or download the repository to your local machine

Open the pixela_graph_automation.py file in your text editor or IDE

Update the USERNAME and TOKEN variables with your own values

Uncomment and update the parameters for creating a new user and/or graph, if needed

Run the script using the following command in your terminal:
```python
python pixela_graph_automation.py

```
This will add data (in minutes) to the graph for today's date, and then remove it. The responses from the Pixela API will be printed to the console.

Note that you can customize the data being added to the graph by changing the quantity parameter in the minutes_details dictionary, and you can change the date by modifying the date parameter.

