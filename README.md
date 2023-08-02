# Color LED Panel

![AltiumDesigner](https://img.shields.io/badge/altium%20designer-A5915F?style=for-the-badge&logo=altium%20designer&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![YouTube](https://img.shields.io/badge/YouTube-%23FF0000.svg?style=for-the-badge&logo=YouTube&logoColor=white)
![GitHub](https://img.shields.io/badge/github%20-%23121011.svg?&style=for-the-badge&logo=github&logoColor=white)

<div style="text-align: center">
<img src="https://raw.githubusercontent.com/ArchTW/ColorLedPanel/master/Image/logo.png"/>
</div>

## Description

This project is created to control a color LED panel on ESP32. Each LED on the panel is of WS2812-2020 type. This README file will explain the project's directory structure, provide relevant instructions and code, and include the copyright notice.

## YouTube

[![Demo Video](https://img.youtube.com/vi/aTWeKnYSMDY/maxresdefault.jpg)](https://youtube.com/shorts/BAYC-MqCSck)

[YouTube Channel](https://www.youtube.com/channel/UCWgpLi7-TcOpDOX5WHsremA)

## Files

- ColorLEDPanel
  - Firmware
    - main.py (Demo)
    - neopixel.py (Neopixel library)
  - Hardware
    - LED_Panel (Altium Designer)

## Variable Descriptions

### ESP32_PIN

In the code, we have defined the variable ESP32_PIN to specify the pin number on the ESP32 that is used for communication with WS2812. Please set this variable to the correct pin number according to your connection.

```
ESP32_PIN = 13
```

### LED_CNT

In the code, we have defined the variable LED_CNT to specify the quantity of LED lights (WS2812) on the strip.

```
LED_CNT= 64
```

### TEST_MODE

In the code, we have defined the variable TEST_MODE to select different test modes:

* Test Mode 0: LED lights with alternating colors.
  
```
TEST_MODE = 0
```

* Test Mode 1: LED lights with random color cycling.

```
TEST_MODE = 1
```

## Authors

Contributors names and contact info

[@ArchTW](mailto:arch@cocaen.com)

## License

This project is licensed under the MIT License - see the LICENSE file for details

## Acknowledgments

Inspiration, code snippets, etc.

* [Micropython](https://github.com/micropython/micropython)
* [NeoPixel](https://github.com/micropython/micropython-lib/tree/master/micropython/drivers/led/neopixel)
