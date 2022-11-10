EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L MCU_Microchip_ATmega:ATmega328-PU U?
U 1 1 636D2036
P 4400 3500
F 0 "U?" H 3756 3546 50  0000 R CNN
F 1 "ATmega328-PU" H 3756 3455 50  0000 R CNN
F 2 "Package_DIP:DIP-28_W7.62mm" H 4400 3500 50  0001 C CIN
F 3 "http://ww1.microchip.com/downloads/en/DeviceDoc/ATmega328_P%20AVR%20MCU%20with%20picoPower%20Technology%20Data%20Sheet%2040001984A.pdf" H 4400 3500 50  0001 C CNN
	1    4400 3500
	1    0    0    -1  
$EndComp
$Comp
L Connector:Conn_01x02_Male J?
U 1 1 636D341F
P 2950 1650
F 0 "J?" H 3058 1831 50  0000 C CNN
F 1 "Conn_01x02_Male" H 3058 1740 50  0000 C CNN
F 2 "" H 2950 1650 50  0001 C CNN
F 3 "~" H 2950 1650 50  0001 C CNN
	1    2950 1650
	1    0    0    -1  
$EndComp
$Comp
L pspice:0 #GND?
U 1 1 636D4236
P 3150 1750
F 0 "#GND?" H 3150 1650 50  0001 C CNN
F 1 "0" H 3150 1839 50  0000 C CNN
F 2 "" H 3150 1750 50  0001 C CNN
F 3 "~" H 3150 1750 50  0001 C CNN
	1    3150 1750
	1    0    0    -1  
$EndComp
$Comp
L Connector:Conn_01x03_Female J?
U 1 1 636D5400
P 6050 4100
F 0 "J?" H 6078 4126 50  0000 L CNN
F 1 "Conn_01x03_Female" H 6078 4035 50  0000 L CNN
F 2 "" H 6050 4100 50  0001 C CNN
F 3 "~" H 6050 4100 50  0001 C CNN
	1    6050 4100
	1    0    0    -1  
$EndComp
$Comp
L pspice:0 #GND?
U 1 1 636D8CBA
P 5850 4200
F 0 "#GND?" H 5850 4100 50  0001 C CNN
F 1 "0" H 5850 4289 50  0000 C CNN
F 2 "" H 5850 4200 50  0001 C CNN
F 3 "~" H 5850 4200 50  0001 C CNN
	1    5850 4200
	1    0    0    -1  
$EndComp
Wire Wire Line
	3150 1650 4400 1650
Wire Wire Line
	4400 1650 4400 2000
$EndSCHEMATC
