from database.db_manager import fetch_all
from utils.csv_exporter import export_to_csv

def export_all_results():
    data = fetch_all()
    export_to_csv(data)
    print("CSV Exported Successfully")