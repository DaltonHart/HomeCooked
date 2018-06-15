$(document).ready(function($){
	console.log('sanity check one')
	cook = $('.cook')
	customer = $('.customer')
	
	$('#custBtn').on('click', (e)=>{
		console.log('check cust btn clicked', $('body').width() )
		if(customer.width() > $('body').width()/2){
			console.log('customer`s width is in 100%')
			$('.custDetail').toggle().hide();
			$(cook).animate({width:"50%"},800);
			$(customer).animate({width:'50%', marginLeft:0}, {duration: 1000});

		}else{
			$(cook).animate({width:"0"},800);
			$(customer).animate({width:'100%',postition:'abosulute', left:0}, {duration: 800});
			$('.custDetail').toggle().show();
		}
	})

	$('#cookBtn').on('click', (e)=>{
		// console.log('before', cook.css('width'))
		// console.log('documtn', $('body').css('width'))
		if(cook.width() > $('body').width()/2){
			console.log('cooks`s width is in 100%')
			console.log('cust`s width is', customer.width())
			$('.cookDetail').toggle().hide();
			$(customer).animate({width:"50%"},800);
			$(cook).animate({width:'50%'}, {duration: 1000});
		}else{
			$(customer).animate({width:"0"},800);
			$(cook).animate({width:'100%'}, {duration: 800});
			$('.cookDetail').toggle().show();
		}
	
	})


});