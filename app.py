import plotly.express as px
from shiny.express import input, ui
from shinywidgets import render_plotly
import palmerpenguins  # This package provides the Palmer Penguins dataset

# Use the built-in function to load the Palmer Penguins dataset
penguins_df = palmerpenguins.load_penguins()

ui.page_opts(title="DavidRm Penguin", fillable=True)

ui.h2("Side bar")
with ui.sidebar(open="open", bg="#f8f8f8"):
    ui.input_selectize(
        "selected_attribute",
        "Select Plotly Attribute",
        ["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"],
    )

    ui.input_numeric("plotly_bin_count", "plotly_bin_count", 1, min=1, max=10)

    (ui.input_slider("seaborn_bin_count", "seaborn_bin_count", 0, 20, 10),) 

ui.input_checkbox_group(
        "selected_species",
        "Species in Scatterplot",
        ["Adelie", "Gentoo", "Chinstrap"],
        selected=["Adelie"],
        inline=True,
    )

ui.a("GitHub", href="https://github.com/drodmay1/cintel-02-data.git", target="_blank")

with ui.card(full_screen=True):

    ui.card_header("Plotly Scatterplot: Species")
    @render_plotly
    def plotly_scatterplot():
        return px.scatter(
            penguins_df(),
            x="bill_length_mm",
            y="body_mass_g",
            color="species",
            title="Penguins Plot (Plotly Express)",
            labels={
                "bill_length_mm": "Bill Length (mm)",
                "body_mass_g": "Body Mass (g)",
            },
            size_max=8, # set the maximum marker size
        )
    
