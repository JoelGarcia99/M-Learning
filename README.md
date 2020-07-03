# M-Learning Platform  

## Idea 
En principio lo que se hará primero será poder recomendar videos, basados en los gustos del usuario y en videos que haya visto previamente. Practicamente serán dos capas de recomendación:  
1. **Capa 1**: Aquí se usará algún proceso de clustering, como KNN para determinar las preferencias del usuario, que podrñan ser de tres tipos: *Videos*, *Libross*, y *Artículos*.  
2. **Capa 2**: Será la capa de recomendación como tal, sabiendo que el usuario pertenece a algún grupo específico gracias a la capa 1. Esta capa usará un item based filtering, ya que, dependiendo de la carrera, materia, y semestre que curse, se le recomendará material más o menos técnico.  
