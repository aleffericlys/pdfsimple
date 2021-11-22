#! /usr/bin/python3
#Copyright ReportLab Europe Ltd. 2000-2017
from reportlab.lib import pagesizes, units
from reportlab.pdfgen import canvas
from skimage.io import imread


class PDF():
	"""[summary]
	"""
	def __init__(self, nome: str, altura = 267, largura = 30) -> None:
		self.pdf = canvas.Canvas("{}.pdf".format(nome), pagesize = pagesizes.A4)
		self.altura = units.mm * altura
		self.largura = units.mm * largura

	def addText(self, texto: str, pos: str= 'esquerda', tipo: str = 'comum'):
		"""[classe de inserção de texto no arquivo pdf]

		Args:
			texto (str): [deverá conter o texto a ser inserido]
			pos (str): [deverá conter a posição onde será inserido o texto(esquerda, centro)]
			tipo (str): [deverá conter o tipo de texto a ser inserido(titulo ou comum)]
		"""
		if tipo == 'titulo':
			self.pdf.setFontSize(18)
		else:
			self.pdf.setFontSize(12)
		if pos == 'centro':
			self.pdf.drawString(self.largura + units.mm * 65, self.altura, texto)
		else:
			self.pdf.drawString(self.largura, self.altura, texto)
		self.altura -= units.mm * 6
		
	def addimage(self, image, pos: str = ""):
		"""fumção para a adição de uma imagem

		Args:
			image (str): local onde a imagem se encontra
			pos (str): muda a posição onde se coloca a imagem (centro)
		"""
		imagem = imread(image)
		tamanho = imagem.shape
		if tamanho[0] > tamanho[1]:
			alt = tamanho[0]/tamanho[1] * 70
			larg = 70
		elif tamanho[0] < tamanho[1]:
			alt = 70
			larg = tamanho[1]/tamanho[0] * 70
		else:
			alt = 70
			larg = 70

		if pos == 'centro':
			self.pdf.drawImage(image, self.largura + (105 - (larg/2)), self.altura - (units.mm * alt), units.mm * larg, units.mm * alt)
		else:
			self.pdf.drawImage(image, self.largura, self.altura - (units.mm * alt), units.mm * larg, units.mm * alt)
			pass
		self.altura -= units.mm * alt + 6


	def salvar(self):
		self.pdf.save()


c = PDF("teste")
c.addimage('pacote/IMG/grafico.png')
c.salvar()