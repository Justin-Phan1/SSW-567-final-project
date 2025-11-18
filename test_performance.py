import csv
import json
import time
from MRTD import MRTD
from MTTDtest import TestMRTD


# Use encoded records data JSON file for decoding section
with open("records_encoded.json", "r") as f:
    encoded_json_data = json.load(f)


# Use decoded records data JSON file for encoding section
with open("records_decoded.json", "r") as f:
    decoded_json_data = json.load(f)


'''
Decoding section
'''
'''
First 100 records
'''
# no tests
start_time_decode_100_no_tests = time.perf_counter() # start timer
# Loop over the first 100 records
for i, record in enumerate(encoded_json_data["records_encoded"][:100], start=1):
    line1, line2 = record.split(";") # Split the record into line1 and line2
MRTD.decode_mrz_data(line1, line2)
stop_time_decode_100_no_tests = time.perf_counter() # stop timer
elapsed_time_decode_100_no_tests = stop_time_decode_100_no_tests - start_time_decode_100_no_tests # calculate total execution time
print("Execution times for decoding function: \n")
print("Execution time for decoding first 100 records without tests: " + str(elapsed_time_decode_100_no_tests) + " seconds") # print the execution time


# with tests
start_time_decode_100_tests = time.perf_counter() # start timer
# Loop over the first 100 records
for i, record in enumerate(encoded_json_data["records_encoded"][:100], start=1):
    line1, line2 = record.split(";") # Split the record into line1 and line2
MRTD.decode_mrz_data(line1, line2)
line1 = "P<UTOERIKSSON<<ANNA<MARIA<<<<<<<<<<<<<<<<<<<"
line2 = "L898902C36UTO7408122F1204159ZE184226B<<<<<<1"
decoded = MRTD.decode_mrz_data(line1, line2)
# Unit test assertions
assert isinstance(decoded, dict)
assert decoded["passport_type"] == "P"
assert decoded["issuing_country"] == "UTO"
assert decoded["surname"] == "ERIKSSON"
assert decoded["given_names"] == "ANNA MARIA"
assert decoded["passport_number"] == "L898902C3"
assert decoded["check_digit_1"] == "6"
assert decoded["country_code"] == "UTO"
assert decoded["birth_date"] == "740812"
assert decoded["gender"] == "F"
assert decoded["expiration_date"] == "120415"
assert decoded["check_digit_4"] == "1"
stop_time_decode_100_tests = time.perf_counter() # stop timer
elapsed_time_decode_100_tests = stop_time_decode_100_tests - start_time_decode_100_tests # calculate total execution time
print("Execution time for decoding first 100 records with tests: " + str(elapsed_time_decode_100_tests) + " seconds") # print the execution time


'''
First 1000 records
'''
# no tests
start_time_decode_1000_no_tests = time.perf_counter() # start timer
# Loop over the first 1000 records
for i, record in enumerate(encoded_json_data["records_encoded"][:1000], start=1):
    line1, line2 = record.split(";") # Split the record into line1 and line2
MRTD.decode_mrz_data(line1, line2)
stop_time_decode_1000_no_tests = time.perf_counter() # stop timer
elapsed_time_decode_1000_no_tests = stop_time_decode_1000_no_tests - start_time_decode_1000_no_tests # calculate total execution time
print("Execution time for decoding first 1000 records without tests: " + str(elapsed_time_decode_1000_no_tests) + " seconds") # print the execution time


# with tests
start_time_decode_1000_tests = time.perf_counter() # start timer
# Loop over the first 1000 records
for i, record in enumerate(encoded_json_data["records_encoded"][:1000], start=1):
    line1, line2 = record.split(";") # Split the record into line1 and line2
MRTD.decode_mrz_data(line1, line2)
line1 = "P<UTOERIKSSON<<ANNA<MARIA<<<<<<<<<<<<<<<<<<<"
line2 = "L898902C36UTO7408122F1204159ZE184226B<<<<<<1"
decoded = MRTD.decode_mrz_data(line1, line2)
# Unit test assertions
assert isinstance(decoded, dict)
assert decoded["passport_type"] == "P"
assert decoded["issuing_country"] == "UTO"
assert decoded["surname"] == "ERIKSSON"
assert decoded["given_names"] == "ANNA MARIA"
assert decoded["passport_number"] == "L898902C3"
assert decoded["check_digit_1"] == "6"
assert decoded["country_code"] == "UTO"
assert decoded["birth_date"] == "740812"
assert decoded["gender"] == "F"
assert decoded["expiration_date"] == "120415"
assert decoded["check_digit_4"] == "1"
stop_time_decode_1000_tests = time.perf_counter() # stop timer
elapsed_time_decode_1000_tests = stop_time_decode_1000_tests - start_time_decode_1000_tests # calculate total execution time
print("Execution time for decoding first 1000 records with tests: " + str(elapsed_time_decode_1000_tests) + " seconds") # print the execution time


'''
First 2000 records
'''
# no tests
start_time_decode_2000_no_tests = time.perf_counter() # start timer
# Loop over the first 2000 records
for i, record in enumerate(encoded_json_data["records_encoded"][:2000], start=1):
    line1, line2 = record.split(";") # Split the record into line1 and line2
