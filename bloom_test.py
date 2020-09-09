from bloomfilter import BloomFilter 
from random import shuffle 
  
n = 20 #no of items to add 
p = 0.05 #false positive probability 
  
bloomf = BloomFilter(n,p) 
print("Size of bit array:{}".format(bloomf.size)) 
print("False positive Probability:{}".format(bloomf.fp_prob)) 
print("Number of hash functions:{}".format(bloomf.hash_count)) 
  
 
word_present = ['abound','abounds','abundance','abundant','accessible', 
                'bloom','blossom','bolster','bonny','bonus','bonuses', 
                'coherent','cohesive','colorful','comely','comfort', 
                'gems','generosity','generous','generously','genial'] 
  
word_absent = ['bluff','cheater','hate','war','humanity', 
               'racism','hurt','nuke','gloomy','facebook', 
               'twitter','Analytics','bloom'] 
  
for item in word_present: 
    bloomf.add(item) 
  
shuffle(word_present) 
shuffle(word_absent) 
  
test_words = word_present[:10] + word_absent 
shuffle(test_words) 
for word in test_words: 
    if bloomf.check(word): 
        if word in word_absent: 
            print("'{}' is not in the bloom filter, but a false positive!\n".format(word)) 
        else: 
            print("'{}' is probably present in the bloom filter!\n".format(word)) 
    else: 
        print("'{}' is definitely not present in the bloom filter!\n".format(word)) 
