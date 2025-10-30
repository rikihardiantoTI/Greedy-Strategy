def find_coin_combination(amount, coins):
    """
    Menghitung kombinasi koin dan jumlah total koin
    menggunakan algoritma Greedy.
    """
     
    coins.sort(reverse=True)
    
    combination = {}
    total_coins = 0
    
    for coin in coins:
        if amount >= coin:
     
            count = amount // coin
            
          
            combination[coin] = count
            
             
            total_coins += count
            
           
            amount -= count * coin
            
    
    print("\n--- Hasil ---")
    print("Kombinasi Koin yang Digunakan:")
    for coin, count in combination.items():
        print(f"  {count} koin Rp{coin}")
        
     
    print(f"\nJumlah Total Koin: {total_coins} koin")
    
    if amount > 0:
        print(f"Sisa uang tidak bisa ditukar: Rp{amount}")

 
if __name__ == "__main__":
    try:
        
        amount_input = int(input("Masukkan jumlah uang (amount): "))
        
        
        coins_input_str = input("Masukkan daftar nilai koin (pisahkan dengan spasi, misal: 1000 500 100): ")
        
         
        coin_denominations = [int(c) for c in coins_input_str.split()]
        
        find_coin_combination(amount_input, coin_denominations)

    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")
    except Exception as e:
        print(f"Terjadi error: {e}")