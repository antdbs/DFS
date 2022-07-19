from routing import Route
from decoder import decode


def get_parcours(list_of_points, coor, costing, time_limite):
    result = []
    i = 0
    while time_limite > 0:

        time, minpath = get_min_path(list_of_points, coor, costing)
            
        result.append(minpath)


        list_of_points = list_of_points[i:]
        print('-----------------')
        print("list_of_points: ",list_of_points)

        if list_of_points == []:
            break
        coor = list_of_points[i]
        print('-----------------')
        print("coor: ",coor)
        time_limite -= time
        i += 1


    json_list = {
        "type": "FeatureCollection",
        "features": []
    }
    for value in result:
        json_list["features"].append(
            {
                "type": "Feature",
                "geometry": {
                    "type": "LineString",
                    "coordinates": decode(value)
                },
                "properties": {
                    "prop0": "value0",
                    "prop1": 0.0
                }
            }
        )

    # json_list = json_list.replace("'",'"')

    return json_list #[:-1]

def get_min_path(list_of_points, coor, costing):

    path_list = {}

    for point in list_of_points:
        path = Route(coor, point, costing).get_shortest_path()
        # path = json.loads(path)
        # print(path)
        shape = path["trip"]["legs"][0]["shape"]
        time = path["trip"]["summary"]["time"]
        path_list.update({time: shape})

    min_path = sorted(path_list.keys())

    print('##########')
    print(min_path)
    print('##########')
    print(path_list[min_path[0]])
    print('##########')

    time = min_path[0]
    path_result = path_list[min_path[0]]

    return time, path_result

# result = json.loads(result)
# result = result["trip"]["legs"][0]["shape"]