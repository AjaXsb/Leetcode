int mid;
int start=0,end=size(nums)-1;

	while (start<=end)
		{
			mid=(start+end)/2;
			if (nums[mid]==target)
			{
				return mid;
			}
			else if (nums[mid]>target)
			{
				end=mid-1;
			}
			else 
			{
				start=mid+1;
			}
				
			cout<<nums[0];
		
			}
			
			return -1;
        
    		}
};