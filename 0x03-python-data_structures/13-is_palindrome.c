#include "lists.h"
#include <stdio.h>
/**
 * is_palindrome - program check if singly linked list is palindrome
 * @head: list to check
 *
 * Return: 1 if true
 * 0 if false or empty list
 */

int is_palindrome(listint_t **head)
{
	listint_t *current = *head;
	listint_t *reverse_list = NULL;
	listint_t *next = NULL;

	if (!head || !*head)
		return (0);
	else if (*head == NULL)
		return (1);

	while (current)
	{
		next = current->next;
		current->next = reverse_list;
		reverse_list = current;
		current = next;
	}

	current = *head;

	while (current != NULL && *head != NULL)
	{
		if (current->n != reverse_list->n)
			return (0);

		current = current->next;
		*head = (*head)->next;
	}

	return (1);
}
