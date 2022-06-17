import re


def valida_cpf(cpf):
    cpf = str(cpf)
    cpf = re.sub(r'[^0-9]', '', cpf)

    if not cpf or len(cpf) != 11:
        return False

    novo_cpf = cpf[:-2]         # Remove os dois ultimos digitos do CPF
    reverso = 10                # Contador Reverso
    total = 0

    # CPF Loop
    for index in range(19):
        if index > 8:           # Primeiro indice vai de 0 a 8,
            index -= 9          # Primeiros 9 digitos do CPF

        total += int(novo_cpf[index]) * reverso  # valor da multiplicação

        reverso -= 1  # Decremento do contador reverso
        if reverso < 2:
            reverso = 11
            d = 11 - (total % 11)

            if d > 9:               # Se o digito for > que 9 entao o valor é 0
                d = 0
            total = 0  # Zera o total
            novo_cpf += str(d)  # Concatena o digito do novo cpf

    # Bloqueia CPF sequencial 11111111111
    sequencia = novo_cpf == str(novo_cpf[0]) * len(cpf)

    # Logica para impedir que sequencias sejam avalidas como verdadeiro (true)
    if cpf == novo_cpf and not sequencia:
        return True
    else:
        return False
