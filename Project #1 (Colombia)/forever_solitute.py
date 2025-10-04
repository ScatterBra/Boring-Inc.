import re
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# 读入文本
with open("/Users/rundonghe/Downloads/百年孤独.txt", "r", encoding="utf-8") as f:
    text = f.read()

# 人名字典（简化示例，可以加完整版本）
name_dict = {
    "何塞·阿尔卡蒂奥·布恩迪亚": ["何塞·阿尔卡蒂奥·布恩迪亚", "何塞·阿尔卡蒂奥", "布恩迪亚老爹", "布恩迪亚族长"],
    "乌尔苏拉": ["乌尔苏拉", "乌尔苏拉·伊瓜兰"],
    "阿玛兰塔": ["阿玛兰塔"],
    "奥雷里亚诺·布恩迪亚": ["奥雷里亚诺·布恩迪亚", "奥雷里亚诺", "奥雷里亚诺上校", "上校"],
    "何塞·阿尔卡蒂奥（长子）": ["何塞·阿尔卡蒂奥（长子）", "何塞·阿尔卡蒂奥二世", "阿尔卡蒂奥"],
    "雷梅黛丝（丽美黛丝）": ["雷梅黛丝", "丽美黛丝"],
    "奥雷里亚诺二世": ["奥雷里亚诺二世", "奥雷里亚诺"],
    "何塞·阿尔卡蒂奥二世": ["何塞·阿尔卡蒂奥二世", "阿尔卡蒂奥"],
    "美人雷梅黛丝": ["美人雷梅黛丝", "雷梅黛丝美人"],
    "佩特拉·科特斯": ["佩特拉·科特斯", "佩特拉"],
    "梅尔基亚德斯": ["梅尔基亚德斯", "吉普赛人"],
    "费尔南达": ["费尔南达"],
    "阿玛兰塔·乌尔苏拉": ["阿玛兰塔·乌尔苏拉"],
    "奥雷里亚诺·巴比伦尼亚": ["奥雷里亚诺·巴比伦尼亚", "巴比伦尼亚"],
}
plt.rcParams['font.sans-serif'] = ['STHeiti']
plt.rcParams['axes.unicode_minus'] = False

# 获取每个人物在文本中的位置索引（归一化到 0-100%）
name_positions = {}
for name, aliases in name_dict.items():
    positions = []
    for alias in aliases:
        for match in re.finditer(alias, text):
            positions.append(match.start() / len(text))  # 归一化
    name_positions[name] = positions

# 绘制KDE
plt.figure(figsize=(20, 6))
for name, positions in name_positions.items():
    if len(positions) > 3:  # 至少3个点才画KDE
        sns.kdeplot(positions, bw_adjust=0.5, label=name, fill=False)

plt.xlabel("小说进度（0 = 开头, 1 = 结尾）")
plt.ylabel("出现密度（KDE）")
plt.title("《百年孤独》人物出场频率 KDE 曲线")
plt.legend()
plt.show()
