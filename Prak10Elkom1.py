mahasiswa=[]
def input_data():
   nama  = input("Masukkan Nama Mahasiswa: ")
   nilai1=int(input("Masukkan Nilai Praktikum 1: "))
   nilai2=int(input("Masukkan Nilai Praktikum 2: "))
   nilai3=int(input("Masukkan Nilai Praktikum 3: "))
   nilai4=int(input("Masukkan Nilai Praktikum 4: "))
   nilai5=int(input("Masukkan Nilai Praktikum 5: "))
   list=[nama,nilai1,nilai2,nilai3,nilai4,nilai5]
   mahasiswa.insert(len(mahasiswa),list)
   menu()
def view_data():
    print(" NAMA |","PRAK 1|","PRAK 2|","PRAK 3|","PRAK 4|","PRAK 5|")
    for i in mahasiswa:
        print(i[0],"     ",i[1],"     ",i[2],"     ",i[3],"     ",i[4],"     ",i[5])
    menu()
def rata_mahasiswa():
    for i in range(len(mahasiswa)):
        total=0
        for j in range (1,len(mahasiswa[i])):
            total+=mahasiswa[i][j]
        print(mahasiswa[i][0],"=",total/len(mahasiswa[i]))
    menu()
def rata_prak():
    totalprak1=0
    totalprak2=0
    totalprak3=0
    totalprak4=0
    totalprak5=0
    for i in range(len(mahasiswa)):
        totalprak1+=mahasiswa[i][1]
        totalprak2+=mahasiswa[i][2]
        totalprak3+=mahasiswa[i][3]
        totalprak4+=mahasiswa[i][4]
        totalprak5+=mahasiswa[i][5]
    totalprak1=totalprak1/len(mahasiswa)
    totalprak2=totalprak2/len(mahasiswa)
    totalprak3=totalprak3/len(mahasiswa)
    totalprak4=totalprak4/len(mahasiswa)
    totalprak5=totalprak5/len(mahasiswa)
    print("Rata-Rata Praktikum 1= ",totalprak1)
    print("Rata-Rata Praktikum 2= ",totalprak2)
    print("Rata-Rata Praktikum 3= ",totalprak3)
    print("Rata-Rata Praktikum 4= ",totalprak4)
    print("Rata-Rata Praktikum 5= ",totalprak5)
    menu()
def rata_prakmaha():
    listrata2mahasiswa=[]
    total=0
    for i in range(len(mahasiswa)):
        total=0
        for j in range (1,len(mahasiswa[i])):
            total+=mahasiswa[i][j]
        listrata2mahasiswa.insert(len(listrata2mahasiswa),total/5)
    total=0
    for i in listrata2mahasiswa:
        total+=i
    total=total/len(listrata2mahasiswa)
    print(total)
    menu()
def update_nilai():
    update=input("Nama Yang Dicari :")
    nilai=int(input("Ingin Update nilai Praktikum ke-: "))
    nilai_baru=int(input("Nilai Baru: "))
    for i in mahasiswa:
        if i [0]==update:
            i[nilai]=nilai_baru
    menu()
def menu():
    print("Program List")
    print("1.INPUT DATA")
    print("2.VIEW DATA")
    print("3.HITUNG NILAI RATA-RATA PRAKTIKUM TIAP MAHASISWA")
    print("4.HITUNG NILAI RATA-RATA TIAP PRAKTIKUM")
    print("5.MENCARI NILAI RATA-RATA PRAKTIKUM MAHASISWA")
    print("6.UPDATE NILAI PRAKTIKUM MAHASISWA")
    print("7.EXIT")
    pilih=int(input("Pilih Menu Yang Tersedia:"))
    if pilih==1:
        input_data()
    elif pilih==2:
        view_data()
    elif pilih==3:
        rata_mahasiswa()
    elif pilih==4:
        rata_prak()
    elif pilih==5:
        rata_prakmaha()
    elif pilih==6:
        update_nilai()
    else:
        print("Terima Kasih :)")
        exit()
menu()