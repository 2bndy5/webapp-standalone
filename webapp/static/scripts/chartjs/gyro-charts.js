var NUM_POINTS = 21;

var configGyroLineChart = {
    type: 'line',
    data: {
        labels: [...range(1, NUM_POINTS)].map(i => -(NUM_POINTS - i)),
        datasets: [{
            label: 'X Axis',
            backgroundColor: chartColors.red,
            borderColor: chartColors.red,
            data: randData(NUM_POINTS),
            fill: false,
        }, {
            label: 'Y Axis',
            fill: false,
            backgroundColor: chartColors.blue,
            borderColor: chartColors.blue,
            data: randData(NUM_POINTS),
        }, {
            label: 'Z Axis',
            fill: false,
            backgroundColor: chartColors.green,
            borderColor: chartColors.green,
            data: randData(NUM_POINTS),
        }]
    },
    options: {
        aspectRatio: 3,
        tooltips: {
            mode: 'index',
            intersect: false,
        },
        hover: {
            mode: 'nearest',
            intersect: true
        },
        scales: {
            xAxes: [{
                display: true,
                scaleLabel: {
                    display: true,
                    labelString: 'Time Elapsed'
                }
            }],
            yAxes: [{
                display: true,
                scaleLabel: {
                    display: true,
                    labelString: 'Value'
                }
            }]
        }
    }
};

var configGyroBarChart = {
    type: 'bar',
    data: {
        datasets: [{
            label: 'X Axis',
            backgroundColor: chartColors.red,
            borderColor: chartColors.red,
            data: randData(1),
            fill: false,
        }, {
            label: 'Y Axis',
            fill: false,
            backgroundColor: chartColors.blue,
            borderColor: chartColors.blue,
            data: randData(1),
        }, {
            label: 'Z Axis',
            fill: false,
            backgroundColor: chartColors.green,
            borderColor: chartColors.green,
            data: randData(1),
        }]
    },
    options: {
        aspectRatio: 1.4,
        tooltips: {
            mode: 'dataset',
            intersect: false,
        },
        hover: {
            mode: 'nearest',
            intersect: true
        },
        scales: {
            yAxes: [{
                display: true,
                ticks: {
                    min: -100,
                    max: 100,
                },
            }]
        }
    }
};