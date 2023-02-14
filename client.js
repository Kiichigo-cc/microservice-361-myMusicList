const http = require('http');

const options = {
    hostname: 'localhost',
    port: 3000,
    path: '/microservice-361-myMusicList',
    method: 'POST',
    headers: {
        'Content-Type': 'application/x-ww-form-urlencoded',
    }
};

const req = http.request(options, (res) =>{
    console.log('Status: ${res.statusCode}');
});

req.on('error', (error)=>{
    console.error('Error: ${error.message');
})

req.end();