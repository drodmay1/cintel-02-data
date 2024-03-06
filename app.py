import plotly.express as px
from shiny.express import input, ui
from shinywidgets import render_plotly
import palmerpenguins  # This package provides the Palmer Penguins dataset
import pandas as pd
import seaborn as sns
from shiny import reactive, render, req

# Use the built-in function to load the Palmer Penguins dataset
penguins_df = palmerpenguins.load_penguins()

ui.page_opts(title="DavidRm Penguin", fillable=True)

with ui.sidebar(open="open"):
    
    ui.h2("Sidebar")
    
    ui.input_selectize(
        "selected_attribute",
        "Select Plotly Attribute",
        ["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"],
    )

    ui.input_numeric("plotly_bin_count", "Number of Plotly bins", 30)
    
    ui.input_slider("seaborn_bin_count", "Number of Seaborn bins", 1, 100, 20)

    ui.hr()
    
    ui.input_checkbox_group(
        "selected_species_list",
        "Species",
        ["Adelie", "Gentoo", "Chinstrap"],
        selected=["Adelie"],
        inline=True,
    )

    ui.a(
        "GitHub",
         href="https://github.com/drodmay1/cintel-02-data.git",
         target="_blank",
         )

# Creates a Plotty Scatterplot showing all species

with ui.card(full_screen=True):
    ui.card_header("Plotly Scatterplot: Species")

    @render_plotly
    def plotly_scatterplot():
        return px.scatter(penguins_df,
            x="bill_length_mm",
            y="body_mass_g",
            color="species",
            title="Penguins Plot",
            labels={
                "bill_length_mm": "Bill Length (mm)",
                "body_mass_g": "Body Mass (g)",
            },
            size_max=8, 
        )
    