MRTD.decode_mrz_data(line1, line2)
stop_time_decode_2000_no_tests = time.perf_counter() # stop timer
elapsed_time_decode_2000_no_tests = stop_time_decode_2000_no_tests - start_time_decode_2000_no_tests # calculate total execution time
print("Execution time for decoding first 2000 records without tests: " + str(elapsed_time_decode_2000_no_tests) + " seconds") # print the execution time


# with tests
start_time_decode_2000_tests = time.perf_counter() # start timer
# Loop over the first 2000 records
for i, record in enumerate(encoded_json_data["records_encoded"][:2000], start=1):
    line1, line2 = record.split(";") # Split the record into line1 and line2
MRTD.decode_mrz_data(line1, line2)
line1 = "P<UTOERIKSSON<<ANNA<MARIA<<<<<<<<<<<<<<<<<<<"
line2 = "L898902C36UTO7408122F1204159ZE184226B<<<<<<1"
decoded = MRTD.decode_mrz_data(line1, line2)
# Unit test assertions
assert isinstance(decoded, dict)
assert decoded["passport_type"] == "P"
assert decoded["issuing_country"] == "UTO"
assert decoded["surname"] == "ERIKSSON"
assert decoded["given_names"] == "ANNA MARIA"
assert decoded["passport_number"] == "L898902C3"
assert decoded["check_digit_1"] == "6"
assert decoded["country_code"] == "UTO"
assert decoded["birth_date"] == "740812"
assert decoded["gender"] == "F"
assert decoded["expiration_date"] == "120415"
assert decoded["check_digit_4"] == "1"
stop_time_decode_2000_tests = time.perf_counter() # stop timer
elapsed_time_decode_2000_tests = stop_time_decode_2000_tests - start_time_decode_2000_tests # calculate total execution time
print("Execution time for decoding first 2000 records with tests: " + str(elapsed_time_decode_2000_tests) + " seconds") # print the execution time


'''
First 3000 records
'''
# no tests
start_time_decode_3000_no_tests = time.perf_counter() # start timer
# Loop over the first 3000 records
for i, record in enumerate(encoded_json_data["records_encoded"][:3000], start=1):
    line1, line2 = record.split(";") # Split the record into line1 and line2
MRTD.decode_mrz_data(line1, line2)
stop_time_decode_3000_no_tests = time.perf_counter() # stop timer
elapsed_time_decode_3000_no_tests = stop_time_decode_3000_no_tests - start_time_decode_3000_no_tests # calculate total execution time
print("Execution time for decoding first 3000 records without tests: " + str(elapsed_time_decode_3000_no_tests) + " seconds") # print the execution time


# with tests
start_time_decode_3000_tests = time.perf_counter() # start timer
# Loop over the first 3000 records
for i, record in enumerate(encoded_json_data["records_encoded"][:3000], start=1):
    line1, line2 = record.split(";") # Split the record into line1 and line2
MRTD.decode_mrz_data(line1, line2)
line1 = "P<UTOERIKSSON<<ANNA<MARIA<<<<<<<<<<<<<<<<<<<"
line2 = "L898902C36UTO7408122F1204159ZE184226B<<<<<<1"
decoded = MRTD.decode_mrz_data(line1, line2)
# Unit test assertions
assert isinstance(decoded, dict)
assert decoded["passport_type"] == "P"
assert decoded["issuing_country"] == "UTO"
assert decoded["surname"] == "ERIKSSON"
assert decoded["given_names"] == "ANNA MARIA"
assert decoded["passport_number"] == "L898902C3"
assert decoded["check_digit_1"] == "6"
assert decoded["country_code"] == "UTO"
assert decoded["birth_date"] == "740812"
assert decoded["gender"] == "F"
assert decoded["expiration_date"] == "120415"
assert decoded["check_digit_4"] == "1"
stop_time_decode_3000_tests = time.perf_counter() # stop timer
elapsed_time_decode_3000_tests = stop_time_decode_3000_tests - start_time_decode_3000_tests # calculate total execution time
print("Execution time for decoding first 3000 records with tests: " + str(elapsed_time_decode_3000_tests) + " seconds") # print the execution time


'''
First 4000 records
'''
# no tests
start_time_decode_4000_no_tests = time.perf_counter() # start timer
# Loop over the first 4000 records
for i, record in enumerate(encoded_json_data["records_encoded"][:4000], start=1):
    line1, line2 = record.split(";") # Split the record into line1 and line2
MRTD.decode_mrz_data(line1, line2)
stop_time_decode_4000_no_tests = time.perf_counter() # stop timer
elapsed_time_decode_4000_no_tests = stop_time_decode_4000_no_tests - start_time_decode_4000_no_tests # calculate total execution time
print("Execution time for decoding first 4000 records without tests: " + str(elapsed_time_decode_4000_no_tests) + " seconds") # print the execution time


# with tests
start_time_decode_4000_tests = time.perf_counter() # start timer
# Loop over the first 4000 records
for i, record in enumerate(encoded_json_data["records_encoded"][:4000], start=1):
    line1, line2 = record.split(";") # Split the record into line1 and line2
