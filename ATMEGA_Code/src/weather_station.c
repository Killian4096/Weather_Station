#include <avr/io.h>
#include <util/delay.h>
#include <USART.c>
#include <Timer.c>
#include <avr/interrupt.h>

#define TICKER 0 //Fire every min, interrupt ticks every 4 sec * 15 = 60 sec

static volatile uint32_t count = 0;

ISR(TIMER1_OVF_vect){
    count = count + 1;
}

void main(void){
    USART_Init();
    Timer_Init();
    while(1){
        if(count >= TICKER){
            USART_Transmit(48);
            count = 0;
        }
    }
}
