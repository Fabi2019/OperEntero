
// Selecciona los botones de operación
const suma = document.getElementById('suma');
const resta = document.getElementById('resta');
const multiplicacion = document.getElementById('multiplicacion');
const division = document.getElementById('division');
const generarNumerosBtn = document.getElementById('generar');
const enviarBtn = document.getElementById('enviar');

// Selecciona los labels de las opciones
const labelOpcion1 = document.getElementById('label-opcion1');
const labelOpcion2 = document.getElementById('label-opcion2');
const labelOpcion3 = document.getElementById('label-opcion3');

// Selecciona el párrafo para mostrar los números
const numeros = document.getElementById('numeros');
const resultadoOpcion = document.getElementById('resultado-opcion');

let operacionActual = "suma";
let respuestaCorrecta;
let num1;
let num2;


// Función para generar números aleatorios
function generarNumeros() {
    num1 = Math.floor(Math.random() * 20) + -20;
    num2 = Math.floor(Math.random() * 20) + -20;
    return [num1, num2];
}

// Función para actualizar las opciones
function actualizarOpciones(operacion, num1, num2) {
    let resultado;
    switch (operacion) {
        case 'suma':
            resultado = num1 + num2;
            break;
        case 'resta':
            resultado = num1 - num2;
            break;
        case 'multiplicacion':
            resultado = num1 * num2;
            break;
        case 'division':
            resultado = num1 / num2;
            break;
    }

    respuestaCorrecta = resultado;

    const opciones = [resultado, resultado + 10, resultado - 10];
    const opcionesAleatorias = opciones.sort(() => Math.random() - 0.5);
    labelOpcion1.textContent = opcionesAleatorias[0];
    labelOpcion2.textContent = opcionesAleatorias[1];
    labelOpcion3.textContent = opcionesAleatorias[2];
}

// Función para mostrar los números
function mostrarNumeros(num1, num2, operacion) {
    let operador;
    switch (operacion) {
        case 'suma':
            operador = '+';
            break;
        case 'resta':
            operador = '-';
            break;
        case 'multiplicacion':
            operador = '•';
            break;
        case 'division':
            operador = '÷';
            break;
    }
    numeros.textContent = `${num1} ${operador} ${num2} =`;
}

// Eventos para los botones de operación
suma.addEventListener('click', () => {
    operacionActual = 'suma';
    [num1, num2] = generarNumeros();
    mostrarNumeros(num1, num2, 'suma');
    actualizarOpciones('suma', num1, num2);
});

resta.addEventListener('click', () => {
    operacionActual = 'resta';
    [num1, num2] = generarNumeros();
    mostrarNumeros(num1, num2, 'resta');
    actualizarOpciones('resta', num1, num2);
});

multiplicacion.addEventListener('click', () => {
    operacionActual = 'multiplicacion';
    [num1, num2] = generarNumeros();
    mostrarNumeros(num1, num2, 'multiplicacion');
    actualizarOpciones('multiplicacion', num1, num2);
});

division.addEventListener('click', () => {
    operacionActual = 'division';
    [num1, num2] = generarNumeros();
    mostrarNumeros(num1, num2, 'division');
    actualizarOpciones('division', num1, num2);
});

generarNumerosBtn.addEventListener('click', () => {
    if (operacionActual) {
        [num1, num2] = generarNumeros();
        mostrarNumeros(num1, num2, operacionActual);
        actualizarOpciones(operacionActual, num1, num2);
    }
});

enviarBtn.addEventListener('click', () => {
    const opciones = document.getElementsByName('opcion');
    let respuesta;
    for (let i = 0; i < opciones.length; i++) {
        if (opciones[i].checked) {
            respuesta = opciones[i].nextElementSibling.textContent;
            break;
        }
    }
    if (respuesta == respuestaCorrecta) {
        resultadoOpcion.textContent = ` ${respuesta} ¡Correcto!`;
    } else {
        resultadoOpcion.textContent = `La respuesta es Incorrecta`;
    }
});



let num= generarNumeros();
mostrarNumeros(num[0], num[1], 'suma');
actualizarOpciones(operacionActual, num[0], num[1]);