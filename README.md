This script allows you to transcribe non-japanese samples for further using in Vocaloid DBTool.
Syntax:
transcribation_tool.py [PATH-TO-ROOT-WAV-DIR (in '', if contains spaces)] -v [VOWEL LIST SEPARATED BY -, EMPTY DEFAULT ] -t [0 - NO TRIPHONES, 1 - VCV ONLY, 2 - ALL TRIPHONES, 0 DEFAULT] -a [ARTICULATIONS SUBFOLDER, articulations DEFAULT] -s [STATIONARIES SUBFOLDER, stationary DEFAULT]
Directory structure:
wav_root
  - stationaries_subfolder
      - "a i M e o.wav"
  - articulations_subfolder
     - "k a k' i k M k e k o.wav"

Multipitch directory structure:
wav_root
  - stationaries_subfolder
     - A4
        - "a i M e o.wav"
     - C4
        - "a i M e o.wav"
  - articulations_subfolder
     - A4
       - "k a k' i k M k e k o.wav"
     - C4
       - "k a k' i k M k e k o.wav"
