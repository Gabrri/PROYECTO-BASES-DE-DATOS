def Cantidad_ICFES_Genero():
    return """select "Genero", count("ID")
        from "Estudiante"
        where "Genero" = 'F' or "Genero" = 'M'
        group by("Genero")
        """
def Trabajo_papa ():
    return """ select trabajo_papa ,count("ID")
        from "Estudiante"
        where trabajo_papa <> '-' or trabajo_papa <> null
        group by trabajo_papa
        """
def Puntaje_Global_Deptos():
    return """ select dep.nombre, round(avg(est."Puntage_Global"),2)
        from "Estudiante" est join "Colegio" col on (col."ID" = est."ID_Colegio")
        join "Ciudad" ciu on (col."ID_Ciudad" = ciu."ID")
        join "Departamento" dep on (ciu."ID_Departamento" = dep."ID")
        group by(dep.nombre)"""

def Puntaje_Municipios():
    return """
        select ciu.nombre, round(avg(est."Puntage_Global"),2)
        from "Estudiante" est join "Colegio" col on (col."ID" = est."ID_Colegio")
        join "Ciudad" ciu on (col."ID_Ciudad" = ciu."ID")
        group by(ciu.nombre)
        limit 20
        """


def Promedio_PuntajeArea():
    return """ select 'Puntaje lectura' as default_value ,round(avg("P_lectura_critica"),2)
		from "Estudiante"
        union
        select 'Puntaje sociales' as default_value, round(avg("P_sociales_ciudadanas"),2) as Sociales_Ciudadanas
        from "Estudiante"
        union
        select 'Puntaje ingles' as default_value,round(avg("P_ingles"),2) as ingles
        from "Estudiante"
        union
        select 'Puntaje ciencias' as default_value,round(avg("P_ciencias_naturales"),2) as Ciencias_naturales
        from "Estudiante"
        union
        select 'Puntaje matematicas' as default_value,round(avg("P_matematicas"),2) as matematicas
        from "Estudiante" """


def Internet_Estudiantes():
    return"""select "Internet", count("Internet")
        from "Estudiante"
        where "Internet" = 'No' or "Internet" = 'Si'
        group by "Internet"
        """

def Estrato():
    return """select "Estrato", count("Estrato")
    from "Estudiante"
    where "Estrato" = 'Estrato 6' or "Estrato" = 'Estrato 5' or "Estrato" = 'Estrato 4' or "Estrato" = 'Estrato 3'
    or "Estrato" = 'Estrato 2' or "Estrato" = 'Estrato 1' or "Estrato" = 'Sin Estrato'
    group by "Estrato" """

def Promedio_Estrato():
    return """ select "Estrato", round(avg("Puntage_Global"),2)
        from "Estudiante"
        where "Estrato" = 'Estrato 6' or "Estrato" = 'Estrato 5' or "Estrato" = 'Estrato 4' or "Estrato" = 'Estrato 3'
        or "Estrato" = 'Estrato 2' or "Estrato" = 'Estrato 1' or "Estrato" = 'Sin Estrato'
        group by "Estrato" """

def Puntajes_Mayor300():
    return """
        select 'Puntaje_Global mayor a 300' as default_value, count("ID")
        from "Estudiante"
        where "Puntage_Global" > 300
        union
        select 'Puntaje_Global menor a 300' as default_value,count("ID")
        from "Estudiante"
        where "Puntage_Global" < 300
        """
def Promedio_Internet():
    return """
    select 'No internet' as default_value, round(avg("Puntage_Global"),2)
    from "Estudiante"
    where "Internet" = 'No'
    union
    select 'Si internet' as default_value, round(avg("Puntage_Global"),2)
    from "Estudiante"
    where "Internet" = 'Si'
    """
def Promedio_Area_Genero():
    return """
        select 'Puntaje lectura' as areas,'Masculino' as default_value ,round(avg("P_lectura_critica"),2)
        from "Estudiante"
        where "Genero" ='M'
        union
        select 'Puntaje sociales' as areas,'Masculino' as default_value, round(avg("P_sociales_ciudadanas"),2) as Sociales_Ciudadanas
        from "Estudiante"
        where "Genero" ='M'
        union
        select 'Puntaje ingles' as areas,'Masculino' as default_value,round(avg("P_ingles"),2) as ingles
        from "Estudiante"
        where "Genero" ='M'
        union
        select 'Puntaje ciencias' as areas,'Masculino' as default_value,round(avg("P_ciencias_naturales"),2) as Ciencias_naturales
        from "Estudiante"
        where "Genero" ='M'
        union
        select 'Puntaje matematicas' as areas,'Masculino' as default_value,round(avg("P_matematicas"),2) as matematicas
        from "Estudiante"
        where "Genero" ='M'
        union
        select 'Puntaje lectura' as areas , 'Femenino' as default_value, round(avg("P_lectura_critica"),2)
        from "Estudiante"
        where "Genero" ='F'
        union
        select 'Puntaje sociales' as areas,'Femenino' as default_value,  round(avg("P_sociales_ciudadanas"),2) as Sociales_Ciudadanas
        from "Estudiante"
        where "Genero" ='F'
        union
        select 'Puntaje ingles' as areas,'Femenino' as default_value, round(avg("P_ingles"),2) as ingles
        from "Estudiante"
        where "Genero" ='F'
        union
        select 'Puntaje ciencias' as areas,'Femenino' as default_value, round(avg("P_ciencias_naturales"),2) as Ciencias_naturales
        from "Estudiante"
        where "Genero" ='F'
        union
        select 'Puntaje matematicas' as areas,'Femenino' as default_value, round(avg("P_matematicas"),2) as matematicas
        from "Estudiante"
        where "Genero" ='F'
        """
def Relacion_1():
    return """
        select "P_matematicas","P_ingles"
        from "Estudiante"
        """
def FunHoras_Internet():
    return """
        select "Horas_Internet",count("ID")
        from "Estudiante"
        where "Horas_Internet" <> 'null' or "Horas_Internet" <> '-'
        group by ("Horas_Internet");
        """
def Funtrabajo():
    return """
        select 'No trabaja' as Horas_Trabajo,count("ID")
        from "Estudiante"
        where "Horas_Trabajo_Semanales" = '0'
        union
        select 'Trabaja' as Horas_Trabajo,count("ID")
        from "Estudiante"
        where "Horas_Trabajo_Semanales" <> '0';
        """
def PromHoras_Internet():
    return"""
        select "Horas_Internet",round(avg("Puntage_Global"),2)
        from "Estudiante"
        where "Horas_Internet" <> 'null' or "Horas_Internet" <> '-'
        group by ("Horas_Internet");
        """
def PromFuntrabajo():
    return """
        select 'No trabaja' as Horas_Trabajo,round(avg("Puntage_Global"),2)
        from "Estudiante"
        where "Horas_Trabajo_Semanales" = '0'
        union
        select 'Trabaja' as Horas_Trabajo,round(avg("Puntage_Global"),2)
        from "Estudiante"
        where "Horas_Trabajo_Semanales" <> '0';
        """
def rel2():
    return """
        select "P_sociales_ciudadanas", "P_lectura_critica"
        from "Estudiante"
        """
def rel3():
    return """
        select "P_ciencias_naturales", "P_matematicas"
        from "Estudiante";
        """
def rel4():
    return """
        select "P_ingles","P_lectura_critica"
        from "Estudiante";
        """
