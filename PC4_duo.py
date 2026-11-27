# python -m venv .venv
# pip install Streamlit
# pip install streamlit_option_menu
# pip install streamlit.components.v1
# python -m streamlit hello
# python -m streamlit run PC4_duo.py

import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as components

### Opción 1: Menú vertical
with st.sidebar:
    opciones = option_menu("Bienvenidx a nuestro blog",['Nosotras', 'Experiencia', 'Resultados'] , 
        icons=['1-circle','2-circle', '3-circle'], menu_icon="bookmark-heart", default_index=0)

### Opción 2: Menú horizontal
#opciones_2 = option_menu(
#    menu_title="Selecciona una sección: ", 
#    options=['Presentación', 'Experiencia', 'Gráficos'], 
#    icons=['0-circle','1-circle', '2-circle'], 
#    menu_icon="cast", default_index=0, orientation="horizontal")

if opciones == 'Nosotras':
    st.markdown("<h1 style='text-align: center; font-size: 50 px; color: black'>MODO PAIDEIA BLOG</h1>", unsafe_allow_html=True)

    # Alumno a
    col1, col2 = st.columns(2)
    
    col1.image("imagen_anapaula.jpg", caption='@massiel_anapaula | a20246587@pucp.edu.pe', width=250)

    texto = """
    Hola! Me llamo Anapaula, soy estudiante de Comunicación para el desarrollo de quinto ciclo. 
    En mis tiempos libres me gusta pintar mandalas y ver podcast peruanos, me gusta la música reggae, en especial Dread Mar I y del Kpop mi banda favorita es BTS. 
    He ido al concierto de 3 de mis 4 artistas favoritos :D. 
    Mi autora latinoamericana favorita es Isabel Allende, también me gusta mucho el pollo a la brasa y la Inca Kola. 
    Al terminar mi carrera me gustaría trabajar en proyectos sociales y políticas de desarrollo.
    """
    col2.markdown(f"<div style='text-align: justify right; font-size: 15px;'>{texto}</div>", unsafe_allow_html=True)

    # Alumno b
    col1, col2 = st.columns(2)

    col2.image("imagen_milagros.jpeg", caption='@mincitw_ | m.poma@pucp.edu.pe', width=250)
    
    texto_2 = """
    ¡Hola! Me llamo Milagros, soy estudiante de Comunicación Audiovisual de sexto ciclo. 
    Soy bastante apasionada a mi carrera y siempre me gusta estar apoyando en rodajes. En mis tiempos libres leo, veo películas o escucho podcasts. 
    Si es que tengo mayor tiempo libre usualmente voy a ferias de artistas gráficos independientes. 
    Mi cantante favorita es Olivia Dean. Mi plato favorito es el ceviche y me gustan mucho los dulces, de hecho siempre pido cancha dulce cuando voy al cine. 
    Tambien me interesa los temas de memoria y activismo político por lo que aspiro a crear piezas audiovisual así. 
    """
    col1.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto_2}</div>", unsafe_allow_html=True)
        
