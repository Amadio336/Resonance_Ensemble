import requests
import json
import spacy
import unicodedata


""" PIPELINE

variables:
- content -> str, it contains the greek text to analyze
- final_path_MJ -> str, it contains a path where the f saves the morpheus results individuated as major conflicts
- final_patn_mc -> str, in contains the path where the f saves the moprheus results individuates as minor conflicts 
- MJ_C -> list, it contains the morpheus major conflicts
- mc -> list, it contains the morpheus minor conflicts

"""


# try if Morpheus API works
try_url = "http://services.perseids.org/bsp/morphologyservice/analysis/word?lang=grc&engine=morpheusgrc&word=ἱστορίης"
def verify_operability(url):
    try:
        response = requests.get(url)
        return response.status_code
    except Exception as e: raise e

print(verify_operability(try_url))

"""τοὐμὸν παρώσας δεσπότης δοῦλον λέχος κακοῖς πρὸς αὐτῆς σχετλίοις ἐλαύνομαι λέγει γὰρ ὥς νιν φαρμάκοις κεκρυμμένοις ἄπαιδα καὶ πόσει μισουμένην αὐτὴ δὲ ναίειν οἶκον αὐτῆς θέλω ἐκβαλοῦσα λέκτρα τἀκείνης βίᾳ ἁγὼ τὸ πρῶτον οὐχ ἐδεξάμην νῦν ἐκλέλοιπα Ζεὺς εἰδείη μέγας ὡς οὐχ ἑκοῦσα ἐκοινώθην λέχει οὔ σφε πείθω βούλεται δέ με κτανεῖν πατήρ τε θυγατρὶ Μενέλεως συνδρᾷ τάδε καὶ νῦν οἴκους ἀπὸ Σπάρτης μολὼν αὐτὸ τοῦτο δειματουμένη ἐγὼ δόμων πάροικον Θέτιδος εἰς ἀνάκτορον θάσσω ἤν με κωλύσῃ θανεῖν Πηλεύς τε γάρ νιν ἔκγονοί τε Πηλέως σέβουσιν ἑρμήνευμα Νηρῇδος γάμων"""




# TODO: when you give text with punctuaction, it fails. You get index error 
content = """τοὐμὸν παρώσας δεσπότης δοῦλον λέχος κακοῖς πρὸς αὐτῆς σχετλίοις ἐλαύνομαι λέγει γὰρ"""
final_path_MJ = "MJ_C.json"
final_path_mc = "mc.json"
MJ_C = []
mc = []

def req_morpheus_Api(content) -> list[list]: # for now, it returns only words_w_MJ.
    """ it makes the request to Morpheus API and saves in two different lists the words with major conflicts and minor conflicts"""
    
    save_json_option = input("Do you want to save the results from Morpheus in a json file? [yes o leave empty]:  ")
    
    content_splitted = content.split()
    words_w_MJ = []
    words_w_m = []
       
    try: 
        for word in content_splitted:
            print(word)
            new_url = f"http://services.perseids.org/bsp/morphologyservice/analysis/word?lang=grc&engine=morpheusgrc&word={word}"
            response = requests.get(new_url)

            data = response.json()
            if isinstance(data["RDF"]["Annotation"]["Body"], list):
                MJ_C.append(data)
                words_w_MJ.append(unicodedata.normalize("NFC", data["RDF"]["Annotation"]["hasTarget"]["Description"]["about"].replace("urn:word:", "")))
            elif isinstance(data["RDF"]["Annotation"]["Body"]["rest"]["entry"]["infl"], list):
                mc.append(data)
        print("acquiring data from Morpheus API succesfully done")    
            
            #retrieval.append(data)
    except Exception as e: raise e

    """ save the two lists in json file format """
    if save_json_option:
        with open(final_path_MJ, "wt", encoding="utf8") as file1:
            json.dump(MJ_C, file1, ensure_ascii=False, indent=4)
    
        with open(final_path_mc, "wt", encoding="utf8") as file2:
            json.dump(mc, file2, ensure_ascii=False, indent=4)
    
    return words_w_MJ
    





