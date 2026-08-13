---
source_url: https://docs.aws.amazon.com/freertos/latest/userguide/cellular-interface.html
---

# Cellular Interface library
<a name="cellular-interface"></a>

**Note**  <a name="out-of-date-message"></a>
The content on this page may not be up-to-date. Please refer to the [FreeRTOS.org library page](https://www.freertos.org/Documentation/03-Libraries/01-Library-overview/01-All-libraries) for the latest update.

## Introduction
<a name="freertos-cellular-interface-introduction"></a>

The Cellular Interface library implements a simple unified [API](https://freertos.github.io/FreeRTOS-Cellular-Interface/v1.3.0/) that hides the complexity of the cellular modem-specific AT commands and exposes a socket-like interface to C programmers.

Most cellular modems implement more or less of the AT commands defined by the [ 3GPP TS v27.007](https://portal.3gpp.org/desktopmodules/Specifications/SpecificationDetails.aspx?specificationId=1515) standard. This project provides an [implementation](https://github.com/FreeRTOS/FreeRTOS-Cellular-Interface/tree/main/source) of such standard AT commands in a [ reusable common component](https://freertos.org/Documentation/api-ref/cellular/cellular_porting_module_guide.html). The three Cellular Interface libraries in this project all take advantage of that common code. The library for each modem only implements the vendor-specific AT commands, then exposes the complete Cellular Interface library API.

The common component that implements the 3GPP TS v27.007 standard has been written in compliance with the following code quality criteria:
+ GNU Complexity scores are not over 8
+ MISRA C:2012 coding standard. Any deviations from the standard are documented in source code comments marked by "coverity".

## Dependencies and requirements
<a name="freertos-cellular-interface-dependencies"></a>

There is no direct dependency for the Cellular Interface library. However, Ethernet, Wi-Fi and cellular cannot co-exist in the FreeRTOS network stack. Developers must choose one of the network interface to integrate with the [Secure Sockets library](https://docs.aws.amazon.com/freertos/latest/userguide/secure-sockets.html).

## Porting
<a name="freertos-cellular-interface-porting"></a>

For information about porting the Cellular Interface library to your platform, see [ Porting the Cellular Interface library](https://docs.aws.amazon.com/freertos/latest/portingguide/freertos-porting-cellular.html) in the *FreeRTOS Porting Guide*.

## Memory use
<a name="freertos-cellular-interface-memory-use"></a>

****
<a name="cellular-memory-estimate"></a>
<table>
<thead>
  <tr><th colspan="3">Code Size of cellular interface library (example generated with GCC for ARM Cortex-M)</th></tr>
  <tr><th>File</th><th>With -O1 Optimization</th><th>With -Os Optimization</th></tr>
</thead>
<tbody>
  <tr><td>cellular_3gpp_api.c</td><td>6.3K</td><td>5.7K</td></tr>
  <tr><td>cellular_3gpp_urc_handler.c</td><td>0.9K</td><td>0.8K</td></tr>
  <tr><td>cellular_at_core.c</td><td>1.4K</td><td>1.2K</td></tr>
  <tr><td>cellular_common_api.c</td><td>0.5K</td><td>0.5K</td></tr>
  <tr><td>cellular_common.c</td><td>1.6K</td><td>1.4K</td></tr>
  <tr><td>cellular_pkthandler.c</td><td>1.4K</td><td>1.2K</td></tr>
  <tr><td>cellular_pktio.c</td><td>1.8K</td><td>1.6K</td></tr>
  <tr><td><b>Total estimates</b></td><td><b>13.9K</b></td><td><b>12.4K</b></td></tr>
</tbody>
</table>

## Getting started
<a name="freertos-cellular-interface-getting-started"></a>

### Download the source code
<a name="freertos-cellular-interface-download-source"></a>

The source code can be downloaded as part of the FreeRTOS libraries or by itself.

To clone the library from Github using HTTPS:

```
git clone https://github.com/FreeRTOS/FreeRTOS-Cellular-Interface.git
```

Using SSH:

```
git clone git@github.com:FreeRTOS/FreeRTOS-Cellular-Interface.git
```

### Folder structure
<a name="freertos-cellular-interface-folder-structure"></a>

At the root of this repository you will see these folders:
+ `source` : reusable common code that implements the standard AT commands defined by 3GPP TS v27.007
+ `doc` : documentation
+ `test` : unit test and cbmc
+ `tools` : tools for Coverity static analysis and CMock

### Configure and build the Library
<a name="freertos-cellular-interface-configure"></a>

The Cellular Interface library should be built as part of an application. In order to do this, you must provide certain configurations. The [ FreeRTOS\_Cellular\_Interface\_Windows\_Simulator](https://github.com/FreeRTOS/FreeRTOS/tree/main/FreeRTOS-Plus/Demo/FreeRTOS_Cellular_Interface_Windows_Simulator) project provides an [ example](https://github.com/FreeRTOS/FreeRTOS/blob/main/FreeRTOS-Plus/Demo/FreeRTOS_Cellular_Interface_Windows_Simulator/MQTT_Mutual_Auth_Demo_with_BG96/cellular_config.h) of how to configure the build. More information can be found in the [Cellular API References](https://freertos.github.io/FreeRTOS-Cellular-Interface/v1.3.0/cellular_config.html).

Please refer to the [Cellular Interface](https://www.freertos.org/cellular/index.html) page for more information.

## Integrate the Cellular Interface library with MCU platforms
<a name="freertos-cellular-interface-integrate"></a>

The Cellular Interface library runs on MCUs using an abstracted interface, the [ Comm Interface](https://github.com/FreeRTOS/FreeRTOS-Cellular-Interface/blob/main/source/interface/cellular_comm_interface.h), to communicate with cellular modems. A Comm Interface must be implemented on the MCU platform as well. The most common implementations of the Comm Interface communicate over UART hardware, but can be implemented over other physical interfaces, such as SPI, as well. The documentation for the Comm Interface can be found in the [ Cellular Library API References](https://freertos.github.io/FreeRTOS-Cellular-Interface/v1.3.0/cellular_porting.html#cellular_porting_comm_if). The following example implementations of the Comm Interface are available:
+ [ FreeRTOS Windows simulator comm interface](https://github.com/FreeRTOS/FreeRTOS/blob/main/FreeRTOS-Plus/Demo/FreeRTOS_Cellular_Interface_Windows_Simulator/Common/comm_if_windows.c)
+ [ FreeRTOS Common IO UART comm interface](https://github.com/aws/amazon-freertos/blob/main/libraries/abstractions/common_io/include/iot_uart.h)
+ [ STM32 L475 discovery board comm interface](https://github.com/aws/amazon-freertos/blob/feature/cellular/vendors/st/boards/stm32l475_discovery/ports/comm_if/comm_if_uart.c)
+ [ Sierra Sensor Hub board comm interface](https://github.com/aws/amazon-freertos/blob/feature/cellular/vendors/sierra/boards/sensorhub/ports/comm_if/comm_if_sierra.c)
