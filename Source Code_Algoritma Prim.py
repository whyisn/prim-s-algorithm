# Program Algoritma Prim untuk Minimum Spanning Tree (MST)

import sys

class Graf():
	def __init__(self, simpul):
		self.JmlhSimpul = simpul
		self.graf = [[0 for kolom in range(simpul)] for baris in range(simpul)]

	def cetakMST(self, induk):
		print("Sisi \tBobot")
		for i in range(1, self.JmlhSimpul):
			print(induk[i], "-", i, "\t", self.graf[i][induk[i]])

	def indeksMin(self, kunci, mstSet):
		min = sys.maxsize

		for v in range(self.JmlhSimpul):
			if kunci[v] < min and mstSet[v] == False:
				min = kunci[v]
				min_index = v

		return min_index

	def primMST(self):
		kunci = [sys.maxsize] * self.JmlhSimpul
		induk = [None] * self.JmlhSimpul
		kunci[0] = 0
		mstSet = [False] * self.JmlhSimpul
		induk[0] = -1 

		for cout in range(self.JmlhSimpul):
			u = self.indeksMin(kunci, mstSet)
			mstSet[u] = True

			for v in range(self.JmlhSimpul):
				if self.graf[u][v] > 0 and mstSet[v] == False \
				and kunci[v] > self.graf[u][v]:
					kunci[v] = self.graf[u][v]
					induk[v] = u

		self.cetakMST(induk)


if __name__ == '__main__':
    # Inisialisasi graf dengan jumlah simpul 5
	g = Graf(5)

    # Definisi matriks ketetanggaan graf
	g.graf = [[0, 2, 0, 6, 0],
			[2, 0, 3, 8, 5],
			[0, 3, 0, 0, 7],
			[6, 8, 0, 0, 9],
			[0, 5, 7, 9, 0]]

    # Temukan dan cetak Minimum Spanning Tree (MST)
	g.primMST()