MRTD.decode_mrz_data(line1, line2)
line1 = "P<UTOERIKSSON<<ANNA<MARIA<<<<<<<<<<<<<<<<<<<"
line2 = "L898902C36UTO7408122F1204159ZE184226B<<<<<<1"
decoded = MRTD.decode_mrz_data(line1, line2)
# Unit test assertions
assert isinstance(decoded, dict)
assert decoded["passport_type"] == "P"
assert decoded["issuing_country"] == "UTO"
assert decoded["surname"] == "ERIKSSON"
assert decoded["given_names"] == "ANNA MARIA"
assert decoded["passport_number"] == "L898902C3"
assert decoded["check_digit_1"] == "6"
assert decoded["country_code"] == "UTO"
assert decoded["birth_date"] == "740812"
assert decoded["gender"] == "F"
assert decoded["expiration_date"] == "120415"
assert decoded["check_digit_4"] == "1"
stop_time_decode_4000_tests = time.perf_counter() # stop timer
elapsed_time_decode_4000_tests = stop_time_decode_4000_tests - start_time_decode_4000_tests # calculate total execution time
print("Execution time for decoding first 4000 records with tests: " + str(elapsed_time_decode_4000_tests) + " seconds") # print the execution time


'''
First 5000 records
'''
# no tests
start_time_decode_5000_no_tests = time.perf_counter() # start timer
# Loop over the first 5000 records
for i, record in enumerate(encoded_json_data["records_encoded"][:5000], start=1):
    line1, line2 = record.split(";") # Split the record into line1 and line2
MRTD.decode_mrz_data(line1, line2)
stop_time_decode_5000_no_tests = time.perf_counter() # stop timer
elapsed_time_decode_5000_no_tests = stop_time_decode_5000_no_tests - start_time_decode_5000_no_tests # calculate total execution time
print("Execution time for decoding first 5000 records without tests: " + str(elapsed_time_decode_5000_no_tests) + " seconds") # print the execution time


# with tests
start_time_decode_5000_tests = time.perf_counter() # start timer
# Loop over the first 5000 records
for i, record in enumerate(encoded_json_data["records_encoded"][:5000], start=1):
    line1, line2 = record.split(";") # Split the record into line1 and line2
MRTD.decode_mrz_data(line1, line2)
line1 = "P<UTOERIKSSON<<ANNA<MARIA<<<<<<<<<<<<<<<<<<<"
line2 = "L898902C36UTO7408122F1204159ZE184226B<<<<<<1"
decoded = MRTD.decode_mrz_data(line1, line2)
# Unit test assertions
assert isinstance(decoded, dict)
assert decoded["passport_type"] == "P"
assert decoded["issuing_country"] == "UTO"
assert decoded["surname"] == "ERIKSSON"
assert decoded["given_names"] == "ANNA MARIA"
assert decoded["passport_number"] == "L898902C3"
assert decoded["check_digit_1"] == "6"
assert decoded["country_code"] == "UTO"
assert decoded["birth_date"] == "740812"
assert decoded["gender"] == "F"
assert decoded["expiration_date"] == "120415"
assert decoded["check_digit_4"] == "1"
stop_time_decode_5000_tests = time.perf_counter() # stop timer
elapsed_time_decode_5000_tests = stop_time_decode_5000_tests - start_time_decode_5000_tests # calculate total execution time
print("Execution time for decoding first 5000 records with tests: " + str(elapsed_time_decode_5000_tests) + " seconds") # print the execution time


'''
First 6000 records
'''
# no tests
start_time_decode_6000_no_tests = time.perf_counter() # start timer
# Loop over the first 6000 records
for i, record in enumerate(encoded_json_data["records_encoded"][:6000], start=1):
    line1, line2 = record.split(";") # Split the record into line1 and line2
MRTD.decode_mrz_data(line1, line2)
stop_time_decode_6000_no_tests = time.perf_counter() # stop timer
elapsed_time_decode_6000_no_tests = stop_time_decode_6000_no_tests - start_time_decode_6000_no_tests # calculate total execution time
print("Execution time for decoding first 6000 records without tests: " + str(elapsed_time_decode_6000_no_tests) + " seconds") # print the execution time


# with tests
start_time_decode_6000_tests = time.perf_counter() # start timer
# Loop over the first 6000 records
for i, record in enumerate(encoded_json_data["records_encoded"][:6000], start=1):
    line1, line2 = record.split(";") # Split the record into line1 and line2
MRTD.decode_mrz_data(line1, line2)
line1 = "P<UTOERIKSSON<<ANNA<MARIA<<<<<<<<<<<<<<<<<<<"
line2 = "L898902C36UTO7408122F1204159ZE184226B<<<<<<1"
decoded = MRTD.decode_mrz_data(line1, line2)
# Unit test assertions
assert isinstance(decoded, dict)
assert decoded["passport_type"] == "P"
assert decoded["issuing_country"] == "UTO"
assert decoded["surname"] == "ERIKSSON"
assert decoded["given_names"] == "ANNA MARIA"
assert decoded["passport_number"] == "L898902C3"
assert decoded["check_digit_1"] == "6"
assert decoded["country_code"] == "UTO"
assert decoded["birth_date"] == "740812"
assert decoded["gender"] == "F"
assert decoded["expiration_date"] == "120415"
assert decoded["check_digit_4"] == "1"
stop_time_decode_6000_tests = time.perf_counter() # stop timer
elapsed_time_decode_6000_tests = stop_time_decode_6000_tests - start_time_decode_6000_tests # calculate total execution time
print("Execution time for decoding first 6000 records with tests: " + str(elapsed_time_decode_6000_tests) + " seconds") # print the execution time


'''
First 7000 records
'''
# no tests
start_time_decode_7000_no_tests = time.perf_counter() # start timer
# Loop over the first 7000 records
for i, record in enumerate(encoded_json_data["records_encoded"][:7000], start=1):
    line1, line2 = record.split(";") # Split the record into line1 and line2
