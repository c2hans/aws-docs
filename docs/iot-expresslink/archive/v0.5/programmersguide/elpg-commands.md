---
source_url: https://docs.aws.amazon.com/iot-expresslink/archive/v0.5/programmersguide/elpg-commands.html
---

# 3 ExpressLink commands
<a name="elpg-commands"></a>

These commands are sent to and from the UART. The default UART configuration shall be 115200, 8, N, 1 (baud rate: 115200; data bits: 8; parity: none; stop bits: 1). There is no hardware or software flow control for UART communications. The baud rate is NOT configurable.

## 3.1 ExpressLink commands format
<a name="elpg-commands-format"></a>

All ExpressLink commands assume the following general format:

◊ `AT+{command}[#][?]{separator}[parameter]{eol}`

Where:

3.1.1 `{command}`
A short, alphabetical character string matching one of the commands listed in the following sections (CONNECT, SEND).
**Note**: Commands are not case sensitive, although in this document, uppercase is always used for consistency.
**Returns:**
3.1.1.1 `ERR3 COMMAND NOT FOUND`
If the command is unknown, then the module returns 'COMMAND NOT FOUND'.

3.1.2 `[#]`
An optional decimal (0..N) suffix qualifier (multiple digits allowed, only used by a few commands).
**Returns:**
3.1.2.1 `ERR4 PARAMETER ERROR`
If the command does not use a numeric suffix, the module returns 'PARAMETER ERROR'.
3.1.2.2 `ERR4 PARAMETER ERROR`
If the numeric suffix is out of the valid range for the command, the module returns 'PARAMETER ERROR'.

3.1.3 `[?]`
A query marker used with some commands to indicate that information is being requested.
**Returns:**
3.1.3.1 `ERR22 INVALID QUERY`
If the command does not respond to a query request, then the module returns 'INVALID QUERY'.

3.1.4 `{separator}`
A single ASCII space character (0x20).
**Returns:**
3.1.4.1 `ERR2 PARSE ERROR`
If ANY character other than 0x20 is present after the first digit or '?' in the command string, then the module returns 'PARSE ERROR'.

3.1.5 `[parameter]`
An (escaped) ASCII string with the data required for the command.
**Returns:**
3.1.5.1 `ERR4 PARAMETER ERROR`
If the command is unable to process the parameter supplied, then the module returns 'PARAMETER ERROR'.

3.1.6 `{eol}`
A single ASCII newline character (0x0a).

3.1.7 Parameter string note
The parameter string includes all bytes from the separator to the {eol}, not including either the separator or the {eol}. ALL ASCII values from 0 - 0x1F are valid in the parameter string.

3.1.8 Numerical suffix range
The maximum value allowed for the numerical suffix is implementation-specific (typically 0-15).

## 3.2 Delimiters and escaping
<a name="elpg-delimiters"></a>

The format described in the previous section, and the specific choice of delimiters, removes the need for quotes surrounding parameters, and for other delimiters between successive parameters. As a further benefit, this removes the need for most escaping sequences with the exclusion of the ASCII characters {eol} (0x0a) and backslash ('\\').

3.2.1 Escaping {eol} in the parameter string
{eol} (0x0a) in the parameter string is represented by the following sequence: 0x5C 0x41

3.2.2 Escaping backslash ('\\') in the parameter string
Backslash (0x5C) in the parameter string is represented by the following sequence: 0x5C 0x5C
3.2.2.1 All other combinations of the escape sequence are illegal and the module returns 'ERR5 INVALID ESCAPE'.

## 3.3 Maximum values
<a name="elpg-max-values"></a>

3.3.1 Maximum bytes in the formatted command string
The formatted command string as received by ExpressLink can be up to 5K bytes in length.
◊ `AT+[ 5K bytes ]{eol}`

3.3.2 Maximum command word size
The command word portion of the command string can be up to 32 bytes long.

## 3.4 Data processing
<a name="elpg-data-processing"></a>

3.4.1 Data entry
The data entry for a command begins with the 'AT\+' and ends with the {eol}. The module will not begin running a command before receiving the {eol}.

3.4.2 Data overflow
If the data buffer overflows during the data entry phase of a command, the ExpressLink module continues to accept, but discards, the incoming data until the next {eol} arrives.
3.4.2.1 The module returns 'ERR1 OVERFLOW' and the entire message is discarded.

3.4.3 Data arriving after {eol}
Any data that arrives after {eol} and before 'AT\+' will be ignored and discarded.

## 3.5 Command responses and error codes
<a name="elpg-responses"></a>

All commands respond when the command has been completed. In some cases, this can take a significant amount of time.

### 3.5.1 General response formats:
<a name="elpg-responses-formats"></a>

◊ `OK|ERR{#}{separator}[detail]{eol}`

