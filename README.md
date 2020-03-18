# Fullstack Demo
This is our task for potential new fullstack engineers. We expect this task to take less than two hours of work

Please fork this repo and make a starting commit with the message 'start'.
Commit your finished code and push to your forked repo when you are finished. Thanks 😄

## TODO

Implement a simple flask web app that serves html.

If you are unfamiliar with flask the documentation can be found here

https://flask.palletsprojects.com/en/1.1.x/#user-s-guide

but the flask boilerplate is provided to you in this demo. Please add your service code in the @app.route('/') endpoint in app.py. The HTML should be added to templates/demo.html.

Any new dependencies should be added to requirements.txt

To run the service please cd into your local repo directory and run:
```
pip install -r requirements.txt
export FLASK_APP=app.py
python -m flask run
```

The service will be running at http://127.0.0.1:5000/.

If your solution requires additional steps to run, please ensure to update the instructions above in the repo you provide as your solution.

**Step 1**

The app should load a form with the following fields
- City string input
- Checkin string input
- Checkout string input
- submit button

The 3 inputs will be string inputs. Do not worry about form validation and or any styling.

**Step 2**

When the form is submitted make **2 HTTP POST requests** in parallel to 'https://experimentation.snaptravel.com/interview/hotels' with the following request body

```
{
  city : city_string_input,
  checkin : checkin_string_input,
  checkout : checkout_string_input,
  provider : 'snaptravel'
}
```

1) The above returns SnapTravel rates for hotels in the city

```
{
  city : city_string_input,
  checkin : checkin_string_input,
  checkout : checkout_string_input,
  provider : 'retail'
}
```

2) The above returns Hotels.com rates for hotels in the city

The responses will be in json and each response will have an array of hotels and prices.
```
[{
  id : 12,
  hotel_name : 'Center Hilton',
  num_reviews : 209,
  address : '12 Wall Street, Very Large City',
  num_stars : 4,
  amenities : ['Wi-Fi', 'Parking'],
  image_url : 'https://images.trvl-media.com/hotels/1000000/20000/19600/19558/19558_410_b.jpg',
  price : 132.11
},
...
]
```

Make sure to cache these responses in the server (assume the endpoint is expensive to call) in whatever way that seems fit using whatever cache that seems fit (db, redis, in memory etc)

**Step 3**

After both these calls have returned take **only** the hotels that appear in both the responses and return an html table with the data. (you can display the data in anyway you wish as long as the data is in a table with a row for each entry)

For example, if the first call returned hotels with id [10,12] with SnapTravel prices 192.34 and 112.33 and the second call returned hotels [12,13] with Hotels.com prices 132.11 and 321.62 respectively, you would only render hotel 12 in the list with a SnapTravel price of 112.33 and a Hotels.com price of 132.11

![](https://i.imgur.com/fqT65hx.png)

## Notes
* If you run into any technical difficulties contact brett@snaptravel.com
* If you wish to write tests you can but it is not a strict requirement.
