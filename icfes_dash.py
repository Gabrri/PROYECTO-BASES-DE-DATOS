import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from Connection_icfes import Connection_icfes
import Search_icfes as sql
import requests
import plotly.graph_objects as go
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm

external_stylesheets = ["https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css"]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#8a6642',
    'text': '#7FDBFF'
}

#Puntaje global por genero
con = Connection_icfes()
con.openConnection()
query = pd.read_sql_query(sql.Cantidad_ICFES_Genero(), con.connection)
con.closeConnection()
TotDep = pd.DataFrame(query, columns=["Genero", "count"])
figPieCant = px.pie(TotDep, values='count', names='Genero',color_discrete_sequence=px.colors.sequential.RdBu)


#Puntaje global por deptos
con = Connection_icfes()
con.openConnection()
query = pd.read_sql_query(sql.Puntaje_Global_Deptos(), con.connection)
con.closeConnection()
PuntDep = pd.DataFrame(query, columns=["nombre", "round"])
figBarPuntDep = px.bar(PuntDep, x='nombre', y='round',color='round')


mpios_json = requests.get('https://raw.githubusercontent.com/caticoa3/colombia_mapa/master/co_2018_MGN_MPIO_POLITICO.geojson')

#Puntaje global por Municipios
con = Connection_icfes()
con.openConnection()
query = pd.read_sql_query(sql.Puntaje_Municipios(), con.connection)
con.closeConnection()
PuntMuni = pd.DataFrame(query, columns=["nombre", "round"])
figBarPunMuni = px.bar(PuntMuni, x='nombre', y='round',color='nombre')


#Trabajo papa
con = Connection_icfes()
con.openConnection()
query = pd.read_sql_query(sql.Trabajo_papa(), con.connection)
con.closeConnection()
TraPapa = pd.DataFrame(query, columns=["trabajo_papa", "count"])
figPieTraPapa = px.pie(TraPapa, values='count', names='trabajo_papa',color_discrete_sequence=px.colors.sequential.RdBu)


#Promedio puntaje area
con = Connection_icfes()
con.openConnection()
query = pd.read_sql_query(sql.Promedio_PuntajeArea(), con.connection)
con.closeConnection()
PuntArea = pd.DataFrame(query, columns=["round","default_value"])
figPiePuntArea = px.bar(PuntArea, y='round', x='default_value', color='default_value')

#Cantidad de estudiates con Internet
con = Connection_icfes()
con.openConnection()
query = pd.read_sql_query(sql.Internet_Estudiantes(), con.connection)
con.closeConnection()
InterEst = pd.DataFrame(query, columns=["Internet","count"])
figBatInterEst = px.bar(InterEst, x='count', y='Internet',color='Internet')

#Distribucion Estrato
con = Connection_icfes()
con.openConnection()
query = pd.read_sql_query(sql.Estrato(), con.connection)
con.closeConnection()
Estrato = pd.DataFrame(query, columns=["Estrato","count"])
figPieEstrato = px.pie(Estrato, values='count', names='Estrato', color_discrete_sequence=px.colors.sequential.RdBu)

#Promedio por estrato
con = Connection_icfes()
con.openConnection()
query = pd.read_sql_query(sql.Promedio_Estrato(), con.connection)
con.closeConnection()
PromEstrato = pd.DataFrame(query, columns=["Estrato","round"])
figBarPromEstrato = px.bar(PromEstrato, x='Estrato', y='round',color='round')

#Cantidad de estudiantes puntaje global mayor a 300 y menor a 300
con = Connection_icfes()
con.openConnection()
query = pd.read_sql_query(sql.Puntajes_Mayor300(), con.connection)
con.closeConnection()
PuntajeMayor300 = pd.DataFrame(query, columns=["count","default_value"])
figPieMayor300 = px.pie(PuntajeMayor300, values='count', names='default_value' ,color_discrete_sequence=px.colors.sequential.RdBu)

#promedio estudiantes con o sin Internet
con = Connection_icfes()
con.openConnection()
query = pd.read_sql_query(sql.Promedio_Internet(), con.connection)
con.closeConnection()
PromedioInternet = pd.DataFrame(query, columns=["round","default_value"])
figPiePromInter = px.bar(PromedioInternet, y='round', x='default_value' ,color='default_value')

#promedio Area Genero
con = Connection_icfes()
con.openConnection()
query = pd.read_sql_query(sql.Promedio_Area_Genero(), con.connection)
con.closeConnection()
PromedioAreaGenero = pd.DataFrame(query, columns=["round","areas","default_value"])
figPromedioAreaGenero = px.sunburst(PromedioAreaGenero, path=['areas', 'default_value'], values='round',
                  color='round', hover_data=['areas'])

