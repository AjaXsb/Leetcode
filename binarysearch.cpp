#include<iostream>

using namespace std;

class getnums
{
	public:
	int x,i,y;
	int nums[100];
	
	
	void getarrn()
	{	
		cout<<"Enter No. of elements in the array(less than 100) :"<<endl;
	    cin>>x;	
	}

	
	
	void getarre()
	{
		cout<<"Enter array elements :"<<endl;
		for (i=0;i<x;i++)
	        {
				cin>>nums[i];
			}
		
	}

	void gettarget()
	{
		cout<<"Enter target no. :"<<endl;
		cin>>y;
	}
	
	void showarre()
	{
		for (i=0;i<x;i++)
		{
			cout<<nums[i]<<endl;
		}
	}
	
	void showtarget()
	{
		cout<<"Target is "<<y<<endl;
	}

};

class check1 : public getnums
{
	public:
		
		
		int mid;
		
		int check()
		{
			int start=0,end=x-1;
			//cout<<start<<" "<<nums[end]<< " "<<end<<" "<<y<<endl;
			while (start<=end)
			{
				mid=(start+end)/2;
				if (nums[mid]==y)
				{
					return mid;
				}
				else if (nums[mid]>y)
				{
					end=mid-1;
				}
				else 
				{
					start=mid+1;
				}
				
			}
			
			return -1;
		}
	};
	
int main ()
{
	check1 f;
	f.getarrn();
	f.getarre();
	f.gettarget();
	
	f.showtarget();
	cout<<"Target is at position :"<<f.check();
	return 0;
}
			
	
	
		
	
