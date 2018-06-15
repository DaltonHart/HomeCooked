$(document).ready(function($){
	console.log('sanity check one')
	cook = $('.cook')
	customer = $('.customer')
	cookdetails = $('.cook').find('.detail')
	customerdetails = $('.customer').find('.detail')
	// cookdetails.hide()
	// customerdetails.hide()
	
	$('#custBtnDiv').on('click', (e)=>{
		console.log('check')
		// cook.fadeToggle('slow', 'linear')
	})
	$('#cookBtnDiv').on('click', (e)=>{
		console.log('check')
		// var toggleWidth = $("#toggle").width() == 300 ? "200px" : "300px";
		var togglewidth = $(cook).width() == "100%" ? "50%" : "70%";
		// $('.cookDetail').toggle().show();
		// cook.toggle().animate({ width: toggleWidth });
		// customer.fadeToggle('slow', 'linear')
	})


});