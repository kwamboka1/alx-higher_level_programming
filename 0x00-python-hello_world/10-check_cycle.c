#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has
 * a cycle in it
 * @list: pointer to the list
 * Return: 0 if there is no cycle,
 * 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *head;
	listint_t *first;

	if(list == NULL)
		return(0);
	head = list;
	first = head->next;

	if (first == NULL)
		return(0);

	while(1)
	{

		if(first == head)
			return(1);

		first = first->next;/* 1st node */
		if (first == NULL)
			return(0);

		first = first->next;/*2nd node*/

		if (first == NULL)
			return(0);

		head = head->next;/*3rd node*/
		if (head == NULL)
			return(0);
	}
}
