#include <iostream>
#include <ctime>
#include <iomanip>
#include <vector>
using namespace std;

//recursive fibonacci function
int FiboR(int value);
//non-recursive fibonacci function
int FiboNR(int value);

int main() {
    //testing
    // cout << "recursive fibonacci: " << FiboR(10) << endl;
    // cout << "non-recursive fibonacci: " << FiboNR(10) << endl;

    //outputs
    cout << "Integer" << setw(30) << "FiboR (seconds)" << setw(30) << "FiboNR (seconds)"
        << setw(30) << "Fibo-value" << endl;
    cout << setfill('-') << setw(100) << ' ' << endl;

    //some values to test
    int values[] = {1,5,10,15,20,25,30,35,40,45,55,60};
    int fibval, fibRtime, fibNRtime;

    // loop
    for(int i=0; i < sizeof(values); i++)
    {
        //recursive time
        time_t start = time(0);
        fibval = FiboR(values[i]);
        fibRtime = time(0) - start;

        //non-recursive time
        start = time(0);
        FiboNR(values[i]);
        fibNRtime = time(0) - start;

        //output
            //outputs
        cout << values[i] << setw(30) << fibRtime << setw(30) << fibNRtime
        << setw(30) << fibval << endl;
    }
    
}   

// recursive
int FiboR(int value) {
    if(value == 0 || value == 1)
        return value;
    return(FiboR(value - 1) + FiboR(value -2));
}

//non-recursive
int FiboNR(int value) {
    //first 2 values of fibonacci
    vector<int> fibonacci;
    fibonacci.push_back(0);
    fibonacci.push_back(1);

    //loop until value
    for(int i = 2; i <= value; i++) {
        fibonacci.push_back(fibonacci[i-1] + fibonacci[i-2]);
    }

    return fibonacci.back();

}