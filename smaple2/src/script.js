// script.js

let chartData = {
    labels: [],
    datasets: [{
        data: [],
        backgroundColor: [],
    }]
};

let pieChart;

function updateChart() {
    if (pieChart) {
        pieChart.destroy();
    }
    let ctx = document.getElementById('pie-chart').getContext('2d');
    pieChart = new Chart(ctx, {
        type: 'pie',
        data: chartData,
    });
}

function addData() {
    let field = document.getElementById('field').value.trim();
    let value = parseFloat(document.getElementById('value').value);
    
    if (!field || isNaN(value)) {
        alert("Please enter valid data.");
        return;
    }
    
    chartData.labels.push(field);
    chartData.datasets[0].data.push(value);
    chartData.datasets[0].backgroundColor.push(getRandomColor());
    
    updateChart();
}

function getRandomColor() {
    return '#' + Math.floor(Math.random()*16777215).toString(16);
}

// Persist data to backend (Assuming you're using AJAX for backend interaction)
function saveDataToBackend() {
    // Implement your AJAX request here to save chartData to backend
    // Example:
    // fetch('/saveData', {
    //     method: 'POST',
    //     body: JSON.stringify(chartData),
    //     headers: {
    //         'Content-Type': 'application/json'
    //     }
    // }).then(response => {
    //     if (response.ok) {
    //         console.log('Data saved successfully');
    //     } else {
    //         console.error('Failed to save data');
    //     }
    // }).catch(error => {
    //     console.error('Error:', error);
    // });
}

// Call saveDataToBackend() when the page unloads to save chart data
window.addEventListener('beforeunload', saveDataToBackend);

// Load chart data from backend when the page loads
window.addEventListener('load', () => {
    // Implement loading data from backend if needed
    // Example:
    // fetch('/loadData')
    //     .then(response => response.json())
    //     .then(data => {
    //         chartData = data;
    //         updateChart();
    //     })
    //     .catch(error => console.error('Error:', error));
});
