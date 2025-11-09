class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        n = len(nums)
        counts = [0] * n # contagem dos numeros menores aa direita pra cada indice
        
        # cria um vetor de pares com o valor e o indice do numero (o indice eh pra atualizar o vetor counts)
        pairs = []
        for i in range(n):
            pairs.append((nums[i], i))
            
        self._merge_sort(pairs, counts)
        
        return counts

    def _merge_sort(self, pairs, counts):
        
        # caso base se o vetor tiver tamanho 1 ja ta ordenado
        if len(pairs) <= 1:
            return pairs

        # quebrar o vetor em 2 e chamar a recursao pra cada parte
        mid = len(pairs) // 2
        left = self._merge_sort(pairs[:mid], counts)
        right = self._merge_sort(pairs[mid:], counts)
        
        # mergear os dois lados
        return self._merge(left, right, counts)

    def _merge(self, left, right, counts):
        
        merged = []
        
        # ponteiros pros vetores de esquerda e direita
        i = 0
        j = 0
        
        # contador de elementos menores aa direita
        j_small_count = 0
        
        while i < len(left) and j < len(right):
            
            # qndo o elemento da esquerda eh menor ou igual ao dda direita
            if left[i][0] <= right[j][0]:
                
                # o elemento da esquerda ainda eh maior que j_small_count elementos da direita q o algoritmo ja passou
                original_index = left[i][1]
                counts[original_index] += j_small_count
                
                merged.append(left[i])
                i += 1
            
            # qndo o elemento da direita eh menor
            else:
                
                j_small_count += 1
                
                merged.append(right[j])
                j += 1

        # qlqr elemento q sobrou na esquerda eh maior que todos os elementos da direita
        while i < len(left):
            original_index = left[i][1]
            counts[original_index] += j_small_count #
            
            merged.append(left[i])
            i += 1
            
        # qlqr elemento q sobrou a direita eh maior q todos dda esquerda e n precisa ser contado
        while j < len(right):
            merged.append(right[j])
            j += 1
            
        return merged