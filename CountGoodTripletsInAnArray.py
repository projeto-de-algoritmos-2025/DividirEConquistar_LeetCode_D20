from typing import List

class FenwickTree:
    __slots__ = ['tree']
    
    def __init__(self, n):
        # inicializa a arvore com n+1 posicoes (indice 0 nao eh usado)
        self.tree = [0] * (n + 1)
    
    def update(self, i):
        # converte pra indice 1-based da fenwick tree
        i += 1
        tree = self.tree
        n = len(tree)
        # atualiza a arvore subindo pelos nos pais
        while i < n:
            tree[i] += 1
            i += i & -i  # pula pro proximo no relevante
    
    def query(self, i):
        # soma dos elementos ate o indice i
        s = 0
        tree = self.tree
        while i > 0:
            s += tree[i]
            i -= i & -i  # pula pro no anterior
        return s

class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        
        # mapeia cada valor pra sua posicao em nums2
        pos2 = [0] * n
        for i, val in enumerate(nums2):
            pos2[val] = i
        
        # pre-computa as posicoes dos elementos de nums1 em nums2
        mapped = [pos2[nums1[i]] for i in range(n)]
        
        # conta quantos elementos aa esquerda sao menores (em nums2)
        ft1 = FenwickTree(n)
        smaller = [0] * n
        for i in range(n):
            pos = mapped[i]
            # quantos elementos antes de i tem posicao menor em nums2
            smaller[i] = ft1.query(pos)
            ft1.update(pos)
        
        # conta quantos elementos aa direita sao maiores (em nums2) e calcula o resultado
        ft2 = FenwickTree(n)
        result = 0
        for i in range(n - 1, -1, -1):  # percorre de tras pra frente
            pos = mapped[i]
            # quantos elementos depois de i tem posicao maior em nums2
            larger_count = ft2.query(n) - ft2.query(pos + 1)
            # multiplica os menores aa esquerda pelos maiores aa direita
            result += smaller[i] * larger_count
            ft2.update(pos)
        
        return result