MRTD.decode_mrz_data(line1, line2)
stop_time_decode_7000_no_tests = time.perf_counter() # stop timer
elapsed_time_decode_7000_no_tests = stop_time_decode_7000_no_tests - start_time_decode_7000_no_tests # calculate total execution time
print("Execution time for decoding first 7000 records without tests: " + str(elapsed_time_decode_7000_no_tests) + " seconds") # print the execution time


# with tests
start_time_decode_7000_tests = time.perf_counter() # start timer
# Loop over the first 7000 records
for i, record in enumerate(encoded_json_data["records_encoded"][:7000], start=1):
    line1, line2 = record.split(";") # Split the record into line1 and line2
MRTD.decode_mrz_data(line1, line2)
line1 = "P<UTOERIKSSON<<ANNA<MARIA<<<<<<<<<<<<<<<<<<<"
line2 = "L898902C36UTO7408122F1204159ZE184226B<<<<<<1"
decoded = MRTD.decode_mrz_data(line1, line2)
# Unit test assertions
assert isinstance(decoded, dict)
assert decoded["passport_type"] == "P"
assert decoded["issuing_country"] == "UTO"
assert decoded["surname"] == "ERIKSSON"
assert decoded["given_names"] == "ANNA MARIA"
assert decoded["passport_number"] == "L898902C3"
assert decoded["check_digit_1"] == "6"
assert decoded["country_code"] == "UTO"
assert decoded["birth_date"] == "740812"
assert decoded["gender"] == "F"
assert decoded["expiration_date"] == "120415"
assert decoded["check_digit_4"] == "1"
stop_time_decode_7000_tests = time.perf_counter() # stop timer
elapsed_time_decode_7000_tests = stop_time_decode_7000_tests - start_time_decode_7000_tests # calculate total execution time
print("Execution time for decoding first 7000 records with tests: " + str(elapsed_time_decode_7000_tests) + " seconds") # print the execution time


'''
First 8000 records
'''
# no tests
start_time_decode_8000_no_tests = time.perf_counter() # start timer
# Loop over the first 8000 records
for i, record in enumerate(encoded_json_data["records_encoded"][:8000], start=1):
    line1, line2 = record.split(";") # Split the record into line1 and line2
MRTD.decode_mrz_data(line1, line2)
stop_time_decode_8000_no_tests = time.perf_counter() # stop timer
elapsed_time_decode_8000_no_tests = stop_time_decode_8000_no_tests - start_time_decode_8000_no_tests # calculate total execution time
print("Execution time for decoding first 8000 records without tests: " + str(elapsed_time_decode_8000_no_tests) + " seconds") # print the execution time


# with tests
start_time_decode_8000_tests = time.perf_counter() # start timer
# Loop over the first 8000 records
for i, record in enumerate(encoded_json_data["records_encoded"][:8000], start=1):
    line1, line2 = record.split(";") # Split the record into line1 and line2
MRTD.decode_mrz_data(line1, line2)
line1 = "P<UTOERIKSSON<<ANNA<MARIA<<<<<<<<<<<<<<<<<<<"
line2 = "L898902C36UTO7408122F1204159ZE184226B<<<<<<1"
decoded = MRTD.decode_mrz_data(line1, line2)
# Unit test assertions
assert isinstance(decoded, dict)
assert decoded["passport_type"] == "P"
assert decoded["issuing_country"] == "UTO"
assert decoded["surname"] == "ERIKSSON"
assert decoded["given_names"] == "ANNA MARIA"
assert decoded["passport_number"] == "L898902C3"
assert decoded["check_digit_1"] == "6"
assert decoded["country_code"] == "UTO"
assert decoded["birth_date"] == "740812"
assert decoded["gender"] == "F"
assert decoded["expiration_date"] == "120415"
assert decoded["check_digit_4"] == "1"
stop_time_decode_8000_tests = time.perf_counter() # stop timer
elapsed_time_decode_8000_tests = stop_time_decode_8000_tests - start_time_decode_8000_tests # calculate total execution time
print("Execution time for decoding first 8000 records with tests: " + str(elapsed_time_decode_8000_tests) + " seconds") # print the execution time


'''
First 9000 records
'''
# no tests
start_time_decode_9000_no_tests = time.perf_counter() # start timer
# Loop over the first 9000 records
for i, record in enumerate(encoded_json_data["records_encoded"][:9000], start=1):
    line1, line2 = record.split(";") # Split the record into line1 and line2
MRTD.decode_mrz_data(line1, line2)
stop_time_decode_9000_no_tests = time.perf_counter() # stop timer
elapsed_time_decode_9000_no_tests = stop_time_decode_9000_no_tests - start_time_decode_9000_no_tests # calculate total execution time
print("Execution time for decoding first 9000 records without tests: " + str(elapsed_time_decode_9000_no_tests) + " seconds") # print the execution time


# with tests
start_time_decode_9000_tests = time.perf_counter() # start timer
# Loop over the first 9000 records
for i, record in enumerate(encoded_json_data["records_encoded"][:9000], start=1):
    line1, line2 = record.split(";") # Split the record into line1 and line2