elif  opciones == 'Experiencia':

    st.markdown("<h1 style='text-align: center; font-size: 50 px; color: black'>Nuestro paso por la programación 💻</h1>", unsafe_allow_html=True)

    # Alumno a
    texto_3 = """
    Esta es la primera experiencia que tengo con realizar programación. 
    Al principio lo veía como algo muy complicado y no estaba tan segura de mi en poder programar, menos una pagina web. 
    No tenía ni idea de cómo se hacía. La programación me ha enseñado a entender que todo resultado requiere de un proceso, una secuencia de pasos a los que se les debe prestar detalle.
    También a romper ese mito de que solo las ingenieras o carreras afines pueden aplicarla a sus áreas de trabajo. 
    Lo que más me está gustando, aunque a la vez lo siento agotador, es poder concretar la propuesta de proyecto que tenía en mente a través de una página web.
    En el futuro, me gustaría elaborar una plataforma web que sirva como repositorio/archivo digital de libros, cuentos, novelas de autoras latinoamericanas. 
    """
    st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_3}</div>", unsafe_allow_html=True)
    
    # Formato Google Drive
    st.subheader("🎥 Mi primer video de programación: nivel principiante")
   
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:  
        st.link_button("🎥 Semejanzas y diferencias entre Strings y Listas",
                       "https://drive.google.com/file/d/1tuVgGtLmWQU7VS8Q1x0DpRuB_lWEySDm/view?usp=drive_link",
                       use_container_width=True
            )
    
    # Formato Google Drive
    st.subheader("🎥 Mi segundo video de programación: sigo principiante")

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:  
        st.link_button("🎥 Semejanzas y diferencias entre los bucles for y while",
                       "https://drive.google.com/file/d/1ebACS9uGAjeuB1MKWAnG2i0-_y7FmCt4/view?usp=drive_link",
                       use_container_width=True
            )

    # Alumno b
    texto_4 = """
    Es la primera vez que aprendo a programar, si bien ya sabia de la existencia de phyton por otros amigos de ciclos superiores, no me atrevia a aprender a programar. 
    Sentí que iba a ser muy dificil debido a las funciones, y sobre todo porque la mayoria esta en ingles. 
    La programación me ha ayudado a comprender que se pueden crear páginas y establecer reglas o condiciones. 
    Me gusta que en realidad no es algo difícil y me puede ayudar a realizar proyectos que sirvan a la comunidad universitaria. 
    A partir de ello, me gustaria realizar mi portafolio audiovisual y paginás web que recolecten las demandas de los estudiantes según facultad. 
    """
    st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_4}</div>", unsafe_allow_html=True)
        
    # Formato YouTube
    st.subheader("🎥 Título apropiado video 1")
    st.video("https://www.youtube.com/watch?v=X_Z7d04x9-E")
        
    # Formato Google Drive
    st.subheader("🎥 Título apropiado video 2")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:  
        st.link_button("🎥 Texto del botón",
                       "https://drive.google.com/file/d/1REvRXSu3GuGD73w8j44135MkRiezd0gP/view?usp=drive_link",
                       use_container_width=True
             )
            
