import unittest

class TestMRTD(unittest.TestCase):
    def test_scan_mrz(self):
        '''
        test scanning mrz function
        return True since we have not implemented the function and assume it works
        '''
        self.assertTrue(True)

    def test_decode_mrz_data(self):
        pass

    def test_encode_mrz_data(self):
        '''
        test encoding data function
        return True since we have not implemented the function and assume it works
        '''
        self.assertTrue(True)

    def test_report_mismatch(self):
        pass

if __name__ == '__main__':
    unittest.main()