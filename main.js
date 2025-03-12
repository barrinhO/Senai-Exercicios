let produtosLista = [];
let produtosPreço = [];
let produtosBaratos = []; // menor que 50 reais
let produtos50a100 = []; // entre 50 e 100 reais
let mediaProdutos = 0;
let produto;
let preco;

alert("Digite o nome e o preço de 5 produtos");

for (let i = 0; i < 5; i++) {
    produto = prompt("Digite o nome do produto"); // digitar produto
    preco = parseFloat(prompt("Digite o preço do produto")); // digitar preço
    produtosLista.push(produto); // enviar o produto para a lista
    produtosPreço.push(preco); // enviar o preço para a lista

    if (preco <= 50) {
        produtosBaratos.push(produto);
    }

    if (preco >= 50 && preco <= 100) {
        produtos50a100.push(produto);
    }

    mediaProdutos += preco;
}

mediaProdutos /= 5;

alert(`Há ${produtosBaratos.length} produtos com preço menor ou 50 reais`);
alert(`Há ${produtos50a100.length} produtos com preço entre 50 e 100 reais`);

alert(`Os produtos são: ${produtosLista}`);
alert(`Seus preços são: ${produtosPreço}`);
alert(`A média dos preços dos produtos é de ${mediaProdutos} reais`);

for (let prod in produtosLista) {
    produto += prod + ", ";
}

for (let prec in preco) {
    preco += prec + ", ";
}

alert(produto + "\n" + preco);
