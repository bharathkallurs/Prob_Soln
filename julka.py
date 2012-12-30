import sys
import re
#https://www.spoj.com/problems/JULKA/
def main() :

  for i in range(10) :
		total = int(input())
		more = int(input())
		t_d = total % 2
		m_d = more % 2
		
		if not t_d and not m_d :
			n = int((total - more)/2)
			k = total - n
		elif t_d and m_d :
			n = int((total-more)/2 + 1)
			k = total - n
		else : print("\n")
		
		print(k) #klaudia
		print(n) #natalia
		



if __name__ == '__main__' :
	main()
