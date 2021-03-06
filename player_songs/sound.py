
import glob

def  getAllHistory():
    '''

        Funcao que retorna um lista com todas as historias contidas
        na pasta sounds_history.
        A lista conta com dicionarios contendo:

         - code_hist: Codigo da historia
         - name_hist: Titulo da Historia
         - dir_hist: Diretorio onde contem os soms da historia
    '''
    resp = []
    for r in glob.glob("../sounds_history/*"):
        aux = {}
        folder_hist = r.replace('../sounds_history\\','')
        hist = folder_hist.split('_')
        aux['code_hist'] = hist[0]
        aux['name_hist'] = hist[1]
        aux['dir_hist'] = folder_hist
        resp.append(aux)
    return resp


def getSoundsHistoy(code_hist):
    '''

        Funcao que retorna um dicionario contendo as informacoes de uma historia e seus soms:

        Entrada:

            - code_hist: Codigo da historia

        Saida:
            Dicionario contendo:

             - code_hist: Codigo da historia
             - name_hist: Titulo da Historia
             - dir_hist: Diretorio onde contem os soms da historia
             - sounds : Lista contendo dicionario com informações do som
                            - name_sound: Nome do Som
                            - cod_sound: Codigo do Som
    '''
    list_hist = getAllHistory()
    hist = [x for x in list_hist if x['code_hist'] == str(code_hist)][0]
    hist['sounds'] = []
    for r in glob.glob("../sounds_history/{}/*".format(hist['dir_hist'])):
        aux = {}
        aux['name_sound'] = r.split('\\')[1]
        aux['cod_sound'] = aux['name_sound'].split('_')[0]
        hist['sounds'].append(aux)
    return hist

def getAllHistoryAndAllSounds():
    '''

        Funcao que retorna um lista contendo as informacoes de todas historia e seus soms:


        Saida:
            Lista contendo dicionario:
                 - code_hist: Codigo da historia
                 - name_hist: Titulo da Historia
                 - dir_hist: Diretorio onde contem os soms da historia
                 - sounds : Lista contendo dicionario com informações do som
                                - name_sound: Nome do Som
                                - cod_sound: Codigo do Som
    '''
    resp = []
    for h in getAllHistory():
        resp.append(getSoundsHistoy(h['code_hist']))
    return resp

