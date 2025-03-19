


def number_to_words(num):
    below_20 = ['Zero', 'One','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen']
    tens = ['Twenty','Thirty','Forty','Fifty','Sixty','Seventy','Eighty','ninety']
    above_1000 = {100: 'Hundred', 1000: 'Thousand', 1000000: 'Million', 1000000000: 'Billion'}
    def helper(n):
        if n < 20:
            return below_20[n]
        elif n < 100:
            return tens[n // 10 - 2] + ('' if n % 10 == 0 else ' ' + below_20[n % 10])
        else:
            for key in sorted(above_1000.keys(), reverse=True):
                if n >= key:
                   return helper(n // key) + ' ' + above_1000[key] + ('' if n % key == 0 else ' ' + helper(n % key))

    return helper (num)

print(number_to_words(12))   
print(number_to_words(786))       


