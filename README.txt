Eğer SSHClient için yeni özellik fikirleriniz varsa, bana memirhansumer@gmail.com e-posta adresinden ulaşabilirsiniz.

SSHClient, SSH erişimi bulunmayan bilgisayarlar için SSH bağlantısı sağlayan bir komut istemcisi uygulamasıdır. Bu araç, ağ üzerinden uzak sistemlere erişim sağlamak için SSH protokolünü kullanarak komutları çalıştırmanıza olanak tanır. Proje, çeşitli uzak sistemlerde komut yürütme ve dizin yönetimi gibi işlevleri destekler.

Özellikler:

- Uzak Sistem Bağlantısı: SSHClient, IP adresi, kullanıcı adı ve şifre kullanarak uzak bir sistemle SSH bağlantısı kurar.
- Dizin Yönetimi: `cd` komutunu kullanarak uzak sistemdeki dizinler arasında geçiş yapabilirsiniz. Geçerli dizini kontrol edebilir ve geçiş yapabilir.
- Komut Yürütme: Uzak sistemde herhangi bir komut çalıştırabilir ve çıktıyı doğrudan yerel terminale alabilirsiniz.
- Hata Yönetimi: Bağlantı hataları, kimlik doğrulama sorunları ve dizin hataları gibi durumlarda kullanıcıya anlamlı hata mesajları sağlar.
- Temizlik ve Kullanım Kolaylığı: Basit ve kullanıcı dostu bir arayüz ile komutları hızlıca çalıştırabilir ve sonuçları görebilirsiniz.

Kurulum ve Kullanım:

1. “pip install requirements.txt” dosyasının kurulu olduğundan emin olun.
2. Uygulamayı çalıştırın ve IP adresi, kullanıcı adı ve şifre bilgilerini girin.
3. `cd`, `pwd` gibi temel komutları kullanarak uzak sistemle etkileşime geçin.

Gelecek Özellikler:

- sudo ve su Destekleri: İlerleyen sürümlerde `sudo` ve `su` komutları ile yetki yönetimi desteklenecektir.

Bu açıklama ile kullanıcılarınız, `SSHClient`'ın ne işe yaradığını, nasıl kullanılacağını ve mevcut özelliklerini hızlıca anlayabilirler.
