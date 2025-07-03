{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "fe02dd05-5e29-482e-907f-1a4a7d2df6bb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Ini adalah output perintah langsung menggunakan print() atau HARDCODE\n",
      "1. Ubah kata 'AKU CINTA KAMU'\n",
      "UKA ATNIC UMAK\n",
      "2. Urutkan kata 'HARI INI SEDANG BELAJAR PYTHON'\n",
      "PYTHON HARI BELAJAR SEDANG INI\n",
      "3. ganti huruf fokal kecil dari kata Aku Cinta Kamu\n",
      "Ak|_| C1nt4 K4m|_|\n",
      "4. ganti huruf vokal besar dari kataAku Cinta Kamu\n",
      "4ku 4ayang Kamu\n"
     ]
    }
   ],
   "source": [
    "def Reverse_kata(kalimat): #membuat function untuk reverse per kata\n",
    "    kata_list = kalimat.split() #kata_list merupakan string dari kalimat yang di split\n",
    "    return ' '.join([kata [::-1] for kata in kata_list]) #disini setiap kata yang ada di index string yang sudah di split akan di reverse\n",
    "\n",
    "def urut_kata(kalimat, urutan): #membuat function urutan kalimat\n",
    "    kata_list = kalimat.split() #kata_list merupakan string dari kalimat yang di split\n",
    "    return ' '.join([kata_list[i - 1] for i in urutan]) #membuat string baru sesuai dengan urutan yang sudah di berikan dan digabung kembali menjadi string\n",
    "\n",
    "def ganti_vokal(kalimat, opsi): #membuat function ganti_vokal\n",
    "    vokalkecil = {'a':'4','i':'1','u':'|_|','e':'3','o':'0'} #vocal kecil yang ada pada list diubah ke simbol\n",
    "    vokalbesar = {'A':'4','I':'1','U':'|_|','E':'3','O':'0'} #vocal besar yang ada pada list diubah ke simbol\n",
    "    hasil = ''#hasil nya sama dengan kosong (karena nanti akan diisi oleh vokal yang di ganti)\n",
    "    for huruf in kalimat: #untuk huruf dalam kalimat\n",
    "        if opsi == 1 and huruf in vokalkecil: #jika opsi 1 dan huruf berada di dalam vokalkecil\n",
    "            hasil += vokalkecil[huruf] #hasil diisi oleh huruf vokalkecil yang sudah diganti\n",
    "        elif opsi == 2 and huruf in vokalbesar: #jika memilih opsi 2 dan huruf ada di dalam vokalbesar\n",
    "            hasil += vokalbesar[huruf] #hasil diisi oleh huruf vokalbesar yang sudah diganti\n",
    "        else: #jika semua opsi tidak dipilih atau tidak ada\n",
    "            hasil += huruf #maka hasil nya tetap kata dari huruf yang di data\n",
    "    return hasil #kembali ke hasil\n",
    "\n",
    "print(\"Ini adalah output perintah langsung menggunakan print() atau HARDCODE\")\n",
    "print(\"1. Ubah kata 'AKU CINTA KAMU'\")\n",
    "#print memanggil function Reverse_kata untuk mengubah kalimat \"AKU CINTA KAMU\" \n",
    "print(Reverse_kata(\"AKU CINTA KAMU\")) \n",
    "print(\"2. Urutkan kata 'HARI INI SEDANG BELAJAR PYTHON'\")\n",
    "#print dan memanggil function urut_kata untuk ngeprint hasil susunan kalimat dari kalimat \"HARI INI SEDANG BELAJAR PYTHON\"\n",
    "print(urut_kata(\"HARI INI SEDANG BELAJAR PYTHON\", [5,1,4,3,2]))  \n",
    "print(\"3. ganti huruf fokal kecil dari kata \"\"Aku Cinta Kamu\")\n",
    "#print dan mengganti huruf vokalkecil dengan opsi pertama\n",
    "print(ganti_vokal (\"Aku Cinta Kamu\", 1))\n",
    "print(\"4. ganti huruf vokal besar dari kata\" \"Aku Cinta Kamu\")\n",
    "#print dan mengganti huruf vokalbesar dengan opsi 2\n",
    "print(ganti_vokal (\"Aku Cinta Kamu\", 2))"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
