# 將訊號覆蓋的州放入串列，並轉換成集合
states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

stations = {} # 先建一個空字典 (即雜湊表)
stations["kone"] = set(["id", "nv", "ut"])  # 放入第 1 組鍵：值
stations["ktwo"] = set(["wa", "id", "mt"])  # 放入第 2 組鍵：值
stations["kthree"] = set(["or", "nv", "ca"])# 放入第 3 組鍵：值
stations["kfour"] = set(["nv", "ut"]) # 放入第 4 組鍵：值
stations["kfive"] = set(["ca", "az"]) # 放入第 5 組鍵：值

final_stations = set()

best_station =None
states_covered = set()
for station,stated_for_station in stations.items():
    coverd = states_needed & stated_for_station
    print(coverd)
    if len(coverd) >len(states_covered):
        print(coverd)
        print(states_covered)
        best_station = station
        states_covered = coverd
final_stations.add(best_station)
states_needed = states_needed - states_covered
print(final_stations)
print(states_covered)
print(states_needed)