let auth_token;
$(document).ready(function () {
    $.ajax({
        type: 'get',
        url: 'https://www.universal-tutorial.com/api/getaccesstoken',
        success: function (data) {
            console.log(data)
            console.log("hello")
            auth_token = data.auth_token
            getCountry(data.auth_token);
        },
        error: function (error) {
            console.log(error);
        },
        headers: {
            "Accept": "application/json",
            "api-token": "NDUsuG3MOOYEpvT1fst5AeVtw8Km4m6Vu24HMOCTz8UvvmkftG-C7NH0kN5Whu9NVBc",
            "user-email": "nageshmudgal70@gmail.com"
        }

    })

    $('#country').change(function () {
        getState();
    })
})



function getCountry(auth_token) {
    $.ajax({
        type: 'get',
        url: 'https://www.universal-tutorial.com/api/countries/',
        success: function (data) {
            data.forEach(element => {
                $('#country').append('<option value="' + element.country_name + '">' + element.country_name + '</option>');
            });
            //getState(auth_token)
        },
        error: function (error) {
            console.log(error);
        },
        headers: {
            "Authorization": "Bearer" + auth_token,
            "Accept": "application/json"
        }

    })
}


function getState() {
    let country_name = $('#country').val();
    $.ajax({
        type: 'get',
        url: 'https://www.universal-tutorial.com/api/states/' + country_name,
        success: function (data) {
            $('#state').empty();
            data.forEach(element => {
                $('#state').append('<option value="' + element.state_name + '">' + element.state_name + '</option>');
            });
            //getCity (auth_token);
        },
        error: function (error) {
            console.log(error);
        },
        headers: {
            "Authorization": "Bearer " + auth_token,
            "Accept": "application/json"
        }
    })
}


function getCity() {
    let state_name = $('#state').val();
    $.ajax({
        type: 'get',
        url: 'https://www.universal-tutorial.com/api/cities/' + state_name,
        success: function (data) {
            $('#city').empty();
            data.forEach(element => {
                $('#city').append('<option value="' + element.state_name + '">' + element.state_name + '</option>');
            });
        },
        error: function (error) {
            console.log(error);
        },
        headers: {
            "Authorization": "Bearer " + auth_token,
            "Accept": "application/json"
        }
    })
}

