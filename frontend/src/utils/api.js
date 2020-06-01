const axios = require("axios");

export default axios.create({
    baseURL: "/api/v1",
    headers: {
        'Authorisation': 'Bearer ' + localStorage.getItem('access_token')
    }
});

// you may add some more api callers and interceptors here
