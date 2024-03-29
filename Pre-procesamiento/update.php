<html>

<head>

<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js"></script>

  <script type="text/javascript" src="http://softm.com.mx/CMM/JS/Highcharts-2.2.5/js/highcharts.js"></script>
  <script type="text/javascript" src="http://softm.com.mx/CMM/JS/Highcharts-2.2.5/js/themes/grid.js"></script>
  <script type="text/javascript" src="http://softm.com.mx/CMM/JS/Highcharts-2.2.5/js/modules/exporting.js"></script>

<script type="text/javascript">

   var chart;
$(document).ready(function() {
    chart = new Highcharts.Chart({
      chart: {
	renderTo: 'graficaDescarga',
	    type: 'column',
	    margin: [ 50, 50, 100, 80]
	    },
	  title: {
	text: 'Indice de Criminalidad'//Aqui va el titulo 
	    },
	  xAxis: {
	categories: [ 'Rollo Durazno','Pay de Queso','Ensueño Mango Mango','Rollo de Mango Jr.','Pastel Mechudo','Rollo Durazno Jr.','Rollo de Piña Jr.','Rollo de Fresa','Rollo de Cajeta','Rollo de Mango' ],
	    //categories: [ <?php echo $valoresX; ?>],
	    labels: {
	  rotation: -45,
	      align: 'right',
	      style: {
	    font: 'normal 10px Verdana, sans-serif'
		}
	  }
	},
	  credits: {
	enabled: false
	    },
	  yAxis: {
	min: 0,
	    title: {
	  text: 'Criminalidad' //Va lo de crimen //'Cantidad de Votos'
	      }
	},
	  legend: {
	enabled: false
	    },
	  tooltip: {
	formatter: function() {
	    return '<b>'+ this.x +'</b><br/>'+'Votos:'+ this.y+ '';
	  }
	},
	  series: [{
	  name: 'Votos',
	      data: [50,34,32,23,23,22,20,19,18,10],
	      //data: [<?php echo $valoresY; ?>], //imprimimos la cantidad de criminalidad actual
	      dataLabels: {
	    enabled: true,
		rotation: -90,
		color: '#FFFFFF',
		align: 'right',
		x: -3,
		y: 10,
		//y: <?php echo $totalE; ?>,
		formatter: function() {
		return this.y;
	      },
		style: {
	      font: 'normal 13px Verdana, sans-serif'
		  }
	    }
	  }]
	  });
  });

</script> 


</head>

<body>

<form action="index.php" method="post" enctype="multipart/form-data">
  <input name="archivo" type="file" size="35" />
  <input name="enviar" type="submit" value="Upload File" />
  <input name="action" type="hidden" value="upload" />     
</form>

<table>
<tr>
<td width="70%">
  <div id="graficaDescarga" style="height: 100%; width:100%; margin: 0 auto"></div>
  </td>
  <td width="30%">
  <div id="graficaEspacio" style="height: 80%; width:100%; margin: 0 auto"></div>
  </td>
  </tr>
  <tr>
  <td colspan="2">
  <div id="graficaPie" style="min-width: 400px; height: 400px; margin: 0 auto"></div>
  </td>
  </tr>
  </table>

<!--<div id="graficaDescarga" style="height: 100%; width:100%; margin: 0 auto"></div>-->


</body>
</html>