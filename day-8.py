import random
import pandas as pd
import numpy as np
import math

def generate_data(n=15):
    data = []
    for i in range(n):
        data.append({
            "zone": i+1,
            "traffic": random.randint(0, 100),
            "air_quality": random.randint(0, 300),
            "energy": random.randint(0, 500)
        })
    return data

def classify(record):
    if record["air_quality"] > 200 or record["traffic"] > 80:
        return "High Risk"
    elif record["energy"] > 400:
        return "Energy Critical"
    elif record["traffic"] < 30 and record["air_quality"] < 100:
        return "Safe Zone"
    else:
        return "Moderate"


def risk_score(record):
    return (record["traffic"]*0.35 +
            record["air_quality"]*0.4 +
            record["energy"]*0.25)


def get_top3(data):
    temp = data.copy()
    top = []
    for _ in range(3):
        max_item = temp[0]
        for item in temp:
            if item["risk_score"] > max_item["risk_score"]:
                max_item = item
        top.append(max_item)
        temp.remove(max_item)
    return top

def detect_clusters(scores, threshold):
    clusters, current = [], []
    for i in range(len(scores)):
        if scores[i] > threshold:
            current.append(i+1)
        else:
            if len(current) > 1:
                clusters.append(current)
            current = []
    if len(current) > 1:
        clusters.append(current)
    return clusters


name = "Ramita"
data = generate_data(18)

data.append({"zone": 100, "traffic": 10, "air_quality": 280, "energy": 300})
data.append({"zone": 101, "traffic": 0, "air_quality": 50, "energy": 200})
data.append({"zone": 102, "traffic": 90, "air_quality": 150, "energy": 480})


if len(name) % 2 == 0:
    random.shuffle(data)
else:
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            if data[i]["traffic"] > data[j]["traffic"]:
                data[i], data[j] = data[j], data[i]

for d in data:
    d["category"] = classify(d)
    d["risk_score"] = risk_score(d)
    d["risk_sqrt"] = math.sqrt(d["risk_score"])

df = pd.DataFrame(data)
traffic_arr = df["traffic"].to_numpy()
aqi_arr = df["air_quality"].to_numpy()
top3 = get_top3(data)
variance = np.var(traffic_arr)
threshold = np.mean(df["risk_score"])

multi_risk = []
for i in range(1, len(df)):
    if df["risk_score"][i] > threshold and df["air_quality"][i] > df["air_quality"][i-1]:
        multi_risk.append(df["zone"][i])

risk_scores = df["risk_score"].tolist()
clusters = detect_clusters(risk_scores, threshold)
categories_set = set(df["category"])
avg_risk = np.mean(df["risk_score"])

if avg_risk < 120:
    decision = "City Stable"
elif avg_risk < 220:
    decision = "Moderate Risk"
elif avg_risk < 320:
    decision = "High Alert"
else:
    decision = "Critical Emergency"

print("DataFrame:", df)
print("Categorized Zones:", df[["zone", "category"]])
print("Top 3 Risk Zones:")
for z in top3:
    print(z)

print("Risk Tuple:")
print((max(risk_scores), avg_risk, min(risk_scores)))
print("Multi-variable Risk Zones:", multi_risk)
print("Traffic Stability:", "Stable" if variance < 500 else "Unstable")
print("Unique Categories:", categories_set)
print("Clusters:", clusters)
print("Final Decision:", decision)
print("Smart City Definition:")
print("A smart city uses data-driven intelligence to ensure safety, sustainability, and efficiency.")