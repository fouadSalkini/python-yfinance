from flask import Flask, request, jsonify
import yfinance as yf

app = Flask(__name__)

@app.route('/currency-rate', methods=['GET'])
def get_currency_rate():

    periods = ['1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max']
    try:
        # Get query parameters from the request
        source = request.args.get('source', 'USD')
        target = request.args.get('target', 'LBP')
        period = request.args.get('period', '1d')

        # Fetch the exchange rate using yfinance
        res = yf.Ticker(f"{source}{target}=X")
        res_data = res.history(period=period)
        data_array = res_data.reset_index().to_dict(orient='records')
        # Extract the last close price, which is the exchange rate
        if not res_data.empty:
            return jsonify({
                'source': source,
                'target': target,
                'period': period,
                'data': data_array,
                'available_periods': periods
            })
        else:
            return jsonify({'error': 'No data found for the given currency pair.', 'data': res_data.to_dict()}), 404
    except Exception as e:
        # Return the error message and a 500 status code (internal server error)
        return jsonify({'error': str(e)}), 500
if __name__ == '__main__':
    app.run(debug=True)