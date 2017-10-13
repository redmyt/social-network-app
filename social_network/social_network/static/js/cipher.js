function getId(id){
    return document.getElementById(id);
}

    //var forge = require('node-forge'),
    //fs = require('fs');
    // request = require('request');
    // path = require('path');
    // pemFile = path.resolve(__dirname, 'public_key.pem');

    var pubKey = `
-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC8dppTkugfr/OQbN2jJIg9uPpK
w5UoACgImnRaXpVQ0/YHgtswTCaCN8MRN/o/1/zcwSPb4+wZzOAh8zej5LL/2Hjf
1R8sPDUatIA03R2wPKnPSnjfPBhJg+0BWhwoEz6N/med/wZlUx69IBHl34g8UHYk
ZncgbG793eE1xOSJLQIDAQAB
-----END PUBLIC KEY-----
    `;

    function EncryptMessage() {
        
        event.preventDefault();

    var publicKey = forge.pki.publicKeyFromPem(pubKey.toString());
    // console.log(publicKey);

    var secretMessage = getId("message").value;
        if (!secretMessage) return
    var encrypted = publicKey.encrypt(secretMessage, "RSA-OAEP", {
                md: forge.md.sha256.create(),
                mgf1: forge.mgf1.create()
            });
    var base64 = forge.util.encode64(encrypted);
        console.log(base64);
    }

    console.log(EncryptMessage());


