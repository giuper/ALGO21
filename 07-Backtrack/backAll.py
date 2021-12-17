class BackTrack:

#la classe derivata deve implementare
# allMoves(stato)   -- restituisce la lista di mosse nello stato 
# isAdm(stato,m)    -- True sse mossa m e' ammissibile in stato
# newStato(stato,m) -- restituisce lo stato che si ottiene applicando m
# isFinal(stato)    -- True se e solo se lo stato e' finale


#restituisce la lista di tutte le soluzioni
#ottenibili a partire da stato
#se non ci sono soluzioni, restituisce la lista vuota

    def _Solve(self,stato,verbose=False):
        if verbose:
            print("Stato:",stato)
        if self.isFinal(stato):
            return [stato]
        results=[]
        for m in self.allMoves(stato):
            if not self.isAdm(stato,m):
                if verbose:
                    print("mossa ",m,"non ammissibile in",stato)
                continue
            if verbose:
                print("mossa ",m,"ammissibile in",stato)
            newStato=self.newStato(stato,m)
            risultato=self._Solve(newStato,verbose)
            for r in risultato:
                results.append(r)
        return results


