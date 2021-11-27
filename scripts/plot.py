import numpy as np
import pandas as pd
import plotly.graph_objects as go


def plot_map(
    counties: list,
    df: pd.DataFrame,
    z: str,
    customdata: np.stack,
    hovertemplate: str,
):
    fig = go.Figure(
        go.Choroplethmapbox(
            geojson=counties,
            locations=df["region_id"],
            z=df[z],
            text=df["region_name"],
            colorscale=[
                [0, "rgb(34, 150, 79)"],
                [0.2, "rgb(249, 247, 174)"],
                [0.8, "rgb(253, 172, 99)"],
                [1, "rgb(212, 50, 44)"],
            ],
            colorbar_thickness=20,
            customdata=customdata,
            hovertemplate=hovertemplate,
            hoverinfo="text, z",
        )
    )
    fig.update_layout(
        mapbox_style="carto-positron",
        mapbox_zoom=1,
        mapbox_center={"lat": 66, "lon": 94},
    )
    fig.update_traces(marker_line_width=0)
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    fig.show()
