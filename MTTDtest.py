import unittest
from MRTD import MRTD


class TestMRTD(unittest.TestCase):

    def test_scan_mrz(self):
        # just check the placeholder function
        self.assertTrue(True)

    def test_decode_mrz_data(self):
        line1 = "P<UTOERIKSSON<<ANNA<MARIA<<<<<<<<<<<<<<<<<<<"
        line2 = "L898902C36UTO7408122F1204159ZE184226B<<<<<<1"

        decoded = MRTD.decode_mrz_data(line1, line2)

        self.assertIsInstance(decoded, dict)
        self.assertEqual(decoded["passport_type"], "P")
        self.assertEqual(decoded["issuing_country"], "UTO")
        self.assertEqual(decoded["surname"], "ERIKSSON")
        self.assertEqual(decoded["given_names"], "ANNA MARIA")
        self.assertEqual(decoded["passport_number"], "L898902C3")
        self.assertEqual(decoded["country_code"], "UTO")
        self.assertEqual(decoded["birth_date"], "740812")
        self.assertEqual(decoded["gender"], "F")
        self.assertEqual(decoded["expiration_date"], "120415")
        self.assertEqual(decoded["personal_number"], "ZE184226B")

    def test_decodeMRZ_incomplete_data(self):
        line1 = "P<UTOERIKSSON<<ANNA<MARIA"
        line2 = "L898902C36UTO7408122F1204"

        result = MRTD.decode_mrz_data(line1, line2)
        self.assertIsInstance(result, str)
        self.assertIn("Error", result)

    def test_decodeMRZ_missing_names(self):
        line1 = "P<GRANTJAMES<MICHAEL<<<<<<<<<<<<<<<<<<<"
        line2 = "L898902C36UTO7408122F1204159ZE184226B<<<<<10"

        decoded = MRTD.decode_mrz_data(line1, line2)
        self.assertEqual(decoded["surname"], "Unknown")
        self.assertEqual(decoded["given_names"], "Unknown")

    def test_decodeMRZ_handles_special_characters(self):
        line1 = "P<UTOERIKSSON<<ANNA<MARIA<<<<<@@@@@@<<<<<<<<"
        line2 = "L898902C36UTO7408122F1204159ZE184226B<<<<<10"

        decoded = MRTD.decode_mrz_data(line1, line2)
        self.assertIn("ANNA", decoded["given_names"])

    def test_decodeMRZ_field_lengths(self):
        line1 = "P<UTOERIKSSON<<ANNA<MARIA<<<<<<<<<<<<<<<<<<<"
        line2 = "L898902C36UTO7408122F1204159ZE184226B<<<<<<1"

        decoded = MRTD.decode_mrz_data(line1, line2)

        expected_fields = [
            "passport_type", "issuing_country", "surname", "given_names",
            "passport_number", "check_digit_1", "country_code",
            "birth_date", "check_digit_2", "gender", "expiration_date",
            "check_digit_3", "personal_number", "check_digit_4",
        ]

        for field in expected_fields:
            self.assertIn(field, decoded)

    def test_encode_mrz_data(self):
        # use the first record from records_decoded.json format
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

        self.assertIsInstance(encoded, str)
        self.assertIn(";", encoded)

        line1, line2 = encoded.split(";")
        self.assertEqual(len(line1), 44)
        self.assertEqual(len(line2), 44)
        self.assertTrue(line1.startswith("P<"))

        decoded = MRTD.decode_mrz_data(line1, line2)
        self.assertEqual(decoded["issuing_country"], "CIV")
        self.assertEqual(decoded["surname"], "LYNN")
        self.assertEqual(decoded["given_names"], "NEVEAH BRAM")
        self.assertEqual(decoded["passport_number"], "W620126G5")
        self.assertEqual(decoded["country_code"], "CIV")
        self.assertEqual(decoded["birth_date"], "591010")
        self.assertEqual(decoded["gender"], "F")
        self.assertEqual(decoded["expiration_date"], "970730")
        self.assertEqual(decoded["personal_number"], "AJ010215I")

    def test_report_mismatch(self):
        passport_number = "L898902C3"
        date_of_birth = "UTO740812"
        expiration_date = "F120415"
        personal_number = "ZE184226B"
        check_digit_1 = 7
        check_digit_2 = 1
        check_digit_3 = 2
        check_digit_4 = 1

        # just make sure it runs without throwing
        MRTD.report_mismatch(
            passport_number,
            date_of_birth,
            expiration_date,
            personal_number,
            check_digit_1,
            check_digit_2,
            check_digit_3,
            check_digit_4,
        )

    def test_adler_32(self):
        data1 = "L898902C3"
        data2 = "UTO740812"
        data3 = "F120415"
        data4 = "ZE184226B"

        ans1 = MRTD.adler_32(data1)
        ans2 = MRTD.adler_32(data2)
        ans3 = MRTD.adler_32(data3)
        ans4 = MRTD.adler_32(data4)

        self.assertEqual(ans1, 176161287)
        self.assertEqual(ans2, 202965551)
        self.assertEqual(ans3, 100925812)
        self.assertEqual(ans4, 185729561)


if __name__ == "__main__":
    unittest.main()