MRTD.decode_mrz_data(line1, line2)
line1 = "P<UTOERIKSSON<<ANNA<MARIA<<<<<<<<<<<<<<<<<<<"
line2 = "L898902C36UTO7408122F1204159ZE184226B<<<<<<1"
decoded = MRTD.decode_mrz_data(line1, line2)
# Unit test assertions
assert isinstance(decoded, dict)
assert decoded["passport_type"] == "P"
assert decoded["issuing_country"] == "UTO"
assert decoded["surname"] == "ERIKSSON"
assert decoded["given_names"] == "ANNA MARIA"
assert decoded["passport_number"] == "L898902C3"
assert decoded["check_digit_1"] == "6"
assert decoded["country_code"] == "UTO"
assert decoded["birth_date"] == "740812"
assert decoded["gender"] == "F"
assert decoded["expiration_date"] == "120415"
assert decoded["check_digit_4"] == "1"
stop_time_decode_9000_tests = time.perf_counter() # stop timer
elapsed_time_decode_9000_tests = stop_time_decode_9000_tests - start_time_decode_9000_tests # calculate total execution time
print("Execution time for decoding first 9000 records with tests: " + str(elapsed_time_decode_9000_tests) + " seconds") # print the execution time


'''
First 10000 records
'''
# no tests
start_time_decode_10000_no_tests = time.perf_counter() # start timer
# Loop over the first 10000 records
for i, record in enumerate(encoded_json_data["records_encoded"][:10000], start=1):
    line1, line2 = record.split(";") # Split the record into line1 and line2
MRTD.decode_mrz_data(line1, line2)
stop_time_decode_10000_no_tests = time.perf_counter() # stop timer
elapsed_time_decode_10000_no_tests = stop_time_decode_10000_no_tests - start_time_decode_10000_no_tests # calculate total execution time
print("Execution time for decoding first 10000 records without tests: " + str(elapsed_time_decode_10000_no_tests) + " seconds") # print the execution time


# with tests
start_time_decode_10000_tests = time.perf_counter() # start timer
# Loop over the first 10000 records
for i, record in enumerate(encoded_json_data["records_encoded"][:10000], start=1):
    line1, line2 = record.split(";") # Split the record into line1 and line2
MRTD.decode_mrz_data(line1, line2)
line1 = "P<UTOERIKSSON<<ANNA<MARIA<<<<<<<<<<<<<<<<<<<"
line2 = "L898902C36UTO7408122F1204159ZE184226B<<<<<<1"
decoded = MRTD.decode_mrz_data(line1, line2)
# Unit test assertions
assert isinstance(decoded, dict)
assert decoded["passport_type"] == "P"
assert decoded["issuing_country"] == "UTO"
assert decoded["surname"] == "ERIKSSON"
assert decoded["given_names"] == "ANNA MARIA"
assert decoded["passport_number"] == "L898902C3"
assert decoded["check_digit_1"] == "6"
assert decoded["country_code"] == "UTO"
assert decoded["birth_date"] == "740812"
assert decoded["gender"] == "F"
assert decoded["expiration_date"] == "120415"
assert decoded["check_digit_4"] == "1"
stop_time_decode_10000_tests = time.perf_counter() # stop timer
elapsed_time_decode_10000_tests = stop_time_decode_10000_tests - start_time_decode_10000_tests # calculate total execution time
print("Execution time for decoding first 10000 records with tests: " + str(elapsed_time_decode_10000_tests) + " seconds\n") # print the execution time


'''
Encoding section
'''
'''
First 100 records
'''
# no tests
start_time_encode_100_no_tests = time.perf_counter() # start timer
for record in decoded_json_data['records_decoded'][:100]: # operate on the first 100 records of records_decoded.json
    MRTD.encode_mrz_data(record)
stop_time_encode_100_no_tests = time.perf_counter() # stop timer
elapsed_time_encode_100_no_tests = stop_time_encode_100_no_tests - start_time_encode_100_no_tests # calculate total execution time
print("Execution times for encoding function: \n")
print("Execution time for encoding first 100 records without tests: " + str(elapsed_time_encode_100_no_tests) + " seconds") # print the execution time


# with tests
start_time_encode_100_tests = time.perf_counter() # start timer
for record in decoded_json_data['records_decoded'][:100]: # operate on the first 100 records of records_decoded.json
    MRTD.encode_mrz_data(record)
# Unit tests
record = {
"line1": {
"issuing_country": "CIV",
"last_name": "LYNN",
"given_name": "NEVEAH BRAM",
},
"line2": {
"passport_number": "W620126G5",
"country_code": "CIV",
"birth_date": "591010",
"sex": "F",
"expiration_date": "970730",
"personal_number": "AJ010215I",
},
}
encoded = MRTD.encode_mrz_data(record)
# Unit test assertions
assert encoded, str
assert ";", encoded
line1, line2 = encoded.split(";")
assert len(line1), 44
assert len(line2), 44
assert(line1.startswith("P<"))
stop_time_encode_100_tests = time.perf_counter() # stop timer
elapsed_time_encode_100_tests = stop_time_encode_100_tests - start_time_encode_100_tests # calculate total execution time
print("Execution time for encoding first 100 records with tests: " + str(elapsed_time_encode_100_tests) + " seconds") # print the execution time


'''
First 1000 records
'''
# no tests
start_time_encode_1000_no_tests = time.perf_counter() # start timer
for record in decoded_json_data['records_decoded'][:1000]:
    MRTD.encode_mrz_data(record)
