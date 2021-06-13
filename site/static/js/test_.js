var data_user = []
var now_question = 0
m_url = 'http://0fc770bdc6b1.ngrok.io/api/0.1/questions_and_img'
data_send = {
    "profession": "Программист"
}
var qdata_q;
sender(m_url, data_send).then(data_q => {
    // print(data_q)
    qdata_q = data_q
    document.addEventListener('click', function() {
        console.log('sslov', 0);
        // console.log(this, arguments);
        cid = arguments[0]['path'][0];
        // console.log(cid);
        if (cid.id) {
            if (cid.id.indexOf("answer_") >= 0) {
                console.log('вариант ответа', cid.id.replace('answer_', ''));
                new_image()

                // console.log(cid);
            }
        }
    })

    function new_image() {
        j_el_1 = document.getElementById('answer_1')
        j_el_2 = document.getElementById('answer_2')

        console.log(j_el_1, qdata_q['elements']["questions"][now_question]['answers'][0]['img']);

        j_el_1.style = `background-image: url(../static/photo/${qdata_q['elements']["questions"][now_question]['answers'][0]['img']});`
            // j_el_2.style.backgroundImage = qdata_q['elements']["questions"][now_question]['answers'][0]['img']
    }

    new_image()
})