import plotly.express as px
from shiny.express import input, ui
from shinywidgets import render_plotly
import palmerpenguins  # This package provides the Palmer Penguins dataset

# Use the built-in function to load the Palmer Penguins dataset
penguins_df = palmerpenguins.load_penguins()

ui.page_opts(title="DavidRm Penguin", fillable=True)
ui.h2("Side bar")
with ui.sidebar():
    ui.input_selectize(
        "var", "Selected_attribute",
        ["species", "island", "bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g", "sex"]
    )
    ui.input_numeric("bins", "Number of bins", 30)



with ui.card(full_screen=True):
    @render_plotly
    def hist():
        import plotly.express as px
        from palmerpenguins import load_penguins
        return px.histogram(load_penguins(), x=input.var(), nbins=input.bins())
