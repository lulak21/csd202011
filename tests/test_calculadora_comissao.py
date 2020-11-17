import unittest
import sistema_vendas.calculadora_comissao as calculadora_comissao
# Victor
# Paulo
# Dayves

class TestCalculadoraComissao(unittest.TestCase):
    def test_venda_de_500_reais_com_comissao_de_25_reais(self):
        #arrange
        valor_venda = 500
        comissa_esperada = 25

        #act
        comissao_calculada = calculadora_comissao.calcular(valor_venda)

        #assert
        self.assertEqual(comissa_esperada, comissao_calculada)

    def test_venda_de_10001_reais_com_comissao_de_600_06(self):
        # arrange
        valor_venda = 10001
        comissa_esperada = 600.06

        # act
        comissao_calculada = calculadora_comissao.calcular(valor_venda)
        # assert
        self.assertEqual(comissa_esperada, comissao_calculada)

    def test_venda_de_10000_reais_com_comissao_de_500_reais(self):
        #arrange
        valor_venda = 10000
        comissa_esperada = 500

        #act
        comissao_calculada = calculadora_comissao.calcular(valor_venda)

        #assert
        self.assertEqual(comissa_esperada, comissao_calculada)

    def test_venda_de_10002_reais_com_comissao_de_600_12_reais(self):
        #arrange
        valor_venda = 10002
        comissa_esperada = 600.12

        #act
        comissao_calculada = calculadora_comissao.calcular(valor_venda)

        #assert
        self.assertEqual(comissa_esperada, comissao_calculada)

    def test_venda_de_55_59_reais_com_comissao_de_2_77_reais(self):
        #arrange
        valor_venda = 55.59
        comissa_esperada = 2.77

        #act
        comissao_calculada = calculadora_comissao.calcular(valor_venda)

        #assert
        self.assertEqual(comissa_esperada, comissao_calculada)