const request = new XMLHttpRequest();
request.addEventListener('load', (event) => {
    const pictures = JSON.parse(event.target.response);
    const tableBody = document.getElementById('tableBody');
    for(let picture of pictures) {
        const img = document.createElement('img');
        img.src = `data:img/jpeg;base64,${picture.blob}`;
        const idData = document.createElement('td');
        idData.className = 'id';
        idData.innerHTML = picture.id;
        const pictureData = document.createElement('td');
        pictureData.appendChild(img);
        const labelData = document.createElement('td');
        labelData.className = 'label';
        labelData.innerHTML = picture.label;
        const row = document.createElement('tr');
        row.append(idData, pictureData, labelData)
        tableBody.appendChild(row);
    }
});
request.addEventListener('error', (event) => {
    console.log('error', event)
});
request.open('GET', '/pictures');
request.send();