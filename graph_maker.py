from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool


class GraphMaker:

    def __init__(self):
        pass

    @staticmethod
    def generateQuadGraphDatetime(dataframe):
        p = figure(x_axis_type = 'datetime', height = 500, width = 1000, title = "Motion graph")
        p.yaxis.minor_tick_line_color = None
        p.ygrid[0].ticker.desired_num_ticks=1


        q = p.quad(left=dataframe["Start"], right=dataframe["End"], bottom=0, top=1, color="green")

        output_file("Graph.hmtl")

        show(p)


    @staticmethod
    def showGraph(graph):
        show(graph)


