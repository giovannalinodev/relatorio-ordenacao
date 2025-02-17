#include "ordenacao.hpp"
#include <iostream>
#include <chrono>
#include <vector>

using namespace std;
using namespace chrono;

// Função para verificar se o array está ordenado
bool ordenado(int a[], unsigned int t) {
    for (unsigned int i = 1; i < t; i++) {
        if (a[i - 1] > a[i]) {
            return false;
        }
    }
    return true;
}

// Medir tempo de execução
void medir_tempo(void (*sort_func)(int[], unsigned int), int a[], unsigned int t, const string& nome_algoritmo) {
    auto inicio = high_resolution_clock::now();
    sort_func(a, t);
    auto fim = high_resolution_clock::now();
    duration<double> tempo = fim - inicio;
    cout << "Tempo de execucao de " << nome_algoritmo << ": " << tempo.count() << " segundos" << endl;
}

// Algoritmo de ordenação por seleção
void selecao(int a[], unsigned int t) {
    for (unsigned int i = 0; i < t - 1; i++) {
        unsigned int minIndex = i;
        for (unsigned int j = i + 1; j < t; j++) {
            if (a[j] < a[minIndex]) {
                minIndex = j;
            }
        }
        swap(a[i], a[minIndex]);
    }
}

// Algoritmo de ordenação por inserção
void insercao(int a[], unsigned int t) {
    for (unsigned int i = 1; i < t; i++) {
        int chave = a[i];
        int j = i - 1;
        while (j >= 0 && a[j] > chave) {
            a[j + 1] = a[j];
            j--;
        }
        a[j + 1] = chave;
    }
}

// Função auxiliar para mesclar dois subarrays
void merge(int a[], int left, int mid, int right) {
    int n1 = mid - left + 1;
    int n2 = right - mid;
    
    vector<int> L(n1), R(n2);
    for (int i = 0; i < n1; i++) L[i] = a[left + i];
    for (int i = 0; i < n2; i++) R[i] = a[mid + 1 + i];
    
    int i = 0, j = 0, k = left;
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) {
            a[k] = L[i];
            i++;
        } else {
            a[k] = R[j];
            j++;
        }
        k++;
    }
    while (i < n1) a[k++] = L[i++];
    while (j < n2) a[k++] = R[j++];
}

// Algoritmo de ordenação Merge Sort
void mergeSortRecursive(int a[], int left, int right) {
    if (left < right) {
        int mid = left + (right - left) / 2;
        mergeSortRecursive(a, left, mid);
        mergeSortRecursive(a, mid + 1, right);
        merge(a, left, mid, right);
    }
}

void merge_sort(int a[], unsigned int t) {
    if (t > 1) {
        mergeSortRecursive(a, 0, t - 1);
    }
}
