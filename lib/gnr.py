#!/usr/bin/env python
# Auth
from inspect import ismethod
from  PyQt5.QtWidgets import QHBoxLayout,QVBoxLayout,QGridLayout,QFormLayout
from  PyQt5.QtWidgets  import  QSizePolicy as QSP
def Layouts(t):

	l				=		{
		'H'   :	QHBoxLayout,
		'V'   : QVBoxLayout,
		'G'   :	QGridLayout,
		'F'   :	QFormLayout,
						}
	return l[t]
def SizePols():

	p={
			'P'   : QSP.Preferred,
			'M'   : QSP.Maximum,
			'm'   : QSP.Minimum,
			'E'   :	QSP.Expanding,
			'mE'  :	QSP.MinimumExpanding,
			'F'   :	QSP.Fixed,
		}
	return p

l=Layouts
p=SizePols()

def dClass(fn):
	def Mtds(key):
		def mtds(o):
			f={}
			for n in dir(o[key]):
				m=getattr(o[key], n)
				if callable(m) and '__' not in n:
					f[n]=m
			return f
		return mtds
	def Attr(key):
		def attr(o):
			v={}
			for n in dir(o[key]):
				a=getattr(o[key], n)
				if not ismethod(a) and '__' not in n:
					v[n]=a
			return v
		return attr
	f=locals()
	return f[fn]
def Mtd():
	def mtd(w):
		m=dClass('Mtds')('Wgt')(w)
		return m
	return mtd
def Atr():
	def atr(w):
		a=dClass('Attr')('Wgt')(w)
		return a
	return atr
