from routing import Route
from decoder import decode
import datetime
import time

def convert_time_in_seconds(times):
    strip_time = time.strptime(times,'%H:%M:%S')
    time_in_sec = datetime.timedelta(
        hours=strip_time.tm_hour,
        minutes=strip_time.tm_min,
        seconds=strip_time.tm_sec
    ).total_seconds()
    
    return int(time_in_sec)

def iterate_on_list_of_points(list_of_points, coor, costing, time_limite):
    """
    list_of_points (List(List)): [[x1, y1], [x2, y2], [..., ...]]    
    coor (List): [x1, y1]
    costing (String): "pedestrian" 
    time_limite (String) = "00:01:00"
    """

    point_series = [coor] +  list_of_points

    
    time_limitation = convert_time_in_seconds(time_limite)

    json_parcours = {}

    # while time_limitation > 0:

    # Itération sur chaque points
    for count, point_coor in enumerate(point_series):
        poped_list = point_series.copy()
        del poped_list[count] #

        json_parcours.update({
            count: {
            "shape": [],
            "count": 0,
            "time": 0
            } 
        })

        for element in poped_list:
            # calculate each shotest path
            path = Route(point_coor, element, costing).get_shortest_path()
            shape = path["trip"]["legs"][0]["shape"]
            time = path["trip"]["summary"]["time"]

            if time < time_limitation:
                json_parcours[count]["shape"].append(shape) # decode(shape)
                # json_parcours[count]["shape"].append(decode(shape))
                json_parcours[count]["count"] += 1
                json_parcours[count]["time"] = time
                # json_parcours.update({
                #     count: {
                #     "shape": shape,
                #     "count": len(count)
                #     } 
                # })
            pass
        pass

    pass

        # time_limitation -= "some time"

    return json_parcours

points = [[48.85035814324781, 2.2619496012533262],[48.87138948741586, 2.3008580899468396], [48.88614170811342, 2.341473214219776], [48.865533628765796, 2.3432659374724696]]
print(iterate_on_list_of_points(points, [48.849442, 2.261198], "pedestrian", "00:32:00"))

"""
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
"""