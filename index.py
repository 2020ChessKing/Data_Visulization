#   imports
import pandas as panda, plotly_express as plotly, csv, plotly.graph_objects as graphs

#   code
framed_data = panda.read_csv(r"C:\Swarup\WhiteHat Jr\Python\Projects\DataVis\data.csv")
scatter_graph = plotly.scatter(framed_data, x="student_id", y="level", color="level", size="attempt")
scatter_graph.show()