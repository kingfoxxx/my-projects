// Parse the JSON data passed from the Django template
var data = JSON.parse(document.getElementById('data').textContent);

// Prepare data for the chart
var labels = data.map(function(item) {
    return item.topic;
});
var counts = data.map(function(item) {
    return item.intensity;
});

// Create chart using Chart.js
var ctx = document.getElementById('myChart').getContext('2d');
var myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: labels,
        datasets: [{
            label: 'Data Visualization',
            data: counts,
            backgroundColor: 'rgba(255, 99, 132, 0.2)',
            borderColor: 'rgba(255, 99, 132, 1)',
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});
