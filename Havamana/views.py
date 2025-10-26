from django.http import HttpResponseRedirect
def search(request):
    return render(request, 'havamana/search.html')

from django.shortcuts import render
from django.conf import settings
import requests

def get_city_landmark_query(city_name):
    """
    Generate search queries for famous landmarks and tourist spots of a city
    """
    city = city_name.lower().strip()
    
    # Famous landmarks and attractions mapping
    city_landmarks = {
        'paris': ['eiffel tower', 'louvre museum', 'notre dame paris', 'champs elysees'],
        'london': ['big ben', 'tower bridge', 'london eye', 'buckingham palace'],
        'new york': ['statue of liberty', 'times square', 'central park', 'brooklyn bridge'],
        'tokyo': ['tokyo tower', 'shibuya crossing', 'mount fuji tokyo', 'cherry blossom tokyo'],
        'rome': ['colosseum', 'vatican city', 'trevi fountain', 'pantheon rome'],
        'dubai': ['burj khalifa', 'palm jumeirah', 'burj al arab', 'dubai marina'],
        'mumbai': ['gateway of india', 'marine drive mumbai', 'taj hotel mumbai', 'mumbai skyline'],
        'delhi': ['red fort', 'india gate', 'lotus temple delhi', 'qutub minar'],
        'bangalore': ['lalbagh garden', 'bangalore palace', 'vidhana soudha', 'cubbon park'],
        'chennai': ['marina beach', 'kapaleeshwarar temple', 'fort st george chennai', 'chennai skyline'],
        'kolkata': ['victoria memorial', 'howrah bridge', 'dakshineswar temple', 'park street kolkata'],
        'hyderabad': ['charminar', 'golconda fort', 'hussain sagar lake', 'ramoji film city'],
        'pune': ['shaniwar wada', 'aga khan palace', 'sinhagad fort', 'pune university'],
        'ahmedabad': ['sabarmati ashram', 'akshardham ahmedabad', 'kankaria lake', 'sidi saiyyed mosque'],
        'jaipur': ['hawa mahal', 'amber fort', 'city palace jaipur', 'jantar mantar jaipur'],
        'goa': ['baga beach', 'basilica of bom jesus', 'dudhsagar falls', 'anjuna beach'],
        'kochi': ['chinese fishing nets', 'mattancherry palace', 'fort kochi', 'backwaters kerala'],
        'sydney': ['sydney opera house', 'harbour bridge', 'bondi beach', 'circular quay'],
        'melbourne': ['federation square', 'flinders street station', 'royal botanic gardens melbourne', 'eureka tower'],
        'singapore': ['marina bay sands', 'merlion singapore', 'gardens by the bay', 'singapore flyer'],
    }
    
    # Check if city has specific landmarks
    if city in city_landmarks:
        # Return the first landmark for primary search
        return city_landmarks[city][0]
    
    # For other cities, use generic landmark search terms
    landmark_terms = ['landmark', 'tourist attraction', 'famous spot', 'architecture', 'skyline', 'monument']
    return f"{city_name} {landmark_terms[0]}"

