import tkinter as tk
from tkinter import messagebox

def calculate_interest():
    try:
        principal = float(entry_principal.get())
        apy = float(entry_apy.get()) / 100  # 百分比转换为小数
        years = float(entry_years.get())

        # 年复利计算
        final_amount = principal * (1 + apy) ** years
        interest_earned = final_amount - principal

        result_label.config(
            text=f"利息：{interest_earned:.2f} USD\n最终余额：{final_amount:.2f} USD",
            fg="blue"
        )
    except ValueError:
        messagebox.showerror("输入错误", "请输入有效的数字，例如：10000、4.5、2。")

# 创建窗口
window = tk.Tk()
window.title("储蓄利息计算器")
window.geometry("300x250")
window.resizable(False, False)

# 本金输入
tk.Label(window, text="本金（USD）:").pack(pady=(10, 0))
entry_principal = tk.Entry(window)
entry_principal.pack()

# 年利率输入
tk.Label(window, text="年利率 APY（%）:").pack(pady=(10, 0))
entry_apy = tk.Entry(window)
entry_apy.pack()

# 存款年限输入
tk.Label(window, text="存款时间（Year）:").pack(pady=(10, 0))
entry_years = tk.Entry(window)
entry_years.pack()

# 计算按钮
tk.Button(window, text="计算", command=calculate_interest).pack(pady=15)

# 结果输出
result_label = tk.Label(window, text="", font=("Arial", 12))
result_label.pack()

# 运行 GUI
window.mainloop()