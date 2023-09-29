from transform import generate_api_analysis
from load      import add_log_and_analysis

def etl_transform():
	analysis = generate_api_analysis()
	add_log_and_analysis(analysis=analysis)

etl_transform()
