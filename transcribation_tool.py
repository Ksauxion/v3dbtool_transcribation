import os
from glob import glob
import argparse


parser = argparse.ArgumentParser(description="V3 DBTool Transcribattion script")
vowels=[]
is_triphone=0
stationary='stationary'
articulations='articulations'
parser.add_argument("wav_root_dir", help="Root dir of wavs, containing articulations and stationary folders")
parser.add_argument("-v", dest="vowels", default=[], type=str, help="Vowels list, separated by dash (-), example: a-i-M-e-o-N")
parser.add_argument("-t", dest="is_triphone", default=0, type=int, help="Generate triphone articulations: 0 - no, 1 - only VCV (vowel-consonant-vowel), 3 - for all phonemes. Requires vowels input")
parser.add_argument("-a", dest="articulations", default='articulations', type=str, help="Articulations subfolder")
parser.add_argument("-s", dest="stationary", default='stationary', type=str, help="Stationaries subfolder")

args = parser.parse_args()

wav_root_dir = args.wav_root_dir
vowels = args.vowels
is_triphone = args.is_triphone

if len(vowels)!=0:
    vowels=vowels.split('-')
vp=' '.join(vowels)
phonemes_overall=[] 

print(f'Vowels are: {vp}')
print(f'Stationaries folder: {stationary}')
print(f'Ariticulations folder: {articulations}')

def create_trans(ph,vowels,is_triphone,tp):
    ph=ph.rsplit()
    for hh in ph:
        phonemes_overall.append(hh)
    trans=[]
    if ph[0]!='Sil':
        ph.insert(0,'Sil')
    if ph[-1]!='Sil':
        ph.append('Sil')
    trans.append(' '.join(ph)+'\n')
    ln=[]
    if tp=='s':
        for q in ph:
            if q!='Sil':
                ln.append(f'[{q}]\n')
    elif tp=='a':
        for q in range(1, len(ph)):
            ln.append(f'[{ph[q-1]} {ph[q]}]\n')
        if is_triphone==2:
            for q in range(2, len(ph)):
                if (q-2)!=-1:
                    if ph[q-1]!='Sil':
                        ln.append(f'[{ph[q-2]} {ph[q-1]} {ph[q]}]\n')
        elif is_triphone==1:
            for q in range(2, len(ph)):
                if (q-2)!=-1:
                    if (ph[q-1]!='Sil' and ph[q-1] not in vowels):
                        ln.append(f'[{ph[q-2]} {ph[q-1]} {ph[q]}]\n')
    for x in ln:
        trans.append(x)
    return trans
      
art=glob(os.path.join(wav_root_dir,articulations,'**','*.wav'),recursive=True)
if len(art)==0:
    print('Articulations folder not found!')
stat=glob(os.path.join(wav_root_dir,'stationary','**','*.wav'),recursive=True)
if len(stat)==0:
    print('Stationaries folder not found!')
    
for i in art:
    tp='a'
    e=(i[:-4])+'.trans'
    phu=os.path.split(i)[-1][:-4]
    g=create_trans(phu,vowels,is_triphone,tp)
    with open(e,'w') as f:
        for j in g:
            f.write(j)
        
    

for i in stat:
    tp='s'
    e=(i[:-4])+'.trans'
    phu=os.path.split(i)[-1][:-4]
    g=create_trans(phu,vowels,is_triphone,tp)
    with open(e,'w') as f:
        for j in g:
            f.write(j)
            
phonemes_overall=set(phonemes_overall)            
           
print('All phonemes found: ' + ' '.join(phonemes_overall))

print('Success!')
