import pandas as pd
import matplotlib.pyplot as plt

# 读取CSV文件
csv_file = "Train_loss.csv"
data = pd.read_csv(csv_file)

# 确保数据包含所需列
if 'epoch' not in data.columns or 'training_loss' not in data.columns:
    raise ValueError("CSV文件必须包含 'epoch' 和 'training_loss' 两列")

# 提取 epoch 和 training_loss
epochs = data['epoch']
training_loss = data['training_loss']

# 绘制曲线
plt.figure(figsize=(8, 6))
plt.plot(epochs, training_loss, label="Training Loss", color='b', marker='o')

# 添加标题和标签
plt.title("Model Convergence Speed", fontsize=16)
plt.xlabel("Epoch", fontsize=14)
plt.ylabel("Training Loss", fontsize=14)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(fontsize=12)

# 显示图形
plt.tight_layout()
plt.show()
