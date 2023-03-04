import json

# Load data from JSON file
with open("channelcost.json", "r") as f:
    data = json.load(f)

# Load cost per unit from JSON file
with open("cost.json", "r") as f:
    cost_per_unit = json.load(f)

# Get the channels present in both data and cost_per_unit dictionaries
common_channels = set(data[0].keys()) & set(cost_per_unit.keys())

# Calculate the total cost for each date
cost_by_date = {}
for d in data:
    date = d["date"].split()[0]
    channels = set(d.keys()) & common_channels
    total_cost = sum(d[channel] * cost_per_unit[channel] for channel in channels)
    cost_by_date[date] = {
        "date": date,
        "sms": round(d.get("sms", 0) * cost_per_unit.get("sms", 0), 2),
        "whatsapp": round(d.get("whatsapp", 0) * cost_per_unit.get("whatsapp", 0), 2),
        "email": round(d.get("email", 0) * cost_per_unit.get("email", 0), 2),
        "ivr": round(d.get("ivr", 0) * cost_per_unit.get("ivr", 0), 2)
    }

# Sort the data by date and convert to list
cost_by_date = sorted(cost_by_date.values(), key=lambda x: x["date"])

# Write the total cost for each date to a new JSON file
with open("total_cost_by_date.json", "w") as f:
    json.dump(cost_by_date, f, indent=4)

# Print the total cost for each date
print(json.dumps(cost_by_date, indent=4))
