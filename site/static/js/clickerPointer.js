var slov = {
    'open_m': {
        'find': false,
        'filter': false
    }
}
document.addEventListener('click', function() {
    // //console.log('sslov', slov);
    // //console.log(this, arguments);
    cid = arguments[0]['path'][0];
    //console.log(arguments[0]);
    //console.log(cid)
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


    }
});