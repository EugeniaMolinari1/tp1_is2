import unittest
from rpn import evaluate, RPNError

class TestRPN(unittest.TestCase):

    # 🟢 casos correctos
    def test_suma(self):
        self.assertEqual(evaluate("3 4 +"), 7)

    def test_expresion_compleja(self):
        self.assertEqual(evaluate("5 1 2 + 4 * + 3 -"), 14)

    def test_constante_pi(self):
        self.assertAlmostEqual(evaluate("p"), 3.1415, places=3)

    def test_sqrt(self):
        self.assertEqual(evaluate("9 sqrt"), 3)

    def test_trig(self):
        self.assertAlmostEqual(evaluate("90 sin"), 1, places=3)

    def test_memoria(self):
        self.assertEqual(evaluate("5 STO0 RCL0"), 5)

    def test_dup(self):
        self.assertEqual(evaluate("5 dup +"), 10)

    def test_swap(self):
        self.assertEqual(evaluate("3 4 swap -"), 1)

    # 🔴 errores (MUY importante para el TP)
    def test_division_por_cero(self):
        with self.assertRaises(RPNError):
            evaluate("3 0 /")

    def test_token_invalido(self):
        with self.assertRaises(RPNError):
            evaluate("3 4 &")

    def test_pila_insuficiente(self):
        with self.assertRaises(RPNError):
            evaluate("+")

    def test_error_final(self):
        with self.assertRaises(RPNError):
            evaluate("3 4")
    def test_clear(self):
        self.assertEqual(evaluate("3 4 clear 5"), 5)

    def test_drop(self):
        self.assertEqual(evaluate("3 4 drop"), 3)

    def test_yx(self):
        self.assertEqual(evaluate("2 3 yx"), 8)

    def test_error_memoria(self):
        with self.assertRaises(RPNError):
            evaluate("5 STO10")

    def test_reciproco_error(self):
        with self.assertRaises(RPNError):
            evaluate("0 1/x")

    

if __name__ == "__main__":
    unittest.main()