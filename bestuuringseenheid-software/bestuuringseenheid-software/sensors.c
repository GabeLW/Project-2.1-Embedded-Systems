/*
 * sensors.c
 *
 * Created: 14-Nov-16 14:06:08
 *  Author: Bas Haaksema
 */
 
#include "sensors.h"
#include "uart.h"
#include <avr/io.h>
#include <avr/sfr_defs.h>

void get_adc_light()
{
	uint8_t sign = 0x00;
	// ref=Vcc, left adjust the result (8 bit resolution),
	// select channel 0 (PC0 = input)	ADMUX = (1<<REFS0)|(1<<ADLAR);
	// enable the ADC & prescale = 128
	ADCSRA = (1<<ADEN)|(1<<ADPS2)|(1<<ADPS1)|(1<<ADPS0);
	// start conversion
	ADCSRA |= (1<<ADSC);
	loop_until_bit_is_clear(ADCSRA, ADSC);
	// 8-bit resolution, left adjusted
	transmit(sign);
	transmit(ADCH);
}

void get_adc_temperature()
{
	uint8_t sign = 0xFF;
	// ref=Vcc, left adjust the result (8 bit resolution),
	// select channel 0 (PC0 = input)	ADMUX = (1<<REFS0)|(1<<ADLAR)|(1<<MUX0);
	// enable the ADC & prescale = 128
	ADCSRA = (1<<ADEN)|(1<<ADPS2)|(1<<ADPS1)|(1<<ADPS0);	
	// start conversion
	ADCSRA |= (1<<ADSC);
	loop_until_bit_is_clear(ADCSRA, ADSC);
	// 8-bit resolution, left adjusted
	transmit(sign);
	transmit(ADCH);
}
