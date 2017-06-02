from django.http import JsonResponse
from . import userapi


def slot(request):
	mid1 = request.POST.get('mid1')
	mid2 = request.POST.get('mid2')
	mid3 = request.POST.get('mid3')
	betamount = float(request.POST.get('betamount'))
	if mid1==mid2==mid3:#jesli srodkowy wiersz ma 3 takie same znaczki
	#symbole oczywiscie moga sie zmienic - tu komentarze i wygrane sa z grafiki z trello
		if mid1=='1':#winogorona x2
			betamount=betamount*2
		if mid1=='2':#wisnie x3
			betamount=betamount*3
		if mid1=='3':#banany x4
			betamount=betamount*4
		if mid1=='4':#gruszki x6
			betamount=betamount*6
		if mid1=='5':#pomarancze x10
			betamount=betamount*10
		if mid1=='6':#serduszka x15
			betamount=betamount*15
		if mid1=='7':#monety x20
			betamount=betamount*20
		if mid1=='8':#jackpot x30
			betamount=betamount*30
	else: #przegrana
		betamount=-betamount
	callModifyBalance(request,betamount)
	return JsonResponse({'amount':betamount})

def roulette(request):
        # przelicznik dla poszczególnych kombinacji
        # number (pojedynczy numer) ------------------ 36
        # red (czerwone) ----------------------------- 2
        # black (czarne) ----------------------------- 2
        # odd (nieparzyste) -------------------------- 2
        # even (parzyste) ---------------------------- 2
        # low (niskie 1-18) -------------------------- 2
        # high (wysokie 19-36) ----------------------- 2
        # 1st 12 (pierwszy tuzin 1-12) --------------- 3
        # 2nd 12 (drugi tuzin 13-24) ----------------- 3
        # 3rd 12 (trzeci tuzin 25-36) ---------------- 3
        # 1st column (pierwsza kolumna %3 == 1) ------ 3
        # 2nd column (druga kolumna %3 == 2) --------- 3
        # 3rd column (trzecia kolumna %3 == 0) ------- 3
        # 1st half (pierwsza połowa 1-18) ------------ 2
        # 2nd half (druga połowa 19-36) -------------- 2
        betList = makeArrayOfIntsFromString(request,'roulettebets')
        roulettespin = float(request.POST.get('roulettespin'))
        betListLen = len(betList)
        betamount = 0
        red = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
        black = [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]
	for i in range(37):
		#spradzenie czy obstawiono dany numer
		if roulettespin == i and betList[i] != 0:
			betamount = 35 * betList[i] + betamount
		else:
			betamount = -1 * betList[i] + betamount
	i = i + 1
	#sprawdzenie czy obstawiono czerwone
	if betList[i] != 0 and roulettespin in red:
		betamount = betList[i] + betamount
	else:
		betamount = -1 * betList[i] + betamount
	i = i + 1
	#sprawdzenie czy obstawiono czarne
	if betList[i] != 0 and roulettespin in black:
		betamount = betList[i] + betamount
	else:
		betamount = -1 * betList[i] + betamount
	i = i + 1
	#sprawdzenie czy obstawiono parzyste
	if betList[i] != 0 and roulettespin % 2 == 0 and roulettespin != 0:
		betamount = betList[i] + betamount
	else:
		betamount = -1 * betList[i] + betamount
	i = i + 1
	#sprawdzenie czy obstawiono nieparzyste
	if betList[i] != 0 and roulettespin % 2 == 1:
		betamount = betList[i] + betamount
	else:
		betamount = -1 * betList[i] + betamount
	i = i + 1
	#sprawdzenie czy obstawiono wysokie
	if betList[i] != 0 and roulettespin <= 18 and roulettespin != 0:
		betamount = betList[i] + betamount
	else:
		betamount = -1 * betList[i] + betamount
	i = i + 1
	#sprawdzenie czy obstawiono niskie
	if betList[i] != 0 and roulettespin > 18:
		betamount = betList[i] + betamount
	else:
		betamount = -1 * betList[i] + betamount
	i = i + 1
	#sprawdzenie czy obstawiono pierwszy tuzin
	if betList[i] != 0 and roulettespin <= 12 and roulettespin != 0:
		betamount = 2 * betList[i] + betamount
	else:
		betamount = -1 * betList[i] + betamount
	i = i + 1
	#sprawdzenie czy obstawiono drugi tuzin
	if betList[i] != 0 and roulettespin > 12 and roulettespin < 25:
		betamount = 2 * betList[i] + betamount
	else:
		betamount = -1 * betList[i] + betamount
	i = i + 1
	#sprawdzenie czy obstawiono trzeci tuzin
	if betList[i] != 0 and roulettespin >= 25:
		betamount = 2 * betList[i] + betamount
	else:
		betamount = -1 * betList[i] + betamount
	i = i + 1
	#sprawdzenie czy obstawiono pierwszą kolumnę
	if betList[i] != 0 and roulettespin % 3 == 1:
		betamount = 2 * betList[i] + betamount
	else:
		betamount = -1 * betList[i] + betamount
	i = i + 1
	#sprawdzenie czy obstawiono drugą kolumnę
	if betList[i] != 0 and roulettespin % 3 == 2:
		betamount = 2 * betList[i] + betamount
	else:
		betamount = -1 * betList[i] + betamount
	i = i + 1
		#sprawdzenie czy obstawiono trzecią kolumę
	if betList[i] != 0 and roulettespin % 3 == 0 and roulettespin != 0:
		betamount = 2 * betList[i] + betamount
	else:
		betamount = -1 * betList[i] + betamount
	callModifyBalance(request,betamount)
	return JsonResponse({'amount':betamount})

