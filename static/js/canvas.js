
/* Author : Paul Bouaffou 
   Statistiques : canvasjs.com

   ________________________En maintenance____________________________________



window.onload = function () {

var pie_chart = new CanvasJS.Chart("chartContainer", {
	animationEnabled: true,
	},
	data: [{
		type: "pie",
		startAngle: 240,
		yValueFormatString: "##0.00\"%\"",
		indexLabel: "{label} {y}",
		dataPoints: [
			{y: 79.45, label: "Sources"},
			{y: 7.31, label: "Promotionnel"},
			{y: 7.06, label: "Neutralité"},
			{y: 4.91, label: "Wikification"},
			{y: 1.26, label: "Suppression"},
		]
	}]
});

var bar_chart = new CanvasJS.Chart("chartContainer1", {
	animationEnabled: true,
	theme: "light2", // "light1", "light2", "dark1", "dark2"
	title:{
		text: "Top Oil Reserves"
	},
	axisY: {
		title: "Reserves(MMbbl)"
	},
	data: [{        
		type: "column",  
		showInLegend: true, 
		dataPoints: [      
			{ y: 300878, label: "Sources" },
			{ y: 266455,  label: "Promotionnel" },
			{ y: 169709,  label: "Neutralité" },
			{ y: 158400,  label: "Wikification" },
			{ y: 142503,  label: "Suppression" },
		]
	}]
});

pie_chart.render();
bar_chart.render();

}

*/