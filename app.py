import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
import importlib
import inspect

# 动态导入utils模块
utils = importlib.import_module('disc6.utils')

# 获取utils模块中的所有函数
functions = {name: func for name, func in inspect.getmembers(utils, inspect.isfunction)}

app = dash.Dash(__name__, suppress_callback_exceptions=True)

app.layout = html.Div([
    html.H1('天文学工具箱'),
    dcc.Dropdown(
        id='function-dropdown',
        options=[{'label': name, 'value': name} for name in functions.keys()],
        value='parallax',
        style={'width': '50%'}
    ),
    html.Div(id='input-container'),
    html.Button('计算', id='calculate-button', n_clicks=0),
    html.Div(id='output')
])

@app.callback(
    Output('input-container', 'children'),
    Input('function-dropdown', 'value')
)
def update_input(selected_function):
    func = functions[selected_function]
    params = inspect.signature(func).parameters
    return [
        html.Div([
            html.Label(f'{param}: '),
            dcc.Input(id={'type': 'dynamic-input', 'index': param}, type='number', placeholder=f'输入 {param}')
        ]) for param in params
    ]

@app.callback(
    Output('output', 'children'),
    Input('calculate-button', 'n_clicks'),
    State('function-dropdown', 'value'),
    State({'type': 'dynamic-input', 'index': dash.ALL}, 'value')
)
def update_output(n_clicks, selected_function, args):
    if n_clicks > 0:
        func = functions[selected_function]
        try:
            # 过滤掉None值,并将字符串转换为浮点数
            args = [float(arg) for arg in args if arg is not None]
            result = func(*args)
            if isinstance(result, dict):
                return html.Div([
                    html.P(f"{selected_function} 的结果是:"),
                    html.Ul([html.Li(f"{k}: {utils.format_distance(v)}") for k, v in result.items()])
                ])
            else:
                return f'{selected_function} 的结果是: {result}'
        except Exception as e:
            return f'错误: {str(e)}'
    return '请点击计算按钮'

if __name__ == '__main__':
    app.run_server(debug=True)
