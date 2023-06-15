# Importing the yfinance package
import yfinance as yf
from datetime import date

#
# Este metodo retorna un pandas dataframe con datos economicos relacionados
# con un 'stock' (e.g. GOOGL, AMZN) entre una fecha inicial (sd) y una fecha
# final (ed). Las fechas pueden estar en formato 'YYYY-MM-DD'.
#
# sd: fecha inicial
# stock: nombre código de la acción
# ed: fecha final. En caso que el usuario no lo indique, se tomara la fecha 
# del dia de hoy
#

def get_stock_data(sd, stock, ed):
    return yf.download(stock, sd, ed)

def test(ticker = 'GOOGL', start_date = '2020-01-01', end_date = date.today()):
    return get_stock_data(start_date,ticker, end_date)

