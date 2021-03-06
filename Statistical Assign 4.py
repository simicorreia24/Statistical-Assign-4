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
# The only way a random variable X can be independent of itself is if for every measurable set A, either Pr(XâA)=1 or Pr(XâA)=0.  
# 
# Question 2:
# 
# Is it always true that if A and B are independent events, then Ac and Bc are independent events? Show that it is, or give a counterexample.
# 
# Solution:
# 
# Assume A and B are independent. Then
# ð(Ac â© Bc)
# =1â ð(ð´âªðµ)
# =1â ð(ð´) â ð(ðµ) + ð(ð´â©ðµ)
# =1â ð(ð´) â ð(ðµ) + ð(ð´)ð(ðµ)
# =(1âð(ð´)) (1âð(ðµ))
# =ð(Ac) ð(Bc) P(Acâ© Bc)
# =1â P(AâªB)
# =1â P(A) â P(B) + P(Aâ©B)
# =1â P(A) â P(B) + P(A)P(B)
# =(1âP(A)) (1âP(B))
# =P(Ac) P(Bc).
# 
