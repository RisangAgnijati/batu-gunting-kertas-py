import Data
import random

print('Memulai permainan batu gunting kertas !!')
player_name = input('Masukan namamu : ')

print('Pilih tangan (0: Batu, 1: Kertas, 2: Gunting)')
player_hand = int(input('Masukkan nomor (0-2): '))

if Data.valid(player_hand):
    computer_hand = random.randint(0,2)

    Data.print_hand(player_hand,player_name)
    Data.print_hand(computer_hand,'Komputer')

    result = Data.eksekusi(player_hand, computer_hand)
    print("Hasil: " + result)
else:
    print('Masukin angka yg bener dongg !!')