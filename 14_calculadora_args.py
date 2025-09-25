class Calculadora:
    def somar(self, *args):
        return sum(args)
    
    def media(sel, *args):
        resultado = sum(args) / len(args)
        return resultado
calc = Calculadora()
print(calc.somar(1,2,3,4,5,6))
print(calc.media(1,2,3,4,5,6))