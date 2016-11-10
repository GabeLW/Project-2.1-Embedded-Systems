/*
 * tasks.c
 *
 * Created: 08-Nov-16 15:29:50
 *  Author: Bas Haaksema
 */ 
 
#include "tasks.h"
#include <avr/io.h>
#define F_CPU 16E6
#include <util/delay.h>

void init()
{
	DDRB = 0xFF;
	PORTB |= (1 << PB0);
	PORTB &= ~(1 << PB2);
}

void up()
{
	PORTB &= ~(1 << PB2);
	blink();
	PORTB |= (1 << PB0);
}

void down()
{
	PORTB &= ~(1 << PB0);
	blink();	
	PORTB |= (1 << PB2);
}

void blink()
{
	_delay_ms(250);
	int i;
	for(i = 0; i < 5; i++)
	{
		PORTB |= (1 << PB1);
		_delay_ms(250);
		PORTB &= ~(1 << PB1);
		_delay_ms(250);
	}
}
