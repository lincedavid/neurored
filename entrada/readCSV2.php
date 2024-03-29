<?php
//
$bandera = False; //Banderilla de si activamos el Query

function dameBool($anterior, $actual)
{
  if($actual > $anterior) return 1;
  else return -1;
}

function escalar($x, $xmin, $xmax)
{
  $lower = -1.0;
  $first = ($x - $xmin)*2.0;
  if($first == 0)
    return 0;
  $second = ($xmax - $xmin);
  $third = $first/$second;
  $result = $lower+$third;
  return $result;
}

function createFile($data, $file)
{
  $file = substr($file, 0, -4); //Al archivo le eliminamos el .csv para quee quede con .txt 
  $data = implode(',', $data); //Hacemos esto ya que recivimos un array
  $fileName = "files/txt/$file.txt";
  $fp = fopen($fileName, 'w');
  fwrite($fp, $data);
  fclose($fp);
  return $fileName;
}

function readCSV($archivoDestino)
{
  $file = "files/csv/".$archivoDestino;
  if (($gestor = fopen($file, "r")) !== FALSE) 
    {
      $listaValores = array();
      $listaFechas = array();
	$anterior = 0;
	$listaUnosCeros = array();

      while (($datos = fgetcsv($gestor, 1000, ",")) !== FALSE) 
	{
	  $numero = count($datos);
	  for ($c = 1; $c < $numero; $c++)  //Cambiamos c = 0, para que cargue tmb las fechas
	    {
	      if(is_numeric($datos[$c]))//Comprobamos que sea numerico
		{
		  $listaValores[] = $datos[$c]; //Guardamos las fechas en un arreglo

		  $listaFechas[] = $datos[$c-1];

		$listaUnosCeros[] = dameBool($anterior, $datos[$c]);
		$anterior = $datos[$c];
		}
	    }	
	}
      $fileName = createFile($listaValores, $archivoDestino); //Creamos el archivo.dat o .txt que leera el python
      fclose($gestor);
	
	//$unos = implode(",",$listaUnosCeros);
      $_SESSION['unosceros'] = implode(",",$listaUnosCeros);
      return array($fileName, $listaValores, $listaFechas);//, $listaEscalada);
    }
}

function callPython($fileName)
{
  return ($python = exec("python a.py $fileName"))? $python : False; //Valor ternario
  //print "<br/>salida python: <br/><b>".exec("python a.py $fileName")."</b><br/><br/>";
}

function callNormalizar($fileName)
{
  return ($python = exec("python escalar.py $fileName"))? $python : False; //Valor ternario
}

function uploadFile()
{
  $bStatus = False;
  $status = "";
  if ($_POST["action"] == "upload") {
    $tamano = $_FILES["archivo"]['size'];
    $tipo = $_FILES["archivo"]['type'];
	$archivo = $_FILES["archivo"]['name'];
	$prefijo = substr(md5(uniqid(rand())),0,6);
	
	if ($archivo != "") {
	    $destino =  $prefijo."_".$archivo;
	  if (copy($_FILES['archivo']['tmp_name'],"files/csv/".$destino)){
	    $status = "Archivo subido: <b>".$archivo."</b>";
	    $bStatus = True;
	  } else {
	    $status = "Error al subir el archivo";
	  }
	} else {
	  $status = "Error al subir archivo";
	}
  } 

	if($status)
{
	$_SESSION['status'] = $status;
}  

  if($bStatus) return $destino; //Si el archivo se cumplio regresamos la ruta del destino
  else return $bStatus; // De lo contrario un false
}

//function main()
//if ($_POST["action"] == "upload")
//{

$archivoDestino =  '0d3054_crimes-recorded-by-the-police.csv';//uploadFile(); //Subimos el archivo CVS
  if(!$archivoDestino)
    {
      die();
    }

$archivoLimpio = readCSV($archivoDestino); //Pasamos el archivo CSV a un .txt que es una simple lista //Regresa un array de dos elementos, destino y la lista de los elementos
$valoresY = implode(",",$archivoLimpio[1]);
$valoresX = implode(",",$archivoLimpio[2]); //El de las fechas

