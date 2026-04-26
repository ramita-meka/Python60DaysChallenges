import random
import pandas as pd
import numpy as np
import math
import copy

def generate_data(n=15):
    data = []
    for i in range(n):
        data.append({
            "zone": i+1,
            "metrics": {
                "traffic": random.randint(0, 100),
                "pollution": random.randint(0, 300),
                "energy": random.randint(0, 500)
            },
            "history": [random.randint(50, 200) for _ in range(3)]
        })
    return data

def replicate_data(data):
    assigned = data
    shallow = data[:]
    deep = copy.deepcopy(data)
    return assigned, shallow, deep

def mutate_data(data):
    for d in data:
        d["metrics"]["traffic"] += 10
        d["history"].append(random.randint(50, 200))
        d["risk"] = math.log(
            d["metrics"]["traffic"] +
            d["metrics"]["pollution"] +
            d["metrics"]["energy"] + 1
        )

def to_dataframe(data):
    rows = []
    for d in data:
        rows.append({
            "zone": d["zone"],
            "traffic": d["metrics"]["traffic"],
            "pollution": d["metrics"]["pollution"],
            "energy": d["metrics"]["energy"],
            "risk": d.get("risk", 0)
        })
    return pd.DataFrame(rows)

def manual_correlation(x, y):
    mean_x, mean_y = np.mean(x), np.mean(y)
    num = sum((x[i]-mean_x)*(y[i]-mean_y) for i in range(len(x)))
    den = math.sqrt(sum((x[i]-mean_x)**2 for i in range(len(x))) *
                    sum((y[i]-mean_y)**2 for i in range(len(y))))
    return num / den if den != 0 else 0

def detect_anomalies(arr):
    mean = np.mean(arr)
    std = np.std(arr)
    return [i+1 for i in range(len(arr)) if arr[i] > mean + std]

def detect_clusters(risks, threshold):
    clusters, temp = [], []
    for i in range(len(risks)):
        if risks[i] > threshold:
            temp.append(i+1)
        else:
            if len(temp) > 1:
                clusters.append(temp)
            temp = []
    if len(temp) > 1:
        clusters.append(temp)
    return clusters


name = "Ramita"
reg_no = int(input("Enter register number: "))

data = generate_data()
print("\n-- BEFORE --\n", data)

if reg_no % 2 == 0:
    data.reverse()
else:
    data = data[3:] + data[:3]

assigned, shallow, deep = replicate_data(data)
mutate_data(shallow)

print("\n-- AFTER SHALLOW --")
print("Original (affected):", data)

mutate_data(deep)
print("\n-- AFTER DEEP --")
print("Original (unchanged):", data)

df = to_dataframe(data)
traffic = df["traffic"].to_numpy()
pollution = df["pollution"].to_numpy()

mean = np.mean(traffic)
var = np.var(traffic)
corr = manual_correlation(traffic, pollution)
anomalies = detect_anomalies(traffic)
risks = df["risk"].to_numpy()
threshold = np.mean(risks)

clusters = detect_clusters(risks, threshold)
stability_index = 1 / (var + 1)
avg_risk = np.mean(risks)

if avg_risk < 3:
    decision = "System Stable"
elif avg_risk < 4:
    decision = "Moderate Risk"
elif avg_risk < 5:
    decision = "High Corruption Risk"
else:
    decision = "Critical Failure"

print("\nDataFrame:\n", df)
print("\nAnomaly Zones:", anomalies)
print("\nClusters:", clusters)
print("\nTuple:", (max(risks), min(risks), stability_index))
print("\nFinal Decision:", decision)
print("\nIntegrity Explanation:")
print("Shallow copy shares nested objects, so modifying inner data affects original.")