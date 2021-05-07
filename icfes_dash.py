import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from Connection_icfes import Connection_icfes
import Search_icfes as sql

external_stylesheets = ["https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css"]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


#Total departments
con = Connection_icfes()
con.openConnection()
query = pd.read_sql_query(sql.totalDepartametos(), con.connection)
con.closeConnection()
TotDep = pd.DataFrame(query, columns=["ID", "nombre"])
figbartDep =  px.bar(TotDep.head(30),x="ID", y="nombre")

#Layout
app.layout = html.Div(children=[
    html.H1(children="Prueba ICFES-2019-2 Dashboard", className="text-center"),
    html.Div(className="container-fluid", children=[
        #Row for cases
        html.Div(className="row", children=[
            #Col for bars
            html.Div(className="col-12 col-xl-6", children=[
                html.Div(className="card border-info", children=[
                    html.Div(className="card-header bg-info text-light", children=[
                        html.H3(children="Total Departametos"),
                    ]),
                    html.Div(className="card-body", children=[
                        dcc.Graph(
                            id="Totaldepartamentos",
                            figure=figbartDep
                        ),
                    ]),
                ]),
            ]),
        ]),
    ]),
])
if __name__ == "__main__":
    app.run_server(debug=True)
