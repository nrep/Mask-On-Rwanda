from flask import Flask, render_template
# import pandas as pd

app = Flask(__name__)

""" url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/03-25-2020.csv'
df = pd.read_csv(url, index_col=0)
rwanda = df.query('Country_Region == "Rwanda"')
rw_confirmed = rwanda['Confirmed'].values.tolist()
rw_recovered = rwanda['Recovered'].values.tolist()
rw_deaths = rwanda['Deaths'].values.tolist()
rw_active = rwanda['Active'].values.tolist() """

SITE_NAME = 'MaskOnRwanda'
SITE_MOTTO = 'Daily Rwanda COVID-19 Updates'

@app.route('/')
def hello_world():
    # return render_template("index.html", confirmed = rw_confirmed[0])
    return render_template("index.html", data = { 'title' : SITE_NAME, 'site_name' : SITE_NAME, 'sub_title' : SITE_MOTTO })