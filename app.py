from flask import Flask, render_template, request
import requests
import json
import pandas as pd

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def hello_world():

  response_1 = None
  response_2 = None

  if request.method == 'POST':
    city = request.form.get('city')
    checkin = request.form.get('checkin')
    checkout = request.form.get('checkout')


    form_body_1 = { 'city': city, 'checkin': checkin, 'checkout': checkout, 'provider': 'snaptravel'}
    form_body_2 = { 'city': city, 'checkin': checkin, 'checkout': checkout, 'provider': 'retail'}


    response_1 = json.loads(requests.post('https://experimentation.snaptravel.com/interview/hotels', json=form_body_1).text)
    response_2= json.loads(requests.post('https://experimentation.snaptravel.com/interview/hotels', json=form_body_2).text)


    # a list
    snaptravel_hotels = response_1['hotels']
    retail_hotels = response_2['hotels']

    common_hotels = []

    for s_hotel in snaptravel_hotels:

      for r_hotel in retail_hotels:

        if s_hotel['id'] == r_hotel['id']:
          hotel = s_hotel
          hotel['snaptravel_price'] = s_hotel['price']
          hotel['amenities'] = tuple(hotel['amenities'])
          hotel['retail_price'] = r_hotel['price'] #retail price can be different from snaptravel price. So add the retail price as well
          del hotel['price'] # don't need this anymore
          common_hotels.append(hotel)
          break


    data_frame = pd.DataFrame(common_hotels)    
    dfg = data_frame.groupby(['id', 'hotel_name', 'num_reviews', 'address', 'num_stars', 'amenities', 'image_url', 'snaptravel_price', 'retail_price']).sum()

    dfg.to_html('templates/result.html')

    return render_template('result.html')




  return render_template('demo.html')