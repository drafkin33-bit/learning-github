"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*args):
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    *list_of_wagons, = args
    return list_of_wagons

def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    :param each_wagons_id: list - the list of wagons.
    :param missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    second_last, last, first, *remainder = each_wagons_id
    master_list = [first, *missing_wagons, *remainder, second_last, last]
    return master_list
    
def add_missing_stops(routing_dict, **kwargs):
    """Add missing stops to route dict.

    :param route: routing_dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    routing_dict["stops"] = list(kwargs.values())
    return routing_dict

def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    return {**route, **more_route_information}

def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """
    row_1, row_2, row_3 = zip(*wagons_rows)
    return [list(row_1), list(row_2), list(row_3)]
