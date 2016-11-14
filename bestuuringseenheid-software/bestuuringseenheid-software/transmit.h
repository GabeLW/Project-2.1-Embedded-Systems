/*
 * tramsmit.h
 *
 * Created: 10-Nov-16 19:41:55
 *  Author: Bas Haaksema
 */ 

#include <stdint.h>

#ifndef TRANSMIT_H_
#define TRANSMIT_H_

void uart_init(void);
void transmit(uint8_t data);

#endif /* TRANSMIT_H_ */