#correlacion ingles y P_matematicas
con = Connection_icfes()
con.openConnection()
query = pd.read_sql_query(sql.Relacion_1(), con.connection)
con.closeConnection()
Relacion1 = pd.DataFrame(query, columns=["P_matematicas","P_ingles"])
figPRegRelacion = px.scatter(
    Relacion1, x='P_matematicas', y='P_ingles',trendline='ols', trendline_color_override='darkblue')


#horas de internet al dia
con = Connection_icfes()
con.openConnection()
query = pd.read_sql_query(sql.FunHoras_Internet(), con.connection)
con.closeConnection()
HorasInternet = pd.DataFrame(query, columns=["Horas_Internet","count"])
figPieHorasInternet = px.pie(HorasInternet,names='Horas_Internet', values='count', hole=.6,color_discrete_sequence=px.colors.sequential.RdBu)

#trabajo estudiantes
con = Connection_icfes()
con.openConnection()
query = pd.read_sql_query(sql.Funtrabajo(), con.connection)
con.closeConnection()
HorasTrabajoSemana = pd.DataFrame(query, columns=["horas_trabajo","count"])
figPieHorasTrabajoSemana = px.pie(HorasTrabajoSemana,names='horas_trabajo', values='count', hole=.6,color_discrete_sequence=px.colors.sequential.RdBu)

#promedio puntage global personas con y sin internet
con = Connection_icfes()
con.openConnection()
query = pd.read_sql_query(sql.PromHoras_Internet(), con.connection)
con.closeConnection()
Promhorasinternet = pd.DataFrame(query, columns=["round","Horas_Internet"])
figPiePromhorasinternet = px.bar(Promhorasinternet, y='round', x='Horas_Internet' ,color='Horas_Internet')


#promedio personas que HorasTrabajoSemana
con = Connection_icfes()
con.openConnection()
query = pd.read_sql_query(sql.PromFuntrabajo(), con.connection)
con.closeConnection()
Promhorastrabajo = pd.DataFrame(query, columns=["round","horas_trabajo"])
figbarPromtrabajo = px.bar(Promhorastrabajo, y='round', x='horas_trabajo' ,color='horas_trabajo')

#relacion lectura critica y sociales ciudadanas
con = Connection_icfes()
con.openConnection()
query = pd.read_sql_query(sql.rel2(), con.connection)
con.closeConnection()
Relacion2 = pd.DataFrame(query, columns=["P_lectura_critica","P_sociales_ciudadanas"])
figPRegRelacion2 = px.scatter(Relacion2, x='P_lectura_critica', y='P_sociales_ciudadanas',trendline='ols', trendline_color_override='darkblue')

# relacion ciencias naturales y matematicas
con = Connection_icfes()
con.openConnection()
query = pd.read_sql_query(sql.rel3(), con.connection)
con.closeConnection()
Relacion3 = pd.DataFrame(query, columns=["P_matematicas","P_ciencias_naturales"])
figPRegRelacion3 = px.scatter(Relacion3, x='P_matematicas', y='P_ciencias_naturales',trendline='ols', trendline_color_override='darkblue')

# relacion ciencias naturales y matematicas
con = Connection_icfes()
con.openConnection()
query = pd.read_sql_query(sql.rel4(), con.connection)
con.closeConnection()
Relacion4 = pd.DataFrame(query, columns=["P_ingles","P_lectura_critica"])
figPRegRelacion4 = px.scatter(Relacion4, x='P_ingles', y='P_lectura_critica',trendline='ols', trendline_color_override='darkblue')



