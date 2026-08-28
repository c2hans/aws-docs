---
source_url: https://docs.aws.amazon.com/freertos/latest/userguide/freertos-common-io.html
---

# Understand the FreeRTOS Common IO APIs
<a name="freertos-common-io"></a>

Common IO APIs act as hardware abstraction layers (HAL) that provide a common interface between drivers and higher-level application code. FreeRTOS Common IO provides a set of standard APIs for accessing common serial devices on supported reference boards; implementations of these APIs are not included. These common APIs communicate and interact with these peripherals and enable your code to function across platforms. Without Common IO, writing code to work with low level devices is silicon-vendor specific.

**Note**
FreeRTOS does not require implementations of the Common IO APIs to function, but it will attempt to use the Common IO APIs as a way to interface with the specific peripherals on a microcontroller-based board instead of vendor-specific APIs.

In general, device drivers are independent of the underlying operating system and are specific to a given hardware configuration. The HAL abstracts away the details of how a specific driver works and provides a uniform API to control such devices. You can use the same APIs to access various device drivers across multiple microcontroller- (MCU-) based reference boards.

## Libraries
<a name="freertos-common-io-libraries"></a>

Currently, FreeRTOS provides two Common IO libraries: Common IO - basic and Common IO - BLE.

### Common IO - basic
<a name="freertos-common-io-libraries-basic"></a>

*Overview*
[Common IO - basic](https://aws.github.io/common-io-basic/) provides APIs that deal with basic I/O peripherals and functions that you may find on MCU-based boards. The Common IO - basic repository is available on [GitHub](https://github.com/aws/common-io-basic).

*Supported peripherals*
+ ADC
+ GPIO
+ I2C
+ PWM
+ SPI
+ UART
+ Watchdog
+ Flash
+ RTC
+ EFUSE
+ Resets
+ I2S
+ Performance counter
+ Hardware platform information

*Supported features*
+ Synchronous read/write

  The function doesn't return until the requested amount of data is transferred.
+ Asynchronous read/write

  The function returns immediately and the data transfer happens asynchronously. When the action completes, a registered user callback is invoked.

*Peripheral specific*
+ I2C

  Combine multiple operations into one transaction. Used to do write then read actions in one transaction.
+ SPI

  Transfer data between primary and secondary, which means the write and read happen simultaneously.

*API reference*
For a full API reference, see the [Common IO - basic API reference](https://aws.github.io/common-io-basic/).

### Common IO - BLE
<a name="freertos-common-io-libraries-BLE"></a>

*Overview*
Common IO - BLE provides abstraction from the manufacturer's Bluetooth Low Energy stack. It provides the following interfaces which can be used to control the device, and perform GAP and GATT operations. The Common IO - BLE repository is available on [ GitHub](https://github.com/aws/common-io-ble).

*Bluetooth Device Manager:*
This provides an interface to control the Bluetooth device, perform device discovery operations and other connectivity related tasks.

*BLE Adapter Manager:*
This provides an interface for the GAP API functions that are specific to BLE.

*Bluetooth Classic Adapter Manager:*
This provides an interface to control BT classic functionalities of a device.

*GATT Server:*
This provides an interface to use the Bluetooth GATT server feature.

*GATT Client:*
This provides an interface to use the Bluetooth GATT client feature.

*A2DP Connection Interface:*
This provides an interface for the A2DP Source profile for the local device.

*API reference*
For a full API reference, see the [Common IO - BLE API reference](https://aws.github.io/common-io-ble/).

## Common IO for Amazon Common Software
<a name="freertos-common-io-acs"></a>

The Common IO APIs are a part of the required implementations needed by [Amazon Common Software for Devices](https://developer.amazon.com/acs-devices), specifically to be implemented in a vendor device porting kit (DPK).

### What is ACS?
<a name="freertos-common-io-acs-what"></a>

Amazon Common Software (ACS) for Devices is software that makes it faster for you to integrate Amazon Device SDKs on your devices. ACS provides a unified API integration layer, pre-validated and memory efficient components for common functions such as connectivity, a device porting kit (DPK), and multi-tier test suites.

### Qualification Program
<a name="freertos-common-io-acs-qualification"></a>

The [Amazon Common Software for Devices](https://developer.amazon.com/acs-devices) qualification program verifies that a build of the ACS DPK (Device Porting Kit) which runs on a specific microcontroller-based development board is compatible with the program's published best practices and robust enough to pass ACS-mandated tests specified by the qualification program.

Vendors qualified under this program are listed on the [ACS Chipset Vendors](https://developer.amazon.com/avs-silicon-vendors) page.

For information about qualifying, contact [ACS for Devices](https://developer.amazon.com/acs-devices).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for FreeRTOS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query freertos` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
