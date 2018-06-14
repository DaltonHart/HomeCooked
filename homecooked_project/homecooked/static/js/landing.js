$(document).ready(function($){
	console.log('sanity check')
	details = $('.overview').children().find('.detail')
	details.hide()
	$('.showbtn').on('click', (e)=>{
		$(details).slideToggle( "slow" );
	})



});