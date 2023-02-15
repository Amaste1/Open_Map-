from ipyleaflet import AntPath, WidgetControl
from ipywidgets import IntSlider, jslink
from ipywidgets import HTML
from ipyleaflet import Map, Marker

m = Map(center=(55.718148, 37.555493), zoom=13)



marathon_path = AntPath(
    locations=[
        [55.717435, 37.561014], [55.712517, 37.569324], [55.712412, 37.569479],
        [55.711333, 37.561858], [55.711344, 37.558516], [55.712049, 37.553513],
        [55.713216, 37.550191], [55.71523, 37.54681], [55.717366, 37.544289],
        [55.719874, 37.542966], [55.721958, 37.542939], [55.723928, 37.543701], 
        [55.725656, 37.545167], [55.7267, 37.546673], [55.727594, 37.54923], 
        [55.727481, 37.549349], [55.727053, 37.547923], [55.726619, 37.546807], 
        [55.724107, 37.549236], [55.723902, 37.549511], [55.720267, 37.5558]
    ],
    dash_array=[1, 10],
    delay=1000,
    color='#9500ff',
    pulse_color='#9500ff'
)

m.add_layer(marathon_path)

start_marker = Marker(location=(55.717435, 37.561014))
m.add_layer(start_marker)

finish_marker = Marker(location=(55.720267, 37.5558))
m.add_layer(finish_marker)

start = HTML()
finish = HTML()
start.value = "Старт"                                                                      
finish.value = "Финиш!"                                                                      
start_marker.popup = start
finish_marker.popup = finish

zoom_slider = IntSlider(description='Масштаб:', min=11, max=15, value=14)
jslink((zoom_slider, 'value'), (m, 'zoom'))
widget_control1 = WidgetControl(widget=zoom_slider, position='topright')
m.add_control(widget_control1)

m