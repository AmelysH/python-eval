class TreeBuilder:
    """
    Cette classe permet de créer un arbre binaire à partir d'un texte 
    selon le codage de Huffman
    """

    def __init__(self, text: str):
        self.text = text

    def tree(self):
        """
        Cette méthode crée un arbre binaire à l'aide de dictionnaires imbriqués
        """

        # Création d'un dictionnaire référençant le nombre d'occurences
        # de chaque caractère
        dico = {}
        for x in self.text:
            if x in dico:
                dico[x] += 1
            else:
                dico[x] = 1

        # Création de l'arbre binaire par dictionnaires imbriqués
        arbre = [(compte, lettre) for (lettre, compte) in dico.items()]
        while len(arbre) >= 2:
            arbre = sorted(arbre, key=lambda x: x[0], reverse=True)
            occ1, noeud1 = arbre.pop()
            occ2, noeud2 = arbre.pop()
            arbre = [(occ1 + occ2, {0: noeud1, 1: noeud2})] + arbre
        arbre = arbre[0][1]

        return arbre

class Codec:
    """
    Cette classe fournit un objet qui permet d' encoder et de décoder un 
    texte à partir d'un arbre binaire donné.
    L'attribut code de l'objet est un dictionnaire qui associe à chaque 
    caractère son code binaire.
    """

    def __init__(self, tree):
        code = {}
        def code_parcours(arbre, pre, code):
            for noeud in arbre :
                if len(arbre[noeud]) == 1:
                    code[arbre[noeud]] = pre + str(noeud)
                else:
                    code_parcours(arbre[noeud], pre + str(noeud), code)
        # Création du dictionnaire correspondant à l'arbre binaire donné
        code_parcours(tree, '', code)
        self.code = code
    
    def encode(self, text: str) -> str:
        """
        La méthode encode permet de coder le texte fourni à l'aide du 
        dictionnaire contenu dans l'attribut code de l'objet.
        """
        code = ""
        for i in text:
            code += self.code[i]
        return code
    
    def decode(self, code: str) -> str:
        """
        La méthode decode permet de décoder le code fourni à l'aide du 
        dictionnaire contenu dans l'attribut code de l'objet.
        """

        # On renverse le dictionnaire pour attribuer à chaque code 
        # binaire le caractère qui lui correspond
        reverse_codec = {i:j for j,i in self.code.items()}
        text=""
        while code != "":
            aux = True
            i = 2
            while aux:
                if code[:i] in self.code.values():
                    aux = False
                    text += reverse_codec[code[:i]]
                    code = code[i:]
                else:
                    i += 1
        return text