print('pilih unit:')
units = ['pedang','tombak', 'pemanah', 'kuda', 'pengepung' ]
print(f'1   :  {units[0]}')
print(f'2   :  {units[1]}')
print(f'3   :  {units[2]}')
print(f'4   :  {units[3]}')
print(f'5   :  {units[4]}')

pilih_unit = input('masukan angka pilihan: ')


if pilih_unit == '1':
    print(' masukan jumlah pedang dalam M: ')
    pedang = int( input() )
    if pedang >= 1 :
        makanan = pedang * 590
        besi = pedang * 1006
        batu= pedang * 0
        kayu = pedang * 160
        perak = pedang * 45
        kekuatan = pedang * 25
        skor = pedang * 5 
        print(f'makanan          : {makanan}M')
        print(f'kayu             : {kayu}M')
        print(f'batu             : {batu}M')
        print(f'besi             : {besi}M')
        print(f'perak            : {perak}M')
        print(f'kekuatan         : {kekuatan}M')
        print(f'skor ajang       : {skor}M')
elif pilih_unit == '2':
    print(' masukan jumlah tombak dalam M: ')
    unit = int( input() )
    makanan = unit * 615
    besi = unit * 0
    batu= unit * 175
    kayu = unit * 1165
    perak = unit * 60
    kekuatan = unit* 25
    skor = unit * 5 
    print(f'makanan          : {makanan}M')
    print(f'kayu             : {kayu}M')
    print(f'batu             : {batu}M')
    print(f'besi             : {besi}M')
    print(f'perak            : {perak}M')
    print(f'kekuatan         : {kekuatan}M')
    print(f'skor ajang       : {skor}M')
elif pilih_unit == '3':
    print(' masukan jumlah pemanah dalam M: ')
    unit = int( input() )
    makanan = unit * 220
    besi = unit * 225
    batu= unit * 135
    kayu = unit * 1115
    perak = unit * 30
    kekuatan = unit* 45
    skor = unit * 5 
    print(f'makanan          : {makanan}M')
    print(f'kayu             : {kayu}M')
    print(f'batu             : {batu}M')
    print(f'besi             : {besi}M')
    print(f'perak            : {perak}M')
    print(f'kekuatan         : {kekuatan}M')
    print(f'skor ajang       : {skor}M')
elif pilih_unit == '4':
    print('masukan jumlah kuda dalam M: ')
    kuda = int( input() )
    makanan = kuda * 1300
    besi = kuda * 151
    batu= kuda * 594
    kayu = kuda * 0
    perak = kuda * 60
    kekuatan = kuda * 25
    skor = kuda * 5 
    print(f'makanan          : {makanan}M')
    print(f'kayu             : {kayu}M')
    print(f'batu             : {batu}M')
    print(f'besi             : {besi}M')
    print(f'perak            : {perak}M')
    print(f'kekuatan         : {kekuatan}M')
    print(f'skor ajang       : {skor}M')
elif pilih_unit == '5':
    print(' masukan jumlah pengepung dalam M: ')
    unit = int( input() )
    makanan = unit * 170
    besi = unit * 45
    batu= unit * 1290
    kayu = unit * 480
    perak = unit * 50
    kekuatan = unit* 55
    skor = unit * 5 
    print(f'makanan          : {makanan}M')
    print(f'kayu             : {kayu}M')
    print(f'batu             : {batu}M')
    print(f'besi             : {besi}M')
    print(f'perak            : {perak}M')
    print(f'kekuatan         : {kekuatan}M')
    print(f'skor ajang       : {skor}M')
else:
    print('goblok')