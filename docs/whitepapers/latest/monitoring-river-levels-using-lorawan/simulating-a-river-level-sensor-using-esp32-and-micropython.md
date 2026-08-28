---
source_url: https://docs.aws.amazon.com/whitepapers/latest/monitoring-river-levels-using-lorawan/simulating-a-river-level-sensor-using-esp32-and-micropython.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Simulating a river level sensor using ESP32 and MicroPython
<a name="simulating-a-river-level-sensor-using-esp32-and-micropython"></a>

 Use a Pycom LoPy4 ESP32 development board equipped with a Semtech SX1276 LoRa transceiver to simulate the river level sensor.

![Photograph of an ESP32 development board running MicroPython](http://docs.aws.amazon.com/whitepapers/latest/monitoring-river-levels-using-lorawan/images/esp32-development-board-running-micropython.jpg)

 The microcontroller is awakened every ten minutes from deep sleep using its real-time clock (RTC), and configured to run a short MicroPython application which retrieves a distance reading to the water surface using the HC-SR04 ultrasonic distance sensor. The captured distance is thereafter reorganized into two bytes – the first byte houses the distance in meters, and the second byte houses the remainder in centimeters.

 This data is then broadcast out using LoRaWAN.

 This paper provides a [MicroPython application example](source-code.md#micropython-application-example) which demonstrates the application running on generic MicroPython for ESP32 firmware. When running, the console displays the distance recorded by the HC-SR04 ultrasonic distance sensor, LoRaWAN OTAA join status, and the bytes sent.

 The following is a running sample MicroPython application:

```
Distance recorded (0.1722414m)
Waiting to join LoRaWAN using OTAA...
Waiting to join LoRaWAN using OTAA...
Waiting to join LoRaWAN using OTAA...
Joined LoRaWAN
Bytes sent (bytearray(b'\x00\x11'))
Sleeping... (600000ms)
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
