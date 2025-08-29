async function loadRaces() {
            try {
                const response = await fetch("http://127.0.0.1:8000/races/upcoming");
                if (!response.ok) {
                    throw new Error(`HTTP error! Status: ${response.status}`);
                }
                const races = await response.json();
                
                // Separate upcoming and completed races
                const cutoffDate = new Date('2025-08-22');
                const upcomingRaces = [];
                const completedRaces = [];
                
                races.forEach(race => {
                    const raceDate = new Date(race.date);
                    if (raceDate < cutoffDate) {
                        completedRaces.push(race);
                    } else {
                        upcomingRaces.push(race);
                    }
                });
                
                // Display upcoming races
                displayRaces(upcomingRaces, 'race-list');
                
                // Display completed races
                displayCompletedRaces(completedRaces, 'completed-races-list');
                
            } catch (error) {
                console.error("Fetch error:", error);
                const list = document.getElementById("race-list");
                list.innerHTML = `
                    <div class="error-message">
                        <i class="fas fa-exclamation-triangle"></i>
                        <p>Could not load upcoming races. Please try again later.</p>
                    </div>
                `;
            }
        }

        function displayRaces(races, containerId) {
            const container = document.getElementById(containerId);
            container.innerHTML = "";

            races.forEach(race => {
                const raceCard = document.createElement("div");
                raceCard.className = "race-card";

                const raceHeader = document.createElement("div");
                raceHeader.className = "race-header";

                const raceInfo = document.createElement("div");
                raceInfo.className = "race-info";

                const raceName = document.createElement("h3");
                raceName.textContent = race.name;
                raceName.className = "race-name";

                const raceDate = document.createElement("p");
                raceDate.textContent = race.date;
                raceDate.className = "race-date";

                const raceActions = document.createElement("div");
                raceActions.className = "race-actions";

                // Qualifying Details button
                const qualBtn = document.createElement("a");
                qualBtn.href = `qualifying.html?race_id=${race.race_id}`;
                qualBtn.className = "action-btn qualifying-btn";
                qualBtn.innerHTML = '<i class="fas fa-clock"></i> Qualifying';

                // Grand Prix Details button
                const gpBtn = document.createElement("a");
                gpBtn.href = `grandprix.html?race_id=${race.race_id}&race_name=${encodeURIComponent(race.name)}`;
                gpBtn.className = "action-btn gp-btn";
                gpBtn.innerHTML = '<i class="fas fa-flag-checkered"></i> Race Predictions';

                raceInfo.appendChild(raceName);
                raceInfo.appendChild(raceDate);

                raceActions.appendChild(qualBtn);
                raceActions.appendChild(gpBtn);

                raceHeader.appendChild(raceInfo);
                raceHeader.appendChild(raceActions);

                raceCard.appendChild(raceHeader);
                container.appendChild(raceCard);
            });
        }

        function displayCompletedRaces(races, containerId) {
            const container = document.getElementById(containerId);
            container.innerHTML = "";

            if (races.length === 0) {
                container.innerHTML = `
                    <div class="no-completed-races">
                        <i class="fas fa-info-circle"></i>
                        <p>No completed races yet this season.</p>
                    </div>
                `;
                return;
            }

            races.forEach(race => {
                const raceCard = document.createElement("div");
                raceCard.className = "race-card completed-race-card";

                const raceHeader = document.createElement("div");
                raceHeader.className = "race-header";

                const raceInfo = document.createElement("div");
                raceInfo.className = "race-info";

                const raceName = document.createElement("h3");
                raceName.textContent = race.name;
                raceName.className = "race-name";

                const raceDate = document.createElement("p");
                raceDate.textContent = race.date;
                raceDate.className = "race-date";

                const completedBadge = document.createElement("span");
                completedBadge.className = "completed-badge";
                completedBadge.innerHTML = '<i class="fas fa-check-circle"></i> Completed';

                const raceActions = document.createElement("div");
                raceActions.className = "race-actions";

                // View Results button
                const resultsBtn = document.createElement("a");
                resultsBtn.href = `grandprix.html?race_id=${race.race_id}&race_name=${encodeURIComponent(race.name)}`;
                resultsBtn.className = "action-btn results-btn";
                resultsBtn.innerHTML = '<i class="fas fa-chart-bar"></i> View Results';

                raceInfo.appendChild(raceName);
                raceInfo.appendChild(raceDate);
                raceInfo.appendChild(completedBadge);

                raceActions.appendChild(resultsBtn);

                raceHeader.appendChild(raceInfo);
                raceHeader.appendChild(raceActions);

                raceCard.appendChild(raceHeader);
                container.appendChild(raceCard);
            });
        }

        // Toggle completed races dropdown
        function toggleCompletedRaces() {
            const content = document.getElementById('completed-races-content');
            const toggle = document.getElementById('completed-races-toggle');
            const icon = toggle.querySelector('i');
            
            if (content.style.display === 'block') {
                content.style.display = 'none';
                toggle.innerHTML = '<i class="fas fa-chevron-down"></i> Show Completed Races';
                toggle.classList.remove('active');
            } else {
                content.style.display = 'block';
                toggle.innerHTML = '<i class="fas fa-chevron-up"></i> Hide Completed Races';
                toggle.classList.add('active');
            }
        }
            
        window.addEventListener("DOMContentLoaded", function() {
            loadRaces();
            
            // Add event listener for the dropdown toggle
            document.getElementById('completed-races-toggle').addEventListener('click', toggleCompletedRaces);
        });