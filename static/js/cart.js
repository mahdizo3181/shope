var updateBtns = document.getElementsByClassName('update-cart');

for (var i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function () {
        var productID = this.dataset.product;
        var action = this.dataset.action;
        console.log('productID', productID, 'action', action);
        console.log("user:", user);
        if (user === 'AnonymousUser') {

            anonymousUserOrder(user)
        } else {
            updateUSerOrder(productID, action, user)
        }

    })
}

function updateUSerOrder(productID, action, user) {
    console.log('user is logged in , sending data ...')

    var url = '/update_item/'

    fetch(url, {
        method: 'POST',
        headers: {
            'Content_Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({'productID': productID, 'action': action, 'user': user})
    })
        .then((response) => {
            return response.json()
        })
        .then((data) => {
            console.log('data:', data)
        })
}

function anonymousUserOrder(user) {
    var url = '/update_item/'

    fetch(url, {
        method: 'POST',
        headers: {
            'Content_Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({'user': user})
    })
        .then((response) => {
            return response.json()
        })
        .then((data) => {
            console.log('data:', data)
        })
}