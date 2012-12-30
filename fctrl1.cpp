#include<stdio.h>

int main()
{
    int n;
    scanf("%d",&n);
    while(n--)
    {
        long long in;
        scanf("%lld",&in);
        long long solu=0;
        while(in)
        {
            in = in/5;
            solu+=in;
        }
        printf("%lld\n",solu);
    }

    return 0;
}
