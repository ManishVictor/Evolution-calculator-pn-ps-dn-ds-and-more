                            ####  This program calculates the dnds/pnps between two sequences  ######
                            ####  All the sequences entered here are single line fasta  ######
                            ####  https://github.com/zhutao1009/dnds   : Download this package ######
import sys
sys.path.append("..")
from dnds import dnds
apfile1=[]#This is the empty list which is going to take the sequences after they are split on \n from the stored read1 list
apfile2=[]#This is the empty list which is going to take the sequences after they are split on \n from the stored read2 list
evol=''
with open("file1.txt","r") as file1:#you open the parent file here i.e apfile2 
    read1=file1.readlines()
with open("file2.txt","r") as file2:#you open the child file here i.e all the sequences 
    read2=file2.readlines()
for i in range(len(read1)):
    nameseq=read1[i].split("\n")#splitting the  file w.r.t \n and each split will have {(header,\n);(seq,\n,);(header,\n);(seq\n)........}
    apfile1.append(nameseq[0])#extracting the zeroeth element we will have {header,seq,header,seq........}
for i in range(len(read2)):
    namesake=read2[i].split("\n")#same goes here
    apfile2.append(namesake[0])#and same goes here
for i in range(0,len(apfile1),2):#looping over  sequences
    for j in range(0,len(apfile2),2):#looping over  sequences
        if((str(apfile1[i]).lower()).strip()==(str(apfile2[j]).lower()).strip()):#comparing the headers of the sequences
            
            a=(str(apfile1[i+1])).strip()#apfile1 sequence is taken as the parent seq for comparison
            b=(str(apfile2[j+1])).strip()#each of the sequence is taken as the child sequence
            if(len(a)==len(b) and a!=b):#only those sequences are selected which are equal in length but not identical
                print(apfile1[i])#headers printed
                dnds(a,b)#calculating the pn,ps,pn/ps
