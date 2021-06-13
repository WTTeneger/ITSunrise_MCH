var element = document.getElementById('sv_map_q');
// var panzoom = Panzoom(elem, {
//     minScale: 1,
//     maxScale: 5,
//     zoomSpeed: 0.065, // 6.5% на событие колеса мышиm
// })
// sz = 1
// var CountHomeEl = 0
//     // panzoom.zoom(sz)
var l_zum = 0
var d, el_div;
var instance = panzoom(element, {
    maxZoom: 4,
    minZoom: 1,
    // beforeMouseDown: function(e) {
    //     // allow mouse-down panning only if altKey is down. Otherwise - ignore

    //     var shouldIgnore = !e.altKey;
    //     return shouldIgnore;
    // },
    beforeWheel: function(e) {
        console.log(e);
        if (e.deltaY > 0) {

            instance.moveTo(0, 0);
            // document.getElementById('sv_map_q').style.transform = 'matrix(1, 0, 0, 1, 0, 0)'
        }
        //     var shouldIgnore = e.altKey;
        //     shouldIgnore.x = 0

        // }
        // // allow wheel-zoom only if altKey is down. Otherwise - ignore
        var shouldIgnore = e.key;
        return shouldIgnore;
    },

});

// instance.on('zoom', function(e) {
//     console.log(e);
//     console.log('Fired when zoom animation ended; l_zum');
// });