function salvar_contato() {

    const nome_preenchido = document.querySelector("#input_nome").value
    const email_preenchido= document.querySelector("#input_email").value
    const msg_preenchida = document.querySelector("#input_msg").value

    const dados = { nome: nome_preenchido, email: email_preenchido, mensagem: msg_preenchida }

    fetch('http://127.0.0.1:5000/contato', { method: "POST", headers: { "Content-Type": "application/json", }, body: JSON.stringify(dados), }).then((response) => response.json()).then((data) => console.log(data)).catch((error) => console.error("Erro:",error))
}
