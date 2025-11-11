
from typing import List, Optional
import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # inicializa o min-heap pra guardar os menores elementos
        min_heap = []
        
        # adiciona o primeiro no de cada lista ao heap (se existir)
        # o i eh usado pra desempatar qndo os valores sao iguais
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(min_heap, (node.val, i, node))
        
        # cria um no dummy pra facilitar a construcao da lista resultado
        dummy = ListNode(0)
        current = dummy
        
        # enquanto tiver elementos no heap
        while min_heap:
            # pega o menor elemento do heap
            val, i, node = heapq.heappop(min_heap)
            
            # adiciona o no aa lista resultado
            current.next = node
            current = current.next
            
            # se o no tiver um proximo, adiciona ele ao heap
            if node.next:
                heapq.heappush(min_heap, (node.next.val, i, node.next))
        
        # retorna a lista mesclada (ignora o dummy)
        return dummy.next