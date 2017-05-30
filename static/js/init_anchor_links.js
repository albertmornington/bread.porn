ready(function() {
	var anchorLinks = document.querySelectorAll('.anchor-link');
	_.each(anchorLinks, function(anchorLink, index) {
		var anchorId = anchorLink.getAttribute('href');
		var anchor = document.querySelector(anchorId);
		anchorLink.addEventListener('click', function(e) {
			e.preventDefault();
			smoothScroll.animateScroll(anchor);
		});
	});
});
