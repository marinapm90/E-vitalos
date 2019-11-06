import csv
import json


fieldnames = ("id","tipo","origen","aditivo","clasificación","aditivos_alergicos")

with open('./additives.csv', 'r') as csvfile:
    with open('./additives.json', 'w') as jsonfile:
        
        next(csvfile)
        
        reader = csv.DictReader(csvfile, fieldnames)
        
        final_data = {}
         
        for row in reader:
            # We also restructure the data so that it exists as 
            # a set of date keys with the value as a dictionary of
            # different data elements from the CSV.
            final_data[row["id"]] = {
                "id": row["id"],
                "tipo": row["tipo"],
                "origen": row["origen"],
                "aditivo": row["aditivo"],
                "clasificación": row["clasificación"],
                "aditivos_alergicos": row["aditivos_alergicos"]
            }
        
        json.dump(final_data, jsonfile)
        
        jsonfile.write('\n')