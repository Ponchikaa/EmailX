import random
import time



print("""
███████╗███╗░░░███╗░█████╗░██╗██╗░░░░░  ░██████╗░███████╗███╗░░██╗███████╗██████╗░░█████╗░████████╗░█████╗░██████╗░
██╔════╝████╗░████║██╔══██╗██║██║░░░░░  ██╔════╝░██╔════╝████╗░██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗
█████╗░░██╔████╔██║███████║██║██║░░░░░  ██║░░██╗░█████╗░░██╔██╗██║█████╗░░██████╔╝███████║░░░██║░░░██║░░██║██████╔╝
██╔══╝░░██║╚██╔╝██║██╔══██║██║██║░░░░░  ██║░░╚██╗██╔══╝░░██║╚████║██╔══╝░░██╔══██╗██╔══██║░░░██║░░░██║░░██║██╔══██╗
███████╗██║░╚═╝░██║██║░░██║██║███████╗  ╚██████╔╝███████╗██║░╚███║███████╗██║░░██║██║░░██║░░░██║░░░╚█████╔╝██║░░██║
╚══════╝╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝╚══════╝  ░╚═════╝░╚══════╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝
                                                                ░░▓▓▓▓▒▒░░                                                                  
                                                            ▓▓▓▓▓▓░░    ▓▓▓▓▒▒                                                              
                                                          ▒▒▓▓▓▓            ▒▒▓▓                                                            
                                                      ░░▓▓▓▓░░                ░░▓▓░░                                                        
                                                    ▒▒▓▓▓▓▒▒                      ▒▒▒▒                                                      
                      ░░                          ▒▒▓▓▓▓░░                          ▒▒▓▓                                                    
                      ░░      ░░                ▒▒▓▓▓▓▒▒                              ▒▒▓▓                                                  
                ░░░░  ░░░░    ░░░░    ░░      ▒▒▓▓▓▓▒▒                                  ▒▒▓▓                                                
                ░░      ░░  ░░░░░░  ░░      ▒▒▓▓▓▓▒▒                                      ▒▒▓▓                                              
                  ░░░░░░░░░░░░░░    ░░    ▓▓▒▒▓▓▓▓                                          ▓▓                                              
          ░░░░░░    ░░░░░░░░░░░░  ░░  ░░▓▓▒▒▓▓▒▒                                          ▒▒▓▓▒▒                                            
            ░░  ░░░░░░░░  ░░░░░░  ░░░░▒▒░░▓▓▓▓                                            ▓▓▓▓▓▓                                            
    ░░░░░░    ░░░░░░  ░░░░░░░░░░  ░░▒▒░░▒▒▒▒                                              ▓▓▓▓▓▓                                            
        ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒░░░░                                          ░░▓▓▓▓▓▓                                            
          ░░░░░░░░░░░░░░░░  ░░░░░░░░░░▒▒░░░░                                    ▒▒████████▓▓▓▓▓▓████████▓▓░░                                
                ░░░░░░░░░░░░░░  ░░░░░░░░░░░░                              ▒▒████████████████████████████████████                            
  ░░░░      ░░░░  ░░  ░░░░░░░░  ░░  ░░░░        ░░                    ▒▒██████████████████████████████████████████▒▒                        
            ░░░░░░░░░░░░░░    ░░░░░░░░░░░░░░                        ██████████████████████████████████████████████████                      
                  ░░░░░░░░    ░░░░░░░░░░░░░░░░░░                ░░██████████████████████████████████████████████████████░░                  
          ░░░░░░░░░░░░░░░░        ░░░░                        ▓▓██████████████████████████████████████████████████████████▓▓                
      ░░░░░░  ░░░░░░░░░░░░░░  ░░░░░░  ░░░░░░                ██████████████████████████████████████████████████████████████████              
            ░░░░░░░░░░░░░░░░  ░░  ░░░░    ░░░░            ▓▓████████████████████████████████████████████████████████████████████            
              ░░  ░░░░░░░░░░░░  ░░  ░░░░                ▒▒▓▓▓▓████████████████████████████████████████████████████████████████████          
          ░░░░  ░░  ░░    ░░░░  ░░░░                  ░░▓▓▓▓▓▓██████████████████████████████████████████████████████████████████████        
        ░░    ░░  ░░░░    ░░░░    ░░      ░░          ██▒▒▒▒████████████████████████████████████████████████████████████████████████        
                ░░  ░░░░    ░░░░  ░░░░              ▒▒▓▓▒▒▒▒██████████████████████████████████████████████████████████████████████████      
                  ░░        ░░░░                    ██▒▒▒▒▓▓██████████████████████████████████████████████████████████████████████████▒▒    
                    ░░      ░░    ░░              ▒▒▓▓▒▒▒▒██████████████████████████████████████████████████████████████████████████████    
                    ░░      ░░                    ██▓▓▓▓████████████████████████████████████████████████████████████████████████████████░░  
                                                  ██▓▓▓▓██████████████████████████████████████████████████████████████████████████████████  
                                                  ██████▓▓░░▒▒▓▓██████████████████████████████████████████████████████████████████████████  
                                                ▓▓██████▒▒      ░░████████████████████████████████████████████████▒▒░░░░░░▓▓██████████████░░
                                                ████████░░        ██████▓▓░░      ▓▓██████▓▓▒▒░░██████░░░░░░▒▒██▓▓          ██████████████▒▒
                                                ████████  ▒▒██    ██████            ██████░░    ▓▓████      ░░██▓▓  ░░▒▒▒▒  ▓▓██████████████
                                                ████████  ▓▓██░░  ████░░    ▒▒▒▒    ▒▒████░░    ▒▒████      ░░████  ░░████  ▒▒██████████████
                                                ██████▓▓  ▒▒▒▒  ░░████    ██████▒▒    ████░░  ▒▒░░██▓▓  ░░  ░░████  ░░████  ▓▓██████████████
                                                ██████▒▒        ▓▓████  ░░██████▓▓    ████░░  ▓▓  ██▓▓  ▓▓    ████    ░░    ████████████████
                                                ██████▒▒        ████▒▒  ▒▒████████    ████    ██  ▓▓▒▒  ██    ████          ░░██████████████
                                                ██████░░  ██░░  ░░██▒▒  ▒▒████████    ████    ▓▓  ▓▓▒▒  ██    ████    ░░░░    ▓▓████████████
                                                ██████░░░░████  ░░██▒▒  ▒▒████████    ████░░  ▓▓  ▒▒░░░░██    ████    ██████  ▒▒██████████▓▓
                                                ██████░░░░████    ██▓▓  ░░████████    ████░░  ▓▓░░    ░░██    ████    ████▓▓  ▒▒████████████
                                                ▒▒████▒▒  ▓▓▒▒    ████  ░░██████▒▒    ████░░  ▓▓░░    ▒▒██    ████    ████▒▒  ▒▒██████████  
                                                ░░████▒▒          ████    ▒▒████░░  ░░████    ▓▓▒▒    ▓▓██    ████    ▒▒      ████████████  
                                                  ████▓▓        ░░████░░    ░░░░    ▒▒████    ▓▓▓▓    ▓▓██    ████          ░░████████████  
                                                  ████████▒▒░░░░▓▓████▓▓            ██████    ▓▓██    ████    ████        ░░████████████░░  
                                                  ▒▒████████████████████▓▓░░      ▒▒██████░░  ████  ░░████░░░░████▒▒▒▒██████████████████    
                                                    ████████████████████████▓▓████████████▓▓▒▒████▓▓▓▓████████████████████████████████▒▒    
                                                    ▒▒████████████████████████████████████████████████████████████████████████████████      
                                                      ██████████████████████████████████████████████████████████████████████████████░░      
                                                        ██████████████████████████████████████████████████████████████████████████▓▓        
                                                        ▒▒████████████████████████████████████████████████████████████████████████          
                                                          ▓▓████████████████████████████████████████████████████████████████████            
                                                            ████████████████████████████████████████████████████████████████▓▓              
                                                              ████████████████████████████████████████████████████████████▓▓                
                                                                ░░██████████████████████████████████████████████████████▒▒                  
                                                                    ██████████████████████████████████████████████████                      
                                                                      ░░██████████████████████████████████████████░░                        
                                                          ░░░░░░░░░░░░░░░░▒▒▓▓████████████████████████████████▒▒░░░░░░░░░░░░                
                                                  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓██████████████████▓▓▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░      
                                                ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░    
                                                  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░      
                                                          ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░                  """)


