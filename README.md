# chess-engine-4kb

Chess engine UCI dalam 1 file Python < 4KB.

## Cara Jalanin
pip install -r requirements.txt
python main.py

## Cara Kerja
- Minimax + Alpha-Beta Pruning, depth 3
- Evaluasi: Material + Piece-Square Table
- Protokol UCI: uci, isready, position, go, quit