stop_time_encode_1000_no_tests = time.perf_counter()
elapsed_time_encode_1000_no_tests = stop_time_encode_1000_no_tests - start_time_encode_1000_no_tests
print("Execution time for encoding first 1000 records without tests: " + str(elapsed_time_encode_1000_no_tests) + " seconds")


# with tests
start_time_encode_1000_tests = time.perf_counter()
for record in decoded_json_data['records_decoded'][:1000]:
    MRTD.encode_mrz_data(record)
encoded = MRTD.encode_mrz_data(record)
# Unit test assertions
assert encoded, str
assert ";", encoded
line1, line2 = encoded.split(";")
assert len(line1), 44
assert len(line2), 44
assert(line1.startswith("P<"))
stop_time_encode_1000_tests = time.perf_counter()
elapsed_time_encode_1000_tests = stop_time_encode_1000_tests - start_time_encode_1000_tests
print("Execution time for encoding first 1000 records with tests: " + str(elapsed_time_encode_1000_tests) + " seconds")


'''
First 2000 records
'''
# no tests
start_time_encode_2000_no_tests = time.perf_counter()
for record in decoded_json_data['records_decoded'][:2000]:
    MRTD.encode_mrz_data(record)
stop_time_encode_2000_no_tests = time.perf_counter()
elapsed_time_encode_2000_no_tests = stop_time_encode_2000_no_tests - start_time_encode_2000_no_tests
print("Execution time for encoding first 2000 records without tests: " + str(elapsed_time_encode_2000_no_tests) + " seconds")


# with tests
start_time_encode_2000_tests = time.perf_counter()
for record in decoded_json_data['records_decoded'][:2000]:
    MRTD.encode_mrz_data(record)
encoded = MRTD.encode_mrz_data(record)
# Unit test assertions
assert encoded, str
assert ";", encoded
line1, line2 = encoded.split(";")
assert len(line1), 44
assert len(line2), 44
assert(line1.startswith("P<"))
stop_time_encode_2000_tests = time.perf_counter()
elapsed_time_encode_2000_tests = stop_time_encode_2000_tests - start_time_encode_2000_tests
print("Execution time for encoding first 2000 records with tests: " + str(elapsed_time_encode_2000_tests) + " seconds")


'''
First 3000 records
'''
# no tests
start_time_encode_3000_no_tests = time.perf_counter()
for record in decoded_json_data['records_decoded'][:3000]:
    MRTD.encode_mrz_data(record)
stop_time_encode_3000_no_tests = time.perf_counter()
elapsed_time_encode_3000_no_tests = stop_time_encode_3000_no_tests - start_time_encode_3000_no_tests
print("Execution time for encoding first 3000 records without tests: " + str(elapsed_time_encode_3000_no_tests) + " seconds")


# with tests
start_time_encode_3000_tests = time.perf_counter()
for record in decoded_json_data['records_decoded'][:3000]:
    MRTD.encode_mrz_data(record)
encoded = MRTD.encode_mrz_data(record)
# Unit test assertions
assert encoded, str
assert ";", encoded
line1, line2 = encoded.split(";")
assert len(line1), 44
assert len(line2), 44
assert(line1.startswith("P<"))
stop_time_encode_3000_tests = time.perf_counter()
elapsed_time_encode_3000_tests = stop_time_encode_3000_tests - start_time_encode_3000_tests
print("Execution time for encoding first 3000 records with tests: " + str(elapsed_time_encode_3000_tests) + " seconds")


'''
First 4000 records
'''
# no tests
start_time_encode_4000_no_tests = time.perf_counter()
for record in decoded_json_data['records_decoded'][:4000]:
    MRTD.encode_mrz_data(record)
stop_time_encode_4000_no_tests = time.perf_counter()
elapsed_time_encode_4000_no_tests = stop_time_encode_4000_no_tests - start_time_encode_4000_no_tests
print("Execution time for encoding first 4000 records without tests: " + str(elapsed_time_encode_4000_no_tests) + " seconds")


# with tests
start_time_encode_4000_tests = time.perf_counter()
for record in decoded_json_data['records_decoded'][:4000]:
    MRTD.encode_mrz_data(record)
encoded = MRTD.encode_mrz_data(record)
# Unit test assertions
assert encoded, str
assert";", encoded
line1, line2 = encoded.split(";")
assert len(line1), 44
assert len(line2), 44
assert(line1.startswith("P<"))
stop_time_encode_4000_tests = time.perf_counter()
elapsed_time_encode_4000_tests = stop_time_encode_4000_tests - start_time_encode_4000_tests
print("Execution time for encoding first 4000 records with tests: " + str(elapsed_time_encode_4000_tests) + " seconds")


'''
First 5000 records
'''
# no tests
start_time_encode_5000_no_tests = time.perf_counter()
for record in decoded_json_data['records_decoded'][:5000]:
    MRTD.encode_mrz_data(record)
stop_time_encode_5000_no_tests = time.perf_counter()
elapsed_time_encode_5000_no_tests = stop_time_encode_5000_no_tests - start_time_encode_5000_no_tests
print("Execution time for encoding first 5000 records without tests: " + str(elapsed_time_encode_5000_no_tests) + " seconds")


# with tests
start_time_encode_5000_tests = time.perf_counter()
for record in decoded_json_data['records_decoded'][:5000]:
    MRTD.encode_mrz_data(record)
