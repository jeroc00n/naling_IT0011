A = {'a', 'b', 'c', 'd', 'f', 'g'}
B = {'b', 'c', 'd', 'f', 'h', 'l', 'm', 'o'}
C = {'c', 'd', 'f', 'h', 'i', 'j', 'k'}

A_union_B = A | B
print("(a) Number of elements in A ∪ B:", len(A_union_B))

A_union_C = A | C
B_difference_A_union_C = B - A_union_C
print("(b) Number of elements in B - (A ∪ C):", len(B_difference_A_union_C))

h_i_j_k = C - (A | B)
c_d_f = A & B & C
b_c_h = (B & A) | (B & C)
d_f = c_d_f - {'c'}
c_only = c_d_f - {'d', 'f'}
l_m_o = B - A_union_C

print("(i) {h, i, j, k}:", h_i_j_k)
print("(ii) {c, d, f}:", c_d_f)
print("(iii) {b, c, h}:", b_c_h)
print("(iv) {d, f}:", d_f)
print("(v) {c}:", c_only)
print("(vi) {l, m, o}:", l_m_o)