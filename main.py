import sys
from pytongues import executar

if len(sys.argv) < 2:
    print("usa: python main.py arquivo.ptpy")
else:
    executar(sys.argv[1])
