#include <avr/io.h>
#include <stdint.h>
#include <config.h>

void USART_Init(void){
    //Set Baud Rate, put something here
    UBRR0H |= (uint8_t)(BAUD_FACTOR>>8);
    UBRR0L |= (uint8_t)(BAUD_FACTOR);

    //Enable Transmitter
    UCSR0B |= _BV(TXEN0);

    //Set frame format: 8data, 2 stop bit
    UCSR0C |= _BV(USBS0) | _BV(UCSZ01) | _BV(UCSZ00);

    //Look at UCSRnC datasheet
}

void USART_Transmit(uint8_t data){
    //Wait for transmit to finish
    while(!(UCSR0A & _BV(UDRE0)));

    //Put data into buffer
    UDR0 = data;
}