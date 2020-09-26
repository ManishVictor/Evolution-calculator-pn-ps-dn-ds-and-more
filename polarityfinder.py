codon1=0
codon2=0
polarity1=0
polarity2=0
with open("file3.txt","r") as file1:
    read1=file1.readlines()
with open("codon-aminoacid.csv","r") as file2:
    read2=file2.readlines()
for i in range(len(read1)):
    split1=str(read1[i]).split(",")
    #split2=str(split1[0]).split("\s")
    for j in range(len(read2)):
        splita=read2[j].split("\n")
        splitb=splita[0].split(",")
        if(splitb[0]==split1[2]):
            codon1=splitb[1]
            polarity1=splitb[2]
        if(splitb[0]==split1[3]):
            codon2=splitb[1]
            polarity2=splitb[2]
    print(codon1,polarity1,codon2,polarity2)
        