def get_static_landmark_image(city_name):
    """
    Get static landmark images as fallback when Unsplash API is not available
    """
    city = city_name.lower().strip()
    
    # Static landmark images (royalty-free/public domain)
    static_landmarks = {
        'paris': 'https://images.unsplash.com/photo-1511739001486-6bfe10ce785f?auto=format&fit=crop&w=1500&q=80',  # Eiffel Tower
        'london': 'https://images.unsplash.com/photo-1513635269975-59663e0ac1ad?auto=format&fit=crop&w=1500&q=80',  # Big Ben
        'new york': 'https://images.unsplash.com/photo-1496442226666-8d4d0e62e6e9?auto=format&fit=crop&w=1500&q=80',  # NYC Skyline
        'tokyo': 'https://images.unsplash.com/photo-1540959733332-eab4deabeeaf?auto=format&fit=crop&w=1500&q=80',  # Tokyo Tower
        'rome': 'https://images.unsplash.com/photo-1552832230-c0197dd311b5?auto=format&fit=crop&w=1500&q=80',  # Colosseum
        'dubai': 'https://images.unsplash.com/photo-1512453979798-5ea266f8880c?auto=format&fit=crop&w=1500&q=80',  # Burj Khalifa
        'mumbai': 'https://images.unsplash.com/photo-1567157577867-05ccb1388e66?auto=format&fit=crop&w=1500&q=80',  # Gateway of India
        'delhi': 'https://images.unsplash.com/photo-1587474260584-136574528414?auto=format&fit=crop&w=1500&q=80',  # India Gate
        'sydney': 'https://images.unsplash.com/photo-1506905925346-21bda4d32df4?auto=format&fit=crop&w=1500&q=80',  # Sydney Opera House
        'singapore': 'https://images.unsplash.com/photo-1525625293386-3f8f99389edd?auto=format&fit=crop&w=1500&q=80',  # Marina Bay
    }
    
    return static_landmarks.get(city, None)

def get_weather_background_query(weather_condition, description):
    """
    Map weather conditions to appropriate Unsplash search terms for dynamic backgrounds
    """
    weather_condition = weather_condition.lower()
    description = description.lower()
    
    # Weather condition mapping for background images
    weather_backgrounds = {
        'clear': ['sunny day', 'blue sky', 'sunshine', 'clear weather'],
        'clouds': ['cloudy sky', 'overcast', 'dramatic clouds', 'grey clouds'],
        'rain': ['rain drops', 'rainy weather', 'storm clouds', 'rainfall'],
        'drizzle': ['light rain', 'drizzle', 'misty rain', 'wet weather'],
        'thunderstorm': ['lightning storm', 'dark storm clouds', 'thunderstorm', 'dramatic weather'],
        'snow': ['snowfall', 'winter snow', 'snowy landscape', 'white snow'],
        'mist': ['foggy morning', 'misty weather', 'fog', 'hazy sky'],
        'fog': ['dense fog', 'foggy landscape', 'misty morning', 'fog weather'],
        'haze': ['hazy sky', 'atmospheric haze', 'dusty sky', 'smoggy weather']
    }
    
    # Check specific descriptions for more accurate mapping
    if 'clear' in description and 'sky' in description:
        return 'sunny blue sky clear weather'
    elif 'few clouds' in description or 'scattered clouds' in description:
        return 'partly cloudy sky few clouds'
    elif 'broken clouds' in description or 'overcast' in description:
        return 'overcast cloudy dramatic sky'
    elif 'heavy' in description and 'rain' in description:
        return 'heavy rain storm dark clouds'
    elif 'light rain' in description:
        return 'light rain drizzle gentle weather'
    elif 'snow' in description:
        return 'beautiful snowfall winter landscape'
    elif 'thunder' in description or 'lightning' in description:
        return 'lightning storm dramatic dark clouds'
    elif 'mist' in description or 'fog' in description:
        return 'misty foggy atmospheric weather'
    
    # Default mapping based on main weather condition
    if weather_condition in weather_backgrounds:
        return ' '.join(weather_backgrounds[weather_condition][:2])  # Use first 2 terms
    
    # Fallback to generic weather search
    return f"{weather_condition} weather atmosphere"

