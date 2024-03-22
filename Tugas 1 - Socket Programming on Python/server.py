import socket

# Membuat objek socket server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Menentukan host dan port
HOST = 'localhost'
PORT = 12345

# Mengikat socket ke alamat dan port tertentu
server_socket.bind((HOST, PORT))

# Mendengarkan koneksi
server_socket.listen(1)

print("Waiting for connection...")

# Menerima koneksi dari client
client_socket, client_address = server_socket.accept()

# Menerima pesan dari client
pesan = client_socket.recv(1024).decode()

# Menghitung jumlah karakter pesan
jumlah_karakter = len(pesan)

# Membuat pesan balasan
pesan_balasan = f"Jumlah karakter pesan: {jumlah_karakter}"

# Mengirim pesan balasan ke client
client_socket.sendall(pesan_balasan.encode())

# Menutup koneksi dengan client
client_socket.close()

# Menutup socket server
server_socket.close()