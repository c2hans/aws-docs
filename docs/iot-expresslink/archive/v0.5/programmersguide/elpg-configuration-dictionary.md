---
source_url: https://docs.aws.amazon.com/iot-expresslink/archive/v0.5/programmersguide/elpg-configuration-dictionary.html
---

# 5 Configuration Dictionary
<a name="elpg-configuration-dictionary"></a>

The configuration dictionary is a key-value store containing all the options necessary for the proper functioning of ExpressLink modules.

## 5.1 Data values referenced
<a name="elpg-data-values"></a>

5.1.1.1 Maximum key length is 16 characters
A key can be from 1 to 16 characters.

5.1.1.2 `ERR9 INVALID KEY LENGTH`
If the command sends a key with more than 16 characters, the ExpressLink module returns 'ERR9 INVALID KEY LENGTH'.

5.1.1.3 Valid key characters are 0-9, A-Z, a-z
A key may only contain alphanumeric characters in any order.

5.1.1.4 `ERR10 INVALID KEY NAME`
If a non-alphanumeric character is used in a key name, then the ExpressLink module returns 'ERR10 INVALID KEY NAME'.

5.1.1.5 `ERR11 UNKNOWN KEY`
All keys are predefined in the ExpressLink module. If an invalid key is used, then the module returns 'ERR11 UNKNOWN KEY'.

## 5.2 Data accessed through the CONF command
<a name="elpg-data-accessed-conf"></a>

### 5.2.1 Assignment using 'CONF *key*=*value*'
<a name="elpg-assignment-conf"></a>Returns:

5.2.1.1 `OK`
If the write is successful, then the module returns 'OK'.

5.2.1.2 `ERR9 INVALID KEY LENGTH`
If the key is too long, then the module returns 'INVALID KEY LENGTH'.

5.2.1.3 `ERR10 INVALID KEY NAME`
If the key uses incorrect characters, then the module returns 'INVALID KEY NAME'.

5.2.1.4 `ERR11 UNKNOWN KEY`
If the key is not present in the system, then the module returns 'UNKNOWN KEY'.

5.2.1.5 `ERR12 KEY READONLY`
Some keys are read-only and cannot be written. If the key is not present in the system, then the module returns 'KEY READONLY'.

Example 1:

```
AT+CONF VERSION=HELLO
ERR12 KEY READONLY
```

### 5.2.2 Retrieval using 'CONF? *key*'
<a name="elpg-retrieval-conf"></a>Returns:

5.2.2.1 `OK`
If the read is successful, then the module returns 'OK'.

5.2.2.2 `ERR9 INVALID KEY LENGTH`
If the key is too long, then the module returns 'INVALID KEY LENGTH'.

5.2.2.3 `ERR10 INVALID KEY NAME`
If the key uses incorrect characters, then the module returns 'INVALID KEY NAME'.

5.2.2.4 `ERR11 UNKNOWN KEY`
If the key is not present in the system, then the module returns 'UNKNOWN KEY'.

5.2.2.5 `ERR13 KEY WRITEONLY`
Some keys are write-only and cannot be read. If the key cannot be read, then the module returns 'KEY WRITEONLY'.

Example 2:

```
AT+CONF? Passphrase
ERR13 KEY WRITEONLY
```

Key-value pairs can be used to set default values for command parameters, to set credentials, and to select connectivity options and timing preferences. These configuration key-value pairs are meant to be long-lived (persist) throughout the life of the application and are therefore stored in non-volatile memory. A basic set of key-value pairs is defined for all ExpressLink devices (EndPoint, Certificate). Some of these key-value pairs have factory presets and/or are read only.

**Table 2 - Configuration Dictionary Persistent Keys**

| Configuration Parameter | Type | Persist | Initial Value | Factory Reset | Description |
| --- | --- | --- | --- | --- | --- |
| About | R | Y | Vendor - Model | N | A descriptive string that uniquely identifies the device make and model - communication capabilities. |
| Version | R | Y | Current module firmware version | N | The specific ExpressLink firmware version. |
| TechSpec | R | Y | Technical Specification Compatibility | N | The Technical Specification version this model is based upon (for example 'v0.6'). |
| ThingName | R | Y | UID | N | The UID as natively provided by the module HW root of trust. |
| Certificate | R | Y | Device Birth Certificate | N | Device certificate used to authenticate with AWS cloud, signed by the manufacturer CA. |
| EndPoint | R/W | Y | Staging account endpoint | Y | The endpoint of the AWS account to which the ExpressLink module connects. |
| TopicRoot | R/W | Y | UID | Y | The default prefix that is used for all user defined topics. |
| Defender | R/W | Y | 0 | Y | The Device Defender upload interval in seconds. (0 indicates the service is disabled.) |
| HOTAcertificate | R/W | Y | {empty} | Y | Host OTA certificate (see chapter 9.10). |
| OTAcertificate | R/W | Y | Vendor OTA Certificate | N | Module OTA certificate. Vendor and Model specific (see chapter 9.5). (Wi-Fi modules only.) |
| SSID | R/W | Y | {Empty} | Y | SSID of local router (Wi-Fi modules only). |
| Passphrase | W | Y | {Empty} | Y | Passphrase of local router (Wi-Fi modules only). |
| APN | R/W | Y | {default} | Y | Cellular modules only. |

Additional configuration parameters are *non-persistent*, and they are re-initialized at power up, or following any reset event. Among these are the topics list items. The host processor has to re-initialize them following any reset, and possibly a deep-sleep awakening (depending on the implementation).

**Table 3 - Configuration Dictionary Non-persistent Keys**

| Configuration Parameter | Type | Persist | Initial Value | Description |
| --- | --- | --- | --- | --- |
| IPv4Address | R | N | 0.0.0.0 | Current device IPv4 address |
| IPv6Address | R | N | :: | Current device IPv6 address |
| DNSAddress | R | N | 0.0.0.0  | Current DNS address (IPv4 or IPv6) |
| GatewayAddress | R | N | 0.0.0.0 | Current router IP address (IPv4 or IPv6) |
| Topic1 | R/W | N | {Empty} | Custom defined topic 1 |
| Topic2 | R/W | N | {Empty} | Custom defined topic 2 |
| ... |  |  |  |  |
| Topic<Max Topic> | R/W | N | {Empty} | Custom defined topic MaxTopic |

## 5.3 Configuration commands
<a name="elpg-configuration-commands"></a>

### 5.3.1 CONF *key=value*: Assign a value to selected configuration parameter
<a name="elpg-conf-command"></a>

Assigns a specific value to the specified configuration parameter.Returns:

`OK`
If the command was successful, the module returns 'OK'.

`ERR# {message}`
If the command was not successful, the module returns an error.

Example:

```
AT+CONF SSID=MY_SSID    # Assign the preferred (local) Wi-Fi router SSID
```

### 5.3.2 CONF? *key*: Read value of selected configuration parameter
<a name="elpg-confq-command"></a>

Query the value of a configuration parameter. Returns:

`OK {value}`
If the command was successful, the module returns 'OK' followed by the value.

`ERR# {message}`
If the command was not successful, the module returns an error.

Example:

```
AT+CONF? MyParameter
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT ExpressLink. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-expresslink` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
