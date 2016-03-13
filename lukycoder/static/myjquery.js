$(window).scroll(function () {
	// body...
	if ($(this).scrollTop()>5) {
		$('#navmenu').addClass("sticky");
		console.log('1');
	}
	else{
		$('#navmenu').removeClass("sticky");
		console.log('0');
	}
})

