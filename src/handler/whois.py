import whois 
import json

def index():
    print("Contoh: example.com")
    domain = input("Masukkan domain: ")

    try:
        whois_info = whois.whois(domain)
        
        if whois_info:
            print(whois_info)
        else:
            print("Domain tidak ditemukan.")
    except Exception as e:
        print("Terjadi kesalahan:", e)

