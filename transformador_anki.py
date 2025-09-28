import re

def tratar_texto(texto):
    # 1. Remover linhas que começam com www.*
    texto = re.sub(r'^www\..*\n?', '', texto, flags=re.MULTILINE)

    # 2. Substituir todas as quebras de linha por '<br>'
    texto = texto.replace('\n', '<br>')

    # 3. Substituir 'Gabarito:' por '|Gabarito'
    texto = texto.replace('Gabarito:', '|Gabarito')
    
    # 4. Substituir o número da questão por quebra de linha
    texto = re.sub(r'<br>[0-9][0-9]\)', '<br>\n', texto)    
    texto = re.sub(r'<br>[0-9]\)', '\n', texto)
    
    # 5. Limpar <br> no começo e fim de quebra de linhas e remover linhas não úteis
    texto = texto.replace('<br>\n <br>', '\n')
    texto = texto.replace('\n <br>', '\n')
    texto = texto.replace('<br><br>', '<br>')
    texto = re.sub(r'<br>.<br>', '<br>', texto)
    texto = texto.replace('<br><br>', '<br>')
    texto = re.sub(r'.*Caderno de Questões.*\n', '', texto)

    return texto

def processar_arquivo(arquivo_entrada, arquivo_saida='Flashcards.txt'):
    # Lê o conteúdo do arquivo
    with open(arquivo_entrada, 'r', encoding='utf-8') as f:
        conteudo = f.read()

    # Aplica os tratamentos
    texto_tratado = tratar_texto(conteudo)

    # Salva o resultado no novo arquivo
    with open(arquivo_saida, 'w', encoding='utf-8') as f:
        f.write(texto_tratado)

    print(f"Arquivo processado com sucesso! Resultado salvo em '{arquivo_saida}'.")

nome_arquivo = 'anki.txt'
processar_arquivo(nome_arquivo)

