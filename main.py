import chess, sys, random

V={chess.PAWN:100,chess.KNIGHT:320,chess.BISHOP:330,chess.ROOK:500,chess.QUEEN:900,chess.KING:20000}
PST={
chess.PAWN:[0,0,0,0,0,0,0,0,50,50,50,50,50,50,50,50,10,10,20,30,30,20,10,10,5,5,10,25,25,10,5,5,0,0,0,20,20,0,0,0,5,-5,-10,0,0,-10,-5,5,5,10,10,-20,-20,10,10,5,0,0,0,0,0,0,0,0],
chess.KNIGHT:[-50,-40,-30,-30,-30,-30,-40,-50,-40,-20,0,0,0,0,-20,-40,-30,0,10,15,15,10,0,-30,-30,5,15,20,20,15,5,-30,-30,0,15,20,20,15,0,-30,-30,5,10,15,15,10,5,-30,-40,-20,0,5,5,0,-20,-40,-50,-40,-30,-30,-30,-30,-40,-50],
chess.BISHOP:[-20,-10,-10,-10,-10,-10,-10,-20,-10,0,0,0,0,0,0,-10,-10,0,5,10,10,5,0,-10,-10,5,5,10,10,5,5,-10,-10,0,10,10,10,10,0,-10,-10,10,10,10,10,10,10,-10,-10,5,0,0,0,0,5,-10,-20,-10,-10,-10,-10,-10,-10,-20],
chess.ROOK:[0,0,0,0,0,0,0,0,5,10,10,10,10,10,10,5,-5,0,0,0,0,0,0,-5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,10,10,10,10,10,10,5,0,0,0,0,0,0,0,0],
chess.QUEEN:[-20,-10,-10,-5,-5,-10,-10,-20,-10,0,0,0,0,0,0,-10,0,0,5,5,5,5,0,0,-5,0,5,5,5,5,0,-5,0,0,5,5,5,5,0,0,-5,0,5,5,5,5,0,-5,-10,5,5,5,5,5,0,-10,-10,-10,-5,-5,-5,-5,-10,-10,-20],
chess.KING:[-30,-40,-40,-50,-50,-40,-40,-30,-30,-40,-40,-50,-50,-40,-40,-30,-30,-40,-40,-50,-50,-40,-40,-30,-30,-40,-40,-50,-50,-40,-40,-30,-20,-30,-30,-40,-40,-30,-30,-20,-10,-20,-20,-20,-20,-20,-20,-10,20,20,0,0,0,0,20,20,0,0,0,0,0,0,0,0],
}

def ev(b):
    s=0
    for t in V:
        for sq in b.pieces(t,chess.WHITE):
            s+=V[t]+PST[t][sq]
        for sq in b.pieces(t,chess.BLACK):
            s-=V[t]+PST[t][chess.square_mirror(sq)]
    return s if b.turn==chess.WHITE else -s

def search(b,d,a,be):
    if d==0 or b.is_game_over(): return ev(b)
    best=-999999
    ms=list(b.legal_moves)
    random.shuffle(ms)
    for m in ms:
        b.push(m)
        sc=-search(b,d-1,-be,-a)
        b.pop()
        if sc>best: best=sc
        if sc>a: a=sc
        if a>=be: break
    return best

def bestmove(b):
    best=None; bs=-999999
    ms=list(b.legal_moves)
    random.shuffle(ms)
    for m in ms:
        b.push(m)
        sc=-search(b,2,-999999,999999)
        b.pop()
        if sc>bs: bs=sc; best=m
    return best

def main():
    b=chess.Board()
    while True:
        line=sys.stdin.readline()
        if not line: break
        p=line.strip().split()
        if not p: continue
        if p[0]=="uci":
            print("id name Rdw212-4kb"); print("uciok",flush=True)
        elif p[0]=="isready":
            print("readyok",flush=True)
        elif p[0]=="ucinewgame":
            b=chess.Board()
        elif p[0]=="position":
            b=chess.Board()
            if "moves" in p:
                i=p.index("moves")
                for mv in p[i+1:]:
                    b.push_uci(mv)
        elif p[0]=="go":
            m=bestmove(b)
            print(f"bestmove {m.uci()}",flush=True)
        elif p[0]=="quit":
            break

if __name__=="__main__":
    main()
