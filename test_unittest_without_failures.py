import unittest
import math
import statistics #required to obtain mean
#import calc //involves pip installs

class test_CalcMethods(unittest.TestCase):

    def test_calculateSum(self):
        self.assertEqual(sum([5, 25, 90]),120)
        
    def test_calculateMean(self):
        self.assertEqual(statistics.fmean([5, 25, 90]), 40)
        
    def test_calculateGcd(self):
        self.assertEqual(math.gcd(5, 25, 90), 5)        
                        
class test_InRange(unittest.TestCase):
    #input within range of parameters
    
    def  test_firstInputRange(self):
        input = 5
        self.assertTrue(input in range(1,11))
        self.assertFalse(1 > input > 10)

    def test_secondInputRange(self):
        input = 25
        self.assertTrue(input in range(20, 31))
        self.assertFalse(20 > input > 30)

    def test_thirdInputRange(self):
        input = 75
        self.assertTrue(input in range(70, 101))
        self.assertFalse(70 > input > 100)

class test_isInputNotNumber(unittest.TestCase):
    # input is not an integer
    def test_FirstInput(self):
        inputT = 100
        inputF = "100"
        self.assertTrue (inputT == int)
        self.assertFalse (inputF != int)

    def test_SecondInput(self):
        inputT = 100
        inputF = "100"
        self.assertTrue (inputT == int)
        self.assertFalse (inputF != int)

    def test_ThirdInput(self):
        inputT = 100
        inputF = "100"
        self.assertTrue (inputT == int)
        self.assertFalse (inputF != int)
        
class test_isInputPresent(unittest.TestCase):
    # no input detected test
    def test_FirstInputPresent(self):
        input = ""
        self.assertTrue(input == "")
    def test_SecondInputPresent(self):
        input = ""
        self.assertTrue(input == "")
    def test_ThirdInputPresent(self):
        input = ""
        self.assertTrue(input == "")

class test_isResultChosen(unittest.TestCase):
    def test_isResultChosen(self):
        input = "foo"
        self.assertTrue(input != "")

class test_userReceives(unittest.TestCase):
    def test_isUserReceivingAlert(self):
        input ="UserError"
        self.assertTrue(input == "UserError")
        
if __name__ == '__main__':
    unittest.main()