
import string
import sys
import re
import os
import subprocess

def wordCounter(input_file):
    wordCounts = {}
   
    with open(input_file, "r") as f:
        
        for line in f:
            line = line.strip()
            line = line.lower()
            line = line.translate(str.maketrans("", "", string.punctuation))
            
            words = line.split()
           
            for word in words:
                
                if word in wordCounts:
                    wordCounts[word] += 1
                else:
                    wordCounts[word] = 1
    
    return wordCounts

def writeWordsToOutput(wordCounts, output_file):
   
    with open(output_file, "w") as f:
        
        sorted_word_counts = sorted(wordCounts.items(), key=lambda x: (-x[1], x[0]))
        
        for word, count in sorted_word_counts:
          
            f.write(f"{word} {count}\n")


input_file = input("Please enter the name of the input file: ")
output_file = input("Please enter the name of the output file: ")

wordCounts = wordCounter(input_file)

writeWordsToOutput(wordCounts, output_file)
print("Finish!, check your ", output_file, " file :) ")
