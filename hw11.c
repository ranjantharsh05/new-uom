#include <stdio.h>
int main() {
 int size = 6;
 for (int row = 0; row < size; row++) {
 for (int col = 0; col < size; col++) {
 if (row == 0 || row == size-1 || col == 0 || col == size-1)
 printf("* ");
 else
 printf(" ");
 }
 printf("\n");
 }
 return 0;
}