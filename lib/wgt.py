#!/usr/bin/env python

from  PyQt5.QtWidgets import QHBoxLayout,QVBoxLayout,QGridLayout,QFormLayout
from  PyQt5.QtWidgets import QWidget
from lib import gnr
def qTools():


def wFnx():

def Wgt(**k):


	def Arg(*a, **k):
		n			= k.get("n")
		t			= k.get("t")
		m			=	k.get("m")
		l			=	k.get("l")
		k=locals()
		return k[a]
	def props():
		name 		= Arg('n')
		layout 	= QT['l'][Arg('t')].__name__
		return locals()

	def Atr():
		a=dClass('Attr')['Wgt'](w)
		return  a



		def Init():
			def init():
				w['Mtd']['setObjectName'](f'wgt_{Arg("n")}')
				w['Mtd']['setContentsMargins'](*Arg('m'))
			init()
			return init

		w= {}
		w['Wgt']			=	QWidget()
		w['Arg']			=	Arg()
		w['Prp']			= props()
		w['Mtd']			=	Mtd()
		w['Atr']			= Atr()
		w['Lay']			= Layout()
		w['Init']			=	Init()
		return w

def Layout():

	def Mtd():
		f=dClass('Mtds')['Lay'](l)
		return f
	def Init():
		def init():
			l['Mtd']['setObjectName'](f'lay_{Arg("n")}')
			l['Mtd']['setContentsMargins'](*Arg('m')
			l['Mtd']['setSpacing'](0)
		init()
		return init
	l={}
	if Arg('t') is not None:
		l['Lay']=QT['l'][Arg('t')](w['Wgt'])
		l['Mtd']=Mtd()
		l['Init']=Init()
	return l

