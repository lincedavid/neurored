<?php

include('readTxt.php');

?>

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
	  categories: [ <?php echo implodeValores(); ?>],
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
	  text: 'Criminalidad' //Va lo de crimen 
	      }
	},
	  legend: {
	enabled: false
	    },
	  tooltip: {
	formatter: function() {
	    return '<b>'+ this.x +'</b><br/>'+'Criminalidad:'+ this.y+ '';
	  }
	},
	  series: [{
	  name: 'Votos',
	      data: [<?php echo implodeValores(); ?>], //imprimimos la cantidad de criminalidad actual
	      dataLabels: {
	    enabled: true,
		rotation: -90,
		color: '#FFFFFF',
		align: 'right',
		x: -3,
		y: <?php echo countValores(); ?>,
		formatter: function() {
		return this.y;
	      },
		style: {
	      font: 'normal 13px Verdana, sans-serif'
		  }
	    }
	  }]
	  });

    chart = new Highcharts.Chart({
      chart: {
	renderTo: 'graficaPostProcesamiento',
	    type: 'column',
	    margin: [ 50, 50, 100, 80]
	    },
	  title: {
	text: 'Indice de Criminalidad'//Aqui va el titulo 
	    },
	  xAxis: {
	  categories: [ <?php echo implodeFecha(); ?>],
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
	  text: 'Criminalidad' //Va lo de crimen
	      }
	},
	  legend: {
	enabled: false
	    },
	  tooltip: {
	formatter: function() {
	    return '<b>'+ this.x +'</b><br/>'+'Criminalidad:'+ this.y+ '';
	  }
	},
	  series: [{
	  name: 'Votos',
	      data: [<?php echo $_SESSION['normalizar']; ?>], //imprimimos la cantidad de criminalidad actual
	      dataLabels: {
	    enabled: true,
		rotation: -90,
		color: '#FFFFFF',
		align: 'right',
		x: -3,
		y: <?php echo countValores(); ?>,
		formatter: function() {
		return this.y;
	      },
		style: {
	      font: 'normal 13px Verdana, sans-serif'
		  }
	    }
	  }]
	  });


    chart = new Highcharts.Chart({
      chart: {
	renderTo: 'graficaProcesamiento',
	    type: 'column',
	    margin: [ 50, 50, 100, 80]
	    },
	  title: {
	text: 'Indice de Criminalidad'//Aqui va el titulo 
	    },
	  xAxis: {
	  categories: [ <?php echo implodeFecha(); ?>],
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
	  text: 'Criminalidad' //Va lo de crimen 
	      }
	},
	  legend: {
	enabled: false
	    },
	  tooltip: {
	formatter: function() {
	    return '<b>'+ this.x +'</b><br/>'+'Criminalidad:'+ this.y+ '';
	  }
	},
	  series: [{
	  name: 'Votos',
	      data: [<?php echo $_SESSION['normalizar']; ?>], //imprimimos la cantidad de criminalidad actual
	      dataLabels: {
	    enabled: true,
		rotation: -90,
		color: '#FFFFFF',
		align: 'right',
		x: -3,
		//y: 10,
		y: <?php echo countValores(); ?>,
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

<style type="text/css">
body{
background-color: #BFC4BE;
#background-color: #6385A0;

}
.fieldset2 {
#width:500px;
width:90%;
#border:4px double #2C2F2C;
-webkit-border-radius: 10px;
-moz-border-radius: 10px;
border-radius: 10px;
#-webkit-box-shadow: 8px 8px 6px #808080;
#-moz-box-shadow: 8px 8px 6px #808080;
#box-shadow: 8px 8px 6px #808080;
background-color: #6385A0;
#padding: 10px;
font-family: Verdana, Geneva, sans-serif;
color: white;
#-webkit-transform: rotate(-2deg);
#-moz-transform: rotate(-2deg);
#-o-transform: rotate(-2deg);
}

.fieldset1 {
width:500px;
border:4px double #2C2F2C;
-webkit-border-radius: 10px;
-moz-border-radius: 10px;
border-radius: 10px;
-webkit-box-shadow: 8px 8px 6px #808080;
-moz-box-shadow: 8px 8px 6px #808080;
box-shadow: 8px 8px 6px #808080;
background-color: #616161;
padding: 10px;
font-family: Verdana, Geneva, sans-serif;
color: white;
#-webkit-transform: rotate(-2deg);
#-moz-transform: rotate(-2deg);
#-o-transform: rotate(-2deg);
}
.legend1 {
text-align:center;
font-weight:bold;
font-size:18pt;
#color:#008000;
color:black;
text-shadow: 0px 0px 4px white;
#text-shadow: 0px 0px 10px #008000;
}
</style>
</head>

<body>

<h1>Predicciones de Crimenes</h1>
<!--<fieldset class="fieldset2">
<legend class="legend1" >Subir Archivo</legend>
<form action="readCSV2.php" method="post" enctype="multipart/form-data">
  <input name="archivo" type="file" size="35" />
  <input name="enviar" type="submit" value="Upload File" />
  <input name="action" type="hidden" value="upload" />     
</form>
</fieldset>-->

<table>
<tr>
<td rowspan="3">
<fieldset class="fieldset3">
<legend class="legend1">Grafica</legend>
<div id="graficaDescarga" style="height: 400px; width:600px; margin: 0 auto"></div>
</fieldset>

</td>
<td>
<fieldset class="fieldset1">
<legend class="legend1">Pre-procesamiento</legend>
<?php echo "Prepocesamiento:<br/>".implodeValores(); ?></fieldset>
</fieldset>
</td>
</tr>
<tr>
<td>
<fieldset class="fieldset1">
<legend class="legend1">Estatus</legend><!--Mandamos el mensaje del archivo subido con exito-->
<?php echo "Estatus: Se cargo con exito";//echo "Estatus: ".$_SESSION['status']; ?>
</td>
</tr>
<tr>
<td>
<fieldset class="fieldset1">
<legend class="legend1">Procesado Python</legend>
<?php echo "Salida Python:<br/>".$_SESSION['normalizar']; ?></fieldset>
</td>
</tr>
</table>

<table size = 100%>
<tr>
<td>
<fieldset class="fieldset3">
<legend class="legend1">Pre-Procesamiento</legend>
<div id="graficaProcesamiento" style="height: 400px; width:600px; margin: 0 auto"></div>
</fieldset>
</td>
<td>
<fieldset class="fieldset3">
<legend class="legend1">Post-Procesamiento</legend>
<div id="graficaPostProcesamiento" style="height: 400px; width:600px; margin: 0 auto"></div>
</fieldset>
</td>
</tr>
<table>

</body>
</html>
