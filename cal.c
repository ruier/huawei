//#include "stdafx.h"
#include "stdio.h"
#include "string.h"
#include "conio.h"

// 函数原型声明
int add(int x,int y){return x+y;}
int sub(int x,int y){return x-y;}
int mul(int x,int y){return x*y;}
int div(int x,int y){return x/y;}
int (*func[])(int x, int y) = {add,sub,mul,div};

// 全局数据定义
int num,curch;
char chtbl[] = "+-*/()=";
char corch[] = "+-*/()=0123456789";

// 函数定义
int getach()
{
  int i;
  while(1)
  {
     curch=getchar();
     if(curch == EOF)
	return -1;

     for(i=0; corch[i] && curch != corch[i];i++);
	if(i < strlen(corch))
	  break;
  }
     return curch;
}

int getid()
{
   int i;

   if(curch>= '0'&& curch <= '9')
   {
       for(num = 0;curch >= '0' && curch <= '9'; getach())
       num=10*num+(curch-'0');
	  return -1;
   }
   else
   {
       for(i=0;chtbl[i];i++)
         if(chtbl[i]==curch) break;

       if(i<=5) getach();
         return i;
   }
}

int cal()
{
	int x1,x2,x3,op1,op2,i;

	i = getid();
	if(i == 4)
	{
          x1 = cal();
	}
	else
	  x1 = num;

	op1 = getid();
	if(op1 >= 5)
	  return x1;

	i = getid();
	if(i == 4)
	{
	  x2 = cal();
	}
	else
	  x2 = num;

	op2=getid();
	while(op2!=6 && op2!= 5)
	{
          i = getid();
	  if(i == 4)
	  {
	    x3 = cal();
	  }
	  else
	    x3=num;

	 if( (op1/2 == 0) && (op2/2 == 1) )
	     x2 = (*func[op2])(x2,x3);
	 else
	 {
	   x1=(*func[op1])(x1,x2);
			x2=x3;
			op1=op2;
		}
		op2=getid();
	}
	return (*func[op1])(x1,x2);
}

int main(int argc, char* argv[])
{
   int value;
   printf("Please input an expression:\n");
   curch = getch();
   while(curch != '=')
   {
      value = cal();
      printf("The result is : %d\n",value);
      printf("Please input an expression:\n");
      curch = getach();
   }
   return 0;
}


