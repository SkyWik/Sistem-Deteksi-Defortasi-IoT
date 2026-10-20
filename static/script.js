let probChart = null;

document.getElementById('btnAnalyze').addEventListener('click', async () => {
    const scenario = document.getElementById('scenarioSelect').value;
    
    try {
        const response = await fetch('/api/analyze', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ driver_scenario: scenario })
        });
        
        const data = await response.json();
        if (data.status === 'success') {
            displayResults(data.analysis_result);
        }
    } catch (err) {
        console.error('Error fetching analysis:', err);
    }
});

function displayResults(result) {
    document.getElementById('resultCard').style.display = 'block';
    document.getElementById('predictedDriver').innerText = result.predicted_driver;
    document.getElementById('confidenceVal').innerText = result.confidence + '%';

    const labels = Object.keys(result.probabilities);
    const values = Object.values(result.probabilities);

    if (probChart) {
        probChart.destroy();
    }

    const ctx = document.getElementById('probChart').getContext('2d');
    probChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
                label: 'Probabilitas (%)',
                data: values,
                backgroundColor: '#3182ce',
                borderColor: '#63b3ed',
                borderWidth: 1
            }]
        },
        options: {
            indexAxis: 'y',
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                x: { beginAtZero: true, max: 100 }
            },
            plugins: {
                legend: { display: false }
            }
        }
    });
}
