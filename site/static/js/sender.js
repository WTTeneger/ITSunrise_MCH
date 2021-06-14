async function sender(url, data, method = 'post') {
    var m_url = location.hostname

    url = m_url + url
    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");

    var raw = JSON.stringify(data);

    var requestOptions = {
        method: 'POST',
        headers: myHeaders,
        body: raw,
        // redirect: 'follow'
    };
    let response = await fetch(url, requestOptions);
    // let json;
    if (response.ok) { // если HTTP-статус в диапазоне 200-299
        // получаем тело ответа (см. про этот метод ниже)
        json = await response.json();
        // console.log(json);
        return (json)

    } else {
        console.log("Ошибка HTTP: " + response.status);
    }

};

// url = m_url + 'api/0.1/get_circle_data'

// data = { "id": 1 }

// otv = sender(url, data)
// console.log(otv);
// el = document.getElementById('qq')
// console.log(el);
// el.innerText = otv['description']
// console.log(otv['description']);

// console.log(otv);