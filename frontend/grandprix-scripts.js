// Get race information from URL parameters
        function getRaceInfoFromURL() {
            const params = new URLSearchParams(window.location.search);
            return {
                raceId: params.get('race_id'),
                raceName: params.get('race_name') || 'Unknown Race'
            };
        }

        // Load race information
        async function loadRaceInfo(raceName) {
            try {
                const response = await fetch(`http://127.0.0.1:8000/raceinfo?race=${encodeURIComponent(raceName)}`);
                if (!response.ok) throw new Error("Race info not found");
                
                const data = await response.json();
                
                // Update race information
                document.getElementById('race-location').textContent = data.location;
                document.getElementById('race-date').textContent = data.date;
                document.getElementById('race-avgtemp').textContent = data.avgtemp;
                document.getElementById('race-avgtracktemp').textContent = data.avgtracktemp;
                document.getElementById('race-lastwinner').textContent = data.lastwinner;
                document.getElementById('race-avglaptime').textContent = data.avglaptime;
                document.getElementById('race-recordlaptime').textContent = data.recordlaptime;
                document.getElementById('race-image').src = data.raceimage;
                document.getElementById('race-flag').src = data.flag;
                
            } catch (error) {
                console.error("Error loading race info:", error);
                showError("Could not load race information");
            }
        }

        // Load race predictions
        async function loadRacePredictions(raceId) {
            try {
                const response = await fetch(`http://127.0.0.1:8000/predictions/${raceId}`);
                if (!response.ok) throw new Error("Predictions not found");
                
                const data = await response.json();
                displayPredictions(data.predictions);
                
            } catch (error) {
                console.error("Error loading predictions:", error);
                showError("Could not load race predictions");
            }
        }

        // Display predictions in the table
        function displayPredictions(predictions) {
            const tbody = document.querySelector("#predictions-table tbody");
            tbody.innerHTML = "";

            predictions.forEach((prediction, index) => {
                const row = document.createElement("tr");
                row.className = "prediction-row";
                
                // Add podium highlighting
                if (index < 3) {
                    row.classList.add("podium-row");
                }

                row.innerHTML = `
                    <td class="position">${index + 1}</td>
                    <td class="driver-name">${prediction.driver}</td>
                    <td class="team-name">${prediction.team}</td>
                    <td class="rating">${prediction.rating}</td>
                    <td class="performance">${prediction.performance}</td>
                    <td class="podium-prob">${prediction.podium_prob}</td>
                    <td class="points-prob">${prediction.pts_prob}</td>
                    <td class="expected-points">${prediction.points}</td>
                `;

                tbody.appendChild(row);
            });
        }

        // Show error message
        function showError(message) {
            const container = document.querySelector('.container');
            const errorDiv = document.createElement('div');
            errorDiv.className = 'error-message';
            errorDiv.innerHTML = `
                <i class="fas fa-exclamation-triangle"></i>
                <p>${message}</p>
            `;
            container.appendChild(errorDiv);
        }

        // Initialize page
        document.addEventListener('DOMContentLoaded', function() {
            const raceInfo = getRaceInfoFromURL();
            
            if (raceInfo.raceName) {
                document.getElementById('race-name').textContent = raceInfo.raceName;
                loadRaceInfo(raceInfo.raceName);
            }
            
            if (raceInfo.raceId) {
                loadRacePredictions(raceInfo.raceId);
            }
        });