/*
 * main.c
 *
 * Created: 08-Nov-16 15:42:35
 *  Author: Bas Haaksema
 */ 

#include "scheduler.h"
#include "tasks.h"

int main()
{
	// Prepares scheduler data structures and sets up timer interrupts at required rate.
	SCH_Init_T1();

	// Causes a task (function) to be executed at regular intervals or after a user-defined delay
	SCH_Add_Task(init, 0, 0);
	SCH_Add_Task(down, 250, 1000);
	SCH_Add_Task(up, 750, 1000);

	// Starts the scheduler, by enabling interrupts.
	SCH_Start();
	
	// When a task (function) is due to run, SCH_Dispatch_Tasks() will run it.
	while(1) SCH_Dispatch_Tasks();
	
	return 0;
}