def show_better_format(mjc, mc):
    """ it shows the contents of MJ_C e mc in a better format:
    For major conflict:
    {word: [poss1, poss2]}
    

    For minor conflict (if word is name)
    {word: [[category, case], [cateogry, case]]}
    """

    """ it provides the user with choosing to see only major conflicts or minor conflict or both """
    option2 = input("Do you want to see all the conflict? if yes: yes, if only majors conflict: mj, if only minor conflict, m:  ")
    
    def show_mj_conflict():
        possibilities = {}
        for el in mjc:
            possibilities[el["RDF"]["Annotation"]["hasTarget"]["Description"]["about"]] =  []
            for poss in el["RDF"]["Annotation"]["Body"]:
                possibilities[el["RDF"]["Annotation"]["hasTarget"]["Description"]["about"]].append(poss["rest"]["entry"]["dict"]["hdwd"]["$"])
        return possibilities
    
    def show_m_conflict():
        possibilities = {}
        for el in mc:
            possibilities[el["RDF"]["Annotation"]["hasTarget"]["Description"]["about"]] =  []
            for poss in el["RDF"]["Annotation"]["Body"]["rest"]["entry"]["infl"]:
                possibilities[el["RDF"]["Annotation"]["hasTarget"]["Description"]["about"]].append([poss["pofs"]["$"], poss["case"]["$"]])
        return possibilities




    if option2 == "mj":
        return show_mj_conflict()
    elif option2 == "m":
        return show_m_conflict()
    elif option2 == "yes":
        raise NotImplementedError

       




def create_models_opinions_for_MJ(words_w_MJ : list, model : str):
    """ it takes all the greek text provided and the name of the model used as string. It returns a list(tuple(word, lemma)) like this:
    [('ὦ', 'ὦ'), ...] where the first element of the tuple is the word, the second element is the subvoce of that word
    In this list there must be only the words with major conflicts
     """
    
    print("Using the model: ", model)
    try:
        nlp = spacy.load(model)

        guidelines = []

        doc = nlp(content)
        for index,token in enumerate(doc):
            print(token.orth_)
            if token.orth_ == " ": continue
            
        
            if unicodedata.normalize("NFC", token.orth_) in words_w_MJ:
                if unicodedata.normalize("NFC", token.lemma_) == unicodedata.normalize("NFC", "λέγω"):
                    guidelines.append((token.orth_, unicodedata.normalize("NFC", "λέγω3")))
                else:
                    guidelines.append((token.orth_, token.lemma_))
        

        return guidelines
    
    except OSError as e:
        print(f"{model} model not found. More detail about error: {e}. You can see the file models_requirements.md > problem 1 ")


def create_RCompliant_obj(mjc : list[dict], mc : None, guidelines : list[tuple]):
    """ it creates the Resonance-compliant obj. TODO: !! for now it creates only obj for major conflict """
    print(f"lenght major conflit: {len(mjc)}")
    print(f"lenght guidelines: {len(guidelines)}")
    assert len(guidelines) == len(mjc), "different numbers between guidlines and major conflicts"
    
    results = []
    for i, el in enumerate(mjc):
        obj = {}
        for poss in el["RDF"]["Annotation"]["Body"]:
            if unicodedata.normalize("NFC", poss["rest"]["entry"]["dict"]["hdwd"]["$"]) == unicodedata.normalize("NFC", guidelines[i][1]):
                obj["SubVoce"] = poss["rest"]["entry"]["dict"]["hdwd"]["$"]
                obj["category"] = poss["rest"]["entry"]["dict"]["pofs"]["$"]


                if unicodedata.normalize("NFC", poss["rest"]["entry"]["dict"]["pofs"]["$"]) == "noun" and isinstance(poss["rest"]["entry"]["infl"], dict):
                    """ this condition is True when che category of the word is "noun" and when the word is not a minor conflict (that is, when infl has as value a dict and not a list) """

                    obj["decl"] = poss["rest"]["entry"]["infl"]["decl"]["$"]
                    obj["case"] =  poss["rest"]["entry"]["infl"]["case"]["$"]
                    obj["num"] =  poss["rest"]["entry"]["infl"]["num"]["$"]
                    obj["gend"] =  poss["rest"]["entry"]["infl"]["gend"]["$"]

                elif unicodedata.normalize("NFC", poss["rest"]["entry"]["dict"]["pofs"]["$"]) == "verb" and isinstance(poss["rest"]["entry"]["infl"], dict):

                    pass

                break
        results.append(obj)
    
    with open("Res-compliant_json_prova.json", "wt", encoding="utf8") as file3:
        json.dump(results, file3, ensure_ascii=False, indent=4)

    return results
        




model_trf = 'grc_odycy_joint_trf'
model_sm = 'grc_odycy_joint_sm'




words_w_MJ = req_morpheus_Api(content)
guidelines = create_models_opinions_for_MJ(words_w_MJ, model_sm)

print("-" *50)
print()

print(show_better_format(MJ_C, None))
print("-" *50)
print()

print(words_w_MJ)

print("-" *50)
print()

print(guidelines) 

print("-" *50)
print()

print(create_RCompliant_obj(MJ_C, None, guidelines))











