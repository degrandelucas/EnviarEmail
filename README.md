# Automação de Envio de E-mails para Notas Fiscais Pendentes

Este script em Python tem como objetivo otimizar o envio de e-mails para diferentes contatos de e-mails relacionados a notas fiscais pendentes de entrega. Ele automatiza o processo de envio de e-mails para cada nota fiscal listada em uma planilha, utilizando as informações de cliente, transportadora e destinatários de e-mail fornecidas.

## Funcionalidades Principais

- **Leitura e Tratamento da Planilha:** O script lê uma planilha contendo informações sobre notas fiscais pendentes de entrega e realiza tratamentos necessários nos dados para prepará-los para o envio de e-mails.

- **Envio de E-mails Personalizados:** Para cada linha da planilha, o script dispara um e-mail personalizado, observando a lista de contatos de e-mails associados à nota fiscal, informando sobre a situação da entrega e solicitando verificação.

## Passo a Passo do Projeto

1. **Leitura da Planilha:** O script lê a planilha contendo informações sobre as notas fiscais pendentes de entrega.

2. **Tratamento dos Dados:** Realiza tratamentos necessários nos dados, como remoção de colunas desnecessárias.

3. **Envio de E-mails:** Para cada linha da planilha, o script envia um e-mail personalizado aos destinatários especificados, informando sobre a situação da entrega e solicitando verificação.

## Tecnologias Utilizadas

- **Python:** Utilizado para desenvolver o script de automação do envio de e-mails.
- **Pandas:** Biblioteca utilizada para manipulação e análise de dados, especialmente para trabalhar com a planilha.
- **smtplib:** Módulo utilizado para enviar e-mails através do protocolo SMTP.
- **email.message:** Módulo utilizado para construir e manipular mensagens de e-mail.

## Autor

- **Nome:** Lucas Degrande
- **Contato:** lucasdegrande15@gmail.com
