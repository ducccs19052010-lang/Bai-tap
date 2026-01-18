import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Định nghĩa các phương trình vi phân
def f_a(y, x): return y - 2*x
def f_b(y, x): return x*y - x**2
def f_c(y, x): return y + x*y
def f_d(y, x): return x + y**2

# Thiết lập lưới điểm để vẽ mũi tên (Direction Field)
x = np.linspace(-2, 2, 20)
y = np.linspace(-2, 2, 20)
X, Y = np.meshgrid(x, y)

# Hàm vẽ chung
def plot_field(ax, f, title, point):
    # Tính độ dốc tại các điểm lưới
    U = 1
    V = f(Y, X)
    # Chuẩn hóa độ dài mũi tên cho đẹp
    N = np.sqrt(U**2 + V**2)
    U2, V2 = U/N, V/N
    ax.quiver(X, Y, U2, V2, angles='xy', scale_units='xy', scale=5, color='gray', alpha=0.5)
    
    # Vẽ đường cong nghiệm đi qua điểm cho trước
    x_sol = np.linspace(point[0]-1, point[0]+1, 100)
    # Giải phương trình vi phân số học
    try:
        y_sol = odeint(f, point[1], x_sol)
        ax.plot(x_sol, y_sol, 'r-', linewidth=2, label=f'Nghiệm qua {point}')
        ax.plot(point[0], point[1], 'bo') # Chấm điểm mốc
    except:
        pass
    
    ax.set_title(title)
    ax.grid(True)
    ax.set_ylim(-2, 2)
    ax.set_xlim(-2, 2)

# Tạo 4 đồ thị
fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# (a) y' = y - 2x
plot_field(axs[0, 0], f_a, "(a) y' = y - 2x", (1, 0))

# (b) y' = xy - x^2
plot_field(axs[0, 1], f_b, "(b) y' = xy - x^2", (0, 1))

# (c) y' = y + xy
plot_field(axs[1, 0], f_c, "(c) y' = y + xy", (0, 1))

# (d) y' = x + y^2
plot_field(axs[1, 1], f_d, "(d) y' = x + y^2", (0, 0))

plt.tight_layout()
plt.show()