#include "lists.h"
/**
 * is_palindrome - program check if singly linked list is palindrome
 * @head: list to check
 *
 * Return: 1 if true
 * 0 if false or empty list
 */

int is_palindrome(listint_t **head)
{
	unsigned int i, len = 0;
	int list_data[];

	if (!head || !*head)
		return (0);
	else if (*head == NULL)
		return (1);

	while (*head)
	{
		list_data[len] = head->p;
		*head = head->next;
		len++;
	}

	len = len + 1;

	for (i = 0; i < len; i++)
	{
		if (list_data[i] != list_data[len - i])
			return (0);
	}

	return (1);
}
