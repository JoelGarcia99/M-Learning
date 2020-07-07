# M-Learning Platform  

## Idea 
En principio lo que se hará primero será poder recomendar videos, basados en los gustos del usuario y en videos que haya visto previamente. Practicamente serán dos capas de recomendación:  
1. **Capa 1**: Aquí se usará algún proceso de clustering, como KNN para determinar las preferencias del usuario, que podrñan ser de tres tipos: *Videos*, *Libross*, y *Artículos*.  
2. **Capa 2**: Será la capa de recomendación como tal, sabiendo que el usuario pertenece a algún grupo específico gracias a la capa 1. Esta capa usará un item based filtering, ya que, dependiendo de la carrera, materia, y semestre que curse, se le recomendará material más o menos técnico.  

En la **capa 2** se tendrá un dataset donde se irán guardando las recomendaciones hechas al usuario y la calificación, la cual será en escala del 1 al 3, quedando definidos de la siguiente manera:  
1. No fue útil.
2. útil.
3. Muy úitl.  

## Temas a consultar  
1. **Máquinas de Boltzmann**, en el curso de Deep Learning se dijo que servían para RS.   

## Enlaces  
1. YouTube API: https://developers.google.com/youtube/v3/docs/search/list  

## Recomendaciones  
1. Se recomienda la creación de un entorno virtual para evitar conflictos con otras dependencias. Se puede crear un entorno virtual de la siguiente manera: `virtualenv Mlearning-platform -p python3`.   
## Instalaciones  
1. Django: `pip install django`  
2. Django RestFramework: `pip install djangorestframework`  


## Comandos  
1. `manage.py migrate`: Crea la DB e inicializa el proyecto.  
2. `python manage.py runserver`: Corre el servidor.  

