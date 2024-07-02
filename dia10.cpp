#include <iostream>
#include <algorithm> // Incluye la función sort
using namespace std;

int main() {
    int arr[] = {64, 25, 12, 22, 11};
    int n = sizeof(arr) / sizeof(arr[0]);

    // Imprime el array original
    cout << "Array original: ";
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;

    // Ordena el array
    sort(arr, arr + n);

    // Imprime el array ordenado
    cout << "Array ordenado: ";
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;

    return 0;
}
