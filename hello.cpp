#include <iostream>
using namespace std;
int main()
{
  int i = 1;

increment:
  if (i <= 10)
  {
    cout << i << endl; // 1 2 3 4 5 6 7 8 9 10
    i++;
    goto increment;
  }
  return 0;
}