import paramiko
import socket

def cdKomutu(komut, suankiDizin):
    if komut.startswith("cd "):
        yeniDizin = komut[3:].strip()
        if yeniDizin == "..":
            suankiDizin = '/'.join(suankiDizin.split('/')[:-1]) or '/' # / ile böler ve son kısmı çıkararak bir üst dizini belirler.
            print("Şuanki dizin: ", suankiDizin)
        
        elif yeniDizin == ".":
            print("Komut bulunamadı")
            return suankiDizin
        
        else:
            yeniDizinPath = f"{suankiDizin}/{yeniDizin}".replace("//","/") #/home/msfadmin/vulnerable
            # Dizin varmı yokmu kontrol et
            stdin, stdout, stderr = ssh.exec_command("ls -ld {}".format(yeniDizinPath))
            stdOutput = stdout.read().decode()
            errorOutput = stderr.read().decode()

            if "No such file or directory" in  errorOutput:
                print("Hata: Böyle bir dizin mevcut değil")
                return suankiDizin  # Böylelikle hatalı dizine gitmemiş oluyor
            
            elif not stdOutput.startswith("d"): # dizinler d ile başladığı için eğer d yokda dedik 
                print("Hata: Belirtilen yol bir dizin değil")
                return suankiDizin    

            else:
                suankiDizin = yeniDizinPath
                stdin, stdout, stderr = ssh.exec_command(f"cd {suankiDizin} && pwd")
                stdOutput = stdout.read().decode().strip()
                errorOutput = stderr.read().decode().strip()

            if errorOutput:
                print(f"Hata: {errorOutput}")

            else:
                print("Şuanki dizin: {}".format(stdOutput))
    else:
        cdKomutu = f"cd {suankiDizin} && {komut}"
        stdin, stdout, stderr = ssh.exec_command(cdKomutu)
        sdtOutput = stdout.read().decode().strip()
        errorOutput = stderr.read().decode().strip()

        if errorOutput:
            if "command not found" in errorOutput:
                print("Hata: Komut bulunamadı")

            elif "Permission denied" in errorOutput:
                print("Hata: Yetki hatası")
                return suankiDizin

            else:
                print(f"Hata: {errorOutput}")

        else:
            print("<< ", sdtOutput)
    return suankiDizin

def pwdOgren(ssh):
    stdin, stdout, stderr = ssh.exec_command("pwd")
    stdOut = stdout.read().decode().strip()
    return stdOut

try:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    ip = input("Ip adresi giriniz: ")
    username = input("Username giriniz: ")
    password = input("Password giriniz: ")

    ssh.connect(ip, port=22, username=username, password=password, timeout=10)
    
    suankiDizin = pwdOgren(ssh)
    print(f"Başlangıç dizini: {suankiDizin}")

    while True:
        komut = input(">> ").strip()
        if komut.lower() == "bye":
            break

        elif komut.lower() == "exit":
            break

        elif komut.lower() == "clear":
            print("\033c", end="")
        
        elif komut.startswith("cd "):
            suankiDizin = cdKomutu(komut, suankiDizin)
        
        elif komut.startswith("sudo "):
            print("sudo özelliği gelecek sürümlerde eklenecektir")
            komut

        elif komut.startswith("su "):
            print("sudo özelliği gelecek sürümlerde eklenecektir")
            komut
        
        elif komut == "su":
            print("sudo özelliği gelecek sürümlerde eklenecektir")
            komut
        
        elif komut == "sudo":
            print("sudo özelliği gelecek sürümlerde eklenecektir")
            komut

        elif komut != "":
            cdKomutu(komut, suankiDizin)
except paramiko.AuthenticationException:
    print("Hata: Username ve password eşleşmiyor")

except socket.gaierror:
    print("Hata: IP adresinin doğru olduğundan emin olun.")

except socket.timeout:
    print("Hata: Bağlantı zaman aşımına uğradı")

except Exception as e:
    print(e)

finally:
    ssh.close()