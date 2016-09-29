$(function () {
	var x=0;
	$(".select").keyup(function () {
			getselect();
			return false;
		});
	$("#select").click(function () {
			getselect();
			return false;
		});

	$("#search_up").click(function () {
			getselect_up();
			return false;
		});
	$("#update").click(function () {
			update();
			return false;
		});
	$("#add").click(function () {
			add();
			return false;
		});
	$("#delete").click(function () {
			delete_();
			return false;
		});

	function delete_() {
		datos = {
			"id":$("#id").val()
		}

		$.getJSON('http://localhost:3000/delete_movie', datos , function(data) {
				if (JSON.stringify(data["status"])) {
					$("#result").text("Correcto");
				}
				else{
					$("#result").text("Ocurrio un error");
				}
			});
	}

	function add() {
		datos = {
			"titulo":$("#title").val(),
			"director":$("#director").val(),
			"genero":$("#genero").val(),
			"compra":$("#compra").val(),
			"venta":$("#venta").val(),
			"stock":$("#stock").val()
		}

		$.getJSON('http://localhost:3000/insert_movie', datos , function(data) {
				if (JSON.stringify(data["status"])) {
					$("#result").text("Correcto");
				}
				else{
					$("#result").text("Ocurrio un error");
				}
			});
	}

	function update() {
		datos = {
			"id" :$("#id").val(),
			"titulo":$("#title").val(),
			"director":$("#director").val(),
			"genero":$("#genero").val(),
			"compra":$("#compra").val(),
			"venta":$("#venta").val(),
			"stock":$("#stock").val()
		}

		$.getJSON('http://localhost:3000/update_movie', datos , function(data) {
				if (JSON.stringify(data["status"])) {
					$("#result").text("Correcto");
				}
				else{
					$("#result").text("Ocurrio un error");
				}
			});
	}

	function getselect_up() {
		datos = {
			"id" :$("#id").val(),
			"titulo":"",
			"director":"",
			"genero":""
		}
		$.getJSON('http://localhost:3000/select', datos , function(data) {
				console.log("Success");
				$("#title").val(JSON.stringify(data[0][1]).replace("\"", "").replace("\"", ""));
				$("#director").val(JSON.stringify(data[0][2]).replace("\"", "").replace("\"", ""));
				$("#genero").val(JSON.stringify(data[0][3]).replace("\"", "").replace("\"", ""));
				$("#compra").val(JSON.stringify(data[0][4]));
				$("#venta").val(JSON.stringify(data[0][5]));
				$("#stock").val(JSON.stringify(data[0][6]));
			});
	}
	function getselect() {
		datos = {
			"id" :$("#id").val(),
			"titulo":$("#title").val(),
			"director":$("#director").val(),
			"genero":$("#gender").val()
		}
		$.getJSON('http://localhost:3000/select', datos , function(data) {
				for (var i =0 ; i < data.length; i++) {
					datos+="<tr>";
					datos+="<td></td>"
					for (var j =0 ; j < data[i].length; j++) {
						datos+="<td>"+JSON.stringify(data[i][j])+"</td>";
					}
					datos+="</tr>";
				}
				$("#results").html(datos);
			});
	}

});
