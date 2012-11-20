<?php

function readCSV($archivoDestino)
{
	$arrResult = array();
	$handle = fopen("files/txt/$archivoDestino", "rb");
	if( $handle ) {
		$listaFechas = array();
//		$listaYear = array();
//		$listaMonth = array();

		$listaValores = array();
		$listaJunta = array();

		while (($data = fgetcsv($handle, 1000, ",")) !== FALSE) {
			$arrResult[] = $data;
		}

		//$elementos = count($data); //Este servira para saber los de los meses

		fclose($handle);

		for ($c = 0; $c < count($arrResult); $c++)
		{
			$listaFechas[] = $arrResult[$c][0]; //Fechas
			
/*			//add			
			$year = substr($arrResult[$c][0], 0, -3);
			//$listaYear[] = substr($year, -2)
			$year = substr($year, -2)

			$month = (int)substr($arrResult[$c][0], -2);
			//$listaMonth[] = date("F", mktime(0, 0, 0, $month, 10));
			$month = date("F", mktime(0, 0, 0, $month, 10));
			$listaMonth[] = '$month \'$year';
			//end add
*/
			$listaValores[] = $arrResult[$c][1]; //Valores
			$listaJunta[] = array($arrResult[$c][0], $arrResult[$c][1]);

		}	
		return array($listaFechas, $listaValores, $listaJunta);
	}
	else
	{
		echo 'No se pudo abrir el archivo';
		die();
	}
}

function createCSV($archivo, $valores)
{
	$fp = fopen("files/txt/$archivo", 'w');
	foreach ($valores as $fields) {
		//echo var_dump($valores);
		fputcsv($fp, $fields);
	}
	fclose($fp);
}

function implodeFecha()
{
	return implode(', ', $_SESSION['fecha']);
}

function implodeValores()
{
	return implode(', ', $_SESSION['valores']);
}

function countValores()
{
	return count($_SESSION['fecha']);
}

function callPython($fileName)
{
	return ($python = exec("python a.py $fileName"))? $python : False; //Valor ternario
}

function callNormalizar($fileName)
{
	return ($python = exec("python escalar.py $fileName"))? $python : False; //Valor ternario
}

function minValores()
{
	return min($_SESSION['valores']);
}

function maxValores()
{
	return max($_SESSION['valores']);
}

function createFile($file, $data)
{
	//$file = substr($file, 0, -4); //Al archivo le eliminamos el .csv para quee quede con .txt 
	$data = implode(',', $data); //Hacemos esto ya que recivimos un array
	$fileName = "files/txt/$file.txt";
	$fp = fopen($fileName, 'w');
	fwrite($fp, $data);
	fclose($fp);
	return $fileName;
}

/*function main()
{
	//$archivo = 'csvDelitos.csv';
	$archivo = 'robo.csv';

	/*if($_POST["action"] == "upload")
	//if($_POST["archivo"])
	{
		if (copy($_FILES['archivo']['tmp_name'],"files/csv/".$archivo)){
			$status = "Archivo subido: <b>".$archivo."</b>";
			$bStatus = True;
		} else {
			$status = "Error al subir el archivo";
		}	
	}*/
/*
	$listaValores = readCSV($archivo);

	$_SESSION['fecha'] = $listaValores[0]; //array
	$_SESSION['valores'] = $listaValores[1]; //array

	$fileFechas = createFile('fechas', $listaValores[0]); //creamos archivo de fechas
	$fileValores = createFile('valores', $listaValores[1]); //creamos archivo de valores

	echo '<br/>'.implodeFecha();
	echo '<br/>'.implodeValores();
	echo '<br/>'.countValores();

	//echo '<br/>'.callPython($fileValores);
	//echo '<br/>'.callNormalizar($fileValores);
	$_SESSION['normalizar'] = callNormalizar($fileValores);	//String

	//unlink('files/txt/'.$archivo); //eliminamos el archivo creado
	//createCSV($archivo, $listaValores[2]);
}

main();*/

?>
