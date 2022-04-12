# Enflasyon Hesaplayıcı
import time
print('--------------------')
print('Enflasyon Hesaplayıcı')
print('--------------------')

# Neyi Hesaplayacağızı Seçin
select_type = input('Hesapla (B/F/E): ').upper()

# Birikmiş Tutarı Hesapla (n)
if select_type == 'B':
    # Kullanıcıdan Yılları alın ve Farkı Hesaplayın (n)
    yil_1 = float(input('İlk Yıl: '))
    yil_2 = float(input('Son Yıl: '))
    yil_fark = float(yil_2 - yil_1)
    # Göster (n)
    print(f"Periyod (n): {yil_fark} yıl")
    print('--------------------')

    # İlk Yıl Fiyatını Al ve Göster (F)
    p_value = float(input(f"Fiyat - {yil_1}: "))
    print(f"İlk fiyat (F) ({yil_1}): R{p_value}")
    print('--------------------')

    # 1. Yıl ve 2. Yıl Arasındaki Ortalama Enflasyonu Alın ve Görüntüleyin (E)
    ort_enflasyon = float(input('Ortalama Enflasyon %: '))
    print(f"Ortalama Enflasyon: ({yil_1} - {yil_2}): {ort_enflasyon} %")
    print('--------------------')

    # Birikmiş Tutarı Hesapla (2. Yıl Fiyatı) (B)
    # Bileşik Formül B = F(1 + E)**n
    a = float(p_value * (1 + ort_enflasyon / 100)**yil_fark)
    print(f"Fiyatı (B) ({yil_2}): R{'%.2f' % a}")
    print('--------------------')

# Fiyat Hesapla
elif select_type == 'F':
    # Kullanıcıdan Yılları Alın ve Farkı Hesaplayın (n)
    yil_1 = float(input('İlk Yıl: '))
    yil_2 = float(input('Son Yıl: '))
    yil_fark = float(yil_2 - yil_1)
    # Göster (n)
    print(f"Periyod (n): {yil_fark} yıl")
    print('--------------------')

    # 1. Yıl ve 2. Yıl Arasındaki Ortalama Enflasyonu Alın ve Görüntüleyin (E)
    ort_enflasyon = float(input('Ortalama Enflasyon: '))
    print(f"Ortalama Enflasyon (%) ({yil_1} - {yil_2}): {ort_enflasyon}%")
    print('--------------------')

    # Birikmiş Tutarı Alın ve Gösterin (B)
    a = float(input('Birikmiş Tutar: '))
    print(f" Son Yıl (B) ({yil_2}): R{a}")
    print('--------------------')

    # Hesaplayın (F) ve Gösterin
    p_value = float(a / (1 + ort_enflasyon / 100) ** yil_fark)
    print(f"Fiyat (F): {yil_1} Yılında Fiyat R{'%.2f' %p_value} ")

# Ortalama Enflasyonu Hesaplayın
elif select_type == 'E':
    # Yılları Alın ve Farkı Hesaplayın (n)
    yil_1 = float(input('İlk Yıl: '))
    yil_2 = float(input('Son Yıl: '))
    yil_fark = float(yil_2 - yil_1)
    # Göster (n)
    print(f"Periyod (n): {yil_fark} yıl")
    print('--------------------')

    # İlk Yıl Fiyatını Alın ve Gösterin (F)
    p_value = float(input(f"Fiyat (İlk Yıl) - "))
    print(f"Price ({yil_1}): R{p_value}")
    print('--------------------')

    # Birikmiş Tutarı Alın Ve Gösterin (2.Yıl Fiyatı) (B)
    a = float(input(f'Fiyat (Son Yıl): '))
    print(f"Birikmiş Tutar ({yil_2}): R{a}")
    print('--------------------')

    # Ortalama Enflasyonu Hesaplayın ve Gösterin (E)
    ort_enflasyon = ((a / p_value) ** (1/yil_fark) - 1) * 100
    print(f"Ortlalama Enflasyon: ({yil_1} - {yil_2}): {'%.2f' % ort_enflasyon} %")

# Eğer B/F/E Girişlerinden Başka Bir Giriş Yapılırsa
else:
    print('Lütfen Yalnızca (B/F/E) Girin!')

time.sleep(10)
