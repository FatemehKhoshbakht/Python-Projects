

class family_tree:
    def __init__(self):
        self._family_members = []
    
    def add_new_person(self,person):
        self._family_members.append(person)
    
    def get_children(self,id):
        for i in self._family_members:
            if i['id'] == id :
                return i['children']
        return " "
    
    def get_prson_by_id(self,id):
        for i in self._family_members:
            if i['id'] == id :
                return i
        return " "
    
    def get_spouse(self,id):
        for i in self._family_members:
            if i['id'] == id :
                return i['spouse']
        return " "
    
    def get_gender(self,id):
        for i in self._family_members:
            if i['id'] == id :
                return i['gender']
        return " "
    
    def check_relationship(self,id1,id2):
        for i in self._family_members:
            if i['id'] == id2 :

                # Check Hamsar
                spouse = i['spouse']
                if id1 in spouse :
                    return "Hamsar"
                
                # Check Farzand
                child = i['children']
                if id1 in child:
                    return "Farzand"
                
                # Check Pedar
                if id1 == i['father_id']:
                    return "Pedar"
                
                # Check Pedar Bozorg ya Modar Bozorg Pedari
                temp = self.get_prson_by_id(i['father_id'])
                if id1 == temp['father_id'] :
                    return "Pedar Bozorg Pedari"
                if id1 == temp['mother_id'] :
                    return "Madar Bozorg Pedari"

                # Check Madar
                if id1 == i['mother_id']:
                    return "Madar"
                
                # Check Pedar Bozorg ya Modar Bozorg Pedari
                temp = self.get_prson_by_id(i['mother_id'])
                if id1 == temp['father_id'] :
                    return "Pedar Bozorg Madari"
                if id1 == temp['mother_id'] :
                    return "Madar Bozorg Madari"

                # Check Khahar ya Baradar
                childs = self.get_children(i['father_id'])
                if id1 in childs :
                    if self.get_gender(id1) == "0":
                        return "Khahar"
                    return "Baradar"
                
                # Check Nave
                for ch in childs :
                    temp = self.get_children(ch)
                    if id1 in temp :
                        return "Nave"

                # Check Shohar Khahar ya Zandadash
                for j in childs:
                    temp = self.get_spouse(j)
                    if id1 in temp :
                        if self.get_gender(id1) == "0":
                            return "Zan Dadash"
                        return "Shohar Khahar"

                # Check Khahar Zade Or Baradar Zadeh
                for j in childs :
                    temp = self.get_children(j)
                    if id1 in temp:
                        if self.get_gender(j) == "0":
                            return "Khahar Zadeh"
                        return "Baradar Zadeh"
                
                # Check Amme ya Amo
                temp = self.get_prson_by_id(i['father_id'])
                childs = self.get_children(temp['father_id'])
                if id1 in childs :
                    if self.get_gender(id1) == "0":
                        return "Amme"
                    return "Amo"
                
                # Check Zan Daii ya Shohar Khale
                for j in childs :
                    temp = self.get_spouse(j)
                    if id1 in temp:
                        if self.get_gender(id1) == "0" :
                            return "Zan Amo"
                        return "Shohar Amme"  

                # Check Pesar Amme ya Dokhtar Amme ya Pesar Amo ya Dokhtar Amo
                for child in childs :
                    temp = self.get_children(child)
                    if id1 in temp :
                        if self.get_gender(child) == "0":
                            if self.get_gender(id1) == "0" :
                                return "Dokhtar Amme"
                            return "Pesar Amme"
                        else:
                            if self.get_gender(id1) == "0" :
                                return "Dokhtar Amo"
                            return "Pesar Amo"
                
                # Check Khale ya Daii
                temp = self.get_prson_by_id(i['mother_id'])
                childs = self.get_children(temp['father_id'])
                if id1 in childs :
                    if self.get_gender(id1) == "0":
                        return "Khale"
                    return "Daii"

                # Check Zan Daii ya Shohar khale
                for j in childs :
                    temp = self.get_spouse(j)
                    if id1 in temp:
                        if self.get_gender(id1) == "0" :
                            return "Zan Daii"
                        return "Shohar Khale"

                # Check Pesar Khale ya Dokhtar Khale ya Pesar Daii ya Dokhtar Daii
                for child in childs :
                    temp = self.get_children(child)
                    if id1 in temp :
                        if self.get_gender(child) == "0":
                            if self.get_gender(id1) == "0" :
                                return "Dokhtar Khale"
                            return "Pesar Khale"
                        else:
                            if self.get_gender(id1) == "0" :
                                return "Dokhtar Daii"
                            return "Pesar Daii"
                
                # Check Pedar Zan ya Madar Zan ya Khahar Zan ya Bradar Zan
                spouse = i['spouse']
                for j in spouse :
                    temp = self.get_prson_by_id(j)
                    if id1 == temp['father_id']:
                        return "Pedar Zan"
                    if id1 == temp['mother_id'] :
                        return "Madar Zan"
                    child = self.get_children(temp['father_id'])
                    if id1 in child :
                        if self.get_gender(id1) == "0" :
                            return "Khahar Zan"
                        return "Baradar Zan"
                
                


name = ["Reza","Zahra","Fahimeh","Fatemeh","Mehrdad","Zohreh"]
family = ["Fallah","Ramezani","Fallah","Fallah","PourHasan","PourHassan"]
id=["1234","2345","3456","4567","5678","6789"]
gender = ["1","0","0","0","1","0"]
spouse = [["2345"],["1234"],["5678"],[" "],["3456"],[" "]]
children = [["3456","4567"],["3456","4567"],["6789"],[" "],["6789"],[" "]]
mother_id = [" "," ","2345","2345"," ","3456"]
father_id = [" "," ","1234","1234"," ","5678"]
FT = family_tree()
for i in range(len(name)):
    dict = {
        'name' : name[i],
        'family' : family[i],
        'id' : id[i],
        'gender' : gender[i],
        'spouse' : spouse[i],
        'children' : children[i] ,
        'mother_id' : mother_id[i],
        'father_id' : father_id[i]
        }
    FT.add_new_person(dict)
id1 = input(" id Nafar Aval : ")
id2 = input(" id Nafar Dovom : ")

print(FT.check_relationship(id1,id2))



                
                