#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    string str;
    cout << "Ingresa una cadena: ";
    cin >> str;

    string rev = str;
    reverse(rev.begin(), rev.end());

    if (str == rev)
        cout << "Es un palindromo" << endl;
    else
        cout << "No es un palindromo" << endl;

    return 0;
}
