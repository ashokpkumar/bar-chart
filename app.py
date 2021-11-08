from flask import Flask, render_template
from plotly.offline import plot
import plotly.graph_objects as go
app = Flask(__name__)

@app.route('/')
def hello():
    graphs = []
    layout = {
        'title': 'Title of the figure',
        'xaxis_title': 'X',
        'yaxis_title': 'Y',
        'height': 420,
        'width': 560,
        #'paper_bgcolor':'rgb(233,233,233)',
        'plot_bgcolor':'rgb(255,255,255)'
        
    }
    x = ['ABC','DEF','HIJ','XYZ','LMN']
    y4 = ['42','43','42','76','45']
    #y3 = [10*abs(i) for i in x]
    y3 = [-10,-5,0,5,10]
    x2 = [1,2,3,4,5]
    fig = go.Figure(layout=layout)

    fig.add_trace(go.Bar(x=x, y=y3, text = y3,textposition='inside' ,
    marker_color='rgb(0, 102, 204)',showlegend=False
    ))
    fig.add_hline(y=0.0)
    #fig.show()
    # graphs.append(go.Bar(x=x, y=y3, text = y3,textposition='inside' ,
    # marker_color='blue',showlegend=False
    # )   )
    #bar with bar chart
    '''
    graphs.append(go.Bar(x=['ABC','DEF','HIJ','XYZ','LMN'], 
                        y=['0','0','0','0','0'] ,
                        name='Right COl',
                        text = y3,
                        textposition='inside',
                        marker_color='white' )   )
    '''
    

    #graphs.append(go.Scatter(x=x, y=y3,text = y3, name='Line y1')    )
    #graphs.append(go.Line(x=x, y=y4, mode='markers', text = y3,opacity=0.8, marker_size=[abs(y) for y in y3], name='Scatter y2') )
    #bar with scatter chart

    fig.add_trace(go.Scatter(x=x, 
                            y=[0,0,0,0,0], 
                            #mode='markers', 
                            text = y3,
                            textposition='bottom right',
                            textfont=dict(color='#FFFFFF'),
                            #mode='lines+markers+text',
                            mode='markers+text',
                            marker=dict(color='#0000FF', size=1),
                            line=dict(color='#52BCA3', width=1, dash='dash'),
                            showlegend=False,
                           
                           ))

    
   
    
    plot_div = plot({'data': fig, 'layout': layout}, 
                    output_type='div')
 
    return render_template('index.html', plot_div= plot_div)

if __name__ == '__main__':
    app.run(debug=True)