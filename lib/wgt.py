#!/usr/bin/env python


from  PyQt5.QtWidgets import QWidget,QApplication
import gnr


def Wgt(**k):



	def Arg(a):
		arg={}
		arg['n']			= k.get("n")
		arg['t']			= k.get("t")
		arg['m']			=	k.get("m") or [0,0,0,0]
		arg['l']			=	k.get("l")
		arg['w']			=	k.get("w")
		r = arg.get(a)
		return r

	def Elements():
		e={}
		return e
	def Props():
		name 		= Arg(a='n')
		layout 	= gnr.Layouts(Arg('t'))
		return locals()

	def Mtd():
		mtd=gnr.Mtd()
		return mtd(w)

	def Atr():
		atr=gnr.Atr()
		return atr(w)

	def Lay():
		l = Layout(w=w,**k) if Arg(a='t') else None
		return l

	def Fnx():
		def Add(i):
			w['Lay']['Add'](i['Wgt'])
			w['Elements'][i['Prp']['name']]= i
		f={}
		f['Add'] = Add
		return f
	def Init():
		def init():
			w['Mtd']['setObjectName'](f'wgt_{Arg(a="n")}')
			w['Mtd']['setContentsMargins'](*Arg(a='m'))

		init()
		return init

	w= {}
	w['Wgt']			=	QWidget()
	w['Elements']	= Elements()
	w['Prp']			= Props()
	w['Mtd']			=	Mtd()
	w['Atr']			= Atr()
	w['Lay']			= Lay()
	w['Fnx']			=	Fnx()
	w['Init']			=	Init()
	return w

def Layout(**k):
	def Arg(a):
		arg={}
		arg['n']			= k.get("n")
		arg['t']			= k.get("t")
		arg['m']			=	k.get("m") or [0,0,0,0]
		arg['l']			=	k.get("l")
		arg['w']			=	k.get("w")
		r = arg.get(a)
		return r
	def Lay():
		lay=gnr.Layouts(Arg('t'))
	def Props():
		name 		= Arg(a='n')
		layout 	= gnr.Layouts(Arg('t')).__name__
		return locals()

	def Mtd():
		mtd=gnr.Mtd()
		return mtd(l)

	def Atr():
		atr=gnr.Atr()
		return atr(l)

	def Add():
		return  l['Mtd']['addWidget']

	def Init():
		def init():
			l['Mtd']['setObjectName'](f'lay_{Arg(a="n")}')
			l['Mtd']['setContentsMargins'](*Arg(a='m'))
		init()
		return init

	l= {}
	l['Wgt']			=	gnr.Layouts(Arg('t'))(Arg('w')['Wgt'])
	l['Prp']			= Props()
	l['Mtd']			=	Mtd()
	l['Atr']			= Atr()
	l['Add']			= Add()
	l['Init']			=	Init()
	return l

if __name__ == '__main__':
	import sys
	def Tree(*a,**k):
			d = k.get('d')
			indent = k.get('indent') or 0
			for key in d:
				if isinstance(d[key], dict):
					sys.stdout.write('  ┃  ' * (indent) + '  ┣━━ ' + '\x1b[1;32m' + str(key) + ':' + '\x1b[0m\n')
					if len(d[key]) > 10:
						sys.stdout.write('  ┃  ' * (indent) + '  ┣━━ ' + '(+ '+ str(len(d[key])) + ' items)' + '\n')
					else:
						Tree(d=d[key],indent=indent + 1)
				else:
					sys.stdout.write('  ┃  ' * (indent) + '  ┣━━ ' + str(key) + '\t:\t' + str(d[key]) + '\n')

	def App():
		from sys import argv
		a = {}
		a['QtApp'] 		= QApplication(argv)
		a['Clip']			= a['QtApp'].clipboard()

		return a
	GUI={}
	GUI['App']=App()
	GUI['Main']	=	Wgt(n='Qt5',t='V')

	test_wgt=Wgt(n='test',t='V')
	GUI['Main']['Fnx']['Add'](test_wgt)

	Tree(d=GUI)
	#
	# for k in GUI:
	# 	print(k)
	# 	if isinstance(GUI.get(k),dict):
	# 		for l in GUI.get(k):
	# 			print(l,GUI[k].get(l))
				# if isinstance(GUI[k].get(l),dict):
				# 	for m in GUI[k].get(l):
				# 		print(m,GUI[k][l])