encoded = MRTD.encode_mrz_data(record)
# Unit test assertions
assert encoded, str
assert ";", encoded
line1, line2 = encoded.split(";")
assert len(line1), 44
assert len(line2), 44
assert(line1.startswith("P<"))
stop_time_encode_5000_tests = time.perf_counter()
elapsed_time_encode_5000_tests = stop_time_encode_5000_tests - start_time_encode_5000_tests
print("Execution time for encoding first 5000 records with tests: " + str(elapsed_time_encode_5000_tests) + " seconds")


'''
First 6000 records
'''
# no tests
start_time_encode_6000_no_tests = time.perf_counter()
for record in decoded_json_data['records_decoded'][:6000]:
    MRTD.encode_mrz_data(record)
stop_time_encode_6000_no_tests = time.perf_counter()
elapsed_time_encode_6000_no_tests = stop_time_encode_6000_no_tests - start_time_encode_6000_no_tests
print("Execution time for encoding first 6000 records without tests: " + str(elapsed_time_encode_6000_no_tests) + " seconds")


# with tests
start_time_encode_6000_tests = time.perf_counter()
for record in decoded_json_data['records_decoded'][:6000]:
    MRTD.encode_mrz_data(record)
encoded = MRTD.encode_mrz_data(record)
# Unit test assertions
assert encoded, str
assert ";", encoded
line1, line2 = encoded.split(";")
assert len(line1), 44
assert len(line2), 44
assert(line1.startswith("P<"))
stop_time_encode_6000_tests = time.perf_counter()
elapsed_time_encode_6000_tests = stop_time_encode_6000_tests - start_time_encode_6000_tests
print("Execution time for encoding first 6000 records with tests: " + str(elapsed_time_encode_6000_tests) + " seconds")


'''
First 7000 records
'''
# no tests
start_time_encode_7000_no_tests = time.perf_counter()
for record in decoded_json_data['records_decoded'][:7000]:
    MRTD.encode_mrz_data(record)
stop_time_encode_7000_no_tests = time.perf_counter()
elapsed_time_encode_7000_no_tests = stop_time_encode_7000_no_tests - start_time_encode_7000_no_tests
print("Execution time for encoding first 7000 records without tests: " + str(elapsed_time_encode_7000_no_tests) + " seconds")


# with tests
start_time_encode_7000_tests = time.perf_counter()
for record in decoded_json_data['records_decoded'][:7000]:
    MRTD.encode_mrz_data(record)
encoded = MRTD.encode_mrz_data(record)
# Unit test assertions
assert encoded, str
assert ";", encoded
line1, line2 = encoded.split(";")
assert len(line1), 44
assert len(line2), 44
assert(line1.startswith("P<"))
stop_time_encode_7000_tests = time.perf_counter()
elapsed_time_encode_7000_tests = stop_time_encode_7000_tests - start_time_encode_7000_tests
print("Execution time for encoding first 7000 records with tests: " + str(elapsed_time_encode_7000_tests) + " seconds")


'''
First 8000 records
'''
# no tests
start_time_encode_8000_no_tests = time.perf_counter()
for record in decoded_json_data['records_decoded'][:8000]:
    MRTD.encode_mrz_data(record)
stop_time_encode_8000_no_tests = time.perf_counter()
elapsed_time_encode_8000_no_tests = stop_time_encode_8000_no_tests - start_time_encode_8000_no_tests
print("Execution time for encoding first 8000 records without tests: " + str(elapsed_time_encode_8000_no_tests) + " seconds")


# with tests
start_time_encode_8000_tests = time.perf_counter()
for record in decoded_json_data['records_decoded'][:8000]:
    MRTD.encode_mrz_data(record)
encoded = MRTD.encode_mrz_data(record)
# Unit test assertions
assert encoded, str
assert ";", encoded
line1, line2 = encoded.split(";")
assert len(line1), 44
assert len(line2), 44
assert(line1.startswith("P<"))
stop_time_encode_8000_tests = time.perf_counter()
elapsed_time_encode_8000_tests = stop_time_encode_8000_tests - start_time_encode_8000_tests
print("Execution time for encoding first 8000 records with tests: " + str(elapsed_time_encode_8000_tests) + " seconds")


'''
First 9000 records
'''
# no tests
start_time_encode_9000_no_tests = time.perf_counter()
for record in decoded_json_data['records_decoded'][:9000]:
    MRTD.encode_mrz_data(record)
stop_time_encode_9000_no_tests = time.perf_counter()
elapsed_time_encode_9000_no_tests = stop_time_encode_9000_no_tests - start_time_encode_9000_no_tests
print("Execution time for encoding first 9000 records without tests: " + str(elapsed_time_encode_9000_no_tests) + " seconds")


# with tests
start_time_encode_9000_tests = time.perf_counter()
for record in decoded_json_data['records_decoded'][:9000]:
    MRTD.encode_mrz_data(record)
encoded = MRTD.encode_mrz_data(record)
# Unit test assertions
assert encoded, str
assert ";", encoded
line1, line2 = encoded.split(";")
assert len(line1), 44
assert len(line2), 44
assert(line1.startswith("P<"))
stop_time_encode_9000_tests = time.perf_counter()
elapsed_time_encode_9000_tests = stop_time_encode_9000_tests - start_time_encode_9000_tests
print("Execution time for encoding first 9000 records with tests: " + str(elapsed_time_encode_9000_tests) + " seconds")


