---
source_url: https://docs.aws.amazon.com/iot-expresslink/archive/v1.1.1/programmersguide/elpg-configuration-dictionary.html
---

# 5 Configuration Dictionary
<a name="elpg-configuration-dictionary"></a>

The configuration dictionary is a key-value store containing all the options necessary for the proper functioning of ExpressLink modules. All keys are case sensitive.

Configuration key-value pairs listed in Table 2 are meant to be long lived (persist) throughout the life of the application and so are stored in non-volatile memory. Note that these key-value pairs have factory preset values, and can be read only or write only.

**Table 2 - Configuration dictionary persistent keys**

| Configuration Parameter | Type | Initial Value | Factory Reset | Buff Size | Description |
| --- | --- | --- | --- | --- | --- |
| About | R | Vendor - Model | N | 64 | A concatenation of Vendor name and Model name. |
| Version | R | X.Y.Z | N | 32 | The specific module firmware version. |
| TechSpec | R | TechSpec version | N | 16 | The Technical Specification version this model implements (for example 'v0.6', 'v1.1'). |
| ThingName | R | UID | N | 64 | The UID provided by the HW root of trust and present in the device certificate (also see [9.1.3 ExpressLink Birth Certificate](elpg-provisioning.md#elpg-provisioning-birth-certificate)). |
| Certificate | R | Device Birth Certificate | N | ≥4KB | Device certificate used to authenticate with AWS cloud, signed by the manufacturer CA (also see [9.1.3 ExpressLink Birth Certificate](elpg-provisioning.md#elpg-provisioning-birth-certificate)). |
| CustomName | R/W | {empty} | Y | ≥128 | Custom Product Name, can be set by the host. |
| Endpoint | R/W | Staging account endpoint | Y | ≥128 | The endpoint of the AWS account to which the ExpressLink module connects (also see [9.3.2 ExpressLink onboarding states and transitions](elpg-provisioning.md#elpg-provisioning-onboarding-states)). |
| RootCA | R/W | AWS root CA | N | ≥4KB | The server root certificate that will be used to authenticate the cloud Endpoint (also see [7.12 Server Root Certificate Update](elpg-ota-updates.md#elpg-server-root-cert)). |
| ShadowToken | R/W | ExpressLink | Y | 64 | The default client-token that will be used to mark Device Shadow updates. |
| DefenderPeriod | R/W | 0 | Y | ≥8 | The Device Defender upload period in seconds. (0 indicates the service is disabled.) |
| HOTAcertificate | R/W | {empty} | Y | ≥4KB | Host OTA certificate (see [7.10 Host OTA Signature Verification](elpg-ota-updates.md#elpg-hota-sig-verification)). |
| OTAcertificate | R/W | Vendor OTA Certificate | N | ≥4KB | Module OTA certificate. Vendor and Model specific (see [7.5 Module OTA signature verification](elpg-ota-updates.md#elpg-ota-signature-verification)). (Wi-Fi modules only.) |
| SSID | R/W | {Empty} | Y | 32 | SSID of local router (Wi-Fi modules only). |
| Passphrase | W | {Empty} | Y | 64 | Passphrase of local router (Wi-Fi modules only). |
| APN | R/W | {default} | Y | 128 | Access Point Name (Cellular modules only). |

The additional configuration parameters in Table 3 are non-persistent. They are re-initialized at power up, and following any reset event. The host processor might have to re-configure them following a reset and (possibly) a *deep sleep* awakening (depending on the implementation).

**Table 3 - Configuration dictionary non-persistent keys**

| Configuration Parameter | Type | Initial Value | Buff Size | Description |
| --- | --- | --- | --- | --- |
| QoS | R/W | 0 | 1 | QoS level selected for SEND commands |
| Topic1 | R/W | {Empty} | ≥128 | Custom defined topic 1 |
| Topic2 | R/W | {Empty} |  | Custom defined topic 2 |
| ... |  |  |  |  |
| Topic<Max Topic> | R/W | {Empty} |  | Custom defined topic MaxTopic |
| EnableShadow | R/W | 0 | 1 | 0 - disabled, or 1 - enabled |
| Shadow1 | R/W | {Empty} | 64 | Custom defined named shadow |
| ... |  |  |  |  |
| Shadow<MaxShadow> | R/W | {Empty} |  | Custom defined named shadow |

## 5.1 Data values referenced
<a name="elpg-data-values"></a>

**5.1.1.1**   Maximum key length is 16 characters
A parameter name (key) can be from 1 to 16 characters.
**Returns:**
**5.1.1.2**   `ERR9 INVALID KEY LENGTH`
If a parameter name (key) exceeds 16 characters, the ExpressLink module returns 'ERR9 INVALID KEY LENGTH'.

**5.1.1.3**   Valid key characters are 0-9, A-Z, a-z
A parameter name (key) may only contain alphanumeric characters.
**Returns:**
**5.1.1.4**   `ERR10 INVALID KEY NAME`
If a non-alphanumeric character is used in a key name, then the ExpressLink module returns 'ERR10 INVALID KEY NAME'.
**5.1.1.5**   `ERR11 UNKNOWN KEY`
If the parameter name (key) is not found in [Table 2 - Configuration dictionary persistent keys](#elpg-table2) or [Table 3 - Configuration dictionary non-persistent keys](#elpg-table3), then the module returns 'ERR11 UNKNOWN KEY'.
**5.1.1.6**   `ERR4 PARAMETER ERROR`
If the parameter (value) length exceeds the buffer size as defined in [Table 2 - Configuration dictionary persistent keys](#elpg-table2) or [Table 3 - Configuration dictionary non-persistent keys](#elpg-table3).

## 5.2 Data accessed through the CONF command
<a name="elpg-data-accessed-conf"></a>

### 5.2.1 CONF KEY=*{value}*   »Assignment«
<a name="elpg-assignment-conf"></a>

Assign a value to a configuration parameter present in the configuration dictionary. (See [7.11.1 CONF? *{certificate} pem*   »Special certificate output formatting option«](elpg-ota-updates.md#elpg-ota-confq-command)).Returns:

**5.2.1.1**   `OK{EOL}`
If the write is successful, then the module returns 'OK'.
Example:

```
AT+CONF Topic1={EOL}  # Assign the empty string to Topic 1
OK
```

**5.2.1.2**   `ERR9 INVALID KEY LENGTH`
If the key is too long, then the module returns 'INVALID KEY LENGTH'.

**5.2.1.3**   `ERR10 INVALID KEY NAME`
If the key uses incorrect characters, then the module returns 'INVALID KEY NAME'.

**5.2.1.4**   `ERR11 UNKNOWN KEY`
If the key is not present in the dictionary, then the module returns 'UNKNOWN KEY'.
Example:

```
AT+CONF VERSION=1.0   # Incorrect capitalization
ERR11 UNKNOWN KEY     # The key is not recognized as spelled
```

**5.2.1.5**   `ERR12 KEY READONLY`
Some keys are read-only and cannot be written. If the key cannot be written to, then the module returns 'KEY READONLY' (for example, ThingName, Certificate, About).
Example

```
AT+CONF Version=1.0   # Attempt to manually modify the Version parameter
ERR12 KEY READONLY
```

**5.2.1.6**   `ERR23 INVALID SIGNATURE`
When updating a certificate (for example, Certificate, OTAcertificate, HOTAcertificate) if a required signature verification failed, then the module returns 'INVALID SIGNATURE'. (See [7.11 Host OTA certificate update](elpg-ota-updates.md#elpg-hota-cert-update) for more detail on the signature verification rules that apply to different types of certificates.)

### 5.2.2 CONF? *key*   »Read the value of a configuration parameter«
<a name="elpg-retrieval-conf"></a>Returns:

**5.2.2.1**   `OK {value}`
If the read is successful, then the module returns 'OK'.

**5.2.2.2**   `ERR9 INVALID KEY LENGTH`
If the key is too long, then the module returns 'INVALID KEY LENGTH'.

**5.2.2.3**   `ERR10 INVALID KEY NAME`
If the key uses incorrect characters, then the module returns 'INVALID KEY NAME'.

**5.2.2.4**   `ERR11 UNKNOWN KEY`
If the key is not present in the system, then the module returns 'UNKNOWN KEY'.

**5.2.2.5**   `ERR13 KEY WRITEONLY`
Some keys are write-only and cannot be read. If the key cannot be read, then the module returns 'KEY WRITEONLY'.

Example:

```
AT+CONF? Passphrase
ERR13 KEY WRITEONLY
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT ExpressLink. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-expresslink` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
