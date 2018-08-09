#將檔案內文轉換成hodo字串或轉回unicode
#
#轉換成hodo字串(轉換的字串會放在被轉換的文件同一個資料夾中副檔名為.hd的檔案)
#python test2.py e C:\hodo.txt
#轉回unicode字串
#python test2.py d C:\hodo.hd > hodo2.txt
import sys
import os
from hodo import hodo

if sys.argv[1] == 'e':
    path, filename = os.path.split(sys.argv[2])
    filename, _ = os.path.splitext(filename)
    file_line = open(sys.argv[2],'r')
    script = open('%s\\%s.hd'%(path,filename),'w')
    for Str in file_line.read():
        Str = hodo.encode(Str)
        script.write(Str+' ')
    file_line.close()
    script.close()
elif sys.argv[1] == 'd':
    script = open(sys.argv[2],'r')
    for Str in script.readlines():
        print(hodo.decode(Str))
    script.close()