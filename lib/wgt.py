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
			r=a[q]
			return r
		return arg

	def Elements():
		e={}
		return e

	def Mtd():
		mtd=gnr.Mtd()
		return mtd(Wgt)

	def Atr():
		atr=gnr.Atr()
		return atr(Wgt)

	def Lay():
		l = Layout(w=W,**k) if A('t') else None
		return l

	def Fnx():
		def Add(i):
			w['Lay']['Add'](i['Wgt'])
			w['Elements']['n']= i
		f={}
		f['Add'] = Add
		return f

	def Init():
		Mt['setObjectName'](f'wgt_{A("n")}')
		Mt['setContentsMargins'](*A('m'))



	W	=		QWidget()
	A	=		Arg(**k)
	El=Elements()
	Mt	=   Mtd()
	At	=   Atr()
	L	=   Lay()
	Fn	=   Fnx()
	# Init()

	w= {}
	w['Wgt']			=	W
	w['Arg']			= A
	w['Elements']	= El
	w['Mtd']			=	Mt
	w['Atr']			= At
	w['Lay']			= L
	w['Fnx']			=	Fn

	return w

def Layout(**k):
	def Arg(**K):
		a={}
		a['n']			= K.get('n')
		a['t']			= K.get('t')
		a['m']			=	K.get('m') or [0,0,0,0]
		a['w']			=	K.get('w')
		a['k']			=	{**k}
		def arg(q):
			r=a[q]
			return r
		return arg

	def Lay():
		type=	A('t')
		wgt=A('w')
		lay=gnr.Layouts(type)
		r=lay(wgt)
		return r

	def Mtd():
		mtd=gnr.Mtd()
		return mtd(L)

	def Atr():
		atr=gnr.Atr()
		return atr(L)

	def Add():
		return  Mt['addWidget']

	def Init():
		def init():
			Mt['setObjectName'](f'lay_{A("n")}')
			Mt['setContentsMargins'](*A('m'))
		init()
		return init

	A  =  Arg(**k)
	L  = 	Lay()

	Mt  = 	Mtd()
	At  =  Atr()
	Ad  =  Add()
	In = 	Init()

	l= {}
	l['Lay']			=	L
	l['Arg']			= A
	l['Mtd']			=	Mt
	l['Atr']			= At
	l['Add']			= Ad
	l['Init']			=	In








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