$(window).scroll(function () {
	// body...
	if ($(this).scrollTop()>1) {
		$('#navmenu').addClass("sticky");
		console.log('1');
	}
	else{
		$('#navmenu').removeClass("sticky");
		console.log('0');
	}
})