def dice(request):
        betamount = float(request.POST.get('betamount'))
        diceroll = request.POST.get('diceroll')
        dicebet = request.POST.get('dicebet')
        dicebetreversed = ''.join(reversed(dicebet))
        premium = 10
        if dicebet == dicebetreversed:
                premium = 20
        if dicebet == diceroll or dicebetreversed == diceroll:
                betamount = betamount * premium
	else:
		betamount = -1 * betamount
        callModifyBalance(request,betamount)
        return JsonResponse({'amount':betamount})

def blackjack(request):
	betamount = float(request.POST.get('betamount'))
	bankCards = makeArrayOfIntsFromString(request,'bank')
	playerCards = makeArrayOfIntsFromString(request,'player')
	bankScore = blackjackScore(bankCards)
	playerScore = blackjackScore(playerCards)
	amount = 0
	if bankScore > playerScore:
		amount = - betamount
	elif bankScore < playerScore:
		amount = betamount
	callModifyBalance(request,amount)
	return JsonResponse({"amount":amount})

def poker(request):
        # przelicznik dla poszczególnych kombinacji
        # royal flush (poker królewski) -------------- 4000
        # straight flush (poker) --------------------- 250
        # four of a kind (kareta) -------------------- 125
        # full house (ful) --------------------------- 45
        # flush (kolor) ------------------------------ 30
        # straight (strit) --------------------------- 20
        # three of a kind (trójka) ------------------- 15
        # two pair (dwie pary) ----------------------- 10
        # jacks or better (para waletów lub lepsza) -- 5
        betamount = float(request.POST.get('betamount'))
        counter = float(request.POST.get('counter'))
        playerCards = makeArrayOfIntsFromString(request,'cards')
        playerScore = pokerScore(playerCards)
        if playerScore == "royal flush":
                betamount = counter * betamount * 4000
        elif playerScore == "straight flush":
                betamount = counter * betamount * 250
        elif playerScore == "four of a kind":
                betamount = counter * betamount * 125
        elif playerScore == "full house":
                betamount = counter * betamount * 45
        elif playerScore == "flush":
                betamount = counter * betamount * 30
        elif playerScore == "straight":
                betamount = counter * betamount * 20
        elif playerScore == "three of a kind":
                betamount = counter * betamount * 15
        elif playerScore == "two pair":
                betamount = counter * betamount * 10
        elif playerScore == "jacks or better":
                betamount = counter * betamount * 5
        else:
                betamount= -1 * betamount * counter
        callModifyBalance(request,betamount)
        return JsonResponse({'amount':betamount})

def baccarat(request):
	betamount = float(request.POST.get('betamount'))
	bet = request.POST.get('bet')
	bankCards = makeArrayOfIntsFromString(request,'bank')
	playerCards = makeArrayOfIntsFromString(request,'player')
	bankScore = baccaratScore(bankCards)
	playerScore = baccaratScore(playerCards)
	result = ''
	amount = 0
	if bankScore == playerScore:
		result = 'tie'
	elif bankScore > playerScore:
		result = 'bank'
	else:
		result = 'player'
	if result==bet:
		if bet == 'player':
			amount = 2 * betamount
		elif bet == 'bank':
			amount = 1.95 * betamount
		else :
			amount = 8 * betamount
	else :
		amount = - betamount
	callModifyBalance(request, amount)
	return JsonResponse({'amount':amount})

def cointoss(request):
	betamount = float(request.POST.get('betamount'))
	bet = request.POST.get('bet')
	toss = request.POST.get('toss')
	if bet==toss:
		betamount = betamount * 1.9
	else:
		betamount=-betamount
	callModifyBalance(request,betamount)
	return JsonResponse({'amount':betamount})
	
#pomocniczne metody

