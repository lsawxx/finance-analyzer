import sys
from analyse import analyse_article


def main():
    print("=" * 50)
    print("  金融资讯分析师 ")
    print("=" * 50)
    print()

    # 方式1：命令行参数传入文件路径
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                article = f.read()
        except FileNotFoundError:
            print(f"错误：找不到文件 {file_path}")
            return
    # 方式2：交互式输入
    else:
        print("请粘贴金融资讯内容（输入完后按两次回车）：")
        lines = []
        while True:
            line = input()
            if line == "":
                break
            lines.append(line)
        article = "\n".join(lines)

    if not article.strip():
        print("错误：文章内容为空")
        return

    print("\n正在分析中...")
    result = analyse_article(article)

    print("\n" + "=" * 50)
    print("  分析结果")
    print("=" * 50)
    print(result)
    print("=" * 50)


if __name__ == "__main__":
    main()
