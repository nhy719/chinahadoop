"""
auther:gibbs
date:20190521
version:3.0
3.0 新增功能，程序可以一直运行，直到用户选择退出
"""

# 汇率：
RMB_VS_USD = 6.77

# 带单位的货币输入
currency_str_value = input("请输入货币金额（USD 或者 CNY），退出程序请输入Q：")

# 获取货币单位
unit = currency_str_value[-3:]
i = 0

while currency_str_value != 'Q':
    i += 1
    print("循环次数：", i)

    if unit == "CNY":     # 输入的是人民币
        # rmb_value = int(currency_str_value[:-3])
        rmb_value = eval(currency_str_value[:-3])
        print("美元金额是：" , rmb_value / RMB_VS_USD)

    elif unit == "USD":    # 输入的是美元
        usd_value = int(currency_str_value[:-3])
        print("人民币金额是：" , usd_value * RMB_VS_USD)
    else:
        print("暂不支持该币种")

    print('*' * 10)

    # 带单位的货币输入
    currency_str_value = input("请输入货币金额（USD 或者 CNY），退出程序请输入Q：")

print("程序已退出！")
