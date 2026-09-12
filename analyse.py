import requests
from config import API_KEY, API_BASE, MODEL, TEMPERATURE, MAX_TOKENS


def analyse_article(article_text):
    """输入金融文章，返回结构化分析结果"""
    url = f"{API_BASE}/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    # Prompt：角色设定 + 输出格式 + 文章内容
    system_prompt = """你是一位拥有10年经验的资深金融分析师。分析前先判断资讯类型，采用对应框架：
宏观政策类（央行/财政部/监管）：重点分析政策传导、流动性、行业轮动
行业动态类（行业数据/技术突破/格局变化）：重点分析竞争格局、供需变化、受益标的
公司微观类（公告/业绩/并购/管理层变动）：重点分析基本面、财务影响、估值、同业对比
市场事件类（暴跌/暴涨/资金流向）：重点分析诱因、情绪、持续性
所有分析必须：区分事实与观点、有数据意识、同时提示机会与风险、不做单边推荐。"""
    user_prompt = f"""请深度分析以下金融资讯，严格按照以下结构输出：

【资讯类型】判断属于：宏观政策 / 行业动态 / 公司微观 / 市场事件

【一句话总结】用一句话概括最核心的信息

【核心事实】提取3-5个关键事实（时间、主体、数据、动作）

【深度分析】根据资讯类型选择重点：
- 如为宏观：分析政策传导、流动性影响、行业轮动方向
- 如为行业：分析供需变化、竞争格局、受益/受损环节
- 如为公司：分析对营收/利润/估值的影响，与同业对比
- 如为市场：分析诱因、资金行为、情绪持续性

【投资启示】
- 机会：1-2个可能受益的方向
- 风险：1-2个需要警惕的点
- 验证指标：后续跟踪什么数据

资讯内容：
{article_text}"""

    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        "temperature": TEMPERATURE,
        "max_tokens": MAX_TOKENS
    }

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=30)
        response.raise_for_status()  # HTTP错误时抛出异常
        data = response.json()
        return data["choices"][0]["message"]["content"]
    except requests.exceptions.Timeout:
        return "错误：请求超时，请检查网络连接"
    except requests.exceptions.HTTPError as e:
        return f"错误：API请求失败 - {e.response.text}"
    except Exception as e:
        return f"错误：{str(e)}"