def pokerScore(arrayOfInts):
        arr = sorted(arrayOfInts)
        arrM13 = [value%13 for value in arrayOfInts]
        arrM13 = sorted(arrM13)
        result = "error"
        #sprawdzanie kombinacji
        if arr[0] >= 1 and arr[4] <= 13 or arr[0] >= 14 and arr[4] <= 26 or arr[0] >= 27 and arr[4] <= 39 or arr[0] >= 40 and arr[4] <= 52:
        #sprawdzanie królewskiego pokera
                if arrM13[0] == 0 and arrM13[1] == 1 and arrM13[2] == 10 and arrM13[4] == 12:
                        result = "royal flush"
        #sprawdzanie pokera
                elif (arrM13[4] - arrM13[0] == 4 and arrM13[0] != 0) or (arrM13[0] == 0 and arrM13[1] == 9 and arrM13[4] == 12):
                        result = "straight flush"
        #jeśli nie poker to kolor
                else:
                        result = "flush"
        #sprawdzanie strita
        elif (arrM13[0] != arrM13[1] != arrM13[2] != arrM13[3] != arrM13[4] and arrM13[0] == 0 and arrM13[1] == 1 and arrM13[2] == 10 and arrM13[4] == 12) or (arrM13[0] != arrM13[1] != arrM13[2] != arrM13[3] != arrM13[4] and arrM13[4] - arrM13[0] == 4 and arrM13[0]!=0) or (arrM13[0] != arrM13[1] != arrM13[2] != arrM13[3] != arrM13[4] and arrM13[0] == 0 and arrM13[1] == 9 and arrM13[4] == 12) :
                result = "straight"
        elif (arrM13[0] == arrM13[1] == arrM13[2] == arrM13[3]) or (arrM13[1] == arrM13[2] == arrM13[3] == arrM13[4]):
                result = "four of a kind"
        elif (arrM13[0] == arrM13[1] == arrM13[2] and arrM13[3] == arrM13[4]) or (arrM13[0] == arrM13[1] and arrM13[2] == arrM13[3] == arrM13[4]):
                result = "full house"
        elif (arrM13[0] == arrM13[1] == arrM13[2]) or (arrM13[1] == arrM13[2] == arrM13[3]) or (arrM13[2] == arrM13[3] == arrM13[4]):
                result = "three of a kind"
        elif (arrM13[0] == arrM13[1] and arrM13[2] == arrM13[3]) or (arrM13[0] == arrM13[1] and arrM13[3] == arrM13[4]) or (arrM13[1] == arrM13[2] and arrM13[3] == arrM13[4]):
                result = "two pair"
        elif (arrM13[0] == arrM13[1] == 0) or (arrM13[0] == 0 and arrM13[1] == 1 and arrM13[2] == 1) or (arrM13[0] == 1 and arrM13[1] == 1) or (arrM13[0] == arrM13[1] and arrM13[0] >= 11) or (arrM13[1] == arrM13[2] and arrM13[1] >= 11) or (arrM13[2] == arrM13[3] and arrM13[2] >= 11) or (arrM13[3] == arrM13[4] and arrM13[3] >= 11)  : 
                result = "jacks or higher"
        else:
                result = "nothing"
        return result
                    
def makeArrayOfIntsFromString(request,postKey):
	arr = request.POST.get(postKey)
	arr = arr.split(',')
	arr = [int(value) for value in arr]
	return arr

def callModifyBalance(request,amount):
	mutable = request.POST._mutable
	request.POST._mutable = True
	request.POST['amount'] = amount
	request.POST._mutable = mutable
	response=userapi.modifyBalance(request)
	
def baccaratScore(arrayOfInts):
	arrayOfInts = [ value%13 for value in arrayOfInts ]
	result = 0;
	for value in arrayOfInts:
		if value < 10:
			result = result + value
	return result % 10

def blackjackScore(arrayOfInts):
	arrayOfInts = [value%13 for value in arrayOfInts]
	result = 0
	numberOfAces = 0
	for value in arrayOfInts:
		if value >=2 and value <=10:
			result = result + value
		elif value == 0 or value == 11 or value == 12: #krol od walet or dama
			result = result + 10
		elif value == 1:#as
			numberOfAces = numberOfAces + 1
	#tu mamy juz policzone wszystkie karty z wyjatkiem asow
	valueFromAces = 0
	bestOption = result + numberOfAces # najmniejszy mozliwy wynik ( punkty z karty + asy za jeden )
	for i in range(1,numberOfAces+1):
		valueFromAces = (numberOfAces-i) * 1 + i*10#tu jest liczona wartosc jezeli z n asow i bedzie traktowane jako '1' a n-i jako 10
		if  result + valueFromAces > 21:#wartosc liczona u gory jest rosnaca wiec jesli ktoras przekroczy 21 to konczymy petle
			break
		else:
			if (result + valueFromAces) > bestOption:#sprawdzamy czy ten podzial na '1' i '10' jest lepszy
				bestOption = result + valueFromAces
	result = bestOption
	if result > 21:
		result = 0
	return result
