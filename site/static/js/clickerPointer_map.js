var slov = {
    'open_m': {
        'find': false,
        'filter': false
    }
}



function project_popup(el_id = 0) {
    console.log('project_popup', el_id);
    m_url = 'http://0fc770bdc6b1.ngrok.io/api/0.1/get_circle_data'
    data = {
            "id": el_id,
            'proff': ''
        }
        // q = sender(m_url, data)
    sender(m_url, data).then(data => {


        // console.log('sq', q);
        // popup_title_text popup_icon popup_content popup_timing_1 popup_timing_2

        document.getElementById('popup_title_text').innerText = data['name']

        document.getElementById('popup_icon').src = data['src_img']

        document.getElementById('popup_icon_1').src = data['src_img']

        document.getElementById('popup_content').innerText = data['description']

        document.getElementById('popup_timing_1').innerText = data['theoryDuration'] + ' часов теории'

        document.getElementById('popup_timing_2').innerText = data['practiceDuration'] + ' часов практики'

        document.getElementById('url_page').setAttribute('url_page', data['url_to_page'])

        document.getElementsByClassName('bg_popup')[0].style.display = 'block'


        j_el = document.getElementById('title_url')
        j_el.innerHTML = ''

        for (ell of data['url_url']) {
            el = `
            <h1 id='popup_content' class="ftext popup_content_text" style="cursor:pointer; text-align: center;" url_page=${ell['url']}>
                ${ell['url_name']}
            </h1>
            `
            document.getElementById('title_url').innerHTML += el
        }


    })
}

document.addEventListener('click', function() {
    console.log('sslov', '');
    // console.log(this, arguments);
    cid = arguments[0]['path'][0];
    // console.log(cid);
    for (const el of arguments[0]['path']) {
        if (el.tagName == 'g' && el.id) {
            console.log('id', el.id);
            project_popup(parseInt(el.id.replace('project_popup_', '')))
        }

    }


    if (cid.id) {
        console.log(cid.id);
        // Основное меню
        if (cid.id == 'Instagram') {
            console.log('Представь что у тебя есть соц жизнь');
        }
        if (cid.id == 'Facebook') {
            console.log('узнай как дела у трампа');
        }
        if (cid.id == 'Twitter') {
            console.log('Мммм птишка');
        }

        if (cid.id == 'Продолжить') {
            console.log('перейти к выбору специальности');
        }


        // Выбор профессий
        if (cid.id == 'Программирование') {
            console.log('перейти к тесту');
        }

        if (cid.id.indexOf("answer_") >= 0) {
            console.log('вариант ответа');
        }


        if (cid.id == 'block_close_popup') {
            console.log('закрыть попуп');
            document.getElementsByClassName('popup_block')[0].style.display = 'block'
            document.getElementsByClassName('popup_block')[1].style.display = 'none'
            document.getElementsByClassName('bg_popup')[0].style.display = 'none'
        }
        if (cid.id == 'url_page') {

            window.open(cid.getAttribute('url_page'), '_blank');
        }

        if (cid.id == 'stydy_me') {
            document.getElementsByClassName('popup_block')[0].style.display = 'none'
            document.getElementsByClassName('popup_block')[1].style.display = 'block'
        }

        if (cid.id == 'popup_content') {
            window.open(cid.getAttribute('url_page'), '_blank');
        }


    }
});