let diaSemana = prompt("Digite um dia da semana: ");
diaSemana = diaSemana.toLowerCase();

while (
    diaSemana != "domingo" &&
    diaSemana != "segunda" &&
    diaSemana != "terça" &&
    diaSemana != "quarta" &&
    diaSemana != "quinta" &&
    diaSemana != "sexta" &&
    diaSemana != "sábado"
) {
    diaSemana = prompt("Dia inválido. Digite um dia da semana: ");
    diaSemana = diaSemana.toLowerCase();
}

alert(`Dia da semana: ${diaSemana}`);
