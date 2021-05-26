def FixedRateDepreciationTable(salvage, cost, life):
    rate = 1 - ((salvage / cost) ** (1 / life))

    for year in range(1, life + 1):
        dv = cost * rate
        cost -= dv
        yield year, round(dv, 2), cost


if __name__ == '__main__':
    print("Year\tDepreciation\tBook Value at the year-end")
    for year, depreciation, new_value in FixedRateDepreciationTable(1000, 100000, 10):
        print("{0:4}\t{1:>18}\t{2:26}".format(year, depreciation, new_value))