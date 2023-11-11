// ==UserScript==
// @name         Lab cripto
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  cripto
// @author       Ignacio
// @match        https://cripto.tiiny.site
// @icon         https://www.google.com/s2/favicons?sz=64&domain=tiiny.site
// @require      https://cdnjs.cloudflare.com/ajax/libs/crypto-js/4.2.0/crypto-js.min.js#sha512-a+SUDuwNzXDvz4XrIcXHuCf089/iJAoN4lmrXJg18XnduKK6YlDHNRalv4yd1N40OKI80tFidF+rqTFKGPoWFQ==
// @grant        none
// ==/UserScript==

(function() {
    'use strict';

    function buscarMayusculas() {
        const texto = document.body.textContent;
        const letrasMayusculas = texto.match(/[A-Z]/g);

        if (letrasMayusculas) {
            const letrasConcatenadas = letrasMayusculas.join('');
            console.log('La llave es:', letrasConcatenadas);
            return letrasConcatenadas;
        } else {
            console.log('No se encontraron letras');
            return "Vacio";
        }
    }

    const claveEncontrada = buscarMayusculas();

    function desencriptarTexto(clave) {
        const elementosConClaseM = document.querySelectorAll('[class*="M"]');
        const numeroElementos = elementosConClaseM.length;

        console.log(`Los mensajes cifrados son :${numeroElementos} `);

        const configuracion = {
            mode: CryptoJS.mode.ECB
        };

        elementosConClaseM.forEach(elemento => {
            const idCifrado = elemento.id;
            const claveCifrado = CryptoJS.enc.Utf8.parse(clave);

            const idDesencriptado = CryptoJS.TripleDES.decrypt(idCifrado, claveCifrado, configuracion);

            console.log(`ID: ${elemento.id}, Texto Desencriptado: ${idDesencriptado.toString(CryptoJS.enc.Utf8)}`);

            const textoDesencriptado = idDesencriptado.toString(CryptoJS.enc.Utf8);
            const elementoH2 = document.createElement('h2');
            elementoH2.textContent = textoDesencriptado;
            document.body.appendChild(elementoH2);
        });
    }

    desencriptarTexto(claveEncontrada);
})();
