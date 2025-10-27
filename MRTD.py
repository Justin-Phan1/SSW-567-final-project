class MRTD:
    '''MRTD simulates a system that can scan and decode Machine Readable Travel Documents (MRTDs) such as passports by reading their Machine Readable Zone (MRZ).'''
    def scan_mrz():
        '''
        This function scans the MRZ of a travel document using a hardware device scanner and get the information in MRZ as two strings. 
        This means that you define an empty method for this function is created since we are not require to worry about the implementation 
        of the hardware device, but we need to define this method for our system. 
        '''
        return True

    def decode_mrz_data(self, str1, str2):
        '''The system shall be able to separate the two strings obtained from the MRZ into these categories: passport type, issuing country, name of the passport holder, passport number, country code, birth date, gender, expiration date, personal number, and the check digits in between the second line of the MRZ. 
        
        Expected Format:
        Line 1: [Type][Issuing Country][Name]
        Line 2: [Passport Number][Check Digit 1][Country Code]
                [Birth Date][Check Digit 2][Gender]
                [Expiration Date][Check Digit 3]
                [Personal Number][Check Digit 4]

        Returns a dictionary with the extracted fields.
        '''
        try:
            # --- Line 1 parsing ---
            passport_type = str1[0:2].replace("<", "").strip()
            issuing_country = str1[2:5].replace("<", "").strip()

            # Extract name field (remainder of line 1)
            name_field = str1[5:]

            # Find '<<' only if it appears before the filler section
            double_arrow_index = name_field.find("<<")

            if 0 <= double_arrow_index < len(name_field) - 5:
                surname, given_names = name_field.split("<<", 1)
                surname = surname.replace("<", " ").strip()
                given_names = given_names.replace("<", " ").strip()
                
                # Check if either part is empty
                if not surname or not given_names:
                    surname = "Unknown"
                    given_names = "Unknown"
            else:
                surname = "Unknown"
                given_names = "Unknown"

            # --- Line 2 parsing ---
            passport_number = str2[0:9].replace("<", "")
            check_digit_1 = str2[9]
            country_code = str2[10:13].replace("<", "")
            birth_date = str2[13:19]
            check_digit_2 = str2[19]
            gender = str2[20]
            expiration_date = str2[21:27]
            check_digit_3 = str2[27]
            personal_number = str2[28:42].replace("<", "")
            check_digit_4 = str2[43]

            # Return structured data
            decoded_fields = {
                "passport_type": passport_type,
                "issuing_country": issuing_country,
                "surname": surname,
                "given_names": given_names,
                "passport_number": passport_number,
                "check_digit_1": check_digit_1,
                "country_code": country_code,
                "birth_date": birth_date,
                "check_digit_2": check_digit_2,
                "gender": gender,
                "expiration_date": expiration_date,
                "check_digit_3": check_digit_3,
                "personal_number": personal_number,
                "check_digit_4": check_digit_4
            }

            return decoded_fields

        except Exception as e:
            return f"Error: Failed to decode MRZ lines ({str(e)})."

    def encode_mrz_data():
        '''
        The system shall be able to encode travel document information fields queried from a database into the 
        two strings for the MRZ in a travel document. Empty function is defined since we are not required to implement this function.
        '''
        return True

    def report_mismatch(passport_number, date_of_birth, expiration_date, personal_number, check_digit_1, check_digit_2, check_digit_3, check_digit_4):
        '''
        This function reports if the check digits in string 2 of the MRZ are wrong
        Input: string passport_number, string date_of_birth, string expiration_date, string personal_number, int check_digit_1, int check_digit_2, int check_digit_3, int check_digit_4
        Output: A string showing if the check digits mismatched or not
        '''
        # calculate the check digits
        passport_number_adler_checksum = MRTD.adler_32(passport_number) % 10 
        date_of_birth__adler_checksum = MRTD.adler_32(date_of_birth) % 10
        expiration_date_adler_checksum = MRTD.adler_32(expiration_date) % 10
        personal_number_adler_checksum = MRTD.adler_32(personal_number) % 10

        if check_digit_1 != passport_number_adler_checksum:
            print("Error: Passport number checkdigit does not match.\n")
        else:
            print("Passport number checkdigit matches.\n")
        if check_digit_2 != date_of_birth__adler_checksum:
            print("Error: Date of birth checkdigit does not match.\n")
        else:
            print("Date of birth checkdigit matches.\n")
        if check_digit_3 != expiration_date_adler_checksum:
            print("Error: Expiration date checkdigit does not match.\n")
        else:
            print("Expiration date checkdigit matches.\n")
        if check_digit_4 != personal_number_adler_checksum:
            print("Error: Personal number checkdigit does not match.\n")
        else:
            print("Personal number checkdigit matches.\n")
            return 

    def adler_32(data):
        '''
        This function utilizes the Adler-32 algorithm to produce a checksum.
        Input: a string of data
        Output: the checksum calculated for that string
        '''
        a = 1 # sum of all bytes 
        b = 0 # sum of all values from A 
        length = len(data)
        for i in range(0, length):
            a = (a + ord(data[i])) % 65521
            b = (b + a) % 65521
        return (b << 16) | a 
