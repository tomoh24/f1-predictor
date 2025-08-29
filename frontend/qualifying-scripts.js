// Get race information from URL parameters
        function getRaceInfoFromURL() {
            const params = new URLSearchParams(window.location.search);
            return {
                raceId: params.get('race_id')
            };
        }

        // Load qualifying predictions from API
        async function loadQualifyingPredictions(raceId) {
            try {
                const response = await fetch(`http://127.0.0.1:8000/qualifying/${raceId}`);
                if (!response.ok) {
                    throw new Error(`HTTP error! Status: ${response.status}`);
                }
                const data = await response.json();
                displayQualifyingPredictions(data.predictions);
                
            } catch (error) {
                console.error("Error loading qualifying predictions:", error);
                showError("Could not load qualifying predictions");
            }
        }

        // Display qualifying predictions in the table
        function displayQualifyingPredictions(predictions) {
            const tbody = document.querySelector("#qualifying-table tbody");
            tbody.innerHTML = "";

            predictions.forEach((prediction, index) => {
                const row = document.createElement("tr");
                row.className = "prediction-row";
                
                // Add pole position highlighting
                if (index === 0) {
                    row.classList.add("pole-row");
                } else if (index < 3) {
                    row.classList.add("podium-row");
                }

                row.innerHTML = `
                    <td class="position">${index + 1}</td>
                    <td class="driver-name">${prediction.driver}</td>
                    <td class="team-name">${prediction.team}</td>
                    <td class="q1-time">${prediction.q1_time}</td>
                    <td class="q2-time">${prediction.q2_time}</td>
                    <td class="q3-time">${prediction.q3_time}</td>
                    <td class="pole-prob">${prediction.pole_prob}</td>
                    <td class="q3-prob">${prediction.q3_prob}</td>
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
            
            if (raceInfo.raceId) {
                loadQualifyingPredictions(raceInfo.raceId);
            }
        });