#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import smtplib
import email.message
import pandas as pd

def enviar_email(Nota, Cliente, Transportadora, EmailDestinatarios):  
    corpo_email = """
    <p>Olá</p>
    <p>Por favor, podem verificar em relação à entrega da NF?</p>
    """

    msg = email.message.Message()
    msg['Subject'] = f"NF {Nota} {Cliente} x Transportadora {Transportadora}"
    msg['From'] = 'lucas.degrande@bmchyundai.com.br'
    Destinatarios = EmailDestinatarios.split(',')
    msg['To'] = ', '.join(Destinatarios)
    password = 'wssbhscozclgrphe' 
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login com as credenciais s.login e enviar os emails com s.sendmail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], Destinatarios, msg.as_string().encode('utf-8'))
    print(f'E-mails enviados para: {Destinatarios}')
    print('Email enviado')
    
planilha = pd.read_excel('TE_Disparo.xlsx')
colunas_para_deletar = ['Cliente DOC','Cidade','UF','Ocorrencia','Vendedor','DATA','1º Data PENSKE','TE','Mínimo','Máximo','Sinal','NOTA.1','Observação','DATA ENTREGA','14.168.536/0001-25','14168536000125']
planilha = planilha.drop(columns=colunas_para_deletar)

print(planilha)

for CadaLinha, row in planilha.iterrows():
    Nota = row['NOTA']
    Cliente = row['Cliente']
    Transportadora = row['Transportadora']
    EmailDestinatarios = row['EmailDestinatarios']

    enviar_email(Nota, Cliente, Transportadora, EmailDestinatarios)

# In[ ]:




