from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool, ColumnDataSource


class GraphMaker:

    def __init__(self):
        pass

    @staticmethod
    def generateQuadGraphDatetime(dataframe):
        dataframe["Start_string"] = dataframe["Start"].dt.strftime("%Y-%m-%d %H:%M:%S")
        dataframe["End_string"] = dataframe["End"].dt.strftime("%Y-%m-%d %H:%M:%S")

        cds=ColumnDataSource(dataframe)

        p = figure(x_axis_type = 'datetime', height = 500, width = 1000, title = "Motion graph")

        hover = HoverTool(tooltips=[("Start", "@Start_string"), ("End", "@End_string")])
        p.add_tools(hover)


        p.yaxis.minor_tick_line_color = None
        p.ygrid[0].ticker.desired_num_ticks=1


        q = p.quad(left="Start", right="End", bottom=0, top=1, color="green", source=cds)

        output_file("Graph.hmtl")

        show(p)


    @staticmethod
    def showGraph(graph):
        show(graph)


