#include<iostream>
using namespace std;

int main()
{
	int x,y,z;
	
	cout<<"Enter a Number"<<endl;
	cin>>x;
	
	while (x!=0)
	{
		y=x%10;
		z+=y;
		x=x/10;
	}
	
	cout<<"Additive Persistence is:"<<z;
	
	return (0);
}
