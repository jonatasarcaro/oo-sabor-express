from modelos.cardapio.item_cardapio import ItemCardapio

class Prato(ItemCardapio):  # A classe 'Prato' herda de 'ItemCardapio', vai usar os atributos dessa classa
        def __init__(self,nome,preco,descricao):
             super().__init__(nome,preco) # Minha classe prato ta usando os atributos e informações da classe principal
             self.descricao = descricao # Vamos usar as informações da classa mãe (nome,preco) porém podemos adicionar mais quando for necessário
             