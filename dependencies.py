import importlib

def install_dependencies():
	dependencies = ['openai', 'openpyxl']

	for dependencie in dependencies:
		try:
			importlib.import_module(dependencie)
			print(f'{dependencie} já instalado(a)')
		except ImportError:
			try:
				import pip
				pip.main(['install', dependencie])
				print(f'{dependencie} Instalado(a)')
			except Exception as e:
				print(f"Erro ao instalar: {str(e)}")

install_dependencies()
