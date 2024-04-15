#include <stdio.h>
#include <string.h>

typedef struct{
	char name[10];
	int age;
} Person;

main(){
	Person p;

	/* I cheated here to make changing the age variable easier
	 by declaring p.name here, before p.age, the address of p.name
	will be higher (lower memory address) on the stack. A long array 
	of chars entered by the user will easily overlap the address
	where p.age is stored */

	p.name;
	printf("Enter your name (Max 10 characters): ");
	p.age = 0;
	gets(p.name);
		
	printf("%s%s%s%i\n", "Thank you " , p.name , "! Age: " , p.age); 
}
