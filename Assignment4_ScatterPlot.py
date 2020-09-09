import pandas as pd
import plotly
import plotly.figure_factory as f
import plotly.express as px

data = pd.read_csv('DataWeierstrass.csv', delimiter=';')

# Scatter Plot
data['lecture'] = data['lecture'].astype('category')
data['lecture'] = data['lecture'].cat.codes
Image = f.create_scatterplotmatrix(data, index='professor', width=1500, height=1300)
plotly.offline.plot(Image,
                    auto_open=True, image='png', image_filename='ScatterPlot',
                    output_type='file',
                    filename='ScatterPlot', validate=False)
# Parallel Coordinates
data['professor'] = data['professor'].astype('category')
data['professor'] = data['professor'].cat.codes

figure = px.parallel_coordinates(data, color="professor",
                                 dimensions=['professor', 'lecture', 'participants', 'professional expertise',
                                             'motivation', 'clear presentation', 'overall impression'],
                                 color_continuous_scale=px.colors.diverging.Tealrose,
                                 )
figure.show()
