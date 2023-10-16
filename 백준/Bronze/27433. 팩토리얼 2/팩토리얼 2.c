#include<stdio.h>

long long int recursive(int n)
{
	if (n==0)
	{
		return 1;
	}
	else
	{
		return n* recursive(n - 1);
		
	}
}

int main()
{
	long long int n;
	scanf("%lld", &n);
	printf("%lld",recursive(n));
	return 0;
}




