"""
auther:gibbs
date:20190509
version:2.0
2.0 新增功能，根据输入判断是人民币还是美元，再进行相应转换计算
"""

# 汇率：
RMB_VS_USD = 6.77

currency_str_value = input("请输入货币金额（USD 或者 CNY）：")

# 获取货币单位
unit = currency_str_value[-3:]

if unit == "CNY":     # 输入的是人民币
    # rmb_value = int(currency_str_value[:-3])
    rmb_value = eval(currency_str_value[:-3])
    print("美元金额是：" , rmb_value / RMB_VS_USD)

elif unit == "USD":    # 输入的是美元
    usd_value = int(currency_str_value[:-3])
    print("人民币金额是：" , usd_value * RMB_VS_USD)
else:
    print("暂不支持该币种")
