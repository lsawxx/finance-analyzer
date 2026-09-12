import os

# API Key从环境变量读取，部署时在Streamlit Secrets里设置
# 本地开发时可以直接在这里填，但不要把真实Key提交到GitHub
API_KEY = os.environ.get("SILICONFLOW_API_KEY", "sk-kskekptzyellbwgpezxynprgrvigxwlmvifckzgdqcqhnqbo")
API_BASE = "https://api.siliconflow.cn/v1"
MODEL = "deepseek-ai/DeepSeek-V3"
TEMPERATURE = 0.3
MAX_TOKENS = 1000
