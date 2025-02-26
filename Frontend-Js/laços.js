console.log("Números pares:");
let num = 1;
while (num <= 10) {
    if (num % 2 == 0) {
        console.log(num);
    }
    num++;
    //num--; de trás para frente
}

console.log("Números ímpares:");
let num2 = 1;
while (num2 <= 10) {
    if (num2 % 2 != 0) {
        console.log(num2);
    }
    num2++;
    //num2--; de trás para frente
}

let nome = "",
    nomes = "";

nome += prompt("Digite um nome") + ", ";
nomes += nome + ", ";

while (nome != "pare" && nome != "PARE") {
    nome = prompt("Digite um nome");
    nomes += nome + ", ";
}

alert(nomes);

let valor,
    total = 0;

valor = parseInt(prompt("Digite um valor"));

while (valor != 0) {
    total += valor;
    valor = parseInt(prompt("Digite um valor"));
}

alert(total);
