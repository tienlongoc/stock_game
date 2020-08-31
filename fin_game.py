from urllib import urlopen
from bs4 import BeautifulSoup
from datetime import datetime
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def process_symbol(symbol):
    url = "https://uk.finance.yahoo.com/quote/" + symbol + "/history"

    page = urlopen(url)

    soup = BeautifulSoup(page, "html.parser")

    main_table = soup("table", {"data-test" : "historical-prices"})

    data_lines = main_table[0]("tr")

    close_prices = []
    dates = []

    for i in range(1,len(data_lines)):
        data_points = data_lines[i]("td")
        if len(data_points) > 5:
            close_prices.append(float(data_points[4].string.replace(',','')))
            dates.append(datetime.strptime(data_points[0].string, "%d %b %Y"))

    plt.plot(dates, close_prices)

    fig = plt.gcf()
    fig.suptitle(symbol)
    fig.set_size_inches(18.5, 10.5)
    fig.savefig('data/' + symbol + '.png', dpi=100)
    plt.close()
