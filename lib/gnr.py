#!/usr/bin/env python
# Auth
from inspect import ismethod

def Layouts():

	l				=		{
		'H'   :	QHBoxLayout,
		'V'   : QVBoxLayout,
		'G'   :	QGridLayout,
		'F'   :	QFormLayout,
						}
	return l
def SizePols():
	from PyQt5.QtWidgets.QSizePolicy import QSizePolicy as QSP
	p={
			'P'   : QSP.Preferred,
			'M'   : QSP.Maximum,
			'm'   : QSP.Minimum,
			'E'   :	QSP.Expanding,
			'mE'  :	QSP.MinimumExpanding,
			'F'   :	QSP.Fixed,
		}
	return p

l=Layouts()
p=SizePols()

def dClass(fn):
	def Mtds(key):
		def mtds(o):
			f={}
			for n in dir(o[key]):
				m=getattr(o, n)
				if callable(m) and '__' not in n:
					f[n]=m
			return f
		return mtds
	def Attr(key):
		def attr(o):
			# v={}
			# for n in dir(o[key]):
			# 	a=getattr(o, n)
			# 	if callable(a) and '__' not in n:
			# 		v[n]=a
			v={n : getattr(o, n) for n in dir(o[key]) if ismethod(a)}
			return v
		return attr
	f=locals()
	return f[fn]
def Mtd():
	def mtd(w):
		m=qTools.dClass('Mtds')['Wgt'](w)
		return m
	return mtd
def Atr():
	def atr(w):
		a=qTools.dClass('Attr')['Wgt'](w)
		return a
	return atr
