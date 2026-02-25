import csv

def export_to_csv(data, filename="output.csv"):
    with open(filename,"w",newline='',encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["id","text","score","tag","time"])
        writer.writerows(data)