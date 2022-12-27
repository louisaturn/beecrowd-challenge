-- Solution of: https://www.beecrowd.com.br/judge/problems/view/1010 Language: Lua

function calculate(unit, price)
    return unit * price
end

function main()
    code1, unit1, price1 = io.read("*n", "*n", "*n")
    code2, unit2, price2 = io.read("*n", "*n", "*n")
    return calculate(unit1, price1) + calculate(unit2, price2)
end

print("VALOR A PAGAR: R$ " .. string.format("%.2f", main()))
