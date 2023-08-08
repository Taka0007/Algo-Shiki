#include <bits/stdc++.h>
using namespace std;
int main() {
	int N;
    cin>>N;
    float answer;
    vector<int> A(N);
    for(int i=0; i<N; ++i){
        cin>>A[i];
    }
    sort(A.begin(),A.end());
    if(N%2==1){
        answer = A[(N-1)/2];
    }
    else{
        answer = (A[(N/2)-1]+A[N/2])/2.0;
    }
    cout<<answer<<endl;
	return 0;
}