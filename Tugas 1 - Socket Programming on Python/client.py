import socket

# Membuat objek socket client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Menentukan host dan port server
HOST = 'localhost'
PORT = 12345

# Menghubungkan ke server
client_socket.connect((HOST, PORT))

# Meminta input dari pengguna
pesan = input("Masukkan pesan: ")

# Mengirim pesan ke server
client_socket.sendall(pesan.encode())

# Menerima respons dari server
pesan_balasan = client_socket.recv(1024).decode()

# Menampilkan pesan balasan
print("Pesan balasan dari server:", pesan_balasan)

# Menutup koneksi dengan server
client_socket.close()
