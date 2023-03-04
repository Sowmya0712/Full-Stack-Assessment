# Full-Stack-Assessment 

This Python script calculates the total cost for different communication channels used on different dates, based on the usage data and cost per unit of each channel, and generates a JSON file with the total cost for each date.

The program reads data from two JSON files, 'channelcost.json' and 'cost.json'.
'channelcost.json' gives the number of times a channel is used at a given date and time.
'cost.json' gives the cost per unit for each channel.
The data from these files are read and the total cost for each date is calculated. The resulting total cost for each date is then sorted by date and written to a new JSON file named 'total_cost_by_date.json'. Finally, the program prints the total cost for each date in a formatted JSON string. The date in the 'total_cost_by_date.json' file is in the format YYYY-MM-DD.

Requirements:
Python 3
JSON Module

Note:
Make sure that the input files 'channelcost.json' and 'cost.json' are present in the same directory as the soucre code file which is 'python11.py'
Open the directory containing the source code file
Run the program with the command:python python11.py
The program will output the total cost for each date in a formatted JSON string to the console and write the same data to a new JSON file named 'total_cost_by_date.json' in the same directory.
