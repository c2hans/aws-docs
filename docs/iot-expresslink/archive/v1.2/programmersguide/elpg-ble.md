---
source_url: https://docs.aws.amazon.com/iot-expresslink/archive/v1.2/programmersguide/elpg-ble.html
---

# 12 Bluetooth Low Energy
<a name="elpg-ble"></a>

ExpressLink modules can take advantage of additional (local) connectivity capabilities, optionally available on selected SoCs. Bluetooth Low Energy (BLE) is one prominent example of such capabilities used to communicate with accessories and other modules or gateways over a local (personal) area network.

BLE interfaces can be configured by means of *profiles* which describe a collection of *attributes* used to transfer individual pieces of information between two devices. Devices can assume one of two roles:

1. Central – a BLE device which initiates an outgoing connection request to an advertising peripheral device.

1. Peripheral - the BLE device which accepts an incoming connection request after advertising its presence and capabilities.

A host processor can access BLE features of a capable ExpressLink module through the set of commands described in this chapter. Additionally, a set of events is available to support asynchronous communication with the host (see the BLE specific events in [Table 4 - ExpressLink event codes](elpg-event-handling.md#elpg-table4)) and the configuration parameters in the ExpressLink configuration dictionary (see [Table 3 - Configuration dictionary non-persistent keys](elpg-configuration-dictionary.md#elpg-table3)).

In particular, BLE devices that adopt a central role require the host to initialize one or more BLECentral\# parameters in order to describe the (peripheral) devices they wish to connect to. The numerical suffix \# is an integer between 1 and MaxBLECentral - a value dependent on the module capabilities. (Manufacturers of ExpressLink modules are required to publish the MaxBLECentral value in the module datasheet).

BLECentral configuration parameters use JSON notation and expect the following keys:
+ **peer** (mac string) – mac address of a target peripheral device (for example, "a4:c1:38:12:56:5d").
+ **filterDups** (1/0) – filters duplicate broadcasts by the same device.
+ **customFilters** (JSON object) – additional vendor-defined filtering options (must be documented by the vendor on the module's datasheet).

BLE devices adopting a peripheral role require the host to initialize the BLEPeripheral (single) configuration parameter in order to describe the device's connection requirements. BLEPeripheral configuration parameters use JSON notation and expect the following keys:
+ **appearance** (string) – a 4 digit hex number that represents the type of device. (See page 28 of the [Bluetooth Specification](https://www.bluetooth.com/specifications/assigned-numbers/)).
+ **customConfig** (JSON object) - additional vendor-defined customization options (must be documented by the vendor on the module datasheet).

Both Central and Peripheral devices require the host to initialize one or more BLEGATT\# parameters in order to describe individual characteristics they wish to publish or access. The numerical suffix \# is an integer between 1 and MaxBLEGATT - a value dependent on the module's capabilities. (Manufacturers of ExpressLink modules are required to publish the MaxBLEGATT value in the module datasheet).

BLEGATT\# configuration parameters use JSON notation and expect the following keys:
+ **service** (UUID string) – the UUID of a BLE service.
+ **chr** (UUID string) – the UUID of a BLE characteristic.
+ **write** (1/0) – optional
+ **read** (1/0) – optional
+ **indicate** (1/0) – optional
+ **notify** (1/0) – optional

**UUID strings** can be in short form 4 hex-digits (for example, "20AD") for short 16-bit services and characteristics, or long form 128-bit for custom service and characteristic identifiers (for example, "00000000-0000-1000-8000-00805F9B34FB"). Long form UUID separators ("-") can be omitted. The default value for optional keys is 0. Furthermore, the maximum value that can be read, written, or stored is 31 bytes.

Example 1: Two services composed of one characteristic each

```
AT+CONF BLEGATT1={"service": "1809", "chr": "2A1C" }
    # Thermometer service, Temperature characteristic.

AT+CONF BLEGATT2={"service": "180F", "chr": "2A19" }
    # Battery Level service and level(%) characteristic.
```

Since BLEGATT\# configuration parameters describe only one characteristic each, multiple parameters are required to describe a complex service composed of a number of characteristics.

Example 2: A service composed of two characteristics.

```
AT+CONF BLEGATT1={"service": "180D", "chr": "2A37" }
    # Heart rate service, heart rate measurement characteristic.

AT+CONF BLEGATT2={"service": "180D", "chr": "2A38" }
    # Heart rate service, body sensor location characteristic
```

## 12.1 BLE initialization
<a name="elpg-ble-commands"></a>

### 12.1.1 BLE INIT *[*CENTRAL\|PERIPHERAL*]*   »Initializing the device role«
<a name="elpg-ble-init-command"></a>

Initialize the BLE interface to operate in the selected (GAP) role. Note how this version of the ExpressLink specification allows a device to be configured as Central or Peripheral but not both. Once a BLE interface is initialized, the only way to terminate it or change its mode of operation is to use the RESET command. However, doing so will disconnect the device (if it is connected) and will reset all internal state. Non-persistent configuration parameters (see [Table 3 - Configuration dictionary non-persistent keys](elpg-configuration-dictionary.md#elpg-table3)) will be reinitialized, all subscriptions will be terminated, and the message queues will also be emptied.

*For Central Mode:*

Issuing the INIT CENTRAL command does not require (yet) any of the BLE configuration parameters to be set. One or more BLECentral\# and BLEGATT\# configuration parameters will be required later, before issuing an actual connection request (see the [BLE CONNECT command](#elpg-ble-connect-command)). BLECentral\# and BLEGATT\# parameters are used in central mode to act as filters to identify suitable connection target devices.

*For Peripheral Mode:*

Issuing the INIT PERIPHERAL command requires the BLEPeripheral and one (or more) BLEGATT\# configuration parameters to be set. BLEGATT keys do not need to be set in numerical order. All BLE parameters found (initialized) in the configuration dictionary will be used to define the peripheral’s GATT service. After initialization, the host may not change the BLEGATT\# service composition (characteristics) without first resetting the device. The host can instead update or retrieve the latest characteristic values using the appropriate SET/GET commands (see [BLE SET](#elpg-ble-set-command) and [BLE GET](#elpg-ble-get-command) commands).Returns:

**12.1.1.1**   `OK{EOL}`
If the command was accepted and the requested central or peripheral role is set.

**12.1.1.2**   `ERR4 PARAMETER ERROR{EOL}`
If the role parameter was not CENTRAL or PERIPHERAL.

**12.1.1.3**   `ERR28 CONFIGURATION ERROR{EOL}`
If the peripheral role was selected and the configuration dictionary does not contain the BLEPeripheral and at least one BLEGATT\# parameter.

**12.1.1.4**   `ERR25 NOT ALLOWED{EOL}`
If the BLE role was already initialized.

**12.1.1.5**   `ERR27 BLE ERROR{EOL}`
Failed to initialize the BLE Stack.

**12.1.1.6**   filterDups is 0 by default.

Example 1:

```
AT+BLE INIT CENTRAL{EOL}
OK
AT+CONF BLECENTRAL1={"peer": "a4:c1:38:12:56:5d"}{EOL}
OK
```

Example 2:

```
AT+CONF BLEPeripheral={"appearance": "4142"}{EOL}
OK
AT+CONF BLEGATT2={"service": "1809" ,"chr": "2A1C" }{EOL}
OK
AT+BLE INIT PERIPHERAL{EOL}
OK
```

## 12.2 BLE CENTRAL role commands
<a name="elpg-ble-central-role-commands"></a>

### 12.2.1 BLE*[\#]* DISCOVER *[duration\|*CANCEL*]*   »Scanning and Advertisement«
<a name="elpg-ble-discover-command"></a>

BLE capable devices can communicate with accessories without establishing permanent connections by means of a scanning and advertising protocol. This protocol is commonly used for characteristics whose value is required infrequently (device battery level, or ambient temperature sensors).

<a name="elpg-figure7"></a>![Figure 7 - BLE scanning for devices](http://docs.aws.amazon.com/iot-expresslink/archive/v1.2/programmersguide/images/ble-scanning-for-devices.png)

The ExpressLink module scans for advertisements from peripherals that match criteria defined in the corresponding configuration string BLECentral\#. This is an asynchronous command. It returns an immediate response to confirm the process has started (or an error prevented it). During the scanning time, any advertised data received will be queued. The scanning process will stop after a set amount of time optionally configured by the duration parameter (30 seconds by default), and a BLE DISCOVER COMPLETE event (see [Table 4 - ExpressLink event codes](elpg-event-handling.md#elpg-table4)) will be produced. Queued data can then be retrieved using the [ BLE GET DISCOVER](#elpg-ble-get-discover-command) command.

The CANCEL parameter is used to terminate an ongoing scanning process.

**12.2.1.1**   Scans for all the nearby devices if BLECentral\# is set to {} (an empty JSON object).

**12.2.1.2**   If the command is issued while a scanning process is in progress, any queued data is discarded and a new scanning process is started.

**12.2.1.3**   If *{duration}* is provided, only devices found within *{duration}* seconds will be captured.

**12.2.1.4**   Enqueues a BLE DISCOVER COMPLETE event on successful Discover complete or cancellation (see [Table 4 - ExpressLink event codes](elpg-event-handling.md#elpg-table4)).

**12.2.1.5**   Enqueues a BLE DISCOVER ERROR event when the discovery fails for any reason. Hint codes can be defined by the vendor to provide additional insight on the reason for the failure. (Hint codes must be documented in the module datasheet). Returns:

**12.2.1.6**   `OK{EOL}`
If the command was accepted and the scanning sequence started.

**12.2.1.7**   `OK{EOL}`
If the CANCEL parameter is given and the cancellation request was successfully submitted. CANCEL will terminate any scanning activity in progress regardless of the \# index given. However, a suffix index is required for the command to execute.

**12.2.1.8**   `ERR4 PARAMETER ERROR{EOL}`
If the parameter is 0 seconds.

**12.2.1.9**   `ERR4 PARAMETER ERROR{EOL}`
If the numerical suffix \# is omitted.

**12.2.1.10**   `ERR7 OUT OF RANGE{EOL}`
If the numerical suffix \# is out of bounds (0 or greater than MaxBLECentral).

**12.2.1.11**   `ERR8 PARAMETER UNDEFINED{EOL}`
If the numerical suffix \# points to an empty BLECentral\# string.

**12.2.1.12**   `ERR25 NOT ALLOWED{EOL}`
If Central role is not initialized or if the message queue is full.

Example 1 - Scan for any advertising device in range for a default timeout of 30 seconds:

```
AT+BLE DISCOVER{EOL}

   ...a BLE DISCOVER COMPLETE event occurs (see Table 4 - ExpressLink event codes)...

AT+EVENT?{EOL}				# check the event queue
OK 31 0 DISCOVER COMPLETE{EOL}		# a BLE DISCOVER event was received
```

Example 2 - Scan for a specific peripheral UUID and timeout after 20 seconds:

```
AT+CONF BLECentral1={ "peer": "a4:c1:38:12:56:5d", "filterDups": 1}{EOL}

AT+BLE1 DISCOVER 20{EOL}

   ...20 seconds later a BLE DISCOVER COMPLETE event occurs (see Table 4 - ExpressLink event codes...
```

Example 3 - Discover until cancelled:

```
AT+BLE DISCOVER{EOL}
OK

   ...a few seconds later...

AT+BLE DISCOVER CANCEL{EOL}
OK

   ...a BLE DISCOVER COMPLETE event occurs (see Table 4 - ExpressLink event codes...
```

### 12.2.2 BLE GET DISCOVER   »Retrieve the collected advertising information«
<a name="elpg-ble-get-discover-command"></a>

Retrieve the advertising information collected during the last discovery process.

Advertising information is stored in memory shared with MQTT messages. Collected information is also cleared when a new discovery is started. Hence, GET DISCOVER only fetches information for the devices that match the filter defined when the last DISCOVER command was issued.Returns:

**12.2.2.1**   `OK{EOL}`
No new advertising information was collected.

**12.2.2.2**   `OK {collected information}{EOL}`
Discovered information was collected and is presented following the 'OK'.

**12.2.2.3**   `ERR25 NOT ALLOWED{EOL}`
If the BLE Central role is not initialized.

Collected information is fetched from the queue and returned as a record containing the following space-separated fields:

```
<peer> <connectable> <Scannable> <rssi> <advertisedData>{EOL}
mac address    0/1          0/1       int     hex string
```

Example 1 - Check the BLE receive queue for any advertising data received, returning two records:

```
AT+BLE GET DISCOVER{EOL}
OK 3a:1a:f7:e4:11:38 0 1 -30 02011A0BFF4C00090603420A3F588B{EOL}
```

Example 2 - Repeat the GET DISCOVER request until the message queue is empty:

```
AT+BLE GET DISCOVER{EOL}
OK{EOL}
```

### 12.2.3 BLE*[\#]* CONNECT   »Connect to a peripheral«
<a name="elpg-ble-connect-command"></a>

In some use cases, instead of just reading sensor data provided in the advertisement message, the host may want to inspect what type of services and characteristics a peripheral exposes. To do this, the ExpressLink module must first establish a direct connection to the BLE peripheral device (using the BLE GAP protocol).

<a name="elpg-figure8"></a>![Figure 8 - Connecting to a BLE device](http://docs.aws.amazon.com/iot-expresslink/archive/v1.2/programmersguide/images/connecting-to-ble-device.png)

When you use the BLE{\#} CONNECT command, the ExpressLink module attempts to connect to a peripheral based on a specific configuration defined int the BLECentral\# parameter.Returns:

**12.2.3.1**   `OK{EOL}`
If the command was accepted and the connection request was successful.

**12.2.3.2**   `ERR7 OUT OF RANGE{EOL}`
The numerical suffix is out of bounds (0 or greater than MaxBLECentral index).

**12.2.3.3**   `ERR28 CONFIGURATION ERROR{EOL}`
The numerical suffix points to a {}, or is missing the "peer" key.

**12.2.3.4**   `ERR8 PARAMETER UNDEFINED{EOL}`
The numerical suffix points to an empty BLECentral\# string or {}.

**12.2.3.5**   `ERR25 NOT ALLOWED{EOL}`
If already connected to a device.

**12.2.3.6**   `ERR25 NOT ALLOWED{EOL}`
If BLE INIT is not set to CENTRAL mode.

**12.2.3.7**   `ERR14 UNABLE TO CONNECT{EOL}`
Discovery attempted for 30 seconds before timing out and returning error.

Example 1 - Connect to a specific peripheral according to the configuration. The attempt will stop if the timeout of 30 seconds is reached. The configuration information included in this example is for demonstration purposes only:

```
AT+CONF BLECENTRAL1={"peer": "a4:c1:38:12:56:5d", "filterDups": 1 }{EOL}
OK{EOL}
AT+BLE INIT CENTRAL{EOL}
OK{EOL}
AT+BLE1 CONNECT{EOL}
OK{EOL}

   ...a BLE CONNECTED event occurs...
```

Example 2 - Connect to a second peripheral according to the configuration. The attempt will stop if the timeout of 30 seconds is reached. The configuration information included in this example is for demonstration purposes only:

```
AT+CONF BLECENTRAL2={"peer": "a4:c1:38:12:56:5d", "filterDups":1}{EOL}
OK{EOL}
AT+BLE2 CONNECT{EOL}
OK{EOL}

   ...a BLE CONNECTED event occurs...
```

### 12.2.4 BLE*[\#]*CONNECT?   »Connection status query«
<a name="elpg-ble-connect-index-command"></a>

This query command allows the host device to check if the status of the specified connection is still active. This command can also be used to confirm a successful connection after the AT\+CONNECT command. Note that if the numerical suffix is not specified then the Peripheral command [12.3.1 BLE CONNECT?   »Connection status query«](#elpg-ble-connectq-command) is invoked.Returns:

**12.2.4.1**   `OK 1 CONNECTED{EOL}`
When connected to a Peripheral.

**12.2.4.2**   `OK 0 DISCONNECTED{EOL}`
When disconnected from a Peripheral.

**12.2.4.3**   `ERR7 OUT OF RANGE{EOL}`
The numerical suffix is out of bounds (0 or greater than MaxBLECentral index).

**12.2.4.4**   `ERR25 NOT ALLOWED{EOL}`
When the module role was not initialized as Central.

Example 1 - When connected over central config 2:

```
AT+BLE INIT CENTRAL{EOL}
OK{EOL}
AT+BLE2 CONNECT{EOL}
OK{EOL}

   ...a BLE CONNECTED event occurs...

AT+BLE2 CONNECT?{EOL}
OK 1 CONNECTED{EOL}
```

### 12.2.5 BLE*[\#]*DISCONNECT   »Connection termination request«
<a name="elpg-ble-disconnect-index-command"></a>

Terminate a BLE device connection.

**12.2.5.1**   Disconnects from the given index's connection.Returns:

**12.2.5.2**   `OK{EOL}`
On successful termination of connection or if there is no connection to terminate.

**12.2.5.3**   `ERR7 OUT OF RANGE{EOL}`
The numerical suffix is out of bounds (0 or greater than MaxBLECentral index).

**12.2.5.4**   `ERR27 BLE ERROR{EOL}`
If the command fails to terminate the connection.

**12.2.5.5**   `ERR25 NOT ALLOWED{EOL}`
If BLE INIT is not set to CENTRAL mode.

Example 1 - Connect to a specific peripheral according to the configuration and then disconnect. The configuration information included in this example is for demonstration purposes only:

```
AT+CONF BLECentral1={"peer": "a4:c1:38:12:56:5d", "filterDups": 1}{EOL}
OK{EOL}
AT+BLE INIT CENTRAL{EOL}
OK{EOL}
AT+BLE1 CONNECT{EOL}
OK{EOL}

   ...a BLE CONNECTED EVENT occurs...

AT+BLE1 DISCONNECT{EOL}
OK{EOL}
```

### 12.2.6 BLE*[\#}* READ*[\#]*   »Synchronous Read of a Characteristic«
<a name="elpg-ble-read-command"></a>

The READ command allows the host to request the value of a characteristic when connected to a peripheral. The BLE (first) numerical suffix \# identifies the connected device by the corresponding BLECentral\# parameter. The READ (second) numerical suffix \# identifies the characteristics by the corresponding BLEGATT\# parameter. The maximum value that can be read from a characteristic is 31 bytes.

<a name="elpg-figure9"></a>![Figure 9 - Reading a connected BLE peripheral](http://docs.aws.amazon.com/iot-expresslink/archive/v1.2/programmersguide/images/reading-a-connected-ble-peripheral.png)

 Returns:

**12.2.6.1**   `OK {value}{EOL}`
On a successful read, returns the characteristic value as a hex string.

**12.2.6.2**   `OK {EOL}`
On a successful read, when the characteristic value is an empty string.

**12.2.6.3**   `ERR8 PARAMETER UNDEFINED{EOL}`
When a BLECentral\# configuration is not set.

**12.2.6.4**   `ERR8 PARAMETER UNDEFINED{EOL}`
When a BLEGATT\# configuration is not set.

**12.2.6.5**   `ERR7 OUT OF RANGE{EOL}`
The first numerical suffix is out of bounds (0 or greater than MaxBLECentral).

**12.2.6.6**   `ERR7 OUT OF RANGE{EOL}`
The second numerical suffix is out of bounds (0 or greater than MaxBLEGATT).

**12.2.6.7**   `ERR6 NO CONNECTION{EOL}`
When not connected to a **peripheral** device.

**12.2.6.8**   `ERR27 BLE ERROR{EOL}`
When the read request fails.

**12.2.6.9**   `ERR25 NOT ALLOWED{EOL}`
If BLE INIT is not set to CENTRAL mode.

Example:

```
    # Assuming the configuration:
AT+CONF BLECentral1={"peer": "a4:c1:38:12:56:5d", "filterDups": 1}{EOL}
OK{EOL}

AT+CONF BLEGATT5={"service": "1f10", "chr": "1f1f"}{EOL}
OK{EOL}

    # BLE is initialized and a connection to a peripheral matching peer a4:c1:38:12:56:5d is established:
AT+BLE INIT CENTRAL{EOL}
OK{EOL}

AT+BLE1 CONNECT{EOL}
OK{EOL}

    # Requst the value of characteristic 0x1F1F (part of the service 0x1F10):
AT+BLE1 READ5{EOL}
OK 48656C6C6F20576F726C64{EOL}

    # Successfully retrieved the value "Hello World"!
```

### 12.2.7 BLE*[\#]* WRITE*[\#] {value}*   »Write to a characteristic«
<a name="elpg-ble-write-command"></a>

The WRITE command allows the host to update the value of (writable) characteristics of a connected peripheral device. The BLE (first) numerical suffix \# identifies the connected device by the corresponding BLECentral\# parameter. The WRITE (second) numerical suffix \#, identifies a characteristic by its corresponding BLEGATT\# parameter. The maximum supported value for write operations is 31 bytes.

<a name="elpg-figure10"></a>![Figure 10 - Writing to a connected BLE device](http://docs.aws.amazon.com/iot-expresslink/archive/v1.2/programmersguide/images/writing-to-connected-ble-device.png)

 Returns:

**12.2.7.1**   `OK{EOL}`
On a successful update of the peripheral characteristic.

**12.2.7.2**   `ERR4 PARAMETER ERROR{EOL}`
Must always take valid byte array encoded in hex as a valid parameter.

**12.2.7.3**   `ERR8 PARAMETER UNDEFINED{EOL}`
A BLEGATT\# configuration was not set.

**12.2.7.4**   `ERR7 OUT OF RANGE{EOL}`
The BLE Central numerical suffix is out of bounds (0 or greater than MaxBLECentral).

**12.2.7.5**   `ERR7 OUT OF RANGE{EOL}`
The BLEGATT numerical suffix is out of bounds (0 or greater than MaxBLEGATT).

**12.2.7.6**   `ERR6 NO CONNECTION{EOL}`
When not connected to a peripheral device.

**12.2.7.7**   `ERR25 NOT ALLOWED{EOL}`
The device was not initialized as a Central.

**12.2.7.8**   `ERR27 BLE ERROR{EOL}`
When the command fails to update the characteristic.

Example:

```
    # Assuming the configuration:
AT+CONF BLECentral2={"peer": "a4:c1:38:12:56:5d", "filterDups": 1}{EOL}
OK{EOL}

AT+CONF BLEGATT6={"service": "1f10", "chr": "1f1f"}{EOL}
OK{EOL}

    # After initializing and connecting to a peripheral device:
AT+BLE INIT CENTRAL{EOL}
OK{EOL}

AT+BLE1 CONNECT{EOL}
OK{EOL}

    # Request to update the characteristic 0x1F1F with the new value "01A3":
AT+BLE2 WRITE6 01A3{EOL}
OK{EOL}
```

### 12.2.8 BLE*[\#]* SUBSCRIBE*[\#]*   »Subscribe to a connected peripheral«
<a name="elpg-ble-subscribe-command"></a>

The host can subscribe to receive notifications (see [Table 4 - ExpressLink event codes](elpg-event-handling.md#elpg-table4)) when connected to a peripheral and the selected characteristic is updated (it must be configured as notify or indicate). The BLE (first) numerical suffix \# identifies the connected device by the corresponding BLECentral\# parameter. The SUBSCRIBE (second) numerical suffix \#, identifies the characteristic by its corresponding BLEGATT\# parameter.

<a name="elpg-figure11"></a>![Figure 11 - Subscribing to receive peripheral notifications](http://docs.aws.amazon.com/iot-expresslink/archive/v1.2/programmersguide/images/subscribe-to-peripheral-notifications.png)

 Returns:

**12.2.8.1**   `OK{EOL}`
On a successful subscription.

**12.2.8.2**   `ERR8 PARAMETER UNDEFINED{EOL}`
A BLEGATT\# configuration was not set.

**12.2.8.3**   `ERR7 OUT OF RANGE{EOL}`
The first numerical suffix is out of bounds (0 or greater than MaxBLECentral).

**12.2.8.4**   `ERR7 OUT OF RANGE{EOL}`
The second numerical suffix is out of bounds (0 or greater than MaxBLEGatt).

**12.2.8.5**   `ERR6 NO CONNECTION{EOL}`
When not connected to a peripheral device.

**12.2.8.6**   `ERR25 NOT ALLOWED{EOL}`
The command can only be executed when initialized as a Central.

**12.2.8.7**   `ERR27 BLE ERROR{EOL}`
When the command fails to successfully subscribe to the indexed characteristics. ExpressLink will support a limited number of subscriptions (minimum 2). The max number of supported subscriptions must be documented by the vendor in the module datasheet.

Example:

```
    # Assuming the configuration:
AT+CONF BLECentral1={"peer": "a4:c1:38:12:56:5d", "filterDups": 1}{EOL}
OK{EOL}
AT+CONF BLEGATT7={"service":"1809", "chr":"1F1F"}{EOL}
OK{EOL}

    # After initializing and connecting to a peripheral device:
AT+BLE INIT CENTRAL{EOL}
OK{EOL}
AT+BLE1 CONNECT{EOL}
OK{EOL}

    # Request to be notified to
AT+BLE1 SUBSCRIBE7{EOL} OK

   ...EVENT 50 101 SUBSCRIPTION RECEIVED...
```

### 12.2.9 BLE*[\#]* GET SUBSCRIBE*[\#]*   »Get information on Subscriptions«
<a name="elpg-ble-get-subscribe-command"></a>

After receiving the event subscribed to, the host can retrieve additional detail about the notification. The first BLE numerical suffix \# identifies the connected device by the corresponding BLECentral\# parameter. The SUBSCRIBE (second) numerical suffix \# identifies the characteristic by its corresponding BLEGATT\# parameter. The second numerical index is optional- if not specified, the most recent subscription detail will be retrieved.Returns:

**12.2.9.1**   `OK{EOL}`
No notification detail record was found.

**12.2.9.2**   `OK {BLEGATT#} [N|I] {detail}{EOL}`
A notification detail record was found.

**12.2.9.3**   `ERR7 OUT OF RANGE{EOL}`
The first numerical suffix is out of bounds (0 or greater than MaxBLECentral).

**12.2.9.4**   `ERR7 OUT OF RANGE{EOL}`
The second numerical suffix is out of bounds (0 or greater than MaxBLEGatt).

**12.2.9.5**   `ERR8 PARAMETER UNDEFINED{EOL}`
A BLECentral\# configuration was not set.

**12.2.9.6**   `ERR25 NOT ALLOWED{EOL}`
If the device is not initialized in the Central role.

Example 1:

```
    # Assuming the configuration:
AT+CONF BLECentral1={"peer": "a4:c1:38:12:56:5d", "filterDups": 1}{EOL}
OK{EOL}
AT+CONF BLEGATT2={"service":"1809", "chr":"1F1F"}{EOL}
OK{EOL}

    # After initializing and connecting to a peripheral device:
AT+BLE INIT CENTRAL{EOL}
OK{EOL}
AT+BLE1 CONNECT{EOL}
OK{EOL}

   # Subscribe to notifications/indication provided by characteristic 0x1F1F
AT+BLE1 SUBSCRIBE2{EOL}
OK{EOL}

   ...EVENT 48 102 SUBSCRIPTION received...

    # Request additional information:
AT+BLE1 GET SUBSCRIBE2{EOL}
OK 2 N 021A45{EOL}
```

### 12.2.10 BLE*[\#]* UNSUBSCRIBE*[\#]*   »Unsubscribe to characteristics«
<a name="elpg-ble-unsubscribe-command"></a>

Terminate a notify or indicate subscription to a peripheral device characteristic.Returns:

**12.2.10.1**   `OK{EOL}`
On successfully terminating the subscription to the peripheral characteristic.

**12.2.10.2**   `ERR8 PARAMETER UNDEFINED{EOL}`
A BLECentral\# configuration was not set.

**12.2.10.3**   `ERR8 PARAMETER UNDEFINED{EOL}`
A BLEGATT\# configuration was not set.

**12.2.10.4**   `ERR7 OUT OF RANGE{EOL}`
The BLECentral numerical suffix is out of bounds (0 or greater than MaxBLECentral).

**12.2.10.5**   `ERR7 OUT OF RANGE{EOL}`
The BLEGATT numerical suffix is out of bounds (0 or greater than MaxBLEGATT).

**12.2.10.6**   `ERR6 NO CONNECTION{EOL}`
When not connected to a peripheral device.

**12.2.10.7**   `ERR25 NOT ALLOWED{EOL}`
The command can only be executed when initialized as a Central.

**12.2.10.8**   `ERR27 BLE ERROR{EOL}`
When the command fails to successfully unsubscribe from the selected characteristic.

Example:

```
    # Assuming the configuration:
AT+CONF BLECentral1={"peer": "a4:c1:38:12:56:5d", "filterDups": 1}{EOL}
OK{EOL}
AT+CONF BLEGATT8={"service":"1809", "chr":"1F1F"}{EOL}
OK{EOL}

    # After initializing and connecting to a peripheral device and subscribing to notifications:
AT+BLE INIT CENTRAL{EOL}
OK{EOL}
AT+BLE1 CONNECT{EOL}
OK{EOL}
AT+BLE1 SUBSCRIBE8{EOL}
OK{EOL}

 ...EVENT 50 108 SUBSCRIPTION received...

AT+BLE1 UNSUBSCRIBE8{EOL}
OK{EOL}

    # No more subscription events will be generated for the selected characteristic.
```

## 12.3 BLE PERIPHERAL role commands
<a name="elpg-ble-peripheral-role-commands"></a>

When initialized as a Peripheral device, an ExpressLink module waits for connections initiated by central devices. Only one Central device at a time can connect to a module initialized as Peripheral.

### 12.3.1 BLE CONNECT?   »Connection status query«
<a name="elpg-ble-connectq-command"></a>

Request the current Peripheral device connection status.Returns:

**12.3.1.1**   `OK 0 NOT CONNECTED{EOL}`
When not connected to a Central device.

**12.3.1.2**   `OK 1 CONNECTED{EOL}`
When connected to a Central device.

**12.3.1.3**   `OK 2 ADVERTISING{EOL}`
When advertising is in progress.

**12.3.1.4**   `ERR25 NOT ALLOWED{EOL}`
When the module role was not initialized as Peripheral.

Example:

```
AT+CONF BLEPeripheral={"appearance": "4142"}{EOL}
OK{EOL}
AT+CONF BLEGATT1=={"service":"1809", "chr":"1F1F"}{EOL}
OK{EOL}
AT+BLE INIT PERIPHERAL{EOL}
OK{EOL}
AT+BLE CONNECT?{EOL}
OK 0 NOT CONNECTED{EOL}

    # Currently initialized in peripheral role but not connected to a central device.
```

### 12.3.2 BLE DISCONNECT   »Connection termination request«
<a name="elpg-ble-disconnect-command"></a>

Terminate the current connection, if one was established by a central device.Returns:

**12.3.2.1**   `OK{EOL}`
On successfully terminating the connection of if there was no connection to terminate.

**12.3.2.2**   `ERR25 NOT ALLOWED{EOL}`
When the module role was not initialized as Peripheral.

**12.3.2.3**   `ERR27 BLE ERROR{EOL}`
If the command fails to terminate the connection.

Example:

```
    # When initialized as a peripheral and wishes to disconnect from central device.
AT+CONF BLEPeripheral={“appearance”: “4142”}{EOL}
OK{EOL}
AT+CONF BLEGATT1={“service”:”1809”, ”chr”:”1F1F”}{EOL}
OK{EOL}
AT+BLE INIT PERIPHERAL{EOL}
OK{EOL}

   ...A central device connects...
   ...a BLE CONNECTED EVENT occurs...

    # The host wishes to terminate the connection with the central device:
AT+BLE DISCONNECT{EOL}
OK{EOL}
```

### 12.3.3 BLE ADVERTISE *{*CANCEL*}*   »Advertise to nearby devices«
<a name="elpg-ble-advertise-command"></a>

Start the advertising process, making the module a connectable, scannable device. The process will continue until connected or cancelled by AT\+BLE ADVERTISE CANCEL.Returns:

**12.3.3.1**   `OK{EOL}`
When the ExpressLink module successfully starts the Advertising process.

**12.3.3.2**   `OK{EOL}`
On successfully canceling advertisements, or if not currently advertising.

**12.3.3.3**   `ERR4 PARAMETER ERROR{EOL}`
When initialized as a peripheral and the command is provided with an index \#.

**12.3.3.4**   `ERR27 BLE ERROR{EOL}`
When the Advertising process fails to start.

**12.3.3.5**   `ERR27 BLE ERROR{EOL}`
When the Advertising process fails to terminate (with the CANCEL parameter).

**12.3.3.6**   `ERR25 NOT ALLOWED{EOL}`
If BLE INIT is not set to PERIPHERAL mode.

Example 1 - A successful startup of the advertising process:

```
AT+CONF BLEPeripheral={“appearance”: “4142”}{EOL}
OK{EOL}
AT+CONF BLEGATT1={ "service" : "72bdd8d118874a3fbedaf6c22d45cfa0", "chr": "72bdd8d218874a3fbedaf6c22d45cfa0"}{EOL}
OK{EOL}
AT+BLE INIT PERIPHERAL{EOL}
OK{EOL}
AT+BLE ADVERTISE{EOL}
OK{EOL}

    # Now other devices can discover the ExpressLink device
```

Example 2 - When the necessary configuration CONF BLEPeripheral and/or BLEGATT\# are missing:

```
AT+CONF BLEGATT1={ "service" : "72bdd8d118874a3fbedaf6c22d45cfa0", "chr": "72bdd8d218874a3fbedaf6c22d45cfa0"}{EOL}
OK{EOL}
AT+BLE INIT PERIPHERAL{EOL}
ERR28 CONFIGURATION ERROR{EOL}
```

Example 3 - Cancelling an ongoing Advertisement:

```
AT+CONF BLEPeripheral={“appearance”: “4142”}{EOL}
OK{EOL}
AT+CONF BLEGATT1={"service" : "72bdd8d118874a3fbedaf6c22d45cfa0", "chr": "72bdd8d218874a3fbedaf6c22d45cfa0"}{EOL}
OK{EOL}
AT+BLE INIT PERIPHERAL{EOL}
OK{EOL}
AT+BLE ADVERTISE{EOL}
OK{EOL}

    # Now other devices can discover the ExpressLink device

AT+BLE ADVERTISE CANCEL{EOL}
OK{EOL}
```

### 12.3.4 BLE GET*[\#]*   »Synchronous read of a local characteristic«
<a name="elpg-ble-get-command"></a>

The BLE GET command allows the host to perform a synchronous read of the value of a local peripheral characteristic. The maximum value that can be retrieved from the local characteristic is 31 bytes.

<a name="elpg-figure12"></a>![Figure 12 - Reading from a local characteristic in BLE peripheral mode](http://docs.aws.amazon.com/iot-expresslink/archive/v1.2/programmersguide/images/reading-from-a-local-characteristic.jpg)

 Returns:

**12.3.4.1**   `OK {value}{EOL}`
The GET request was successful, the characteristic value is returned as a hex string.

**12.3.4.2**   `OK {EOL}`
On a successful get read, when the characteristic value is an empty string.

**12.3.4.3**   `ERR8 PARAMETER UNDEFINED{EOL}`
A BLEGATT\# configuration is not set.

**12.3.4.4**   `ERR7 OUT OF RANGE{EOL}`
The BLEGATT\# numerical suffix is out of bounds (0 or greater than MaxBLEGATT).

**12.3.4.5**   `ERR25 NOT ALLOWED{EOL}`
The characteristic can be only be read when the peripheral is initialized.

**12.3.4.6**   `ERR27 BLE ERROR{EOL}`
When the command fails to successfully read from a characteristic.

Example: Read value of local characteristics configured at BLEGATT1 index.

```
AT+BLE GET1{EOL}
OK 014A{EOL}
```

### 12.3.5 BLE SET*[\#} [payload]*   »Write to a local characteristic«
<a name="elpg-ble-set-command"></a>

The BLE SET command allows the host to perform a synchronous write to the value of a local peripheral characteristic. The maximum value that can be written to the local characteristic is 31 bytes.

<a name="elpg-figure13"></a>![Figure 13 - Writing to a connected BLE device](http://docs.aws.amazon.com/iot-expresslink/archive/v1.2/programmersguide/images/writing-to-a-local-characteristic.jpg)

 Returns:

**12.3.5.1**   `OK{EOL}`
On a successful write to the local characteristic.

**12.3.5.2**   `ERR4 PARAMETER ERROR{EOL}`
If the payload is not valid hex array.

**12.3.5.3**   `ERR8 PARAMETER UNDEFINED{EOL}`
If the BLEGATT\# configuration is not set.

**12.3.5.4**   `ERR7 OUT OF RANGE{EOL}`
If the numerical suffix is out of bounds (0 or greater than MaxBLEGATT).

**12.3.5.5**   `ERR25 NOT ALLOWED{EOL}`
The command can only be executed when initialized as a Peripheral.

**12.3.5.6**   `ERR27 BLE ERROR{EOL}`
When the command fails to set the value of a local characteristic.

Example- Update the value of local characteristics configured at BLEGATT2 index to 014A:

```
AT+BLE SET2 014A{EOL}
OK{EOL}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT ExpressLink. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-expresslink` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
