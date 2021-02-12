
def dotUsdtSpotBnb(fiatBahtAmount, usdtPriceBitkub, bnbPriceBinance, dotPriceBitkub, dotPriceSpotBnb):
	#  INPUTS descriptions : 
	# fiatBahtAmount = THB you want to put to Bitkub
	# usdtPriceBitkub = current USDT price or the price you'd like to bid in Bitkub (example: THB 30.2)
	# bnbPriceBinance = BNB price in Binance (example: USDT 125)
	# dotPriceBitkub = current DOT price in Bitkub or the price you'd like to bid
	# dotPriceSpotBnb = current DOT spot price against BNB (example: DOT/BNB 0.2)

	### convert THB fiat to USDT in Bitkub > transfer USDT to Binance to purchase DOT in BNB spot ###
	USDT_FEE = 18
	usdtAmountBitkub = fiatBahtAmount/usdtPriceBitkub
	usdtAmountBitkubTransferred = usdtAmountBitkub-USDT_FEE
	bnbTotal = usdtAmountBitkubTransferred/bnbPriceBinance
	dotTotal1 = bnbTotal/dotPriceSpotBnb

	### direct purchase DOT in Bitkub by THB fiat > transfer DOT to Binance ###
	DOT_FEE = 0.1
	dotAmountBitkub = fiatBahtAmount/dotPriceBitkub
	dotTotal2 = dotAmountBitkub - DOT_FEE

	print("DOTs amount (purchase USDT in Bitkub, then use the transferred USDT to purchase DOTs in Binance in BNB Spot: {}\
		DOTS amount (purchase DOTs in THB fiat from Bitkub, then transfer these DOTs to Binance: {})".format(dotTotal1, dotTotal2))



def dotUsdtBnb(fiatBahtAmount, usdtPriceBitkub, dotPriceBitkub, dotPriceBinance):
	#  INPUTS descriptions : 
	# fiatBahtAmount = THB you want to put to Bitkub
	# usdtPriceBitkub = current USDT price or the price you'd like to bid in Bitkub (example: THB 30.2)
	# dotPriceBitkub = current DOT price or the price you'd like to bid in Bitkub (example: THB 700)
	# dotPriceBinance = current DOT price or the price you'd like to bid in binance in USDT (example: USDT 25)

	# convert THB fiat to USDT in Bitkub > transfer USDT to Binance to purchase DOT in USDT
	USDT_FEE = 18
	usdtAmountBitkub = fiatBahtAmount/usdtPriceBitkub
	usdtAmountBitkubTransferred = usdtAmountBitkub-USDT_FEE
	dotTotal1 = usdtAmountBitkubTransferred/dotPriceBinance

	# direct purchase DOT in bitkub by THB fiat > transfer DOT to Binance
	DOT_FEE = 0.1
	dotAmountBitkub = fiatBahtAmount/dotPriceBitkub
	dotTotal2 = dotAmountBitkub - DOT_FEE

	print("DOTs amount (purchase USDT in Bitkub, then use the transferred USDT to purchase DOTs in Binance: {}\
		DOTS amount (purchase DOTs in THB fiat from Bitkub, then transfer these DOTs to Binance: {})".format(dotTotal1, dotTotal2))





