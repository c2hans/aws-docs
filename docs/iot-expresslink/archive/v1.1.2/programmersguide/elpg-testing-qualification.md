---
source_url: https://docs.aws.amazon.com/iot-expresslink/archive/v1.1.2/programmersguide/elpg-testing-qualification.html
---

# 12 Testing and qualification
<a name="elpg-testing-qualification"></a>

## 12.1 Test hardware
<a name="elpg-testing-qualification-hardware"></a>

The ExpressLink testing and qualification process requires a Raspberry Pi 4 single board computer and a hardware harness providing the following connections:

<a name="elpg-figure7"></a>![Figure 7 - RaspberryPi 4 I/O connections](http://docs.aws.amazon.com/iot-expresslink/archive/v1.1.2/programmersguide/images/image7.png)

The ExpressLink candidate will be attached to the GPIO header of the PI using the following pins.

**Table 7 - Test I/O pin assignments**

| ExpressLink function | GPIO Pin Number |
| --- | --- |
| Command TX (Transmit from ExpressLink to Host) | GPIO 15 |
| Command RX (Receive from Host to ExpressLink) | GPIO 14 |
| Reset | GPIO 23 |
| Event | GPIO 27 |
| Wake | GPIO 22 |

## 12.2 Test software
<a name="elpg-testing-qualification-software"></a>

A test suite is provided by the AWS FreeRTOS service team to perform the ExpressLink Qualification, a program managed by the AWS Partner Network team.
