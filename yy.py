#!/usr/bin/env python

gua=(
("qian",        ( 1, 1, 1, 1, 1, 1)),
("kun",			(-1,-1,-1,-1,-1,-1)),
("zhun",		( 1,-1,-1,-1, 1,-1)),
("meng", 		(-1, 1,-1,-1,-1, 1)),
("xu",			( 1, 1, 1,-1, 1,-1)),
("song",		(-1, 1,-1, 1, 1, 1)),
("shi",			(-1, 1,-1,-1,-1,-1)),
("bi",			(-1,-1,-1,-1, 1,-1)),
("xiaoxu",		( 1, 1, 1,-1, 1, 1)),
("lv",			( 1, 1,-1, 1, 1, 1)),
("tai",			( 1, 1, 1,-1,-1,-1)),
("pi",			(-1,-1,-1, 1, 1, 1)),
("tongren",		( 1,-1, 1, 1, 1, 1)),
("dayou",		( 1, 1, 1, 1,-1, 1)),
("qianxu",		(-1,-1, 1,-1,-1,-1)),
("yu",			(-1,-1,-1, 1,-1,-1)),
("sui",			( 1,-1,-1, 1, 1,-1)),
("gu",			(-1, 1, 1,-1,-1, 1)),
("lin",			( 1, 1,-1,-1,-1,-1)),
("guan",		(-1,-1,-1,-1, 1, 1)),
("shihe",		( 1,-1,-1, 1,-1, 1)),
("fen",			( 1,-1, 1,-1,-1, 1)),
("bo",			(-1,-1,-1,-1,-1, 1)),
("fu",			( 1,-1,-1,-1,-1,-1)),
("wuwang",		( 1,-1,-1, 1, 1, 1)),
("daxu",		( 1, 1, 1,-1,-1, 1)),
("yi",			( 1,-1,-1,-1,-1, 1)),
("daguo",		(-1, 1, 1, 1, 1,-1)),
("xikan",		(-1, 1,-1,-1, 1,-1)),
("li",			( 1,-1, 1, 1,-1, 1)),
("xian",		(-1,-1, 1, 1, 1,-1)),
("heng",		(-1, 1, 1, 1,-1,-1)),

("dun",			(-1,-1, 1, 1, 1, 1)),
("dazhuang",	( 1, 1, 1, 1,-1,-1)),
("jin",			(-1,-1,-1, 1,-1, 1)),
("mingyi",		( 1,-1, 1,-1,-1,-1)),
("jiaren",		( 1,-1, 1,-1, 1, 1)),
("kui",			( 1, 1,-1, 1,-1, 1)),
("qian",		(-1,-1, 1,-1, 1,-1)),
("jie",			(-1, 1,-1, 1,-1,-1)),
("shun",		( 1, 1,-1,-1,-1, 1)),
("yi",			( 1,-1,-1,-1, 1, 1)),
("guai",		( 1, 1, 1, 1, 1,-1)),
("hou",			(-1, 1, 1, 1, 1, 1)),
("cui",			(-1,-1,-1, 1, 1,-1)),
("sheng",		(-1, 1, 1,-1,-1,-1)),
("kun",			(-1, 1,-1, 1, 1,-1)),
("jing",		(-1, 1, 1,-1, 1,-1)),
("ge",			( 1,-1, 1, 1, 1,-1)),
("ding",		(-1, 1, 1, 1,-1, 1)),
("zhen",		( 1,-1,-1, 1,-1,-1)),
("gen",			(-1,-1, 1,-1,-1, 1)),
("jian",		(-1,-1, 1,-1, 1, 1)),
("guimei",		( 1, 1,-1, 1,-1,-1)),
("feng",		( 1,-1, 1, 1,-1,-1)),
("lv",			(-1,-1, 1, 1,-1, 1)),
("zhua",		(-1, 1, 1,-1, 1, 1)),
("dui",			( 1, 1,-1, 1, 1,-1)),
("huan",		(-1, 1,-1,-1, 1, 1)),
("jie",			( 1, 1,-1,-1, 1,-1)),
("zhonfu",		( 1, 1,-1,-1, 1, 1)),
("xiaoguo",		(-1,-1, 1, 1,-1,-1)),
("jiji",		( 1,-1, 1,-1, 1,-1)),
("weiji",		(-1, 1,-1, 1,-1, 1)),
)

a=[0,0,0,0,0,0]
s=0
for i in range(31,64):
	a[0]=a[0]+gua[i][1][0]
	a[1]=a[1]+gua[i][1][1]
	a[2]=a[2]+gua[i][1][2]
	a[3]=a[3]+gua[i][1][3]
	a[4]=a[4]+gua[i][1][4]
	a[5]=a[5]+gua[i][1][5]
	s=s+sum(gua[i][1])
	print sum(gua[i][1])
	
print a,s