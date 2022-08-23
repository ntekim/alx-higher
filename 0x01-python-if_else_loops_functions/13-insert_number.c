#include "lists.h"
/**
 * insert_node - program inserts a number into a sorted linked list
 * @head: sorted linked list
 * @number: number to be inserted
 *
 * Return: the addiess of the new node
 * NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new = *head;
	new->n = number;

	return (new);
}