#Layout
app.layout = html.Div(style={'backgroundColor': colors['background']},children=[
    html.H1(children="PRUEBA ICFES-2019-2 DASHBOARD", style={
            'textAlign': 'center',
            'color': colors['text']
        }),
    html.Div(className="container-fluid", children=[
        #Row for cases
        html.Div(className="row", children=[
            #promedio puntage global
            html.Div(className="col-12 col-xl-6", children=[
                html.Div(className="card border-info", children=[
                    html.Div(className="card-header bg-info text-light", children=[
                        html.H3(children="DISTRIBUCIÓN DE HOMBRES Y MUJERES"),
                    ]),
                    html.Div(className="card-body", children=[
                        dcc.Graph(
                            id="Estudiantes que presentaron el ICFES segun el genero",
                            figure=figPieCant
                        ),
                    ]),
                ]),
            ]),
            #Promedio Puntaje area
            html.Div(className="col-12 col-xl-6", children=[
                html.Div(className="card border-info", children=[
                    html.Div(className="card-header bg-info text-light", children=[
                        html.H3(children="PROMEDIO PUNTAJE POR AREA"),
                    ]),
                    html.Div(className="card-body", children=[
                        dcc.Graph(
                            id="PuntArea",
                            figure=figPiePuntArea
                        ),
                    ]),
                ]),
            ]),
            #Puntajes mayores a 300
            html.Div(className="col-12 col-xl-6", children=[
                html.Div(className="card border-info", children=[
                    html.Div(className="card-header bg-info text-light", children=[
                        html.H3(children="DISTRIBUCION PUNTAJES MAYORES Y MENORES A 300"),
                    ]),
                    html.Div(className="card-body", children=[
                        dcc.Graph(
                            id="Puntaje_Mayor300",
                            figure=figPieMayor300
                        ),
                    ]),
                ]),
            ]),
            #promedio area genero
            html.Div(className="col-12 col-xl-6", children=[
                html.Div(className="card border-info", children=[
                    html.Div(className="card-header bg-info text-light", children=[
                        html.H3(children="PROMEDIO DE AREA POR GÉNERO"),
                    ]),
                    html.Div(className="card-body", children=[
                        dcc.Graph(
                            id="Promedio_Depto_Genero",
                            figure=figPromedioAreaGenero
                        ),
                    ]),
                ]),
            ]),
            #Puntage global departamentos
            html.Div(className=" ", children=[
                html.Div(className=" ", children=[
                    html.Div(className="card border-info", children=[
                        html.Div(className="card-header bg-info text-light", children=[
                            html.H3(children="PROMEDIO PUNTAJE GLOBAL POR DEPARTAMENTOS"),
                        ]),
                        html.Div(className="card-body", children=[
                            dcc.Graph(
                                id="Puntaje_Global_Deptos",
                                figure=figBarPuntDep
                            ),
                        ]),
                    ]),
                ]),
            ]),
            #puntaje global municipios
            html.Div(className="row", children=[
                html.Div(className=" ", children=[
                    html.Div(className="card border-info", children=[
                        html.Div(className="card-header bg-info text-light", children=[
                            html.H3(children="PROMEDIO PUNTAJE POR MUNICIPIOS"),
                        ]),
                        html.Div(className="card-body", children=[
                            dcc.Graph(
                                id="Puntaje_Global_muni",
                                figure=figBarPunMuni
                            ),
                        ]),
                    ]),
                ]),
            ]),
            #Internet
            html.Div(className="row", children=[
                html.Div(className="col-12 col-xl-6", children=[
                    html.Div(className="card border-info", children=[
                        html.Div(className="card-header bg-info text-light", children=[
                            html.H3(children="CANTIDAD DE ESTUDIANTES CON SERVICIO A INTERNET"),
                        ]),
                        html.Div(className="card-body", children=[
                            dcc.Graph(
                                id="Internet_Est",
                                figure=figBatInterEst
                            ),
                        ]),
                    ]),
                ]),
                #Estrato
                html.Div(className="col-12 col-xl-6", children=[
                    html.Div(className="card border-info", children=[
                        html.Div(className="card-header bg-info text-light", children=[
                            html.H3(children="CANTIDAD DE ESTUDIANTES POR ESTRATO"),
                        ]),
                        html.Div(className="card-body", children=[
                            dcc.Graph(
                                id="Estrato_Est",
                                figure=figPieEstrato
                            ),
                        ]),
                    ]),
                ]),
            ]),
            #Promedio por Estrato
            html.Div(className="row", children=[
                html.Div(className="col-12 col-xl-6", children=[
                    html.Div(className="card border-info", children=[
                        html.Div(className="card-header bg-info text-light", children=[
                            html.H3(children="PROMEDIO POR ESTRATO"),
                        ]),
                        html.Div(className="card-body", children=[
                            dcc.Graph(
                                id="Promedio_Estrato",
                                figure=figBarPromEstrato
                            ),
                        ]),
                    ]),
                ]),
            #promedio estudiante qe tienen internet
                html.Div(className="col-12 col-xl-6", children=[
                    html.Div(className="card border-info", children=[
                        html.Div(className="card-header bg-info text-light", children=[
                            html.H3(children="PROMEDIO DE ESTUDIANTES QUE TIENEN INTERNET"),
                        ]),
                        html.Div(className="card-body", children=[
                            dcc.Graph(
                                id="Promedio_Internet",
                                figure=figPiePromInter
                            ),
                        ]),
                    ]),
                ]),
            ]),
            #trabajo padre
            html.Div(className=" ", children=[
                html.Div(className=" ", children=[
                    html.Div(className="card border-info", children=[
                        html.Div(className="card-header bg-info text-light", children=[
                            html.H3(children="DISTRIBUCIÓN TRABAJO PADRES"),
                        ]),
                        html.Div(className="card-body", children=[
                            dcc.Graph(
                                id="Trabajo_Papa",
                                figure=figPieTraPapa
                            ),
                        ]),
                    ]),
                ]),
            ]),
            #horas dia Internet
            html.Div(className="row", children=[
                html.Div(className="col-12 col-xl-6", children=[
                    html.Div(className="card border-info", children=[
                        html.Div(className="card-header bg-info text-light", children=[
                            html.H3(children="HORAS DE INTERNET AL DIA"),
                        ]),
                        html.Div(className="card-body", children=[
                            dcc.Graph(
                                id="Horas_Dia_Internet",
                                figure=figPieHorasInternet
                            ),
                        ]),
                    ]),
                ]),
                #horas de trabajo a la semana del estudiante
                html.Div(className="col-12 col-xl-6", children=[
                    html.Div(className="card border-info", children=[
                        html.Div(className="card-header bg-info text-light", children=[
                            html.H3(children="PORCENTAJE DE ESTUDIANTES TRABAJADORES ACTIVOS"),
                        ]),
                        html.Div(className="card-body", children=[
                            dcc.Graph(
                                id="Horas_Trabajo_Semana",
                                figure=figPieHorasTrabajoSemana
                            ),
                        ]),
                    ]),
                ]),
            ]),
            #promedio puntage global horas de internet al dia
            html.Div(className="row", children=[
                html.Div(className="col-12 col-xl-6", children=[
                    html.Div(className="card border-info", children=[
                        html.Div(className="card-header bg-info text-light", children=[
                            html.H3(children="PROMEDIO PUNTAJE GLOBAL SEGUN HORAS DE INTERNET AL DIA"),
                        ]),
                        html.Div(className="card-body", children=[
                            dcc.Graph(
                                id="prom_horas_internet",
                                figure=figPiePromhorasinternet
                            ),
                        ]),
                    ]),
                ]),
                #promedio puntage global horas de trabajo al dia de estudiantes
                html.Div(className="col-12 col-xl-6", children=[
                    html.Div(className="card border-info", children=[
                        html.Div(className="card-header bg-info text-light", children=[
                            html.H3(children="RELACIÓN ENTRE EL PROMEDIO Y LOS ESTUDIANTES TRABAJADORES ACTIVOS"),
                        ]),
                        html.Div(className="card-body", children=[
                            dcc.Graph(
                                id="prom_horas_trabajo",
                                figure=figbarPromtrabajo
                            ),
                        ]),
                    ]),
                ]),
            ]),
            #relacion entre matematicas e ingles
            html.Div(className="col-12 col-xl-6", children=[
                html.Div(className="card border-info", children=[
                    html.Div(className="card-header bg-info text-light", children=[
                        html.H3(children="RELACIÓN MATEMÁTICAS E INGLES"),
                    ]),
                    html.Div(className="card-body", children=[
                        dcc.Graph(
                            id="Correlacion matematicas e ingles",
                            figure=figPRegRelacion
                        ),
                    ]),
                ]),
            ]),
                # rel 2 lectura CRITICA Y SOCIALES CIUDADANAS
            html.Div(className="col-12 col-xl-6", children=[
                html.Div(className="card border-info", children=[
                    html.Div(className="card-header bg-info text-light", children=[
                        html.H3(children="RELACIÓN LECTURA CRÍTICA Y SOCIALES CIUDADANAS"),
                    ]),
                    html.Div(className="card-body", children=[
                        dcc.Graph(
                            id="Correlacion ciencias sociales y lectura critica",
                            figure=figPRegRelacion2
                        ),
                    ]),
                ]),
            ]),
            html.Div(className="col-12 col-xl-6", children=[
                html.Div(className="card border-info", children=[
                    html.Div(className="card-header bg-info text-light", children=[
                        html.H3(children="RELACIÓN MATEMÁTICAS Y CIENCIAS NATURALES"),
                    ]),
                    html.Div(className="card-body", children=[
                        dcc.Graph(
                            id="relacion_matematicas_ciencias_naturales",
                            figure=figPRegRelacion3
                        ),
                    ]),
                ]),
            ]),
            html.Div(className="col-12 col-xl-6", children=[
                html.Div(className="card border-info", children=[
                    html.Div(className="card-header bg-info text-light", children=[
                        html.H3(children="RELACIÓN LECTURA CRÍTICA E INGLES"),
                    ]),
                    html.Div(className="card-body", children=[
                        dcc.Graph(
                            id="relacion_lectura_critica_ingles",
                            figure=figPRegRelacion4
                        ),
                    ]),
                ]),
            ]),
        ]),
    ]),
])
if __name__ == "__main__":
    app.run_server(debug=True)
