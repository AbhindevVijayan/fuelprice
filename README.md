⛽ Fuel Price Route Optimizer (Django + React)
*****************📌 Overview*****************

This project is a full-stack fuel optimization system that calculates an optimal driving route between two locations in the USA and suggests cost-effective fuel stops along the journey.
It uses real-world routing data and a fuel price dataset to minimize total fuel cost while respecting vehicle constraints.

*******🚀 Features********

🌍 Get route between any two US locations
🛣️ Real-world routing using OpenRouteService API
⛽ Smart fuel stop planning based on:
Fuel price optimization
Vehicle range (500 miles)
Fuel efficiency (10 MPG)
💰 Total fuel cost estimation
🗺️ Route geometry (polyline) returned for map rendering
⚡ Fast API response (single routing API call)

*******🏗️ Tech Stack**********
Backend
Django 6
Django REST Framework
Python 3.12
OpenRouteService API
Pandas (fuel dataset processing)
Polyline decoding
Frontend
React (Vite)
Axios
Modern UI components

***************************************************************************
*                                                                         *
*                           📂 Project Structure                          *
*                                                                         *
* *************************************************************************   

fuelplanner/
│
├── api/
│   ├── services/
│   │   ├── geo.py
│   │   ├── routing.py
│   │   ├── route_optimizer.py
│   │   ├── fuel.py
│   │   └── fuel_prices.csv
│   │
│   ├── views.py
│   ├── urls.py
│
├── frontend/
│   ├── src/
│   ├── components/
│   └── api/
│
├── fuelplanner/
├── manage.py



*****🔧 API Endpoint********
📍 Calculate Route & Fuel Plan

POST
    /api/route-fuel-plan/

Request Body:
       {
  "start": "New York, USA",
  "end": "Los Angeles, USA"
}
Response:
       {
  "start": "New York, USA",
  "end": "Los Angeles, USA",
  "distance_miles": 2793.85,
  "route_map": "encoded_polyline_string",
  "fuel_stops": [
    {
      "location": "Texas, TX",
      "station": "7-ELEVEN #218",
      "price_per_gallon": 2.69,
      "gallons": 50,
      "cost": 134.5
    }
  ],
  "total_fuel_cost": 812.45
}



**********Algorithm Logic*************
Get start and end coordinates using geocoding
Fetch route using OpenRouteService API
Decode route polyline into coordinate path
Divide route into segments based on:
Max vehicle range = 500 miles
At each stop:
Filter fuel stations by region
Select lowest-cost fuel station available
Compute:
Fuel required per segment (500 miles / 10 MPG)
Cost per stop
Total trip fuel cost



***********Constraints Assumed************
Vehicle range: 500 miles
Fuel efficiency: 10 MPG
Fuel stops are selected based on:
Route progression
Regional availability
Lowest fuel price preference


*********Performance Considerations**************
Only one routing API call per request
Fuel stop calculation is local (fast)
No repeated external API calls
Efficient pandas sorting for station lookup





********How to Run*******
Backend
  pip install -r requirements.txt
  python manage.py runserver

Frontend
  cd frontend
  npm install
  npm run dev


👨‍💻 Author
Abhindev Vijayan