'''
First 10000 records
'''
# no tests
start_time_encode_10000_no_tests = time.perf_counter()
for record in decoded_json_data['records_decoded'][:10000]:
    MRTD.encode_mrz_data(record)
stop_time_encode_10000_no_tests = time.perf_counter()
elapsed_time_encode_10000_no_tests = stop_time_encode_10000_no_tests - start_time_encode_10000_no_tests
print("Execution time for encoding first 10000 records without tests: " + str(elapsed_time_encode_10000_no_tests) + " seconds")


# with tests
start_time_encode_10000_tests = time.perf_counter()
for record in decoded_json_data['records_decoded'][:10000]:
    MRTD.encode_mrz_data(record)
encoded = MRTD.encode_mrz_data(record)
# Unit test assertions
assert encoded, str
assert ";", encoded
line1, line2 = encoded.split(";")
assert len(line1), 44
assert len(line2), 44
assert(line1.startswith("P<"))
stop_time_encode_10000_tests = time.perf_counter()
elapsed_time_encode_10000_tests = stop_time_encode_10000_tests - start_time_encode_10000_tests
print("Execution time for encoding first 10000 records with tests: " + str(elapsed_time_encode_10000_tests) + " seconds")
'''
CSV section
'''
'''
Decode CSV file
'''
# Add results for decode function to csv file
with open("decoded_output.csv", "w", newline="") as f:
    writer = csv.writer(f)
# Create columns for our data
writer.writerow(["Number of lines read from the beginning of the file",
"Execution time without tests",
"Execution time with unit tests assertions in place"])
# Add our results to the file
writer.writerow(["100", str(elapsed_time_decode_100_no_tests) + " seconds", str(elapsed_time_decode_100_tests) + " seconds"])
writer.writerow(["1000", str(elapsed_time_decode_1000_no_tests) + " seconds", str(elapsed_time_decode_1000_tests) + " seconds"])
writer.writerow(["2000", str(elapsed_time_decode_2000_no_tests) + " seconds", str(elapsed_time_decode_2000_tests) + " seconds"])
writer.writerow(["3000", str(elapsed_time_decode_3000_no_tests) + " seconds", str(elapsed_time_decode_3000_tests) + " seconds"])
writer.writerow(["4000", str(elapsed_time_decode_4000_no_tests) + " seconds", str(elapsed_time_decode_4000_tests) + " seconds"])
writer.writerow(["5000", str(elapsed_time_decode_5000_no_tests) + " seconds", str(elapsed_time_decode_5000_tests) + " seconds"])
writer.writerow(["6000", str(elapsed_time_decode_6000_no_tests) + " seconds", str(elapsed_time_decode_6000_tests) + " seconds"])
writer.writerow(["7000", str(elapsed_time_decode_7000_no_tests) + " seconds", str(elapsed_time_decode_7000_tests) + " seconds"])
writer.writerow(["8000", str(elapsed_time_decode_8000_no_tests) + " seconds", str(elapsed_time_decode_8000_tests) + " seconds"])
writer.writerow(["9000", str(elapsed_time_decode_9000_no_tests) + " seconds", str(elapsed_time_decode_9000_tests) + " seconds"])
writer.writerow(["10000", str(elapsed_time_decode_10000_no_tests) + " seconds", str(elapsed_time_decode_10000_tests) + " seconds"])
'''
Encode CSV file
'''
# Add results for encode function to csv file
with open("encoded_output.csv", "w", newline="") as f:
    writer = csv.writer(f)
# Create columns for our data
writer.writerow(["Number of lines read from the beginning of the file",
"Execution time without tests",
"Execution time with unit tests assertions in place"])
# Add our results to the file
writer.writerow(["100", str(elapsed_time_encode_100_no_tests) + " seconds", str(elapsed_time_encode_100_tests) + " seconds"])
writer.writerow(["1000", str(elapsed_time_encode_1000_no_tests) + " seconds", str(elapsed_time_encode_1000_tests) + " seconds"])
writer.writerow(["2000", str(elapsed_time_encode_2000_no_tests) + " seconds", str(elapsed_time_encode_2000_tests) + " seconds"])
writer.writerow(["3000", str(elapsed_time_encode_3000_no_tests) + " seconds", str(elapsed_time_encode_3000_tests) + " seconds"])
writer.writerow(["4000", str(elapsed_time_encode_4000_no_tests) + " seconds", str(elapsed_time_encode_4000_tests) + " seconds"])
writer.writerow(["5000", str(elapsed_time_encode_5000_no_tests) + " seconds", str(elapsed_time_encode_5000_tests) + " seconds"])
writer.writerow(["6000", str(elapsed_time_encode_6000_no_tests) + " seconds", str(elapsed_time_encode_6000_tests) + " seconds"])
writer.writerow(["7000", str(elapsed_time_encode_7000_no_tests) + " seconds", str(elapsed_time_encode_7000_tests) + " seconds"])
writer.writerow(["8000", str(elapsed_time_encode_8000_no_tests) + " seconds", str(elapsed_time_encode_8000_tests) + " seconds"])
writer.writerow(["9000", str(elapsed_time_encode_9000_no_tests) + " seconds", str(elapsed_time_encode_9000_tests) + " seconds"])
writer.writerow(["10000", str(elapsed_time_encode_10000_no_tests) + " seconds", str(elapsed_time_encode_10000_tests) + " seconds"])
