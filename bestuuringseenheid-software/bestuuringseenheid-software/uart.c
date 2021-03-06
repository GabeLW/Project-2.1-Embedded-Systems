/*
 * uart.c
 *
 * Created: 10-Nov-16 19:42:18
 *  Author: Bas Haaksema
 */ 
 
#include "uart.h"
#include <avr/io.h>
#include <avr/sfr_defs.h>

// output on USB = PD1 = board pin 1
// datasheet p.190; F_OSC = 16 MHz & baud rate = 9.600
#define UBBRVAL 103
void uart_init()
{
	// set the baud rate
	UBRR0H = 0;
	UBRR0L = UBBRVAL;
	// disable U2X mode
	UCSR0A = 0;
	// enable transmitter
	UCSR0B = _BV(RXEN0) | _BV(TXEN0);
	// set frame format : asynchronous, 8 data bits, 1 stop bit, no parity
	UCSR0C = _BV(UCSZ01) | _BV(UCSZ00);
}

void transmit(uint8_t data)
{
	// wait for an empty transmit buffer
	// UDRE is set when the transmit buffer is empty
	loop_until_bit_is_set(UCSR0A, UDRE0);
	// send the data
	UDR0 = data;
}

uint8_t receive(void)
{
    // wait until data exists
	loop_until_bit_is_set(UCSR0A, RXC0);
	// return the data
    return UDR0;
}