else:

    st.markdown("<h1 style='text-align: center;font-size: 50 px; color: black'>Visualización de nuestros gráficos</h1>", unsafe_allow_html=True)
    
    # Aquí todos los integrantes deben poner sus 3 gráficos y su mapa en la lista 
    # y aumentar la estructura condicional como sea necesaria
    graficos = ['Gráfico de barras', 'Histograma', 'Piechart', 'Wordcloud', 'Mapas'] 
    grafico_seleccionado = st.selectbox('Selecciona un gráfico', graficos)
    
    if grafico_seleccionado == 'Gráfico de barras':
        st.subheader("📊 Gráfico de barras de Anapaula")
        texto_5 = """
        El gráfico de barras muestra el promedio de tarjetas amarrillas recibidas por 20 equipos que jugaron como visitantes (Away Team). 
        Todos los equipos presentan un promedio de 2 o 3 tarjetas amarrillas, de los cuales, 13 equipos promedian 2 tarjetas, mientras que 7 promedian 3. 
        Sevilla se encuentra en el grupo de equipos con mayor promedio de tarjetas (3 AY))
        """
        st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_5}</div>", unsafe_allow_html=True)

        col1, col2, col3 = st.columns([1, 7, 1])
        with col2:
            st.image("barras_anapaula.png", width=800)

        st.subheader("📊 Gráfico de barras de Milagros")
        texto_6 = """
        El gráfico muestra el promedio de tarjetas amarillas que recibe cada equipo jugando como visitante, dividiéndolos estrictamente en dos grupos. 
        Por un lado, Villarreal, Vallecano, Sociedad, Sevilla, Getafe, Español y Alavés lideran como los más amonestados con poco más de 3 tarjetas por partido. 
        Por otro lado, los trece equipos restantes (incluyendo a Real Madrid, Barcelona y Valencia) se mantienen todos en un mismo nivel inferior, promediando justo por encima de las 2 tarjetas. 
        El hecho de que existan solo dos valores exactos sugiere que los datos provienen de una muestra muy pequeña, probablemente de un único encuentro por equipo.
        """
        st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_6}</div>", unsafe_allow_html=True)
    
        col1, col2, col3 = st.columns([1, 7, 1])
        with col2:
            st.image("barras_milagros.png", width=800)
            
    elif grafico_seleccionado == 'Histograma':
        st.subheader("📊 Histogramas de Anapaula")
        texto_6 = """
        Como local, Sevilla anotó con mayor frecuencia 1 solo gol (8 partidos) y en 5 partidos no anotó ninguno, mientras que como visitante, Sevilla recibe con mayor frecuencia 2 goles (8 partidos). 
        Además, Sevilla anotó 4 goles en solo 2 partidos y, como visitante, recibió 4 o más goles en 2 partidos, con un máximo de 5 en uno de ellos.
        Al comparar ambos gráficos, vemos que en promedio Sevilla anota menos como local que como visitante. 
        Anotan 0 o 1 goles en 13 de 19 partidos, mientras que suelen recibir 2 o más goles en 12 de 19 partidos.
        Por último, pese al análisis de los gráficos, estos no determinan el rendimiento total del equipo puesto que no toma en consideracion los goles recibidos como local ni goles anotados como visitantes.
        """
        st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_6}</div>", unsafe_allow_html=True)
    
        col1, col2, col3 = st.columns([1, 7, 1])
        with col2:
            st.image("histogramas_anapaula.png", width=800)

        st.subheader("📊 Histogramas de Milagros")
        texto_6 = """
        Ambos gráficos muestran el rendimiento de goles del Rayo Vallecano en 19 partidos como local y 19 como visitante. 
        El histograma superior indica que, jugando en casa, lo más habitual es anotar exactamente 1 gol (en 11 encuentros), sin superar nunca los 3 tantos. 
        El gráfico inferior revela que, fuera de casa, el escenario más frecuente también es recibir 1 gol (en 8 ocasiones), aunque muestra mayor vulnerabilidad al llegar a encajar hasta 3 o 4 goles en varios partidos.
        """
        st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_6}</div>", unsafe_allow_html=True)
    
        col1, col2, col3 = st.columns([1, 7, 1])
        with col2:
            st.image("histograma_milagros.png", width=800)
   
    elif grafico_seleccionado == 'Piechart':
        st.subheader("📊 Gráfico de Pastel by Anapaula")
        texto_7 = """
        En la temporada 2025-2026, Sevilla jugó 19 partidos como local, de los cuales ganó el 36.8% (7 partidos), perdió el 42.1% (8 partidos) y empató el 21.1% (4 partidos). 
        En el gráfico, observamos que la derrota fue el resultado con mayor frecuencia, mientras que un empate fue el caso menos común. 
        La diferencia entre derrotas y victorias fue de un partido. 
        Sin embargo, al sumar porcentajes, Sevilla no perdió en el 57.9% de sus partidos, es decir, en 11 de 19 jugados.
        """
        st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_7}</div>", unsafe_allow_html=True)
    
        col1, col2, col3 = st.columns([1, 7, 1])
        with col2:
            st.image("piechart_anapaula.png", width=800)

        st.subheader("📊 Gráfico de Pastel de Milagros")
        texto_7 = """
        El gráfico muestra que el Rayo Vallecano es un equipo muy difícil de vencer en casa, aunque con fuerte tendencia a repartir puntos. 
        Más de la mitad de los partidos del Rayo Vallecano como local terminan en empate (52.6 %), mientras que gana el 36.8 % y apenas pierde el 10.5 % restante. 
        En síntesis, logra sumar puntos en casi 9 de cada 10 encuentros disputados en su estadio.
        """
        st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_7}</div>", unsafe_allow_html=True)
    
        col1, col2, col3 = st.columns([1, 7, 1])
        with col2:
            st.image("piechart_milagros.png", width=800)
            
    elif grafico_seleccionado == 'Wordcloud':
        st.subheader("📊 Nube de palabras Anapaula")
        texto_7 = """
        Interpretación del Gráfico 2 Durante el procesamiento del texto, decidí trabajar con un texto convertido a minúsculas por dos razones. 
        Primeramente, porque Python no codificará de la misma manera una "a" que una "A" por lo que es importante realizar la conversión de todo el texto a un solo formato. 
        Segundo, seleccioné trabajar directamente con minúsculas ya que reduciría la extensión de tamaño (MAYUSCULA es más abarcador que escribir en minúscula) además que, visualmente, consideré que se percibiría mejor para generar la nube de palabras. 
        Por otro lado, eliminé todos los signos de puntuación comunes como ";" "," "." "()" pero también signos de pregunta, exclamación , dos puntos, guiones y puntos suspensivos ya que el texto es como un monólogo en el que la protagonista se hace preguntas hacia sí misma y no era necesario dejarlos ya que estos caracteres no eran trascendentes, decidí no considerar ningún carácter extra.
        Respecto a los stopwords, mi criterio para discriminar cierto grupo de palabras fue depurar todas aquellas que no tuvieran una conexión trascendental o fueran muy generales con el contenido del texto. 
        Es decir, aquellas palabras que no aportaban tanto valor significativo para realizar el análisis del stopword: conectores, determinantes, pronombres, palabras que se atribuyan a tamaños (tan, muy...), distancias (desde, hasta...), cantidades (muchos, poco, aquellas...),preguntas o exclamaciones (qué, porque...), onomatopeyas (uf) e incluso algunos verbos como: había, era, son. 
        En síntesis de lo anterior, estas decisiones tomadas me permitía que el resultado final en la imagen, las palabras con mayor frecuencia sean por ejemplo "marido" que tiene una frecuencia de 11 repeticiones o "carne" con 23 y así con el resto de palabras en el wordcloud lo que nos permite ir teniendo una aproximación más clara respecto al contenido del texto a partir de ellas, que del contrario, si no se hubiera hecho la depuración terminarían siendo resaltadas palabras más generales y con poco valor significativo respecto del texto.
        """
        st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_7}</div>", unsafe_allow_html=True)
    
        col1, col2, col3 = st.columns([1, 7, 1])
        with col2:
            st.image("wordcloud_anapaula.png", width=800)

        st.subheader("📊 Nube de palabras Milagros")
        texto_7 = """
        Esta nube de palabras muestra los términos que aparecen con mayor frecuencia en el texto, destacando en mayor tamaño palabras clave como gente, todo, pasado, tiempo y yo. 
        El vocabulario refleja una narración introspectiva en primera persona centrada en la memoria, el recuerdo y la reflexión sobre las personas y el paso del tiempo, 
        e incluye nombres propios como Juan, Pablo, Castel, Iribarne y María (que corresponden a los personajes de la novela El túnel de Ernesto Sabato) junto con términos como pintor, mató y verdad
        """
        st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_7}</div>", unsafe_allow_html=True)
    
        col1, col2, col3 = st.columns([1, 7, 1])
        with col2:
            st.image("wordcloud_milagros.png", width=800)
    
    else:
        st.subheader("🗺️ Mapa de Anapaula: Distribución geográfica")
        texto_8 = """
        Para desarrollar el mapa interactivo se utilizó la librería Folium. 
        Los datos sobre los pilotos los organicé en un diccionario anidado, uno mismo para ambos pilotos. Como base utilicé StreetMap, en ella empleé marcadores para los pilotos. 
        Primero escogí corazones pero luego opté por carros para el marcador de ambos pues era la aplicación más acertada. 
        Para la ventana emergente elaboré un popup que da información sobre el nombre, escudería y el puntaje del piloto seleccionado así como una fotografía obtenida mediante URL que fue ajustada en tamaño para que sea visible y proporcional. 
        Finalmente, utilicé dos colores distintos para cada marcador, basandome en dos colores complementarios directos: verde y rosado.
        """
        st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_8}</div>", unsafe_allow_html=True)
            
        with open("mapa_anapaula.html", "r", encoding="utf-8") as mapa:
                html_content = mapa.read()
    
        components.html(html_content,height=600)

        
        st.subheader("🗺️ Mapa de Milagros: Distribución geográfica")
        texto_8 = """
        Interpretación del mapa
        """
        st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_8}</div>", unsafe_allow_html=True)
            
        with open("mapa_milagros.html", "r", encoding="utf-8") as mapa:
                html_content = mapa.read()
    
        components.html(html_content,height=600)