$totalE = count($archivoLimpio[1]);
$run = callPython($archivoLimpio[0]); //corremos el archivo de python 

$normalizar = callNormalizar($archivoLimpio[0]); //corremos el archivo de python 
//echo $run."<br/>";
if($run) $_SESSION['python'] = $run;

if($normalizar) $_SESSION['unosceros'] = $normalizar;

$bandera = True;
//}

//else $bandera = False;


?>

<html>

<head>

<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js"></script>

  <script type="text/javascript" src="http://softm.com.mx/CMM/JS/Highcharts-2.2.5/js/highcharts.js"></script>
  <script type="text/javascript" src="http://softm.com.mx/CMM/JS/Highcharts-2.2.5/js/themes/grid.js"></script>
  <script type="text/javascript" src="http://softm.com.mx/CMM/JS/Highcharts-2.2.5/js/modules/exporting.js"></script>

<?php if($bandera){ ?>

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
	  categories: [ <?php echo $valoresX; ?>],
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
	      data: [<?php echo $valoresY; ?>], //imprimimos la cantidad de criminalidad actual
	      //data: <?php echo $_SESSION['unosceros']; ?>, //imprimimos la cantidad de criminalidad actual
<<<<<<< HEAD
	      dataLabels: {
	    enabled: true,
		rotation: -90,
		color: '#FFFFFF',
		align: 'right',
		x: -3,
		y: <?php echo $totalE; ?>,
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
	  categories: [ <?php echo $valoresX; ?>],
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
	      //data: [<?php echo $valoresY; ?>], //imprimimos la cantidad de criminalidad actual
	      data: <?php echo $_SESSION['unosceros']; ?>, //imprimimos la cantidad de criminalidad actual
	      dataLabels: {
	    enabled: true,
		rotation: -90,
		color: '#FFFFFF',
		align: 'right',
		x: -3,
		y: <?php echo $totalE; ?>,
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
	  categories: [ <?php echo $valoresX; ?>],
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
	      //data: [<?php echo $valoresY; ?>], //imprimimos la cantidad de criminalidad actual
	      data: <?php echo $_SESSION['unosceros']; ?>, //imprimimos la cantidad de criminalidad actual
=======
>>>>>>> 3706b106294ea06972256a9d7f20add5c7f1e21a
	      dataLabels: {
	    enabled: true,
		rotation: -90,
		color: '#FFFFFF',
		align: 'right',
		x: -3,
		//y: 10,
		y: <?php echo $totalE; ?>,
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
<?php } ?>

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
<fieldset class="fieldset2">
<legend class="legend1" >Subir Archivo</legend>
<form action="readCSV2.php" method="post" enctype="multipart/form-data">
  <input name="archivo" type="file" size="35" />
  <input name="enviar" type="submit" value="Upload File" />
  <input name="action" type="hidden" value="upload" />     
</form>
</fieldset>

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
<?php echo "Prepocesamiento:<br/>".$_SESSION['unosceros']; ?></fieldset>
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
<?php echo "Salida Python:<br/>".$_SESSION['python']; ?></fieldset>
</td>
</tr>
</table>

<table size = 100%>
<tr>
<<<<<<< HEAD
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
=======
  <td width="50%" rowpan="2">
    <div id="graficaDescarga" style="height: 400px; width:600px; margin: 0 auto"></div>
  </td>
  
<?php 
if($_SESSION['status'] && $_SESSION['python']){
	echo "<td>Estatus: ".$_SESSION['status']."</td>";	
	echo "<tr><td>Salida Python:<br/>".$_SESSION['python']."</td></tr>";	
}
?>

 <!--</tr>-->
  <!--<div id="graficaDescarga" style="height: 80%; width:100%; margin: 0 auto"></div>
  <div id="graficaDescarga" style="height: 400px; width:600px; margin: 0 auto"></div>-->

  <!--</td>-->
  <!--</tr>
  <tr>
  <td colspan="2">
  <div id="graficaPie" style="min-width: 400px; height: 400px; margin: 0 auto"></div>
  </td>-->
  <!--</tr>
  </table>-->
>>>>>>> 3706b106294ea06972256a9d7f20add5c7f1e21a

</body>
</html>
