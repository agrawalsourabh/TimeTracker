google.charts.load("current", {packages:["corechart"]});
      google.charts.setOnLoadCallback(getData);

      function getData() {
        var filePath = '../../user_activity_data/';
        var fileName = '2020/4/2';
        var fileExt = '.json';
          $.getJSON(filePath+fileName+fileExt, function(d){
            displayChart(d);
        });

          console.log(this.d);
      }

      function displayChart(d){
        var data = new google.visualization.DataTable();
            data.addColumn('string', 'Tracking');
            data.addColumn('number', 'Duration');

            $.each(d, function(i, f){
              data.addRow([f.name, f.duration]);
            });


            var options = {
                title: 'My Daily Activities',
                titleTextStyle: { color: '#302929',
                    fontName: 'Amita',
                    fontSize: 30,
                    bold: true,
                    italic: false,
                },
                is3D: false,
                pieHole: 0.4,
                pieSliceTextStyle: {
                    color: 'white',
                    },
                pieStartAngle: 100,

            };

          var chart = new google.visualization.PieChart(document.getElementById('piechart'));
          chart.draw(data, options);
      }

