google.charts.load("current", { packages: ["corechart"] });
google.charts.setOnLoadCallback(getData);

function getData() {
    var filePath = '../../user_activity_data/';
    var fileName = '2020/4/7';
    var fileExt = '.json';
    $.getJSON(filePath + fileName + fileExt, function(d) {
        displayTasks(d);
        displayChart(d);
    });

    console.log(this.d);
}

function displayChart(d) {
    var data = new google.visualization.DataTable();
    data.addColumn('string', 'Tracking');
    data.addColumn('number', 'Duration');

    $.each(d, function(i, f) {
        data.addRow(["Task " + (i + 1), f.duration]);
    });

    var col = [
        '#5e7fb5',
        '#80bf50',
        '#e39b49',
        '#6329a6',
        '#b54612',
        '#129ab5',
        '#2a912e',
        '#785537',
        '#fa7e70',
        '#2e8b57'
    ];

    var options = {
        title: 'Daily Activities',
        titleTextStyle: {
            color: '#008080',
            fontName: 'Lucida Sans',
            fontSize: 30,
            bold: false,
            italic: false,
        },
        pieHole: 0.4,
        legend: 'none',
        pieSliceTextStyle: {
            color: 'white',
        },
        colors: col,
    };

    var chart = new google.visualization.PieChart(document.getElementById('piechart'));
    chart.draw(data, options);
}

function displayTasks(d) {
    $.each(d, function(i, f) {
        var listData = '<li class="my-list">' + f.name + '</li>'
        $(listData).appendTo(".task-list");
    });

}