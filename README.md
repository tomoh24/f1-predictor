# F1 Predictor - AI-Powered Formula 1 Race Predictions

A full-stack Formula 1 prediction application that uses data on current team builds, driver stats, and track characteristics to predict race outcomes. This application helps users make educated predictions for F1 Fantasy and provides insights into upcoming Grand Prix events.

## 🏎️ Features

### Homepage
- **Modern, Responsive UI**: Beautiful gradient design with glassmorphism effects
- **Race Grid Layout**: Clean card-based display of upcoming races
- **Quick Actions**: Direct links to qualifying and race predictions for each event
- **Feature Highlights**: Information about AI predictions, fantasy insights, and real-time updates
- **Completed Races**: Dropdown section for viewing past race results and analysis

### Grand Prix Details
- **Comprehensive Race Information**: Date, location, temperatures, lap times, and historical data
- **Track Visualization**: High-quality track images and country flags
- **AI Race Predictions**: Leaderboard-style table with driver rankings, ratings, and probabilities
- **Podium Highlighting**: Visual indicators for predicted top 3 finishers

### Qualifying Predictions
- **Qualifying Format**: Clear explanation of Q1, Q2, and Q3 sessions
- **Performance Predictions**: Expected lap times for each session
- **Strategy Insights**: Track-specific factors affecting qualifying performance
- **Pole Position Probability**: Special highlighting for predicted pole sitter

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- FastAPI
- uvicorn

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd f1-predictor
   ```

2. **Install Python dependencies**
   ```bash
   cd backend/data
   pip install fastapi uvicorn
   ```

3. **Start the backend server**
   ```bash
   python -m uvicorn app:app --reload --host 127.0.0.1 --port 8000
   ```

4. **Open the frontend**
   - Navigate to `frontend/` directory
   - Open `index.html` in your web browser
   - Or serve with a local server (e.g., Live Server extension in VS Code)

## 🏗️ Architecture

### Backend (FastAPI)
- **RESTful API**: Clean endpoints for race data, predictions, and team information
- **CSV Data Sources**: Structured data files for races, teams, drivers, and track information
- **Race-Specific Predictions**: Each race has its own prediction set based on track characteristics
- **ML-Ready Structure**: CSV-based prediction system designed for easy machine learning integration
- **Fallback System**: Automatic fallback to mock data if CSV files are unavailable

### Frontend (HTML/CSS/JavaScript)
- **Modern Design**: Glassmorphism effects, gradients, and smooth animations
- **Responsive Layout**: Works seamlessly on desktop, tablet, and mobile devices
- **Interactive Elements**: Hover effects, smooth transitions, and intuitive navigation
- **Real-time Data**: Dynamic loading of race information and predictions
- **Completed Races**: Interactive dropdown for historical race data

### Data Structure
- **Races**: Comprehensive information about upcoming Grand Prix events
- **Teams**: Current team ratings and performance metrics
- **Drivers**: Driver statistics and team affiliations
- **Race Predictions**: CSV-based system for race-specific predictions
- **Qualifying Predictions**: Separate CSV for qualifying session predictions

## 📊 API Endpoints

- `GET /races/upcoming` - List of upcoming races
- `GET /raceinfo?race={name}` - Detailed race information
- `GET /predictions/{race_id}` - Race-specific predictions from CSV
- `GET /qualifying/{race_id}` - Qualifying predictions from CSV
- `GET /teams` - Team information and ratings
- `GET /drivers` - Driver statistics
- `GET /team-ratings` - Team performance metrics

## 🤖 Machine Learning Integration

### CSV-Based Prediction System
The application uses a structured CSV system that makes it easy for ML models to integrate:

- **`race_predictions.csv`**: Contains race-specific predictions for all Grand Prix events
- **`qualifying_predictions.csv`**: Contains qualifying predictions for all races
- **Automatic Updates**: Frontend automatically reflects changes in CSV files
- **Fallback Protection**: System remains functional even if CSV files are missing

### ML Integration Benefits
- **Simple Interface**: Just update CSV files with new predictions
- **Real-time Updates**: Changes are immediately reflected in the application
- **Track-Specific**: Each race can have completely different predictions
- **Flexible Schema**: Easy to add new prediction fields as needed
- **No Code Changes**: ML models can update predictions without touching the application code

### Quick Start for ML Models
1. Generate predictions in the CSV format
2. Update the prediction files
3. Application automatically serves new predictions
4. No restart or code changes required

For detailed ML integration instructions, see [`docs/ml_integration_guide.md`](docs/ml_integration_guide.md).

## 🎨 Design Features

### Visual Elements
- **F1 Branding**: Official F1 red (#e10600) color scheme
- **Glassmorphism**: Modern translucent card designs with backdrop blur
- **Gradient Backgrounds**: Subtle color transitions for visual appeal
- **Icon Integration**: Font Awesome icons for enhanced user experience

### User Experience
- **Intuitive Navigation**: Clear back buttons and consistent layout
- **Information Hierarchy**: Well-organized sections with logical flow
- **Mobile-First**: Responsive design that works on all devices
- **Performance**: Optimized loading and smooth animations
- **Historical Data**: Easy access to completed races and results

## 🔮 Future Enhancements

### Machine Learning Integration
- **Real-time Predictions**: Live updates based on practice sessions
- **Historical Analysis**: Driver and team performance trends
- **Track-Specific Models**: Specialized algorithms for different circuit types
- **Weather Integration**: Weather-based prediction adjustments
- **Confidence Metrics**: Prediction reliability indicators

### Additional Features
- **User Accounts**: Save favorite predictions and track accuracy
- **Fantasy Integration**: Direct F1 Fantasy platform connections
- **Live Updates**: Real-time race weekend data
- **Social Features**: Share predictions and compare with friends
- **Advanced Analytics**: Detailed performance analysis and trends

### Data Sources
- **Live Telemetry**: Real-time car performance data
- **Weather Integration**: Current and forecasted weather conditions
- **Team Updates**: Latest car upgrades and development news
- **Practice Results**: Integration with practice session data

## 🛠️ Development

### Project Structure
```
f1-predictor/
├── backend/
│   └── data/
│       ├── app.py                    # FastAPI application
│       ├── race_predictions.csv      # Race predictions (ML-ready)
│       ├── qualifying_predictions.csv # Qualifying predictions (ML-ready)
│       ├── *.csv                     # Other data files
│       └── __init__.py
├── frontend/
│   ├── index.html                    # Homepage with completed races
│   ├── grandprix.html                # Race details
│   ├── qualifying.html               # Qualifying predictions
│   ├── styles.css                    # Main stylesheet
│   └── images/                       # Track and flag images
├── docs/
│   ├── roadmap.md                    # Development roadmap
│   └── ml_integration_guide.md       # ML integration guide
└── README.md                         # This file
```

### Contributing
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

### ML Model Development
- Use the CSV structure defined in the ML integration guide
- Test with the fallback system before deploying
- Validate data format and consistency
- Consider track-specific factors in your predictions

## 📱 Browser Support

- Chrome 80+
- Firefox 75+
- Safari 13+
- Edge 80+

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👨‍💻 Author

**tomoh24** - F1 enthusiast and developer

---

*Built with ❤️ for the Formula 1 community*

*Ready for machine learning integration with a simple CSV-based prediction system*