def get_weather(request):
    import datetime
    api_key = settings.API_KEY
    city = request.GET.get('city')
    if not city:
        return HttpResponseRedirect('/')
    
    # Debug: Print the city being searched
    print(f"DEBUG: Searching weather for city: {city}")
    
    context = {}
    
    # Current weather - Get this first to extract weather condition
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}"
    print(f"DEBUG: Weather API URL: {url}")
    
    response = requests.get(url)
    data = response.json() if response.status_code == 200 else {}
    
    # Debug: Print response status and basic data
    print(f"DEBUG: Weather API response status: {response.status_code}")
    if response.status_code == 200 and data:
        print(f"DEBUG: Weather data for {data.get('name', 'Unknown')}: {data.get('main', {}).get('temp', 'N/A')}°C")
    else:
        print(f"DEBUG: Weather API error or no data: {data}")
    
    # Enhanced background image system with fallbacks
    unsplash_access_key = getattr(settings, 'UNSPLASH_ACCESS_KEY', None)
    landmark_image_url = None
    city_image_url = None
    weather_image_url = None
    
    print(f"DEBUG: Unsplash API key available: {'Yes' if unsplash_access_key else 'No'}")
    
    # Try static landmark images first (works without API key)
    static_landmark_url = get_static_landmark_image(city)
    if static_landmark_url:
        landmark_image_url = static_landmark_url
        print(f"DEBUG: Using static landmark image for {city}")
    
    if unsplash_access_key:
        # Priority 1: Try to get better landmark images from Unsplash
        landmark_query = get_city_landmark_query(city)
        print(f"DEBUG: Landmark search query: {landmark_query}")
        
        landmark_unsplash_url = f"https://api.unsplash.com/photos/random?query={landmark_query}&client_id={unsplash_access_key}&orientation=landscape"
        print(f"DEBUG: Landmark API URL: {landmark_unsplash_url}")
        
        try:
            landmark_img_resp = requests.get(landmark_unsplash_url, timeout=5)
            print(f"DEBUG: Landmark API response status: {landmark_img_resp.status_code}")
            
            if landmark_img_resp.status_code == 200:
                landmark_img_data = landmark_img_resp.json()
                unsplash_landmark_url = landmark_img_data.get('urls', {}).get('regular')
                if unsplash_landmark_url:
                    landmark_image_url = unsplash_landmark_url  # Override static with dynamic
                    print(f"DEBUG: Dynamic landmark image obtained from Unsplash")
            else:
                print(f"DEBUG: Landmark API error: {landmark_img_resp.status_code}")
        except requests.RequestException as e:
            print(f"DEBUG: Landmark API request failed: {e}")
        
        # Priority 2: General city search as fallback
        city_unsplash_url = f"https://api.unsplash.com/photos/random?query={city} city architecture&client_id={unsplash_access_key}&orientation=landscape"
        try:
            city_img_resp = requests.get(city_unsplash_url, timeout=5)
            print(f"DEBUG: City API response status: {city_img_resp.status_code}")
            
            if city_img_resp.status_code == 200:
                city_img_data = city_img_resp.json()
                city_image_url = city_img_data.get('urls', {}).get('regular')
                print(f"DEBUG: City image URL obtained: {'Yes' if city_image_url else 'No'}")
            else:
                print(f"DEBUG: City API error: {city_img_resp.status_code}")
        except requests.RequestException as e:
            print(f"DEBUG: City API request failed: {e}")
    else:
        print("DEBUG: No Unsplash API key - using static landmark images only")
        
        # Priority 3: Weather-based backgrounds as final option
        if response.status_code == 200 and 'weather' in data and data['weather']:
            weather_main = data['weather'][0].get('main', 'clear')
            weather_desc = data['weather'][0].get('description', 'clear sky')
            
            # Get weather-specific search query
            weather_query = get_weather_background_query(weather_main, weather_desc)
            
            # Search for weather-appropriate background
            weather_unsplash_url = f"https://api.unsplash.com/photos/random?query={weather_query}&client_id={unsplash_access_key}&orientation=landscape"
            weather_img_resp = requests.get(weather_unsplash_url)
            
            if weather_img_resp.status_code == 200:
                weather_img_data = weather_img_resp.json()
                weather_image_url = weather_img_data.get('urls', {}).get('regular')
    
    # Priority order: Landmarks > City > Weather > Default
    final_background_url = landmark_image_url or city_image_url or weather_image_url
    
    # Forecast for graph
    forecast_url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&units=metric&appid={api_key}"
    print(f"DEBUG: Forecast API URL: {forecast_url}")
    
    forecast_resp = requests.get(forecast_url)
    forecast_data = forecast_resp.json() if forecast_resp.status_code == 200 else {}
    
    print(f"DEBUG: Forecast API response status: {forecast_resp.status_code}")
    if forecast_resp.status_code == 200 and forecast_data:
        print(f"DEBUG: Forecast data available for {forecast_data.get('city', {}).get('name', 'Unknown')}")
    else:
        print(f"DEBUG: Forecast API error: {forecast_data}")

    if response.status_code == 200 and 'main' in data and 'weather' in data:
        # Wind
        wind_speed = data.get('wind', {}).get('speed', 'N/A')
        wind_deg = data.get('wind', {}).get('deg', 'N/A')
        # Rain
        rain_1h = data.get('rain', {}).get('1h', 0)
        rain_3h = data.get('rain', {}).get('3h', 0)
        # Sun times and city local time calculation
        sunrise = data.get('sys', {}).get('sunrise')
        sunset = data.get('sys', {}).get('sunset')
        timezone_offset = data.get('timezone', 0)  # Timezone offset in seconds from UTC
        
        # Format times with city's timezone
        def format_time_with_timezone(ts, tz_offset):
            if ts:
                # Convert UTC timestamp to city's local time
                utc_time = datetime.datetime.utcfromtimestamp(ts)
                local_time = utc_time + datetime.timedelta(seconds=tz_offset)
                return local_time.strftime('%H:%M')
            return 'N/A'
        
        def format_time(ts):
            if ts:
                return datetime.datetime.fromtimestamp(ts).strftime('%H:%M')
            return 'N/A'
            
        sunrise_fmt = format_time_with_timezone(sunrise, timezone_offset)
        sunset_fmt = format_time_with_timezone(sunset, timezone_offset)
        
        # Calculate current time in the city's timezone
        utc_now = datetime.datetime.utcnow()
        city_current_time = utc_now + datetime.timedelta(seconds=timezone_offset)
        current_time = city_current_time.strftime('%H:%M')
        
        print(f"DEBUG: City timezone offset: {timezone_offset} seconds ({timezone_offset/3600} hours)")
        print(f"DEBUG: City current time: {current_time}")
        # Expected rain (next forecast)
        expected_rain = 'N/A'
        if 'list' in forecast_data and forecast_data['list']:
            for item in forecast_data['list']:
                if 'rain' in item and '3h' in item['rain']:
                    expected_rain = item['rain']['3h']
                    break
        # Graph data (next 8 forecast points, 24h)
        chart_labels = []
        chart_temps = []
        chart_humidity = []
        chart_wind = []
        chart_rain = []
        hourly_forecast = []
        daily_forecast = []
        if 'list' in forecast_data:
            for item in forecast_data['list'][:8]:
                chart_labels.append(item['dt_txt'][11:16])
                chart_temps.append(item['main']['temp'])
                chart_humidity.append(item['main']['humidity'])
                chart_wind.append(item['wind']['speed'])
                chart_rain.append(item.get('rain', {}).get('3h', 0))
                hourly_forecast.append({
                    'time': item['dt_txt'][11:16],
                    'temp': item['main']['temp'],
                    'desc': item['weather'][0]['description'] if item['weather'] else ''
                })
            # Daily forecast (group by day)
            days = {}
            for item in forecast_data['list']:
                day = item['dt_txt'][:10]
                if day not in days:
                    days[day] = {'temps': [], 'descs': []}
                days[day]['temps'].append(item['main']['temp'])
                days[day]['descs'].append(item['weather'][0]['description'] if item['weather'] else '')
            for day, vals in list(days.items())[:5]:
                avg_temp = round(sum(vals['temps'])/len(vals['temps']), 1)
                main_desc = max(set(vals['descs']), key=vals['descs'].count)
                daily_forecast.append({'date': day, 'temp': avg_temp, 'desc': main_desc})
    if response.status_code == 200 and 'main' in data and 'weather' in data:
        # Extract weather info for fallback handling
        weather_main = data['weather'][0].get('main', 'Clear').lower() if data['weather'] else 'clear'
        weather_description = data['weather'][0].get('description', 'clear sky') if data['weather'] else 'clear sky'
        
        # Get actual city name from API response (more accurate than input)
        actual_city_name = data.get('name', city)
        country_code = data.get('sys', {}).get('country', '')
        city_display_name = f"{actual_city_name}, {country_code}" if country_code else actual_city_name
        
        # Calculate timezone display
        tz_hours = timezone_offset / 3600
        tz_display = f"UTC{'+' if tz_hours >= 0 else ''}{tz_hours:g}"
        
        context = {
            'city': city,  # Keep original for form/URL
            'city_name': actual_city_name,  # Actual city name from API
            'city_display': city_display_name,  # City with country code
            'timezone_display': tz_display,  # Timezone info
            'temp': data['main'].get('temp', 'N/A'),
            'feels_like': data['main'].get('feels_like', 'N/A'),
            'temp_min': data['main'].get('temp_min', 'N/A'),
            'temp_max': data['main'].get('temp_max', 'N/A'),
            'pressure': data['main'].get('pressure', 'N/A'),
            'visibility': data.get('visibility', 'N/A'),
            'clouds': data.get('clouds', {}).get('all', 'N/A'),
            'humidity': data['main'].get('humidity', 'N/A'),
            'description': weather_description,
            'weather_main': weather_main,  # For CSS fallback logic
            'wind_speed': wind_speed,
            'wind_deg': wind_deg,
            'rain_1h': rain_1h,
            'rain_3h': rain_3h,
            'sunrise': sunrise_fmt,
            'sunset': sunset_fmt,
            'current_time': current_time,
            'expected_rain': expected_rain,
            'chart_labels': chart_labels,
            'chart_temps': chart_temps,
            'chart_humidity': chart_humidity,
            'chart_wind': chart_wind,
            'chart_rain': chart_rain,
            'hourly_forecast': hourly_forecast,
            'daily_forecast': daily_forecast,
            # Background image URLs (ENHANCED FEATURE)
            'city_image_url': final_background_url,  # Primary background (landmarks > city > weather)
            'landmark_image_url': landmark_image_url,  # Famous landmark background
            'city_fallback_url': city_image_url,     # General city background
            'weather_image_url': weather_image_url,  # Weather-specific background
        }
    else:
        context = {
            'error': 'City not found or API error. Please try again.',
            'city': city,
            'city_image_url': final_background_url,
            'weather_main': 'clear',  # Default for CSS fallbacks
            'description': 'clear sky',  # Default for CSS fallbacks
        }
    # Add debugging context for troubleshooting
    context['debug_city'] = city
    context['debug_timestamp'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Render response with cache control headers
    response = render(request, 'havamana/dashboard.html', context)
    response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'
    return response

from django.http import JsonResponse

def reverse_geocode(request):
    """
    API endpoint for reverse geocoding using OpenWeatherMap
    Provides more accurate city names for weather applications
    """
    lat = request.GET.get('lat')
    lon = request.GET.get('lon')
    
    if not lat or not lon:
        return JsonResponse({'error': 'Latitude and longitude required'}, status=400)
    
    try:
        # Use OpenWeatherMap reverse geocoding
        api_key = settings.API_KEY
        url = f'https://api.openweathermap.org/geo/1.0/reverse?lat={lat}&lon={lon}&limit=1&appid={api_key}'
        
        response = requests.get(url)
        data = response.json()
        
        if data and len(data) > 0:
            location = data[0]
            city = location.get('name', '')
            state = location.get('state', '')
            country = location.get('country', '')
            
            # Format the location string
            if state and country:
                full_location = f"{city}, {state}, {country}"
            elif country:
                full_location = f"{city}, {country}"
            else:
                full_location = city
            
            return JsonResponse({
                'city': city,
                'full_location': full_location,
                'state': state,
                'country': country,
                'coordinates': {'lat': lat, 'lon': lon}
            })
        else:
            return JsonResponse({'error': 'Location not found'}, status=404)
            
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


