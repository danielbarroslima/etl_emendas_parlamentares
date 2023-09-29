import pandas as pd
import locale
import formater_file_for_utf8

locale.setlocale(locale.LC_ALL, 'pt_BR')

data_frame = pd.read_csv('emendas_utf8.csv', sep=';')

def extract_data():
	return attr_values(data_frame)

def attr_values(data_frame):
	dict_values = {
		'valor_empenhado': format_value(data_frame["Valor Empenhado"].tolist()),
		'valor_liquidado': format_value(data_frame["Valor Liquidado"].tolist()),
		'valor_pago': format_value(data_frame["Valor Pago"].tolist()),
		'valor_restos_a_pagar_inscritos': format_value(data_frame["Valor Restos A Pagar Inscritos"].tolist()),
		'valor_restos_a_pagar_cancelados': format_value(data_frame["Valor Restos A Pagar Cancelados"].tolist()),
		'valor_restos_a_pagar_pagos': format_value(data_frame["Valor Restos A Pagar Pagos"].tolist())
	}

	return dict_values

def format_value(values):
	decimal_values = format_decimal(values)
	float_values   = convert_to_float(decimal_values)
	sum_values     = sum(float_values)

	brasilian_currency = locale.format('%.2f', sum_values, grouping=True)

	return brasilian_currency

def format_decimal(list_values):
	return [value.replace(',', '.') for value in list_values]


def convert_to_float(list):
	list_float = [float(value) for value in list]
	return list_float
