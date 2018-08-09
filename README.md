# hodo
將任何unicode文字轉換成以hodo表示，例如: \
"禾多"就會轉換成"hhhhhhhhooooooooooddddddddddddooooooooooooooo hhhhhhooooooooooddooooooooooo" \
至於hodo是怎麼表示unicode?如下說明: \
hodo表示0x0000 \
hhodo表示0x1000 \
hodddoo表示0x0021 \

Q:我該怎麼使用hodo? \
A:將hodo.py放到任一資料夾，在該資料夾下的python中使用from hodo import hodo \
在hodo物件中有encode用來編碼，decode用來解碼，例如: \
s = hodo.encode('禾多')
s = hodo.decode('hhhhhhhhooooooooooddddddddddddooooooooooooooo hhhhhhooooooooooddooooooooooo')
