import unittest
from authntication import Authenticator
from dataProcessing import DataProcessing


class TestBackend(unittest.TestCase):
    def test_get_user(self):
        auth = Authenticator()
        user = auth.GetUser()
        self.assertEqual(user["email"], "mirzacvalerian@gmail.com")

    def test_data_processing_bass(self):
        pitches = [1.0, 1.0, 1.0, 1.0, 0, 0, 0, 0, 0, 0, 0, 0]
        dp = DataProcessing()
        ledValues = dp.ReturnRGB(pitches)
        self.assertEqual(ledValues[0], 255)
        self.assertEqual(ledValues[1], 0)

    def test_data_processing_midrange(self):
        pitches = [0, 0, 0, 0, 1.0, 1.0, 1.0, 1.0, 0, 0, 0, 0]
        dp = DataProcessing()
        ledValues = dp.ReturnRGB(pitches)
        self.assertEqual(ledValues[0], 0)
        self.assertEqual(ledValues[1], 255)

    def test_data_processing_treble(self):
        pitches = [0, 0, 0, 0, 0, 0, 0, 0, 1.0, 1.0, 1.0, 1.0]
        dp = DataProcessing()
        ledValues = dp.ReturnRGB(pitches)
        self.assertEqual(ledValues[0], 255)
        self.assertEqual(ledValues[1], 255)


if __name__ == "__main__":
    unittest.main()
