import unittest
import math
import statistics #required to obtain mean
#import calc //involves pip installs

#created for TDD development assignment. Values replaced with self. Self is to be replaced with proper values in future assignments.
class test_CalcMethods(unittest.TestCase):

    def test_calculateSum(self):
        self.assertEqual(sum([self]),self)
        
    def test_calculateMean(self):
        self.assertEqual(statistics.fmean([self]), self)
        
    def test_calculateGcd(self):
        self.assertEqual(math.gcd(self, self, self), self)        
                        
class test_InRange(unittest.TestCase):
    #input within range of parameters
    
    def  test_firstInputRange(self):
        input = self
        self.assertTrue(input in range(1,11))
        self.assertFalse(1 > input > 10)

    def test_secondInputRange(self):
        input = self
        self.assertTrue(input in range(20, 31))
        self.assertFalse(20 > input > 30)

    def test_thirdInputRange(self):
        input = self
        self.assertTrue(input in range(70, 101))
        self.assertFalse(70 > input > 100)

class test_isInputNotNumber(unittest.TestCase):
    # input is not an integer
    def test_FirstInput(self):
        inputT = self
        inputF = self
        self.assertTrue (inputT == int)
        self.assertFalse (inputF != int)

    def test_SecondInput(self):
        inputT = self
        inputF = self
        self.assertTrue (inputT == int)
        self.assertFalse (inputF != int)

    def test_ThirdInput(self):
        inputT = self
        inputF = self
        self.assertTrue (inputT == int)
        self.assertFalse (inputF != int)
        
class test_isInputPresent(unittest.TestCase):
    # no input detected test
    def test_FirstInputPresent(self):
        input = self
        self.assertTrue(input == self)
    def test_SecondInputPresent(self):
        input = self
        self.assertTrue(input == self)
    def test_ThirdInputPresent(self):
        input = self
        self.assertTrue(input == self)

class test_isResultChosen(unittest.TestCase):
    def test_isResultChosen(self):
        input = self
        self.assertTrue(input != self)

class test_userReceives(unittest.TestCase):
    def test_isUserReceivingAlert(self):
        input = self
        self.assertTrue(input == self)
        
if __name__ == '__main__':
    unittest.main()