#!/usr/bin/env python
from inspect import ismethod
from  PyQt5.QtWidgets import QHBoxLayout,QVBoxLayout,QGridLayout,QFormLayout
from  PyQt5.QtWidgets import QWidget

def Qt_tools():
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
	f={}
	f['l']=Layouts()
	f['p']=SizePols()
	return f

def Wgt_Func(fn):
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
		return mtds

	f=locals()

	return f[fn]

def Wgt(**k):
		QT=Qt_tools()
		Mtds=Wgt_Func('Mtds')['Wgt']
		def Arg(*a, **k):
			n			= k.get("n")
			t			= k.get("t")
			m			=	k.get("m")
			l			=	k.get("l")
			k=locals()
			return k[a]
		def props():
			name 		= Arg('n')
			layout 	=	QT['l'][Arg('t')].__name__
			return locals()
		def Mtd():
			f=Mtds(w)
			return f
		def Layout():
			Mtds=Wgt_Func('Mtds')['Lay']
			def Mtd():
				f=Mtds(l)
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
		def Init():
			def init():
				w['Mtd']['setObjectName'](f'wgt_{Arg("n")}')
				w['Mtd']['setContentsMargins'](*Arg('m'))
			init()
			return init

		w= {}
		w['Wgt']			=	QWidget()
		w['Arg']			=	Arg()
		w['Prop']			= props()
		w['Mtd']			=	Mtd()
		w['Lay']			= Layout()
		w['Init']			=	Init()
		return w
