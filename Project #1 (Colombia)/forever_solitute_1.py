import re
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import matplotlib

# ===== 设置中文字体 =====
matplotlib.rcParams['font.sans-serif'] = ['STHeiti']  # Mac
matplotlib.rcParams['axes.unicode_minus'] = False

# ===== 读入文本 =====
with open("/Users/rundonghe/Downloads/百年孤独.txt", "r", encoding="utf-8") as f:
    text = f.read()

# ===== 人名字典（可扩展） =====
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

# ===== 获取出现位置 =====
name_positions = {}
for name, aliases in name_dict.items():
    positions = []
    for alias in aliases:
        for match in re.finditer(alias, text):
            positions.append(match.start() / len(text))  # 归一化
    name_positions[name] = sorted(positions)

# ===== 构造热力图矩阵 =====
n_bins = 100  # 细分100格（每1%进度）
heatmap_data = np.zeros((len(name_dict), n_bins))
bins = np.linspace(0, 1, n_bins + 1)

for i, (name, positions) in enumerate(name_positions.items()):
    counts, _ = np.histogram(positions, bins=bins)
    heatmap_data[i, :] = counts

# ===== 绘制热力图 =====
plt.figure(figsize=(14, 5))
sns.heatmap(
    heatmap_data, 
    cmap="YlOrRd",         # 颜色对比更强
    cbar=True, 
    yticklabels=list(name_dict.keys()), 
    xticklabels=10      # 每隔10%显示一个刻度
)

plt.xlabel("小说进度（%）")
plt.ylabel("人物")
plt.title("《百年孤独》人物出现热力图")

# 修改横轴为百分比
xticks = np.linspace(0, n_bins, 11)  # 0%, 10%, ..., 100%
plt.xticks(xticks, [f"{int(x)}%" for x in np.linspace(0, 100, 11)])

plt.tight_layout()
plt.show()
