import tkinter as tk
from tkinter import messagebox, ttk


users = []
donations = []

def add_user():
    name = entry_name.get()
    email = entry_email.get()
    if name and email:
        users.append({'name': name, 'email': email})
        combo_user['values'] = [user['name'] for user in users]
        entry_name.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        messagebox.showinfo("Sucesso", "Usuário adicionado com sucesso!")
    else:
        messagebox.showwarning("Aviso", "Preencha todos os campos!")

def add_donation():
    user_name = combo_user.get()
    amount = entry_amount.get()
    donation_type = combo_type.get()

    if user_name and amount and donation_type:
        for user in users:
            if user['name'] == user_name:
                donations.append({
                    'user': user_name,
                    'amount': float(amount),
                    'type': donation_type
                })
                entry_amount.delete(0, tk.END)
                combo_user.set('')
                combo_type.set('')
                messagebox.showinfo("Sucesso", "Doação registrada com sucesso!")
                return
    else:
        messagebox.showwarning("Aviso", "Preencha todos os campos!")

def show_stats():
    stats_window = tk.Toplevel(root)
    stats_window.title("Estatísticas de Doações")

    stats = {}
    for donation in donations:
        stats[donation['type']] = stats.get(donation['type'], 0) + donation['amount']

    tk.Label(stats_window, text="Estatísticas de Doações", font=("Arial", 14)).pack(pady=10)

    for donation_type, total in stats.items():
        tk.Label(stats_window, text=f"{donation_type}: R$ {total:.2f}", font=("Arial", 12)).pack()

    tk.Button(stats_window, text="Fechar", command=stats_window.destroy).pack(pady=10)

root = tk.Tk()
root.title("Sistema de Doações")
root.geometry("400x500")


frame_users = tk.Frame(root, pady=10)
frame_users.pack(fill=tk.X)

tk.Label(frame_users, text="Cadastro de Usuários", font=("Arial", 14)).pack()

tk.Label(frame_users, text="Nome:").pack()
entry_name = tk.Entry(frame_users)
entry_name.pack()

tk.Label(frame_users, text="Email:").pack()
entry_email = tk.Entry(frame_users)
entry_email.pack()

tk.Button(frame_users, text="Adicionar Usuário", command=add_user).pack(pady=5)

frame_donations = tk.Frame(root, pady=10)
frame_donations.pack(fill=tk.X)

tk.Label(frame_donations, text="Registrar Doação", font=("Arial", 14)).pack()

tk.Label(frame_donations, text="Usuário:").pack()
combo_user = ttk.Combobox(frame_donations, state="readonly")
combo_user.pack()

tk.Label(frame_donations, text="Valor:").pack()
entry_amount = tk.Entry(frame_donations)
entry_amount.pack()

tk.Label(frame_donations, text="Tipo de Doação:").pack()
combo_type = ttk.Combobox(frame_donations, state="readonly")
combo_type['values'] = ['Dinheiro', 'Alimentos', 'Roupas']
combo_type.pack()

tk.Button(frame_donations, text="Registrar Doação", command=add_donation).pack(pady=5)

tk.Button(root, text="Ver Estatísticas", command=show_stats, font=("Arial", 12)).pack(pady=10)


root.mainloop()
