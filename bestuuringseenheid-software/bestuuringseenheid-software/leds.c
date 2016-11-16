/*
 * leds.c
 *
 * Created: 08-Nov-16 15:29:50
 *  Author: Bas Haaksema
 */ 
 
#include "leds.h"
#include "uart.h"
#include <avr/io.h>
#include <stdint.h>
#define F_CPU 16E6
#include <util/delay.h>

void init_leds()
{
	DDRB = 0xFF;
	PORTB |= (1 << PB0);
	PORTB &= ~(1 << PB2);
}

void manage_leds()
{
	uint8_t status = receive();
	
	if (status == 0x7F)
	{
		//up
		PORTB &= ~(1 << PB2);
		blink_led();
		PORTB |= (1 << PB0);
	}

	if (status == 0xFF)
	{
		//down
		PORTB &= ~(1 << PB0);
		blink_led();
		PORTB |= (1 << PB2);
	}
}

void blink_led()
{
	_delay_ms(50);
	int i;
	for(i = 0; i < 5; i++)
	{
		PORTB |= (1 << PB1);
		_delay_ms(50);
		PORTB &= ~(1 << PB1);
		_delay_ms(50);
	}
}
