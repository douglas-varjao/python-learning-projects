from datetime import datetime

def contar_dias(data_inicial, data_final):

    try:
        inicio = datetime.strptime(data_inicial, '%d/%m/%Y')
        fim = datetime.strptime(data_final, '%d/%m/%Y')

        diferenca = fim - inicio

        return diferenca.days
    except ValueError as e:
        print(f"ERROUUUUUUU: {e}")
        return None
    
data1 = "16/02/2025"
data2 = "16/06/2025"

dias = contar_dias(data1, data2)
if dias is not None:
    print(f"Parabens vocês estão juntos há: {dias} dias")
