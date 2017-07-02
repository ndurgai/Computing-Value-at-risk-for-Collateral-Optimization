import readData
import parametricVar

x = readData.readQuandl(["CHRIS/ICE_B17.1", "CHRIS/ICE_B1.1"], 20)
y = readData.cleanData(x)

# varPanda = parametricVar.dailyMultiParametricVar(y, 99, 20)
# print(varPanda)

w = readData.portfolioWeights()
parametricVar.paraPortfolioVaR(y, w, 99, 1)
parametricVar.paraPortfolioVaR(y, w, 99, 2)