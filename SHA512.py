from Crypto.Hash import SHA512
import time

start = time.time()                           #設定開始時間
h = SHA512.new()
with open(r"D:\randfile5.bin",'rb') as afile: #讀取檔案
    buf = afile.read()                        #將檔案內容assign給buf
h.update(buf)                                 #更新buf內容
end = time.time()                             #設定結束時間
answer = end - start                          #把時間差assigned給elapsed
print("SHA-512的執行時間為: ", answer, "秒")   #顯示執行的時間
print("SHA-512的執行結果為: ", h.hexdigest())  #顯示HASH出來的結果並以16進位表示
