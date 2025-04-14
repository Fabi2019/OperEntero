let num1, num2, operacion = "+";

function generarNumeros() {
    num1 = Math.floor(Math.random() * 41) - 20;
    num2 = Math.floor(Math.random() * 41) - 20;
    document.getElementById("numeros").innerText = `${num1} ${getSimbolo()} ${num2}`;
}

function calcularResultado() {
    let resultado;
    switch (operacion) {
        case "+":
            resultado = num1 + num2;
            break;
        case "-":
            resultado = num1 - num2;
            break;
        case "*":
            resultado = num1 * num2;
            break;
        case "/":
            if (num2 !== 0) {
                resultado = num1 / num2;
            } else {
                resultado = "Error: División por cero";
            }
            break;
        default:
            resultado = "Operación no válida";
    }
    document.getElementById("resultado").innerText = `El resultado de ${num1} ${getSimbolo()} ${num2} es ${resultado}`;
}

function getSimbolo() {
    switch (operacion) {
        case "+":
            return "+";
        case "-":
            return "-";
        case "*":
            return "•";
        case "/":
            return "÷";
        default:
            return "";
    }
}

document.getElementById("generar").addEventListener("click", generarNumeros);
document.getElementById("suma").addEventListener("click", () => {
    operacion = "+";
    if (num1 && num2) {
        document.getElementById("numeros").innerText = `${num1} ${getSimbolo()} ${num2}`;
    }
});
document.getElementById("resta").addEventListener("click", () => {
    operacion = "-";
    if (num1 && num2) {
        document.getElementById("numeros").innerText = `${num1} ${getSimbolo()} ${num2}`;
    }
});
document.getElementById("multiplicacion").addEventListener("click", () => {
    operacion = "*";
    if (num1 && num2) {
        document.getElementById("numeros").innerText = `${num1} ${getSimbolo()} ${num2}`;
    }
});
document.getElementById("division").addEventListener("click", () => {
    operacion = "/";
    if (num1 && num2) {
        document.getElementById("numeros").innerText = `${num1} ${getSimbolo()} ${num2}`;
    }
});
document.getElementById("mostrar").addEventListener("click", calcularResultado);

generarNumeros();