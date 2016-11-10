/*
 * light.c
 *
 * Created: 10-Nov-16 18:44:11
 *  Author: Bas Haaksema
 */ 

#include "light.h"
#include "transmit.h"
#include <avr/io.h>
#include <avr/sfr_defs.h>

void init_adc_light()
{
	// ref=Vcc, left adjust the result (8 bit resolution),
	// select channel 0 (PC0 = input)	ADMUX = (1<<REFS0)|(1<<ADLAR);
	// enable the ADC & prescale = 128
	ADCSRA = (1<<ADEN)|(1<<ADPS2)|(1<<ADPS1)|(1<<ADPS0);
}

void get_adc_light()
{
	ADCSRA |= (1<<ADSC); // start conversion
	loop_until_bit_is_clear(ADCSRA, ADSC);
	transmit(ADCH); // 8-bit resolution, left adjusted
}
