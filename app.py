import streamlit as st
from analyse import analyse_article

st.set_page_config(
    page_title="金融资讯深度分析助手",
    page_icon="📊",
    layout="centered"
)

# 侧边栏
with st.sidebar:
    st.header("📊 关于")
    st.markdown("""
    基于大模型的金融资讯结构化分析工具。
    
    **功能：**
    - 自动识别资讯类型
    - 自适应分析框架
    - 输出专业分析报告
    
    **模型：** DeepSeek-V3
    """)
    st.divider()
    st.caption("分析结果仅供参考，不构成投资建议")

# 主界面
st.title("📊 金融资讯深度分析助手")
st.caption("粘贴金融资讯，AI自动输出结构化分析报告")

st.divider()

# 输入区域
article = st.text_area(
    "📝 粘贴资讯内容",
    height=200,
    placeholder="在这里粘贴央行公告、公司财报、行业新闻、市场动态..."
)

col1, col2 = st.columns([1, 5])
with col1:
    analyze_btn = st.button("开始分析", type="primary", use_container_width=True)
with col2:
    if st.button("清空", use_container_width=True):
        st.rerun()

st.divider()

# 分析结果
if analyze_btn:
    if article.strip():
        with st.spinner("AI正在深度分析中，请稍候..."):
            result = analyse_article(article)
        
        if result.startswith("错误"):
            st.error(result)
        else:
            st.success("分析完成！")
            st.markdown(result)
            
            # 复制按钮
            st.download_button(
                label="📥 下载分析结果",
                data=result,
                file_name="分析结果.txt",
                mime="text/plain"
            )
    else:
        st.warning("请先粘贴资讯内容")

# 底部
st.divider()
st.caption("💡 提示：资讯内容越详细，分析结果越准确。支持宏观政策、行业动态、公司公告、市场事件等各类金融资讯。")
