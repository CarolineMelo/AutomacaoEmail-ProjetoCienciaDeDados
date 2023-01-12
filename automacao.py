import pandas as pd
import pyautogui as pa
import time
import pyperclip

tabela = pd.read_excel(r'C:\Users\carlo\OneDrive\Documents\carol\Controle de gastos.xlsx')
print(tabela)
valor = tabela['Valor'].sum()

pa.hotkey('ctrl','t')
time.sleep(2)
pyperclip.copy('https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox')
pa.hotkey('ctrl','v')
pa.press('enter')
time.sleep(2)
#clicar no botão escrever
pa.click(x=1467, y=203)
time.sleep(2)
pa.write('pankamo1@hotmail.com')
pa.press('tab')
pa.press('tab')
pa.write('Controle de Gasto')
pa.press('tab')
time.sleep(2)
texto = f'''Prezado,

Controle-se!

O Nosso gasto está em R${valor:,.2f}
Beijos da Anita
'''
pyperclip.copy(texto)
pa.hotkey('ctrl','v')
time.sleep(2)
pa.hotkey('ctrl','enter')



