# 📝 Transformador de Texto para Anki - Streamlit

Este é um aplicativo web criado com Streamlit que transforma texto para ser usado no Anki, baseado no script `transformador_anki.py`.

## 🚀 Como executar

### 1. Instalar dependências
```bash
pip install -r requirements.txt
```

### 2. Executar o aplicativo
```bash
streamlit run transformador_anki_streamlit.py
```

### 3. Acessar no navegador
O aplicativo abrirá automaticamente no seu navegador, geralmente em `http://localhost:8501`

## 🎯 Funcionalidades

- **Interface amigável**: Campo de texto para entrada e área de resultado
- **Processamento em tempo real**: Clique no botão para processar o texto
- **Mesmas transformações**: Aplica todas as transformações do script original:
  - Remove linhas que começam com www.*
  - Substitui quebras de linha por `<br>`
  - Substitui 'Gabarito:' por '|Gabarito'
  - Formata números de questões
  - Remove formatação desnecessária

## 📋 Como usar

1. **Cole o texto**: No campo "Texto de entrada", cole o texto que deseja transformar
2. **Processe**: Clique no botão "🔄 Processar Texto"
3. **Copie o resultado**: O texto processado aparecerá na área "Resultado processado"
4. **Use no Anki**: Copie o texto processado e cole no Anki para criar seus flashcards

## 🔧 Transformações aplicadas

O aplicativo aplica as seguintes transformações no texto:

1. **Remove URLs**: Remove linhas que começam com `www.`
2. **Formata quebras de linha**: Substitui `\n` por `<br>`
3. **Formata gabaritos**: Substitui `Gabarito:` por `|Gabarito`
4. **Formata questões**: Substitui números de questões por quebras de linha apropriadas
5. **Limpa formatação**: Remove formatação desnecessária e linhas vazias

## 📁 Arquivos

- `transformador_anki_streamlit.py`: Aplicativo principal
- `requirements.txt`: Dependências necessárias
- `transformador_anki.py`: Script original (para referência)

## 💡 Dicas

- O texto processado está pronto para ser usado diretamente no Anki
- Você pode processar textos longos sem problemas
- O aplicativo mantém o estado entre processamentos
