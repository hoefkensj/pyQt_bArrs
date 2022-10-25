#!/usr/bin/env python


from  PyQt5.QtWidgets import QWidget,QApplication,QLineEdit
import gnr



def Wgt(**k):

	def Arg(**K):
		a={}
		a['n']			= K.get("n")
		a['t']			= K.get("t")
		a['m']			=	K.get("m") or [0,0,0,0]
		a['k']			=	{**k}
		def arg(q):
			r=a['q']
			return r
		return arg

	def Elements():
		e={}
		return e


	def Mtd():
		mtd=gnr.Mtd()
		return mtd(w)

	def Atr():
		atr=gnr.Atr()
		return atr(w)

	def Lay():
		l = Layout(w=w,**k) if Arg('t') else None
		return l

	def Fnx():
		def Add(i):
			w['Lay']['Add'](i['Wgt'])
			w['Elements']['n']= i
		f={}
		f['Add'] = Add
		return f

	def Init():
		def init():
			w['Mtd']['setObjectName'](f'wgt_{Arg("n")}')
			w['Mtd']['setContentsMargins'](*Arg('m'))

		init()
		return init

	Arg=Arg(**k)
	Elements=Elements()
	Prp=Props()
	w= {}
	w['Wgt']			=	QWidget()
	w['Arg']			= Arg
	w['Elements']	= Elements
	w['Prp']			= Props
	w['Mtd']			=	Mtd()
	w['Atr']			= Atr()
	w['Lay']			= Lay()
	w['Fnx']			=	Fnx()
	w['Init']			=	Init()
	return w

def Layout(**k):
	def Arg(*a):
		arg={}
		arg['n']			= k.get("n")
		arg['t']			= k.get("t")
		arg['m']			=	k.get("m") or [0,0,0,0]
		arg['l']			=	k.get("l")
		arg['w']			=	k.get("w")
		arg['k']			=	k
		return arg
	def Lay():
		type=	Arg('t')
		wgt=Arg('w')
		lay=gnr.Layouts(type)
		r=lay(wgt['Wgt'])
		return r

	def Props():
		name 		= Arg('n')
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
			l['Mtd']['setObjectName'](f'lay_{Arg("n")}')
			l['Mtd']['setContentsMargins'](*Arg('m'))
		init()
		return init

	l= {}
	l['Wgt']			=	Lay()
	l['Arg']			= Arg()
	l['Prp']			= Props()
	l['Mtd']			=	Mtd()
	l['Atr']			= Atr()
	l['Add']			= Add()
	l['Init']			=	Init()
	return l


def lEdit(**k):
	n,w,h,ro=[*[0]*4]
	def Arg():
		nonlocal n,w,h,ro
		n		=	k['n']				=	k.get('n')
		w		=	k['w']				= k.get('w')	or 20
		h		=	k['h']				= k.get('h')	or 20
		ro	=	k['ro']				= k.get('ro')	or False

		return k




	l={}
	l['Wgt'] 		=  QLineEdit()
	l['Arg'] = Arg()



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
		a['QApp'] 		= QApplication(argv)
		a['Clip']			= a['QApp'].clipboard()

		return a
	GUI={}
	GUI['App']=App()
	GUI['Main']	=	Wgt(n='Qt5',t='V')

	test_wgt=lEdit(n='test')
	GUI['Main']['Fnx']['Add'](test_wgt)






	GUI['Main']['Mtd']['show']()
	Tree(d=GUI)
	sys.exit(GUI['App']['QApp'].exec())


	for k in GUI:
		print(k)
		if isinstance(GUI.get(k),dict):
			for l in GUI.get(k):
				print(l,GUI[k].get(l))
				if isinstance(GUI[k].get(l),dict):
					for m in GUI[k].get(l):
						print(m,GUI[k][l])