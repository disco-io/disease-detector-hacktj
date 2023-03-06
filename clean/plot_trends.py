def graph_trends(symptom, areaCode):
  from pytrends.request import TrendReq
  import matplotlib.pyplot as plt

  # Create pytrends object and specify region and time period
  pytrends = TrendReq(hl='en-US', tz=360)
  pytrends.build_payload(kw_list=[symptom], timeframe='today 5-y',  geo='US-VA-' + str(areaCode))

  # Request data and extract values
  data = pytrends.interest_over_time().values[:, 0]

  # Plot data using matplotlib
  plt.plot(range(len(data)), data)
  plt.xlabel('Week')
  plt.ylabel('Search Trend')
  plt.title('Google Search Trend for ' + symptom)
  plt.show()

graph_trends("cough", 757)
