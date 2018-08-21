#Programın orijinali Starwarsfan2099 isimli geliştiriciye aittir, ben Erol Umut *GreXLin85* Atalay programı sadece Türkçeye çevirmiştir.
#Orijinal kaynak : https://github.com/Starwarsfan2099/Python-Hash-Cracker

#!/usr/bin/python
import StringIO
import getopt
import hashlib
import sys
import os
import time
print "  "
print "Python Hash-Cracker"
print "Sürüm 3.0-3 Stabil"


def info():
  print " "
  print "Bilgi:"
  print "[*] Ayarlar:"
  print "[*](-h) Hash"
  print "[*](-t) Tür [Desteklenen hashleri gör]"
  print "[*](-w) Kelime listesi"
  print "[*](-n) Numbers bruteforce"
  print "[*](-v) Verbose [{WARNING}Slows cracking down!]\n"
  print "[*] Örnek:"
  print "[>] ./Hash-Cracker.py -h <hash> -t md5 -w DICT.txt"
  print "[>] ./Hash-Cracker.py -h <hash> -t sha384 -n -v"
  print "[*] Desteklenen hashler:"
  print "[>] md5, sha1, sha224, sha256, sha384, sha512"
  print "[*] Thats all folks!\n"
  

def checkOS():
    if os.name == "nt":
        operatingSystem = "Windows"
    elif os.name == "posix":
        operatingSystem = "posix"
    else:
        operatingSystem = "Unknown"
    return operatingSystem


class hashCracking:
  
  def hashCrackWordlist(self, userHash, hashType, wordlist, verbose):
    start = time.time()
    self.lineCount = 0
    if (hashType == "md5"):
       h = hashlib.md5
    elif (hashType == "sha1"):
       h = hashlib.sha1
    elif (hashType == "sha224"):
       h = hashlib.sha224
    elif (hashType == "sha256"):
       h = hashlib.sha256
    elif (hashType == "sha384"):
       h = hashlib.sha384
    elif (hashType == "sha512"):
       h = hashlib.sha512
    else:
       print "[-]Bu %s desteklenen bir hash türü mü?" % hashType
       exit()
    with open(wordlist, "rU") as infile:
      for line in infile:
        line = line.strip()
        lineHash = h(line).hexdigest()
        if (verbose == True):
            sys.stdout.write('\r' + str(line) + ' ' * 20)
            sys.stdout.flush()
        if (lineHash == userHash.lower()):
            end = time.time()
            print "\n[+]Hash: %s" % line
            print "[*]Kelime denendi: %s" % self.lineCount
            print "[*]Süre: %s saniye" % round((end-start), 2)
            exit()
        else:
            self.lineCount = self.lineCount + 1
    end = time.time()
    print "\n[-]Kırma işlemi başarısız"
    print "[*]Kelime listesinin sonuna ulaşıldı"
    print "[*]Kelime denendi: %s" % self.lineCount
    print "[*]Süre: %s seconds" % round((end-start), 2)
    exit()

  def hashCrackNumberBruteforce(self, userHash, hashType, verbose):
    start = time.time()
    self.lineCount = 0
    if (hashType == "md5"):
       h = hashlib.md5
    elif (hashType == "sha1"):
       h = hashlib.sha1
    elif (hashType == "sha224"):
       h = hashlib.sha224
    elif (hashType == "sha256"):
       h = hashlib.sha256
    elif (hashType == "sha384"):
       h = hashlib.sha384
    elif (hashType == "sha512"):
       h = hashlib.sha512
    else:
       print "[-]Bu %s desteklenen bir hash türü mü?" % hashType
       exit()
    while True:
       line = "%s" % self.lineCount
       line.strip()
       numberHash = h(line).hexdigest().strip()
       if (verbose == True):
           sys.stdout.write('\r' + str(line) + ' ' * 20)
           sys.stdout.flush()
       if (numberHash.strip() == userHash.strip().lower()):
           end = time.time()
           print "\n[+]Hash: %s" % lineCount
           print "[*]Süre: %s saniye" % round((end-start), 2)
           break
       else:
         self.lineCount = self.lineCount + 1

def main(argv):
  hashType = userHash = wordlist = verbose = numbersBruteforce = None
  print "[%s 'da çalışıyor]\n" % checkOS()
  try:
      opts, args = getopt.getopt(argv,"ih:t:w:nv",["ifile=","ofile="])
  except getopt.GetoptError:
      print '[*]./Hash-Cracker.py -t <tür> -h <hash> -w <wordlist>'
      print '[*]Tür ./Hash-Cracker.py -i yazarak bilgi alabilirsiniz.'
      sys.exit(1)
  for opt, arg in opts:
      if opt == '-i':
          info()
          sys.exit()
      elif opt in ("-t", "--type"):
          hashType = arg
      elif opt in ("-h", "--hash"):
          userHash = arg
      elif opt in ("-w", "--wordlist"):
          wordlist = arg
      elif opt in ("-v", "--verbose"):
          verbose = True
      elif opt in ("-n", "--numbers"):
          numbersBruteforce = True
  if not (hashType and userHash):
      print '[*]./Hash-Cracker.py -t <tür> -h <hash> -w <wordlist>'
      sys.exit()
  print "[*]Hash: %s" % userHash
  print "[*]Hash türü: %s" % hashType
  print "[*]Kelime listesi: %s" % wordlist
  print "[+]Kırılıyor..."
  try:
      h = hashCracking()
      if (numbersBruteforce == True):
         h.hashCrackNumberBruteforce(userHash, hashType, verbose)
      else:
         h.hashCrackWordlist(userHash, hashType, wordlist, verbose)

  except IndexError:
        print "\n[-]Hash kırma işlemi başarısız:"
        print "[*]Kelime listesinin sonuna ulaşıldı"
        print "[*]Başka bir kelime listesi dene"
        print "[*]Bu kadar kelime denendi: %s" % h.lineCount
        
  except KeyboardInterrupt:
        print "\n[Kapatılıyor...]"
        print "Bu kadar kelime denendi: %s" % h.lineCount
        
  except IOError:
        print "\n[-]Couldn't find wordlist"
        print "[*]Is this right?"
        print "[>]%s" % wordlist
        
if __name__ == "__main__":
    main(sys.argv[1:])
