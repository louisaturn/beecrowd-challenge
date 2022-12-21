// Solution of: https://www.beecrowd.com.br/judge/problems/view/1006 Language: C++

#include <iostream>
#include <iomanip>   
 
using namespace std;
 
int main() {
    double A, B, C;
    cin >> A >> B >> C;

    double MEDIA = (A*2.0 + B*3.0 + C*5.0)/10.0;
    
    cout << fixed << setprecision(1) << "MEDIA = " << MEDIA << endl;
 
    return 0;
}