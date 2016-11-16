/*
 * main.c
 *
 * Created: 08-Nov-16 15:42:35
 *  Author: Bas Haaksema
 */ 

#include "leds.h"
#include "scheduler.h"
#include "sensors.h"
#include "uart.h"

int main()
{
	// Prepares scheduler data structures and sets up timer interrupts at required rate.
	SCH_Init_T1();

	// Causes a task (function) to be executed at regular intervals or after a user-defined delay
	SCH_Add_Task(init_leds, 0, 0);
	SCH_Add_Task(uart_init, 5, 0);
	SCH_Add_Task(get_adc_light, 10, 50);
	SCH_Add_Task(get_adc_temperature, 20, 50);
	SCH_Add_Task(manage_leds, 30, 50);

	// Starts the scheduler, by enabling interrupts.
	SCH_Start();
	
	// When a task (function) is due to run, SCH_Dispatch_Tasks() will run it.
	while(1) SCH_Dispatch_Tasks();
	
	return 0;
}
