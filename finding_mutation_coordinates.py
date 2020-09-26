                    #This program finds the mutation co-ordinates based on codons and not amino-acids#
                    #The position is of the first nucleotide of the codon that shows the change#
                                        # use single line fasta file #
apfile1=[]
apfile2=[]
codon1=[]
codon2=[]
pos=[]
with open("file1.txt","r") as file1:#opens file
    read1=file1.readlines()#reads file
with open("file2.txt","r") as file2:#opens file
    read2=file2.readlines()#reads file
for i in range(len(read1)):#looping over file1
    splitfile1=str(read1[i]).split("\n")#removinf the newlines
    apfile1.append(str(splitfile1[0]).strip())#appending the data after newline removal
for j in range(len(read2)):#-do-#
    splitfile2=str(read2[j]).split("\n")#-do-#
    apfile2.append(str(splitfile2[0]).strip())#-do-#
for k in range(0,len(apfile1),2):
    header1=apfile1[k]#keeping the header to check whether the same is there in the other file
    for l in range(0,len(apfile2),2):
        header2=apfile2[l]
        if(header1==header2):#if headers match then load the sequences to be checked
            seq1=apfile1[k+1]
            seq2=apfile2[l+1]
            if(len(seq1)==len(seq2)):#match only when sequences have same length
                for m in range(0,len(seq1),3):#window of three, codons are made up of three nucleotides
                        seqC=seq1[m:m+3:]#step-size three in first sequence
                        seqW=seq2[m:m+3:]#step size three in second sequence
                        if(seqC==seqW):#matching the codons
                            pass
                        else:#if mutation is there then this block executes
                            codon1.append(seqC)
                            codon2.append(seqW)
                            pos.append(m+1)
        else:# if no mutation happens the programs moves to next codon
            continue
        for n in range(len(codon1)):#This loop print the headers,initial and the mutated codons and the position
            print(header1,header2,codon1[n],codon2[n],pos[n])
#         print(header1,header2)#check your process
#         print(codon1,codon2)#check your process
#         print(pos)#check your process
        codon1=[]#re-initialisation
        codon2=[]#re-initialization
        pos=[]#re-initialisation
