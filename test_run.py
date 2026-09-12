from analyse import analyse_article

# 测试文章直接写在这里
article = """中国人民银行决定下调金融机构存款准备金率0.5个百分点，预计释放长期资金约1万亿元，旨在保持银行体系流动性合理充裕，支持实体经济发展。"""

print("正在分析中...\n")
result = analyse_article(article)
print(result)