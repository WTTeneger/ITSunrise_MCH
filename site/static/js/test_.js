var data_user = []
var now_question = 0
m_url = '/api/0.1/questions_and_img'
data_send = {
    "profession": "Программист"
}
var get_nr = false;
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
            if (cid.id.indexOf("answer_") >= 0 && get_nr == false) {
                console.log('вариант ответа', cid.id.replace('answer_', ''));

                console.log(data_user);
                // data_user.push(parseInt(cid.id.replace('answer_', '')));
                data_user.push(parseInt(cid.id.replace('answer_', '')));
                console.log(data_user.length, qdata_q['elements']["questions"].length);
                if (data_user.length < qdata_q['elements']["questions"].length) {
                    new_image()
                } else {
                    get_nr = true
                    document.getElementsByClassName('main_test_block')[0].style = 'display: none;'
                    m_url = '/api/0.1/neyrondata'
                    data_send = {
                        "neyron": data_user
                    }
                    sender(m_url, data_send).then(data_neyron => {
                        console.log(data_neyron);
                        document.getElementById('prof_recom').innerText = data_neyron['word']
                        document.getElementsByClassName('main_test_block')[1].style = 'top: 22vh; display: block;'

                    })
                };

                // console.log(cid);
            }

            if (cid.id == 'go_circl') {
                document.location.href = "cr";
            }
        }
    })

    function new_image() {
        j_el_1 = document.getElementById('answer_1')
        j_el_2 = document.getElementById('answer_0')


        console.log(j_el_1, qdata_q['elements']["questions"][now_question]['answers'][0]['img']);

        j_el_1.style = `background-image: url(../static/photo/${qdata_q['elements']["questions"][now_question]['answers'][0]['img']});`
        j_el_1.getElementsByTagName('h1')[0].innerText = qdata_q['elements']["questions"][now_question]['answers'][0]['answer']

        j_el_2.style = `background-image: url(../static/photo/${qdata_q['elements']["questions"][now_question]['answers'][1]['img']});`
        j_el_2.getElementsByTagName('h1')[0].innerText = qdata_q['elements']["questions"][now_question]['answers'][1]['answer']


        now_question += 1
            // j_el_2.style.backgroundImage = qdata_q['elements']["questions"][now_question]['answers'][0]['img']
    }

    new_image()
})