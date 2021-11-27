from pypresence import Presence

class DiscordActivity :
    def __init__(self,client_id):
        self.presence = Presence(client_id) 
        self.presence.connect() 

    def updatePresence(self,sous_titre,titre):
        if(titre !=None and len(titre)<2): #not ok
            titre = None
        if(sous_titre !=None and len(sous_titre)<2): #not ok
            sous_titre = None

        if(titre !=None and sous_titre !=None):
            self.presence.update(state=titre, details=sous_titre)
        elif(titre != None and sous_titre == None):
            self.presence.update(state=titre)
        elif(titre == None and sous_titre != None):
            self.presence.update(state=sous_titre)

if __name__ == "__main__":
    """
        test function if u launch this file
    """
    p = DiscordActivity('783274457665765377')
    p.updatePresence("Title !","Sub-Title :)")

    while True:
        pass