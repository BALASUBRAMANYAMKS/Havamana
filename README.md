# 🌤️ HAVAMANA Weather Dashboard

A modern, responsive Django-based weather dashboard that provides real-time weather information, forecasts, and dynamic backgrounds for any city worldwide.

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Django](https://img.shields.io/badge/Django-5.2.5-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

## ✨ Features

- 🔍 **Real-time Weather Search** - Search weather by city name with accurate timezone display
- 🌡️ **Comprehensive Weather Data** - Temperature, humidity, wind speed, pressure, visibility, and more
- 📊 **Interactive Charts** - Visual trends for temperature, humidity, wind, and rainfall using Chart.js
- 📅 **5-Day Forecast** - Detailed weather predictions with hourly breakdowns
- 🖼️ **Dynamic Backgrounds** - Beautiful city landmarks and weather-based backgrounds via Unsplash API
- 📍 **Location Detection** - Automatic user location detection with reverse geocoding
- 📱 **Responsive Design** - Works seamlessly on desktop, tablet, and mobile devices
- 🌍 **Global Support** - Weather data for cities worldwide

## 🚀 Demo

<img width="1885" height="895" alt="Screenshot 2025-10-30 121703" src="https://github.com/user-attachments/assets/d29859a1-1f33-4df7-b9ea-d1c1310cf501" />
<img width="1906" height="916" alt="Screenshot 2025-10-30 121719" src="https://github.com/user-attachments/assets/aead24f6-a14c-4048-b7c1-a350a27b1b9e" />
<img width="1882" height="809" alt="Screenshot 2025-10-30 121738" src="https://github.com/user-attachments/assets/e7381a2c-b4a7-4195-b722-f68677d1029f" />


*Real-time weather dashboard with interactive charts and dynamic backgrounds*

## 🛠️ Technologies Used

- **Backend**: Django 5.2.5
- **Language**: Python 3.12
- **APIs**: 
  - OpenWeatherMap API (Weather Data)
  - Unsplash API (Background Images)
- **Frontend**: 
  - HTML5, CSS3, JavaScript
  - Chart.js (Data Visualization)
  - Font Awesome (Icons)
- **Environment Management**: python-dotenv

## 📋 Prerequisites

- Python 3.12 or higher
- pip (Python package manager)
- OpenWeatherMap API key ([Get it here](https://openweathermap.org/api))
- Unsplash API key - Optional ([Get it here](https://unsplash.com/developers))

## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/havamana-weather-dashboard.git
cd havamana-weather-dashboard/weather_dashboard
```

### 2. Create and activate virtual environment
**Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**Linux/MacOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install django requests python-dotenv
```

Or if you have a requirements.txt:
```bash
pip install -r requirements.txt
```

### 4. Configure environment variables
Create a `.env` file in the `weather_dashboard/` directory:

```env
# OpenWeatherMap API Key (Required)
API_KEY=your_openweathermap_api_key_here

# Unsplash API Key (Optional - for enhanced backgrounds)
UNSPLASH_ACCESS_KEY=your_unsplash_api_key_here
```

**Note**: Never commit your `.env` file to version control!

### 5. Run the development server
```bash
python manage.py runserver
```

### 6. Access the application
Open your browser and navigate to:
```
http://127.0.0.1:8000/
```

## 📁 Project Structure

```
weather_dashboard/
├── HAVAMANA/                   # Main Django application
│   ├── templates/
│   │   └── havamana/
│   │       ├── dashboard.html  # Main dashboard template
│   │       └── search.html     # Search page
│   ├── views.py               # Weather logic & API integration
│   ├── urls.py                # URL routing
│   ├── admin.py               # Admin configuration
│   └── models.py              # Data models
├── weather_dashboard/         # Django project settings
│   ├── settings.py           # Main configuration
│   ├── urls.py               # Project URL routing
│   └── wsgi.py               # WSGI configuration
├── .env                      # Environment variables (not in repo)
├── .gitignore               # Git ignore rules
├── manage.py                # Django management script
└── README.md                # This file
```

## 🎯 Usage

1. **Search for a City**: Enter any city name in the search bar
2. **View Current Weather**: See real-time temperature, humidity, wind, and more
3. **Explore Charts**: Interactive graphs show weather trends over 24 hours
4. **Check Forecast**: View detailed 5-day weather predictions
5. **Enjoy Dynamic Backgrounds**: Background changes based on city landmarks or weather conditions

## 🔑 API Keys Setup

### OpenWeatherMap API (Required)
1. Visit [OpenWeatherMap](https://openweathermap.org/api)
2. Sign up for a free account
3. Generate an API key from your dashboard
4. Add it to your `.env` file

### Unsplash API (Optional)
1. Visit [Unsplash Developers](https://unsplash.com/developers)
2. Create a new application
3. Copy your Access Key
4. Add it to your `.env` file

## 👨‍💻 Author

Balasubramanyam K S 
- GitHub: https://github.com/BALASUBRAMANYAMKS
- LinkedIn: www.linkedin.com/in/ksb2003

## 🙏 Acknowledgments

- [OpenWeatherMap](https://openweathermap.org/) for weather data API
- [Unsplash](https://unsplash.com/) for beautiful background images
- [Chart.js](https://www.chartjs.org/) for data visualization
- [Django](https://www.djangoproject.com/) framework




