---
source_url: https://docs.aws.amazon.com/whitepapers/latest/monitoring-river-levels-using-lorawan/source-code.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Source code
<a name="source-code"></a>

## MicroPython application example
<a name="micropython-application-example"></a>

 The Pycom LoPy4 ESP32 development board used for this demonstration has the following physical connectivity, as outlined in this schematics diagram:

![Diagram showing ESP32 development board schematics](http://docs.aws.amazon.com/whitepapers/latest/monitoring-river-levels-using-lorawan/images/esp32-development-board-schematics.png)

**Note**
 In this example, a voltage divider is used on the output of the HC-SR04’s echo pin to convert the 5V to 3.3V.
 Note that this diagram does not show receive/transmit (RX/TX) serial connections required to program the board, nor the recommended button between P2 and ground (GND) to place the device into bootloader mode. Refer to the [Pycom LoPy4 Product Info, Datasheets](https://docs.pycom.io/datasheets/development/lopy4/) webpage for additional information on the connections required to program the device.

* Table 1 – ESP32 development board physical connectivity *

|  Module  |  ESP32 (LoPy4) pin  |  Description  |
| --- | --- | --- |
|  HC-SR04  |  P9  |  Trigger  |
|  HC-SR04  |  P10  |  Echo  |
|  5V  |  Vin  |  5V  |
|  GND  |  GND  |  Ground  |

```
"""
Sample MicroPython application for the Pycom LoPy4 development board. Demonstrates
unconfirmed data uplink of HC-SR04 ultrasonic distance sensor readings using
LoRaWAN. Uses LoRaWAN OTAA support of Pycom's network driver. Spends time in
deep sleep between readings to conserve power.
"""

# Required MicroPython libraries
# pylint: disable=E0401
import socket
import utime
import ubinascii
from machine import Pin, deepsleep
from network import LoRa

# HC-SR04 ultrasonic distance sensor configurations
HCSR04_TRIGGER_PIN = "P9"
HCSR04_ECHO_PIN = "P10"
HCSR04_ECHO_TIMEOUT_MS = const(50)          # pylint: disable=E0602

# LoRaWAN OTAA connection details. Replace with own settings.
LORAWAN_APP_EUI = ubinascii.unhexlify("REPLACE")
LORAWAN_APP_KEY = ubinascii.unhexlify("REPLACE")
LORAWAN_OTAA_TIMEOUT_MS = const(30000)      # pylint: disable=E0602

# Additional program configurations
PROGRAM_LOOP_MS = const(600000)             # pylint: disable=E0602
PROGRAM_WAIT_MS = const(3000)               # pylint: disable=E0602

# pylint: disable=R0903
class HCSR04():
    """ Driver for HC-SR04 ultrasonic distance sensor """

    # HC-SR04 fixed parameters
    HCSR04_US_TO_CM_CONST = const(58)       # pylint: disable=E0602
    HCSR04_MAX_RANGE_CM = const(400)        # pylint: disable=E0602

    def __init__(self, trigger_pin, echo_pin, echo_timeout_ms):
        """ Initialises HC-SR04 ultrasonic distance sensor pins """
        self.trigger_pin = Pin(trigger_pin, mode=Pin.OUT, pull=None)
        self.echo_pin = Pin(echo_pin, mode=Pin.IN, pull=None)
        self.echo_timeout_ms = echo_timeout_ms
        self.distance_cm = None

    def get_distance_cm(self):
        """ Retrieves distance to nearest surface in m (decimal).
        Raises exception if range is unsupported, or if echo response
        times out. This is a blocking method. """
        echo_detected = False
        self.trigger_pin(True)
        utime.sleep_us(10)
        self.trigger_pin(False)
        echo_timeout_start_ms = utime.ticks_ms()
        while (utime.ticks_ms() - echo_timeout_start_ms) < self.echo_timeout_ms:
            if self.echo_pin():
                # If high is detected on echo pin, start echo timer
                echo_detected = True
                echo_timer_start_us = utime.ticks_us()
                break
        if echo_detected:
            while self.echo_pin():
                pass
            # If echo pin goes low, stop echo timer
            duration_us = utime.ticks_us() - echo_timer_start_us
            self.distance_cm = duration_us / self.HCSR04_US_TO_CM_CONST
            if self.distance_cm > self.HCSR04_MAX_RANGE_CM:
                raise OSError(
                    "Unsupported HC-SR04 range (>" +
                    str(self.HCSR04_MAX_RANGE_CM) +
                    "cm)"
                )
        else:
            # If no error signal is detected, time out
            raise OSError(
                "Failed to detect echo signal (>" +
                str(self.echo_timeout_ms) +
                "ms)"
            )
        return self.distance_cm

def main():
    """ Runs the ultrasonic distance sensor check and dispatches results as
    unconfirmed data upload LoRaWAN payload. Payload is 2 bytes (first byte is
    distance in m, second byte is remaining distance in cm). Programs enters
    deep sleep in between checks. """
    start_time = utime.ticks_ms()
    data = bytearray(2)
    sensor = HCSR04(
        trigger_pin=HCSR04_TRIGGER_PIN,
        echo_pin=HCSR04_ECHO_PIN,
        echo_timeout_ms=HCSR04_ECHO_TIMEOUT_MS
    )
    try:
        distance_m = sensor.get_distance_cm() / 100
        print(
            "Distance recorded (" +
            str(distance_m) +
            "m)"
        )
    except OSError as exception:
        print(
           "Sensor fault (" +
           str(exception) +
           ")"
        )
    else:
        # First byte of output is distance in m
        data[0] = int(str(distance_m).split(".")[0])
        # Second byte of output is remainder of the distance in cm
        data[1] = int(str(distance_m).split(".")[1][:2])
        # LoRaWAN OTAA data upload. Region is EU868 (change as required).
        lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.EU868)
        lora.join(activation=LoRa.OTAA, auth=(LORAWAN_APP_EUI, LORAWAN_APP_KEY), timeout=0)
        otaa_timeout_start_ms = utime.ticks_ms()
        while (utime.ticks_ms() - otaa_timeout_start_ms) < LORAWAN_OTAA_TIMEOUT_MS:
            if lora.has_joined():
                print("Joined LoRaWAN")
                break
            print("Waiting to join LoRaWAN using OTAA...")
            utime.sleep(2.5)
        if lora.has_joined():
            lora_socket = socket.socket(socket.AF_LORA, socket.SOCK_RAW)    # pylint: disable=E1101
            lora_socket.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)        # pylint: disable=E1101
            lora_socket.setblocking(True)
            lora_socket.send(data)
            print(
                "Bytes sent (" +
                str(data) +
                ")"
            )
            lora_socket.setblocking(False)
        else:
            print("Failed to join LoRaWAN using OTAA")
    finally:
        utime.sleep_ms(PROGRAM_WAIT_MS)
        print(
            "Sleeping... (" +
            str(PROGRAM_LOOP_MS) +
            "ms)"
        )
        deepsleep(PROGRAM_LOOP_MS - (utime.ticks_ms() - start_time))

if __name__ == "__main__":
    main()
```

## Lambda decoder function example
<a name="lambda-decoder-function-example"></a>

```
import json
import base64
import boto3
import botocore

client = boto3.client('iot-data')
mqtt_topic = 'myTopic/'

def lambda_handler(event, context):
    """ Decode LoRa payload and republish back to AWS IoT as a transformed event """

    river_level_bytes = base64.b64decode(event['PayloadData'])
    # First byte of payload is meters, second byte centimeters
    river_level = river_level_bytes[0] + (river_level_bytes[1] / 100)
    event_transformed = {
        'river_level': river_level,
        'timestamp': event['WirelessMetadata']['LoRaWAN']['Timestamp']
    }
    try:
        response = client.publish(
            topic=mqtt_topic+event['WirelessDeviceId']+'/',
            payload=json.dumps(event_transformed)
        )
    except botocore.exceptions.ClientError as error:
        print('Operataion failed! ' + str(error))
    else:
        print('Event successfully transformed and republished!')
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
