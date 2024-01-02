#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"
/**
 * check_cycle - check list
 * @list: list
 * Return: 1 or  0.
 */
int check_cycle(listint_t *list)
{
	listint_t *i;
	listint_t *j;

	i = list;
	j = list;
	if (list == NULL)
	{
		return (0);
	}
	j = j->next;
	while (j != NULL && j->next != NULL && i != NULL)
	{
		if (i == j)
		{
			return (1);
		}
		i = i->next;
		j = j->next->next;
	}
	return (0);
}
