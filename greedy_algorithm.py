states_needed = {'aa', 'bb', 'cc', 'dd', 'ff', 'ee', 'aa', 'qq', 'ww', 'rr', 'tt', 'yy'}

stations = {}
stations["kone"] = {'bb', 'ff', 'ee', 'aa'}
stations["ktwo"] = {'cc', 'ww', 'ff', 'tt'}
stations["kthree"] = {'ff', 'ee', 'qq', 'rr', 'ww'}
stations["kfour"] = {'dd', 'yy', 'rr', 'tt'}
stations["kfive"] = {'ee', 'bb', 'ff', 'ww', 'rr'}

final_stations = set()
while states_needed:
    best_station = None
    states_covered = set()

    for station, states_for_station in stations.items():
        covered = states_needed & states_for_station
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered

    final_stations.add(best_station)
    states_needed -= states_covered
    print(best_station)
    print(states_needed)


print(final_stations)