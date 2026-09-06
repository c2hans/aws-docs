---
source_url: https://docs.aws.amazon.com/freertos/latest/userguide/lts-dt-vars.html
---

# IDT for FreeRTOS variables
<a name="lts-dt-vars"></a>

The commands to build your code and flash the device might require connectivity or other information about your devices to run successfully. AWS IoT Device Tester allows you to reference device information in flash and build commands using [JsonPath](https://goessner.net/articles/JsonPath/). By using simple JsonPath expressions, you can fetch the required information specified in your `device.json` file.

## Path variables
<a name="path-variables-lts"></a>

IDT for FreeRTOS defines the following path variables that can be used in command lines and configuration files:

** `{{testData.sourcePath}}` **
Expands to the source code path. If you use this variable, it must be used in both the flash and build commands.

** `{{device.connectivity.serialPort}}` **
Expands to the serial port.

** `{{device.identifiers[?(@.name == 'serialNo')].value[0]}}` **
Expands to the serial number of your device.

** `{{config.idtRootPath}}` **
Expands to the AWS IoT Device Tester root path.
