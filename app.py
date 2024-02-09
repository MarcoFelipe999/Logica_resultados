from time import sleep


def result():
    resultados = []
    result = driver.find_element(By.CLASS_NAME,'roulette-game-area__history-line') 
    elemento = result.text
    ad_lista = elemento.split("\n")   
    resultados.extend(ad_lista) 
    return resultados

def result_final():
    resultado_function = result()
    while True:
        sleep(1.5)
        resultados_new = []
        resulta = driver.find_element(By.CLASS_NAME,'roulette-game-area__history-line')
        elementos = resulta.text
        adicionar_lista = elementos.split("\n") 
        resultados_new.extend(adicionar_lista)
        if resultado_function != resultados_new:
            break
    return resultados_new
    
"""
Dentro da função result(), atribua à variável result a classe ou o xpath dos 
resultados desejados, em seguida, converta-o em texto. 
Realizo uma quebra de linha no ad_lista e então estendo-o para a lista vazia onde resultados = [].

Em seguida, entra a função result_final():

Inicio chamando a função result() para obter os resultados 
disponíveis até o momento, por exemplo: [5, 8, 10, 12].
O loop só será interrompido quando um novo resultado for encontrado, 
utilizando a mesma lógica da função result().
A condição if resultado_function, que está atribuída à função result(), 
irá parar o loop se for diferente de resultados_new, retornando então resultados_new 
que contém os resultados novos, por exemplo: [14, 5, 8, 10].
Por fim, basta chamar a função result_final() em algum lugar do código.

"""