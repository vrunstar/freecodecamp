import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np


def draw_plot():
    # Read data
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(
        df["Year"],
        df["CSIRO Adjusted Sea Level"]
    )

    # First line of best fit (all data)
    res = linregress(
        df["Year"],
        df["CSIRO Adjusted Sea Level"]
    )

    years_extended = np.arange(
        df["Year"].min(),
        2051
    )

    ax.plot(
        years_extended,
        res.intercept + res.slope * years_extended,
        color="red"
    )

    # Second line of best fit (from year 2000 onward)
    df_recent = df[df["Year"] >= 2000]

    res_recent = linregress(
        df_recent["Year"],
        df_recent["CSIRO Adjusted Sea Level"]
    )

    years_recent = np.arange(
        2000,
        2051
    )

    ax.plot(
        years_recent,
        res_recent.intercept + res_recent.slope * years_recent,
        color="green"
    )

    # Labels and title
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")

    # Save and return
    fig.savefig("sea_level_plot.png")
    return fig
