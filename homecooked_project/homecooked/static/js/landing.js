$(document).ready(function($){
	console.log('sanity check one')
	cook = $('.cook')
	customer = $('.customer')
	
	$('#custBtn').on('click', (e)=>{
		console.log('check cust btn clicked', $('body').width() )
		if(customer.width() > $('body').width()/2){
			console.log('customer`s width is in 100%')
			$('.custDetail').hide()
			$(cook).animate({width:"50%"},300);
			$(customer).animate({width:'50%'}, {duration: 300});

		}else{
			$(cook).animate({width:"0"},350);
			$(customer).animate({width:'100%'}, {duration: 400});
			$('.custDetail').fadeIn(2000)
		}
	})

	$('#cookBtn').on('click', (e)=>{
		// console.log('before', cook.css('width'))
		// console.log('documtn', $('body').css('width'))
		if(cook.width() > $('body').width()/2){
			// console.log('cooks`s width is in 100%')
			// console.log('cust`s width is', customer.width())
			$('.cookDetail').hide();
			$(customer).animate({width:"50%"},500);
			$(cook).animate({width:'50%'}, {duration: 500});
		}else{
			$(customer).animate({width:"0"},350);
			$(cook).animate({width:'100%'}, {duration: 400});
			$('.cookDetail').fadeIn(2000 );;
		}
	
	})

});