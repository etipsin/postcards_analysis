import csv
import pandas as pd
from enum import Enum

from geo import get_region_by_coordinate, calculate_distance


class Fields(Enum):
    DEP_LAT = "Широта (откуда)"
    DEP_LONG = "Долгота (откуда)"
    DEST_LAT = "Широта (куда)"
    DEST_LONG = "Долгота (куда)"


def postcards_info(regions):
    regions_dict = {
        item: {
            "sent": 0,
            "received": 0,
            "money_tag": 0,
            "language_tag": 0,
            "trip_tag": 0,
        }
        for item in regions
    }

    distances = []

    with open("../data/postcards.csv", newline="") as csvfile:
        reader = csv.DictReader(csvfile)

        for idx, row in enumerate(reader):
            if not (row[Fields.DEP_LAT.value] and row[Fields.DEP_LONG.value]) or not (
                row[Fields.DEST_LAT.value] and row[Fields.DEP_LONG.value]
            ):
                continue

            departure = float(row[Fields.DEP_LAT.value]), float(
                row[Fields.DEP_LONG.value]
            )
            destination = float(row[Fields.DEST_LAT.value]), float(
                row[Fields.DEP_LONG.value]
            )

            dep_region_name = get_region_by_coordinate(regions=regions, coord=departure)
            if dep_region_name:
                regions_dict[dep_region_name]["sent"] += 1

            dest_region_name = get_region_by_coordinate(
                regions=regions, coord=destination
            )
            if dest_region_name:
                regions_dict[dest_region_name]["received"] += 1

            distances.append(
                calculate_distance(coords_1=departure, coords_2=destination)
            )

    df = pd.DataFrame()
    sent_list = []
    received_list = []
    total_list = []

    for reg in regions:
        sent_list.append(regions_dict[reg]["sent"])
        received_list.append(regions_dict[reg]["received"])
        total_list.append(regions_dict[reg]["sent"] + regions_dict[reg]["received"])

    df["region_name"] = regions
    df["total"] = total_list
    df["sent"] = sent_list
    df["received"] = received_list

    return df, (
        min(distances),
        max(distances),
        sum(distances) / len(distances),
        sum(distances),
    )
