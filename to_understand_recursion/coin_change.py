

def recMC(coinValueList, change):
    minCoins = change
    if change in coinValueList:
        return 1
    else:
        for i in [c for c in coinValueList if c <= change]:
            numCoins = 1 + recMC(coinValueList, change-i)
            if numCoins < minCoins:
                minCoins = numCoins
    return minCoins

def recDC(coinValueList, change, kownResults):
    minCoins = change
    if change in coinValueList:
        kownResults[change] = 1
        return 1
    elif kownResults.get(change, 0) > 0:
        return kownResults[change]
    else:
        for i in [c for c in coinValueList if c <= change]:
            numCoins = 1 + recDC(coinValueList, change-i, kownResults)
            if numCoins < minCoins:
                minCoins = numCoins
                kownResults[change] = minCoins
    return minCoins


def dpMakeChange(coinValueList, change, minCoins):
    for cents in range(change+1):
        coinCount = cents
        for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents-j] + 1 < coinCount:
                coinCount = minCoins[cents-j] + 1
        minCoins[cents] = coinCount
    return minCoins[cents]

def dpMakeChangeV2(coinValueList, change, minCoins, coinsUsed):
    for cents in range(change+1):
        coinCount = cents
        newCoin = 1
        for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents-j] + 1 < coinCount:
                coinCount = minCoins[cents-j] + 1
                newCoin = j
        minCoins[cents] = coinCount
        coinsUsed[cents] = newCoin
    return minCoins[change]

def printCoins(coinUsed, change):
    coin = change
    while coin > 0:
        thisCoin = coinUsed[coin]
        print(thisCoin)
        coin = coin - thisCoin

# res = recDC([1, 5, 10, 25], 63, {})
# res = recMC([1, 5, 10, 25], 63)
# res = dpMakeChange([1, 5, 10, 25], 63, {})

c1 = [1, 5, 10, 25]
coinsUsed = [0] * 64
coinsCount = [0] * 64
res = dpMakeChangeV2(c1, 63, coinsCount, coinsUsed)
print(res)
printCoins(coinsUsed, 63)