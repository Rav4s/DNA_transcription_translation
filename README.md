# DNA_transcription_translation
A simple, fast program which transcribes a DNA strand into messenger RNA (mRNA), which it then translates into amino acids.
## What does it do? ##
It takes in a DNA strand as input and converts this strand to a complementary messenger RNA strand using these mappings:  
  
A &#8594; U  
T &#8594; A  
C &#8594; G  
G &#8594; C  
  
For example, `GTACTAGAGCATTT` would be converted to `CAUGAUCUCGUAAA`  
After this, it looks for a start codon (AUG) and a stop codon (UAA, UAG, UGA) and it removes anything out of the range from start to stop.  
For example, `CAUGAUCUCGUAAA` would be converted to `AUGAUCUCGUAA`  
Then, it turns the result of the previous step into a list broken into 3-character items.  
For example, `AUGAUCUCGUAA` would be converted to `['AUG', 'AUC', 'UCG', 'UAA']`  
Finally, it compares each item in the list to the amino_acids.py file, which is basically a predefined [codon chart.](https://www.google.com/search?q=codon+chart&rlz=1C1CHBF_enUS912US912&tbm=isch&source=iu&ictx=1&fir=SVhfz4tRL5GzVM%252Cx4w9lB13r4FJ7M%252C_&vet=1&usg=AI4_-kSuwWL4sbNFjTZd3fkSLRoPujadRw&sa=X&ved=2ahUKEwi7verdq-7sAhVQSK0KHUXZAp8Q9QF6BAgBEFg&biw=1366&bih=625&safe=active&ssui=on#imgrc=SVhfz4tRL5GzVM)  
This returns a list of the amino acids for the codons: `['AUG', 'AUC', 'UCG', 'UAA']` would return `['Methionine', 'Isoleucine', 'Serine', 'STOP']`  

You can find sample DNA strands and what the script returns for them in the sample_strands.txt file.   
**WARNING: I HAVEN'T DONE A LOT OF TESTING, SO USE THIS TOOL AT YOUR OWN RISK.**
