import requests
import os
from flask import Flask, Response, request
import json
app = Flask(__name__)
from datetime import datetime
from global_portfolio import GlobalPortfolio

gp = GlobalPortfolio()


@app.route('/api/get-global-portfolio')
def get_global_portflio():

    mode = request.args.get('mode')
    if mode not in ['value', 'porcentaje']:
        return Response("missing query parameter 'mode' in ['value', 'porcentaje']", status=400, mimetype='application/json')

    month = request.args.get('month') or datetime.now().month
    year = request.args.get('year') or datetime.now().year

    holdings = gp.compute_global_holdings(mode='value', month=month, year=year)

    return Response(json.dumps(holdings), status=200, mimetype='application/json')


if __name__ == '__main__':

    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=True)
    # app.run(host='127.0.0.1', port=5000, debug=True)

