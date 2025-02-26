// testes prompt

let n1, n2, n3, media;

n1 = parseFloat(prompt('Digite a sua primeira nota: '));
n2 = parseFloat(prompt('Digite a sua segunda nota: '));
n3 = parseFloat(prompt('Digite a sua terceira nota: '));

media = (n1 + n2 + n3) / 3;

console.log(`Sua media final: ${media.toFixed(1)}`);

if (media >= 7) {
    alert('Aprovado!');
} else if (media < 7) {
    alert('Recuperação');
} else if (media <= 4) {
    alert('Reprovado');
}
