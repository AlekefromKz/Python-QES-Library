import unittest
import src.main.mathmatic as mathmatic

class Testing(unittest.TestCase):
    
    def test_quadraticfunction_test0(self):
        test = mathmatic.quadraticEquate(1, 1, 1).roots()
        print(test)
        self.assertEqual(None ,test)
            
    def test_quadraticfunction_test1(self):
        
        test = mathmatic.quadraticEquate(2, 6, 4).roots()
        self.assertEqual(
            (-1.0, -2.0), test
            )

    def test_quadraticfunction_test2(self):
        
        test = mathmatic.quadraticEquate(8, 5, 3).roots()
        self.assertEqual(
            None, test
            )

    def test_quadraticfunction_test3(self):
        test = mathmatic.quadraticEquate(24, 32, 9).roots()
        self.assertEqual(
            (-0.40314352831930167, -0.9301898050140317), test
            )
        
    
if __name__ == '__main__':
    unittest.main()
    