list = ["userniger415@gmail.com mamasheni123",
"egwere215@gmail.com	215egwere",
"fgerewr1346@gmail.com	1346fgerewr",
"b01jasonabanil@gmail.com	1240awrha",
"biktimirova0908veronika@gmail.com	348awfho",
"ekaterinayatut@gmail.com	1245wrwor",
"39kristin82@gmail.com	239kawrih",
"hesterkaren711@gmail.com	711kasfjren",
"ericaholding1@gmail.com	124ajowf",
"whitedior66@gmail.com	237skjdgf",
"egjop31@gmail.com	2359njakwf",
"ailynrosesabanmagdayao@gmail.com	2375hjasfb",
"lifeheartlive16@gmail.com	0987asfeg",
"jamnawty17@gmail.com	16235asfh",
"smithjenny160@gmail.com	294abkjfs",
"daniellamcdonald1989@gmail.com	2073awbf",
"honestyq0@gmail.com	7092ajbwf",
"johnmelissa354@gmail.com	0127afsew",
"kloewebb166@gmail.com	1276fwfh",
"harrisbraddlee@gmail.com	984nhsegr",
"dannychidny@gmail.com	2365awfaw",
"puppysheaven13@gmail.com	347efjna",
"lisabrown11005@gmail.com	9326awoi",
"shevestinadazzi@gmail.com	8723ajbsf",
"poalacassenito101@gmail.com	6124asgg",
"floridahaberie1980@gmail.com	1289iuwhf",
"emayesunday7@gmail.com	3934whog",
"goldsuki77@gmail.com	1926aawg",
"benzoaremarvellous@gmail.com	0379awgha",
"franciscayossi04@gmail.com	2305pjaf",
"frankharrisonny@gmail.com	5109bhjrf",
"naomicambell447@gmail.com	9837dfgbj",
"maureendanar@gmail.com	4219uwiqr",
"babaracodi15@gmail.com	3017zdgfwe",
"drakeerick37@gmail.com	0982jygqw",
"ransonsamantha4@gmail.com	3785awsfio",
"mavistedy@gmail.com	1572ienfsa",
"susanadam749@gmail.com	72457sedj",
"berryscott484@gmail.com	8411ndmnz",
"sophiepart9@gmail.com	3882bvnaw",
"hb1387027@gmail.com	7391jbsdfj",
"sophiapeterson64@gmail.com	8998hrghj",
"arafat.suha061@gmail.com	6363jbsdg",
"donaldbencatering@gmail.com	7893nbdrt",
"davemorgan1221@gmail.com	2743hureg",
"roselawson773@gmail.com	4723wejse",
"oliviahartwell42@gmail.com	5235huwef",
"yameenarashid@gmail.com	8899faejih",
"oliviawilson2025@gmail.com	02433segjb",
"angelawarren025@gmail.com	87833cegia",
"josephpatric010@gmail.com	3248rgiha",
"coeur.douceur20@gmail.com	49801oksrge",
"el0195178@gmail.com	5214jksege",
"daniellasmithjones86@gmail.com	0937wegw",
"ottoh4373@gmail.com	2358hknae"]

inp = input("How many emails do you want?: ")

rand = random.choice(list)

if inp >= "11":
    print("ERROR Maximum 10 email")
if inp == "1":
    print(rand)
    exit()
if inp == "2":
    print(rand, rand)
    exit()
if inp == "3":
    print(rand, rand, rand)
    exit()
if inp == "4":
    print(rand, rand, rand, rand)
if inp == "5":
    print(rand, rand, rand, rand, rand)
if inp == "6":
    print(rand, rand, rand, rand, rand, rand)
if inp == "7":
    print(rand, rand, rand, rand, rand,rand,rand)
if inp == "8":
    print(rand,rand,rand,rand,rand,rand,rand,rand)
if inp == "9":
    print(rand,rand,rand,rand,rand,rand,rand,rand,rand)
if inp == "10":
    print(rand,rand,rand,rand,rand,rand,rand,rand,rand,rand)



