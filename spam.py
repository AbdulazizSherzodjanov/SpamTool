import pyautogui
import time
xabar = input("Xabarni kiriting : ")
soni = int(input("Nechta jonatmoqchisiz ? : "))
boshlash = int(input("Nechchi sekunddan keyin boshlansin ? : "))
message = xabar


n = soni
time.sleep(boshlash)
print("Boshlandi")

count = 5

while (count !=5):
  time.sleep(1)

count-=1

print('')

for i in range(0,int(n)):
  pyautogui.typewrite(message+'\n')