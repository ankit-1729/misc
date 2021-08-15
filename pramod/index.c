/*=========================================================================*/
// * Program Description : Program for Database Manipulation
// * Author  	     :
// * Class 	     : SE (EnTC)
// * Roll no. 	     :
// * Date	     :
/*=========================================================================*/
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

//function definations
void create();
void display();
void search();
void modify();
void append();
void sort();
void del();

//structure declaration

typedef struct emp
{
  char name[10];
  int salary;
  int id;
} EMP;

EMP e[10];
int n;
//===============main function==========
int main(void)
{
  int i, ch;
  // clrscr();

  while (1)
  {
    printf("\n Enter the choice\n");
    printf("\n1:Create\n2:Display\n3:Search\n4:Modify\n5:Append\n6:Sort\n7:delete\n8:Exit\n");
    scanf("%d", &ch);
    switch (ch)
    {
    //taking choice from user
    case 1:
      create();
      break;
    case 2:
      display();
      break;
    case 3:
      search();
      break;
    case 4:
      modify();
      break;
    case 5:
      append();
      break;
    case 6:
      sort();
      break;
    case 7:
      del();
      break;
    default:
      exit(0);
    }
  }
  // getch();

} //end of main

//function to create the database
void create()
{
  int i;
  printf("\n Enter the no. of employees record");
  scanf("%d", &n);
  for (i = 0; i < n; i++)
  {
    printf("\n Enter the name of the employ\n");
    scanf("%s", e[i].name);
    printf("Enter the salary of the employ\n");
    scanf("%d", &e[i].salary);
    printf("Enter the id of the employ\n");
    scanf("%d", &e[i].id);
  }
}

// function to display the database
void display()
{
  int i;
  if (n == 0)
    printf("\n Database is empty.\n");
  else
  {
    printf("\n===================================================================");
    printf("\n Employ_name\t Employ_salary\t Employ_id\n");
    printf("\n===================================================================");
    for (i = 0; i < n; i++)
    {
      printf("\n%10s", e[i].name);
      printf("\t\t%.d", e[i].salary);
      printf("\t\t%3d\n", e[i].id);
    }
    printf("\n===================================================================");
  }
}

//function to search info of an employee

void search()
{
  int flag = 0, id, i;
  if (n == 0)
  {
    printf("\n Database is empty.");
  }
  else
  {
    printf("\n Enter the employ_id to be searched");
    scanf("%d", &id);
    for (i = 0; i < n; i++)
    {
      if (e[i].id == id)
      {
        printf("\n RECORD FOUND");
        //	pos=i;
        flag = 1;
        //	display();
        printf("\n===================================================================");
        printf("\n Employ_name\t Employ_salary\t Employ_id\n");
        printf("\n===================================================================");
        printf("\n%10s", e[id].name);
        printf("\t\t%.d", e[id].salary);
        printf("\t\t%3d\n", e[id].id);

        printf("\n===================================================================");
      }
    }
    if (flag == 0)
      printf("\n No similar id found\n");
  }
}

//function to modify the employee database

void modify()
{
  int rec, id;
  int salary;
  char name[10];
  if (n == 0)
  {
    printf("\n Database is empty.\n");
  }
  else
  {
    printf("\n Enter the no. of records to modify\n");
    scanf("%d", &rec);
    printf("\n Enter the employ name");
    scanf("%s", e[rec].name);
    printf("\n Enter the employ salary");
    scanf("%d", &e[rec].salary);
    printf("\nEnter new id");
    scanf("%d", &e[rec].id);
    display();
  }
}
//function to append the database

void append()
{
  int rec, m, i;
  printf("\n Enter the no. of records to be appended");
  scanf("%d", &rec);
  m = n + rec;
  for (i = n; i < m; i++)
  {
    printf("\n Enter the employ name");
    scanf("%s", e[i].name);
    printf("\n Enter the employ salary");
    scanf("%d", &e[i].salary);
    printf("\n Enter the employ id");
    scanf("%d", &e[i].id);
  }
  n = m;
  display();
}

void del()
{
  int rec, m, i;
  printf("\n Enter the  record no. to be deleted");
  scanf("%d", &rec);

  strcpy(e[rec].name, "---");
  e[i].salary = 0;

  e[i].id = 0;

  display();
}

//function to sort the records
void sort(void)
{
  int i, j;
  EMP temp;
  for (i = 0; i < n; i++)
  {
    for (j = 0; j < n - i - 1; j++)
    {
      if (e[j].id < e[j + 1].id)
      {
        temp = e[j + 1];
        e[j + 1] = e[j];
        e[j] = temp;
      }
    }
  }
  printf("\n Sorted database is :\n\n");
  display();
}

//======================end of progarm======================
