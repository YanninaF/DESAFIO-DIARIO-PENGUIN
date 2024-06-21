
#include <iostream>
using namespace std;
int main(){
    int num1, num2; // declara 2 variables
    cout << "INGRESA EL PRIMER NUMERO: "; //ingresa el primer numero
    cin >> num1; // primer numero ingresado
    cout << "INGRESA EL SEGUNDO NUMERO: "; //ingresa el segundo numero
    cin >> num2; // segundo numero ingresado
    int suma = num1 + num2; //suma de los 2 numeros
    cout << "EL RESULTADO ES: " << suma; // se muestra el resultado

    return 0; // retorna cero o indica que el programa finalizo correctamente
}