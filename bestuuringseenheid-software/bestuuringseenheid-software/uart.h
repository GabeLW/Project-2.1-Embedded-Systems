/*
 * uart.h
 *
 * Created: 10-Nov-16 19:41:55
 *  Author: Bas Haaksema
 */ 

#include <stdint.h>

#ifndef UART_H_
#define UART_H_

void uart_init(void);
void transmit(uint8_t data);
uint8_t receive(void);

#endif /* UART_H_ */
