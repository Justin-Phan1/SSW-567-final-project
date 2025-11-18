# encode_all.py
import json
from MRTD import MRTD


def main():
    # load decoded records
    with open("records_decoded.json", "r") as f:
        data = json.load(f)

    records = data.get("records_decoded", [])
    encoded_records = []

    # encode each record
    for record in records:
        encoded = MRTD.encode_mrz_data(record)
        encoded_records.append(encoded)

    # save encoded MRZ lines
    output = {"records_encoded": encoded_records}
    with open("records_encoded.json", "w") as f:
        json.dump(output, f, indent=4)


if __name__ == "__main__":
    main()
