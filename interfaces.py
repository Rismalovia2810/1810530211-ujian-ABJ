print("UTS APLIKASI BERBASIS JARINGAN - 1810530211")
print('='*40)

Data_Tunk_Interfaces=[]
file=open("db-interfaces.txt","a")
while True :
    Answer = input("Input Data Trunk Interface baru (yes/no)? : ")
    if Answer == "yes" :
        print('-'*34)
        HostnameSwitch = input("Masukkan hostname switch : ")
        HostnameInterface = input("Masukkan nama interface : ")
        print('-'*34)
        file.write('Hostname Switch : '+HostnameSwitch+', ' 'Hostname Interface : '+HostnameInterface+'\n')
    else :
        print('='*34)
        print('-'*13 +'  DONE  '+'-'*13)
        print('='*34)
        file=open('db-interfaces.txt','r')
        for item in file:
            item=item.strip()
            print(item)
        file.close()
        break
print('='*34)
file.close()