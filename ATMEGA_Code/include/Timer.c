#include <avr/io.h>
#include <stdint.h>
#include <config.h>

void Timer_Init(void){
    //Using Timer 1

    //Enable interrupts
    SREG |= _BV(7);

    //Prescale to 1024
    TCCR1B |= _BV(CS12) | _BV(CS10);

    //Enable overflow flag
    TIMSK1 |= _BV(TOIE1);   
}