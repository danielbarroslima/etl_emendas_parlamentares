import csv
import datetime
import pandas as pd

def add_log_and_analysis(*, analysis):
  name_file = f'emendas_utf8.csv'
  date_currency = datetime.datetime.now()
  log_anaisys = f'Analise feita em {date_currency}, por Daniel, com o uso do chatgpt 3.5\nAnalise: {analysis}'

  with open(name_file, encoding='utf-8', mode='a', newline='') as file_log:
    file_log.write(f'\n\n{log_anaisys}')

  print(f"log e dados gravados com sucesso'{name_file}'.")
