importar  os
from  flask  import  Flask , jsonify , request
de  matemática  import  sqrt

app  =  Flask ( __name__ )

@ app . rota ( '/' )
def  nao_entre_em_panico ():


    primos  =  "Tudo vai dar certo, caros alunos!"


    voltar  primos

if  __name__  ==  "__main__" :
    porta  =  int ( os . amb . get ( "PORT" , 5000 ))
    app . executar ( host = '0.0.0.0' , porta = porta )
