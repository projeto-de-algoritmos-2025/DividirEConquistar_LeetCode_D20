class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        
        # garantir que nums1 seja o mais curto
        if m > n:
            # trocar as variaveis
            nums1, nums2, m, n = nums2, nums1, n, m
            
        total_len = m + n
        
        # numero de elementos na metade esquerda dos vetores mergeados
        half_len = (total_len + 1) // 2
        
        # busca binaria pra encontrar a particao ideal pro nums1
        l, r = 0, m
        
        while l <= r:
            # criar as particoes
            cut1 = (l + r) // 2 # indice da particao pra nums1
            cut2 = half_len - cut1 # pra nums 2
            
            # elementos de borda
            L1 = nums1[cut1 - 1] if cut1 > 0 else float('-inf') # maximo aa esquerda de cut1
            R1 = nums1[cut1] if cut1 < m else float('inf') # minimo aa direita de cut1
            
            L2 = nums2[cut2 - 1] if cut2 > 0 else float('-inf') # maximo a esquerda de cut2
            R2 = nums2[cut2] if cut2 < n else float('inf') # minimo aa direita de cut2
            
            # condicoes da ordem
            if L1 <= R2 and L2 <= R1: # particao correta
                # impar ent a mediana eh o maximo da metade esquerda
                if total_len % 2 == 1:
                    return float(max(L1, L2))
                else:
                    # par ent a meddiana eh a media entre o maior da esquerda e o menor da direita
                    return (max(L1, L2) + min(R1, R2)) / 2.0
            
            elif L1 > R2:
                # mover cut1 pra esquerda se L1 estiver mto grande
                r = cut1 - 1
            
            else: # L2 > R1
                # pra direita se L2 estiver mto grande 
                l = cut1 + 1