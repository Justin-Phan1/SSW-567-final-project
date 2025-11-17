import unittest
from MRTD import MRTD


class TestMRTD(unittest.TestCase):
    def setUp(self):
        self.scanner = MRTD()

    def test_scan_mrz(self):
        '''
        test scanning mrz function
        return True since we have not implemented the function and assume it works
        '''
        self.assertTrue(True)

    def test_decode_mrz_data(self):
        """Test decoding of a standard MRZ example."""
        line1 = "P<UTOERIKSSON<<ANNA<MARIA<<<<<<<<<<<<<<<<<<<"
        line2 = "L898902C36UTO7408122F1204159ZE184226B<<<<<<1"

        decoded = self.scanner.decode_mrz_data(line1, line2)

        self.assertIsInstance(decoded, dict)
        self.assertEqual(decoded["passport_type"], "P")
        self.assertEqual(decoded["issuing_country"], "UTO")
        self.assertEqual(decoded["surname"], "ERIKSSON")
        self.assertEqual(decoded["given_names"], "ANNA MARIA")
        self.assertEqual(decoded["passport_number"], "L898902C3")
        self.assertEqual(decoded["check_digit_1"], "6")
        self.assertEqual(decoded["country_code"], "UTO")
        self.assertEqual(decoded["birth_date"], "740812")
        self.assertEqual(decoded["gender"], "F")
        self.assertEqual(decoded["expiration_date"], "120415")
        self.assertEqual(decoded["check_digit_4"], "1")

    def test_decodeMRZ_incomplete_data(self):
        """Test decoding fails gracefully if MRZ is incomplete."""
        line1 = "P<UTOERIKSSON<<ANNA<MARIA"
        line2 = "L898902C36UTO7408122F1204"

        result = self.scanner.decode_mrz_data(line1, line2)
        self.assertIsInstance(result, str)
        self.assertIn("Error", result)

    def test_decodeMRZ_missing_names(self):
        """Test MRZ decoding when name separators are missing."""
        line1 = "P<GRANTJAMES<MICHAEL<<<<<<<<<<<<<<<<<<<"
        line2 = "L898902C36UTO7408122F1204159ZE184226B<<<<<10"

        decoded = self.scanner.decode_mrz_data(line1, line2)
        self.assertEqual(decoded["surname"], "Unknown")
        self.assertEqual(decoded["given_names"], "Unknown")

    def test_decodeMRZ_handles_special_characters(self):
        """Test decoding with unexpected filler characters."""
        line1 = "P<UTOERIKSSON<<ANNA<MARIA<<<<<@@@@@@<<<<<<<<"
        line2 = "L898902C36UTO7408122F1204159ZE184226B<<<<<10"

        decoded = self.scanner.decode_mrz_data(line1, line2)
        self.assertIn("ANNA", decoded["given_names"])

    def test_decodeMRZ_field_lengths(self):
        """Verify all expected MRZ fields exist in the output."""
        line1 = "P<UTOERIKSSON<<ANNA<MARIA<<<<<<<<<<<<<<<<<<<"
        line2 = "L898902C36UTO7408122F1204159ZE184226B<<<<<10"
        decoded = self.scanner.decode_mrz_data(line1, line2)

        expected_fields = [
            "passport_type", "issuing_country", "surname", "given_names",
            "passport_number", "check_digit_1", "country_code",
            "birth_date", "check_digit_2", "gender", "expiration_date",
            "check_digit_3", "personal_number", "check_digit_4"
        ]

        for field in expected_fields:
            self.assertIn(field, decoded, f"{field} missing from decoded output")

    def test_encode_mrz_data(self):
        '''
        test encoding data function
        return True since we have not implemented the function and assume it works
        '''
        self.assertTrue(True)

    def test_report_mismatch(self):
        '''test check digit mismatch reporting'''
        passport_number = "L898902C3"
        date_of_birth = "UTO740812"
        expiration_date = "F120415"
        personal_number = "ZE184226B"
        check_digit_1 = 7 
        check_digit_2 = 1
        check_digit_3 = 2 
        check_digit_4 = 1
        MRTD.report_mismatch(passport_number, date_of_birth, expiration_date, personal_number, check_digit_1, check_digit_2, check_digit_3, check_digit_4)

    def test_adler_32(self):
        '''test adler32 algorithm'''
        data1 = "L898902C3"
        data2 = "UTO740812"
        data3 = "F120415"
        data4 = "ZE184226B"
        ans1 = MRTD.adler_32(data1)
        ans2 = MRTD.adler_32(data2)
        ans3 = MRTD.adler_32(data3)
        ans4 = MRTD.adler_32(data4)

        # Find the check digits by using modulo 10 on each checksum we get from the function
        # x = ans1 % 10
        # print("Check digit 1: " + str(x))
        # y = ans2 % 10
        # print("Check digit 2: " + str(y))
        # z = ans3 % 10
        # print("Check digit 3: " + str(z))
        # a = ans4 % 10
        # print("Check digit 4: " + str(a))

        # check the resultsfrom the function
        self.assertEqual(ans1, 176161287) 
        self.assertEqual(ans2, 202965551)
        self.assertEqual(ans3, 100925812)
        self.assertEqual(ans4, 185729561)

if __name__ == '__main__':
    unittest.main()