from compiler import parser
from compiler import scanner

testScript = '''
    programa patito; 
    var
    int id1, id2, id3, a, b, c, i ;
    float flo;
    char letra;
    funcion void prueba(int y, float x)
    var 
        int i, a, b, j;
    {
        i = j + i;
        si ( a > b ) entonces {
            a = a+1;
            b = (10 + 15) * 7;
            
        } sino {
            b = 1 +1;
        }
    }
    funcion int patito(int x1, int f, char s)
    var
        float x;
        int y;
        char e;
    {
        x = 1 + 1;
        y = patito(1,2,'s');
        return(y + 12 * 5);
        e = 'E' ;
        e = 'S';
        
    }
    principal(){
        id1 = patito(3 + id1, 5 * id2 + id1 , 'e') * 5;
        si ( id1 >= id2) entonces {
            a = a+1;
            b = (10 + 15) * 7;
        } sino {
            b = 1 +1;
        }
        a =  b = 1 + id2 * (10 * (id1 + 55)) * id3;
        mientras (a > b) haz{
            a = a + 1;
        }
        mientras ( c > a) haz{
            a = 2 + 1;
        }
        a = 2;
        desde i = 0 hasta 9 hacer{
            a = 10;
        }
        a = i + 1;
        a = 12;
        lee(id1);
        escribe(id2);
    }
'''

parser.parse(testScript)