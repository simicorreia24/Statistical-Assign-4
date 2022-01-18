#!/usr/bin/env python
# coding: utf-8

# Statistical Assignment 4
# 
# Question 1:
#     
# Is it possible that an event is independent of itself? If so, when?
# 
# Solution: 
# The only events that are independent of themselves are those with probability either 0 or 1.
# Because, 02 =0 and 12 =1
# The only way a random variable X can be independent of itself is if for every measurable set A, either Pr(X∈A)=1 or Pr(X∈A)=0.  
# 
# Question 2:
# 
# Is it always true that if A and B are independent events, then Ac and Bc are independent events? Show that it is, or give a counterexample.
# 
# Solution:
# 
# Assume A and B are independent. Then
# 𝑃(Ac ∩ Bc)
# =1− 𝑃(𝐴∪𝐵)
# =1− 𝑃(𝐴) − 𝑃(𝐵) + 𝑃(𝐴∩𝐵)
# =1− 𝑃(𝐴) − 𝑃(𝐵) + 𝑃(𝐴)𝑃(𝐵)
# =(1−𝑃(𝐴)) (1−𝑃(𝐵))
# =𝑃(Ac) 𝑃(Bc) P(Ac∩ Bc)
# =1− P(A∪B)
# =1− P(A) − P(B) + P(A∩B)
# =1− P(A) − P(B) + P(A)P(B)
# =(1−P(A)) (1−P(B))
# =P(Ac) P(Bc).
# 
