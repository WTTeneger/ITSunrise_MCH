function stop_a(el) {
    el.style = ''
}


jQuery('body').swipe({
    swipe: function(event, direction, distance, duration, fingerCount, fingerData) {
        console.log(event, direction);

        if (direction == 'left') {
            document.getElementById('test_block').style = 'animation: swipe_left 0.3s ease-in-out;'
            setTimeout(stop_a, 400, document.getElementById('test_block'));

        }
        if (direction == 'right') {
            document.getElementById('test_block').style = 'animation: swipe_right 0.3s ease-in-out;'
            setTimeout(stop_a, 400, document.getElementById('test_block'));

        }

    }
});