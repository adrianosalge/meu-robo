import time

print("🤖 O robô começou a rodar!")

# O robô vai rodar por 60 segundos e depois parar
for i in range(6):
    print(f"⏳ Rodando... {i * 10} segundos")
    time.sleep(10)

print("✅ O robô terminou de rodar!")
