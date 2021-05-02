import unittest, Moreno_Ramirez_Rodriguez as p

M = [[ 0 for j in range (4)] for i  in range(4) ]

M[0][0] = 2 
M[0][1] = 3
M[0][2] = 4
M[0][3] = 5

M[1][0] = 6
M[1][1] = 7
M[1][2] = 8
M[1][3] = 9

M[2][0] = 13
M[2][1] = 114
M[2][2] = 1415
M[2][3] = 123

M[3][0] = 111
M[3][1] = 99
M[3][2] = 88
M[3][3] = 77



class tests(unittest.TestCase):
    def test1(self):
        self.assertTrue(p.aleatorio(M))

if __name__ == "__main__":
    unittest.main()