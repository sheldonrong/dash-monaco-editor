import code_editor
import dash
from dash.dependencies import Input, Output
import dash_html_components as html

app = dash.Dash(__name__)

app.layout = html.Div([
    code_editor.CodeEditor(
        id='my-code-edit',
        value='my-value',
        label='my-label',
        language='javascript',
        theme='vs-dark',
        height='80vh',
        width='100vh'
    ),
    html.Div(id='output')
])


@app.callback(Output('output', 'children'), [Input('my-code-edit', 'value')])
def display_output(value):
    return 'You have entered {}'.format(value)


if __name__ == '__main__':
    app.run_server(debug=True)
