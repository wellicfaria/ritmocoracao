import pygame
import glob


def _getPathSound(folder, name_sound):
    '''
        Funcao para montar o caminho para acessar o som.
        Entrada:
            - folder : Diretorio localizado o Audio
            - name_sound : Nome do som com a extensao

        Saida:
            String contendo o caminho do som
    '''
    path_sounds = '../sounds_history'
    path_sound = '{}/{}/{}'.format(path_sounds, folder, name_sound)
    return path_sound


def getDurationSound(path_sound):
    '''
        Funcao para retornar o duracao em segundos do som.

        Entrada:
            - path_sound: String contendo o caminho do som

        Saida:
            Inteiro contendo a quantidade em segundo da duracação do Som.
    '''

    pygame.mixer.init()
    durantionSeconds = round(pygame.mixer.Sound(path_sound).get_length())

    return durantionSeconds

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
             - sounds : Lista contendo dicionario com informacoes do som
                            - name_sound: Nome do Som
                            - cod_sound: Codigo do Som
                            - folder: Diretorio que esta Localidado o som
                            - code_hist: Codigo da Historia que som pertence
                            - path: Caminho completo para o som
                            - duration : Duracao em segundos do som
    '''
    list_hist = getAllHistory()
    hist = [x for x in list_hist if x['code_hist'] == str(code_hist)][0]
    hist['sounds'] = []
    for r in glob.glob("../sounds_history/{}/*".format(hist['dir_hist'])):

        aux = {}
        aux['name_sound'] = r.split('\\')[1]
        aux['cod_sound'] = aux['name_sound'].split('_')[0]
        aux['folder'] = hist['dir_hist']
        aux['code_hist'] = hist['code_hist']
        aux['path'] = _getPathSound(aux['folder'],aux['name_sound'])
        aux['duration'] = getDurationSound(aux['path'])

        hist['sounds'].append(aux)

    return hist

def getSoundOfaHistoy(code_hist,cod_sound):
    '''

        Funcao que retorna um dicionario contendo as informacoes do som e de uma historia:

        Entrada:

            - code_hist: Codigo da historia
            - cod_sound: Codigo do som

        Saida:
            Dicionario contendo:

                - name_sound: Nome do Som
                - cod_sound: Codigo do Som
                - folder: Diretorio que esta Localidado o som
                - code_hist: Codigo da Historia que som pertence
                - path: Caminho completo para o som
                - duration : Duracao em segundos do som
    '''
    list_sounds = getSoundsHistoy(code_hist)

    sound = [x for x in list_sounds['sounds'] if x['cod_sound'] == str(cod_sound)][0]


    return sound

def getAllHistoryAndAllSounds():
    '''

        Funcao que retorna um lista contendo as informacoes de todas historia e seus soms:


        Saida:
            Lista contendo dicionario:
                 - code_hist: Codigo da historia
                 - name_hist: Titulo da Historia
                 - dir_hist: Diretorio onde contem os soms da historia
                 - sounds : Lista contendo dicionario com informacoes do som
                            - name_sound: Nome do Som
                            - cod_sound: Codigo do Som
                            - folder: Diretorio que esta Localidado o som
                            - code_hist: Codigo da Historia que som pertence
                            - path: Caminho completo para o som
                            - duration : Duracao em segundos do som
    '''
    resp = []
    for h in getAllHistory():
        resp.append(getSoundsHistoy(h['code_hist']))
    return resp
