#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * infinite_while - creates an infinite loop that leaves
 * program process hanging
 * Return: always 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - creates 5 zombie processes
 * Return: always 0
 */
int main(void)
{
	int z;
	pid_t zombie_process;

	for (z = 0; z < 5; z++)
	{
		zombie_process = fork();
		if (!zombie_process)
			return (0);
		printf("Zombie process created, PID: %d\n", zombie_process);
	}

	infinite_while();
	return (0);
}
