import json
import numpy as np
import pandas as pd

from plot import plot_map
from info import postcards_info


if __name__ == "__main__":
    with open("../data/russia.geojson") as f:
        counties = json.load(f)

        for k in range(len(counties["features"])):
            counties["features"][k]["id"] = k

        region_id_list = []
        regions_list = []
        for k in range(len(counties["features"])):
            region_id_list.append(counties["features"][k]["id"])
            regions_list.append(counties["features"][k]["properties"]["name"].lower())

        df_regions = pd.DataFrame()
        df_regions["region_id"] = region_id_list
        df_regions["region_name"] = regions_list

    df_total, distances = postcards_info(regions_list)
    df = df_total.merge(df_regions, on="region_name")

    while True:
        print("1 - общее количество открыток")
        print("2 - отправленные")
        print("3 - полученные")
        print("4 - минимальное расстояние")
        print("5 - максимальное расстояние")
        print("6 - среднее расстояние")
        print("7 - общее расстояние")

        action = input("Номер карты: ")

        if action == "1":
            plot_map(
                counties=counties,
                df=df,
                z="total",
                customdata=np.stack([df["total"], df["sent"], df["received"]], axis=-1),
                hovertemplate="<b>%{text}</b>"
                + "<br>"
                + "Общее количество: %{customdata[0]}"
                + "<br>"
                + "Получено: %{customdata[1]}"
                + "<br>"
                + "Отправлено: %{customdata[2]}"
                + "<br>"
                + "<extra></extra>",
            )
        elif action == "2":
            plot_map(
                counties=counties,
                df=df,
                z="sent",
                customdata=np.stack([df["total"], df["sent"], df["received"]], axis=-1),
                hovertemplate="<b>%{text}</b>"
                + "<br>"
                + "Общее количество: %{customdata[0]}"
                + "<br>"
                + "Получено: %{customdata[1]}"
                + "<br>"
                + "Отправлено: %{customdata[2]}"
                + "<br>"
                + "<extra></extra>",
            )
        elif action == "3":
            plot_map(
                counties=counties,
                df=df,
                z="received",
                customdata=np.stack([df["total"], df["sent"], df["received"]], axis=-1),
                hovertemplate="<b>%{text}</b>"
                + "<br>"
                + "Общее количество: %{customdata[0]}"
                + "<br>"
                + "Получено: %{customdata[1]}"
                + "<br>"
                + "Отправлено: %{customdata[2]}"
                + "<br>"
                + "<extra></extra>",
            )
        elif action == "4":
            print(distances[0])
        elif action == "5":
            print(distances[1])
        elif action == "6":
            print(distances[2])
        elif action == "7":
            print(distances[3])
