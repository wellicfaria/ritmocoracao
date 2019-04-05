
from sound import getSoundOfaHistoy
from playsound import playsound
import _thread

'''
    FUNCOES PARA TOCAR OS SOM
'''


def playOneSound(code_hist,cod_sound):
    '''
        Funcao para execuçao do som. Espera finalizar o som para depois começar outro.

        Entrada:
            - code_hist: Codigo da Historia
            - cod_sound: Codigo do Som
    '''
    sound = getSoundOfaHistoy(code_hist,cod_sound)
    print('-> [PLAY SOUND] '+str(sound))
    playsound(sound['path'])


def playTogetherSound(code_hist,cod_sound):
    '''
        Funcao para execuçao do som. Pode executar varios som simultaneos, usando thread.

        Entrada:
            - code_hist: Codigo da Historia
            - cod_sound: Codigo do Som
    '''

    _thread.start_new_thread( playOneSound, (code_hist,cod_sound, ) )