Where:
+ **OK**: Indicates that the command was valid and ran.
+ **ERR{\#}**: Error codes are listed in [Table 1 - Error codes](#elpg-table1).
+ *{separator}*: Is a single ASCII space character (0x20).
+ *[detail]*: Is an optional ASCII string.
+ *{eol}*: Is a single ASCII newline character (0x0a).

**Table 1 - Error codes**

| Code | ExpressLink text | Description |
| --- | --- | --- |
| 1 | OVERFLOW | More bytes have been received than fit in the receive buffer.  |
| 2 | PARSE ERROR | Message not formatted correctly. |
| 3 | COMMAND NOT FOUND | Invalid command. |
| 4 | PARAMETER ERROR | Command does not recognize the parameters. |
| 5 | INVALID ESCAPE | An incorrect escape sequence was detected. |
| 6 | NO CONNECTION | Command requires an active connection to AWS IoT. |
| 7 | TOPIC OUT OF RANGE | The topic index is larger than the maximum valid topic index. |
| 8 | TOPIC UNDEFINED | The topic index provided references an empty topic position. |
| 9 | INVALID KEY LENGTH | Key is longer than 16 characters. |
| 10 | INVALID KEY NAME | A non-alphanumeric character was used in the key name. |
| 11 | UNKNOWN KEY | The supplied key cannot be found in the system. |
| 12 | KEY READONLY | The key cannot be written. |
| 13 | KEY WRITEONLY | The key cannot be read. |
| 14 | UNABLE TO CONNECT | The module is unable to connect. |
| 15 | TIME NOT AVAILABLE | A time fix could not be obtained. |
| 16 | LOCATION NOT AVAILABLE | A location fix could not be obtained. |
| 17  | MODE NOT AVAILABLE | The requested mode is not available. |
| 18 | ACTIVE CONNECTION | An active connection prevents the command from running. |
| 19 | HOST IMAGE NOT AVAILABLE | A host OTA command was issued but no valid HOTA image is present in the OTA buffer. |
| 20 | INVALID ADDRESS | The OTA buffer pointer is out of bounds (> image size). |
| 21 | INVALID OTA UPDATE  | The OTA update failed. |
| 22  | INVALID QUERY | The command does provide a query option. |
| 23  | INVALID SIGNATURE | A signature verification failed. |

### 3.5.2 Response timeout
<a name="elpg-response-timeout"></a>

The maximum runtime for every command must be listed in the datasheet. No command can take more than 120 seconds to complete (the maximum time for a TCP connection timeout).

### 3.5.3 AT: Communication test
<a name="elpg-at-command"></a>

By sending only the 'AT' (attention) command, the host can verify the presence and readiness of the module command parser.

Example:

```
AT{eol}    # request the module's attention
```Returns:

`OK{eol}`
If the module is connected and the command parser active, then the module returns 'OK'.

## 3.6 Power and connection control
<a name="elpg-power-control"></a>

### 3.6.1 CONNECT?: Request the connection status
<a name="elpg-connectq-command"></a>

Requests the current status of the module's connection to the AWS cloud.Returns:

`OK {status}`
3.6.1.1 `OK 1 `
If the connection is active, then the module returns 'OK 1'.
3.6.1.2 `OK 0 `
If the connection is inactive, then the module returns 'OK 0'.

### 3.6.2 CONNECT: Explicitly request a module to connect to AWS IoT Core
<a name="elpg-connect-command"></a>

Request a connection to the AWS cloud, bringing an active device into a higher power consumption mode where it is able to communicate with the AWS IoT Core endpoint.Returns:

3.6.2.1 `OK 1 CONNECTED`
The module has successfully connected to AWS IoT Core.

3.6.2.2 `ERR14 UNABLE TO CONNECT [detail]`
The module is unable to connect. Additional clues can be provided by the optional *[detail]* provided (for example, 'Invalid Endpoint').

If the ExpressLink module is already connected, issuing a CONNECT command does not return an error, but simply returns immediately with a success value ('OK CONNECTED').

In case of a connection failure, the ExpressLink module keeps a timestamp of the event. This is used to ensure that a subsequent (repeated) connection request complies with the correct backoff timing limits. If the retry request from the host arrives too close to the previous attempt (the interval between requests is shorter than the prescribed minimum backoff time), the ExpressLink module automatically delays running the command. Delays will increase according to the backoff algorithm until a successful connection is established.

Example:

```
AT+CONNECT        # request to connect
OK 1 CONNECTED    # connection established successfully
```

Or

```
ERR14 UNABLE TO CONNECT Invalid Endpoint
```

### 3.6.3 DISCONNECT: Leave the connected state and enter the active state
<a name="elpg-disconnect-command"></a>

This command allows the host to prepare for a transition to low power (using the SLEEP command), or to update the connection parameters before it attempts to reconnect again with the changed parameters (using a new CONNECT command).Returns:

3.6.3.1 `OK 0 DISCONNECTED`

If the module is already disconnected, the command does not return an error, and instead returns immediately with a success value ('OK').

### 3.6.4 SLEEP*\# [duration]*: Request to enter a low power mode
<a name="elpg-sleeph-command"></a>

This command forces the module to enter a low power mode. ExpressLink module manufacturers can implement specific low power modes with increasing values (\#) that correspond to deeper sleep states (as capable) to provide the lowest power consumption and longest possible battery life. The duration parameter, if present, indicates the number of seconds before the module awakes automatically. If absent, the module remains in low power mode until a Reset event is generated externally, or a new AT CONNECT command is received.

A SLEEP command without a numerical suffix defaults to mode 0. This is a basic low power mode where the ExpressLink module disconnects and reduces its power consumption as low as possible. At the same time, it maintains the serial interface active, and preserves the contents of all configuration parameters and the status dictionary.

Be aware that *advanced low power modes* can deactivate the serial command interface. In these cases, in absence of the sleep duration parameter, the only way to awaken the device is to apply an external reset signal.

Similarly, a deep sleep state might imply loss of all volatile (RAM) information, including all module state information and configuration parameters that are not maintained in non-volatile memory (for example, Topics). The host processor must reconfigure such parameters as required by the application.Returns:

3.6.4.1 `OK [{detail}]`
The device is ready and will immediately proceed to the lower power mode selected.

3.6.4.2 `ERR18 ACTIVE CONNECTION`
The device cannot transition to a low power mode because there is an active cloud connection. Use the DISCONNECT command first to shut down the connection.

Example 1:

```
AT+SLEEP 100  # Disconnect and suspend all activities for 100 seconds
OK            # Drop connections and goes to sleep
AT+CONNECT    # Resume connection and all pending activities
```

Example 2:

```
AT+SLEEP9     # Goes to deep sleep (proprietary mode) indefinitely
OK
```

Note that the device might require a hardware reset to be re-awakened, and all status (non-volatile) information might be lost requiring a new initialization and configuration.

### 3.6.5 CONFMODE *[parameter]*: Activate modal credential entry
<a name="elpg-confmode-command"></a>

ExpressLink modules that require additional user credentials can be set by the host to enter CONFMODE (see [Figure 1](elpg-run-states.md#elpg-figure1)) to enable or repurpose an interface to receive additional connection credentials from user input.

**Example 1:** An ExpressLink Wi-Fi module could use this command to enter a SoftAP mode, temporarily assume the role of an Access Point, and serve an HTML form. This would allow the user to enter the local Wi-Fi router credentials using a mobile device web browser. The optional parameter could be used to provide a customized, unique SSID based on the device UID.

**Example 2:** If a Bluetooth interface is available, the ExpressLink module could receive the credentials using a serial interface (SPP profile). For Bluetooth LE modules, this could be performed using a dedicated (GATT) service using a custom mobile application.Returns:

3.6.5.1 `OK CONFMODE ENABLED`
The device has entered CONFMODE and is ready to receive user input.

3.6.5.2 `ERR17 MODE NOT AVAILABLE`
This ExpressLink model/version does not support CONFMODE.

3.6.5.3 `ERR18 CURRENT CONNECTION`
The device cannot enter CONFMODE because it is currently connected. The host must disconnect first.

While in CONFMODE, an ExpressLink module can still process all commands that do not require an active connection (for example, 'AT\+CONF? Version'). Commands that require an active connection return 'ERR6 NO CONNECTION'. Attempting to issue a CONNECT command while in CONFMODE results in an 'ERR14 UNABLE TO CONNECT'.

The host may issue a RESET command at any time to shut down CONFMODE (see [ Figure 1](elpg-run-states.md#elpg-figure1)).

A CONFMODE notification event (see [Table 4 - ExpressLink event codes](elpg-event-handling.md#elpg-table4) is provided to the host when the entry of new credentials has been completed. Only after that can the host issue a new CONNECT command to attempt to establish a connection using the newly entered credentials.

### 3.6.6 RESET: Request a reset of the ExpressLink internal state
<a name="elpg-reset-command"></a>

This command disconnects the device (if connected) and resets its internal state. Non-persistent configuration parameters (see [Table 3 - Configuration Dictionary Non-persistent Keys](elpg-configuration-dictionary.md#elpg-table3)) are reinitialized, all subscriptions are terminated, and the message queue is emptied. Returns:

3.6.6.1 `OK`
If the command was successful, the module returns 'OK'.

### 3.6.7 FACTORY\_RESET: Request a factory reset of the ExpressLink module
<a name="elpg-factory-reset-command"></a>

This command performs a full factory reset of the ExpressLink module, including re-initializing all non-persistent configuration parameters (see [Table 3 - Configuration Dictionary Non-persistent Keys](elpg-configuration-dictionary.md#elpg-table3)), but also selected persistent parameters as indicated in [Table 2 - Configuration Dictionary Persistent Keys](elpg-configuration-dictionary.md#elpg-table2) (see the Factory Reset column).Returns:

3.6.7.1 `OK`
If the command was successful, the module returns 'OK'.
