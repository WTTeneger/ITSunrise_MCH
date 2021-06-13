// import Panzoom from '@panzoom/panzoom'
const elem = document.getElementById('sv_map_q')
const panzoom = Panzoom(elem, {
    maxZoom: 4,
    minZoom: 2,
    beforeMouseDown: function(e) {
        // allow mouse-down panning only if altKey is down. Otherwise - ignore

        var shouldIgnore = !e.altKey;
        return shouldIgnore;
    },
})
panzoom.pan(10, 10)
panzoom.zoom(0.9, { animate: false })

// elem.parentElement.addEventListener('wheel', panzoom.zoomWithWheel)