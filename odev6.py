import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time


np.random.seed(int(time.time()))
x_range = 1000
y_range = 1000
n_points = 500


x = np.random.randint(0, x_range, n_points)
y = np.random.randint(0, y_range, n_points)


df = pd.DataFrame({
    'X Koordinatları': x,
    'Y Koordinatları': y
})


excel_path = 'C:\\Users\\Osman Yusuf Kurt\\odev6py\\koordinatlar.xlsx'
df.to_excel(excel_path, index=False)


color_map = {
    'b': 'Mavi',
    'g': 'Yeşil',
    'r': 'Kırmızı',
    'c': 'Cyan',
    'm': 'Mor',
    'y': 'Sarı',
    'k': 'Siyah',
    'orange': 'Turuncu',
    'purple': 'Eflatun',
    'brown': 'Kahverengi'
}
colors = list(color_map.keys())
groups = np.random.choice(colors, n_points)


plt.figure(figsize=(10, 8))
for color in set(groups):
    indices = groups == color
    plt.scatter(x[indices], y[indices], c=color, label=color_map[color])

plt.title('Rastgele Koordinatlar ile Nokta Dağılımı')
plt.xlabel('X Koordinatları')
plt.ylabel('Y Koordinatları')
plt.grid(True)
plt.legend(title='Renk Grupları', loc='lower left')
plt.axis([0, x_range, 0, y_range])

plot_path = 'C:\\Users\\Osman Yusuf Kurt\\odev6py\\koordinatlar_plot.png'
plt.savefig(plot_path)
plt.show()
