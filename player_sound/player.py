
from sound import getSoundOfaHistoy
from playsound import playsound
import _thread


def playOneSound(code_hist,cod_sound):
    '''
        Funcao para execuçao do som. Espera finalizar o som para depois começar outro.

        Entrada:
            - code_hist: Codigo da Historia
            - cod_sound: Codigo do Som
    '''

    path_sounds = '../sounds_history'
    sound = getSoundOfaHistoy(code_hist,cod_sound)
    path_sound = '{}/{}/{}'.format(path_sounds,sound['folder'],sound['name_sound'])
    playsound(path_sound)


def playTogetherSound(code_hist,cod_sound):
    '''
        Funcao para execuçao do som. Pode executar varios som simultaneos, usando thread.

        Entrada:
            - code_hist: Codigo da Historia
            - cod_sound: Codigo do Som
    '''

    _thread.start_new_thread( playOneSound, (code_hist,cod_sound, ) )

