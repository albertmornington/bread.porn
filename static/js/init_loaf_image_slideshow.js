ready(function() {
    var idx = 0;
    var loafImages = document.querySelectorAll('.loaf-image');
    var numImages = loafImages.length;

    var rightArrow = document.querySelector('.loaf-image_arrow-right'); 
    var leftArrow = document.querySelector('.loaf-image_arrow-left'); 

    leftArrow.addEventListener('click', function(e) {
        var nextIdx = (idx - 1 + numImages) % numImages;
        loafImages[nextIdx].classList.remove('u-hidden');
        loafImages[idx].classList.add('u-hidden');
        idx = nextIdx;
    });

    rightArrow.addEventListener('click', function(e) {
        var nextIdx = (idx + 1) % numImages;
        loafImages[nextIdx].classList.remove('u-hidden');
        loafImages[idx].classList.add('u-hidden');
        idx = nextIdx;
    });
});
