---
source_url: https://docs.aws.amazon.com/iot-expresslink/archive/v0.5/programmersguide/elpg-iot-services.html
---

# 8 AWS IoT Services
<a name="elpg-iot-services"></a>

## 8.1 Device Defender
<a name="elpg-device-defender"></a>

ExpressLink devices support the [AWS IoT Device Defender](https://docs.aws.amazon.com/iot/latest/developerguide/device-defender.html) service. They can publish a basic set of metrics to IoT Core at a configurable interval, including:

**Table 6 - ExpressLink Defender metrics**

| ExpressLink Custom Metric | Type | Description |
| --- | --- | --- |
| Bytes Out | Count | Number of bytes sent since last update. |
| Messages sent | Count | Number of messages sent since last update. |
| Messages received | Count | Number of messages received since last update. |
| Hard Reset Event | Flag | Set to 1 if a hardware reset occurred since last update. |
| Reconnect Events | Flag | Set to 1 if a reconnect occurred since last update. |
| Flash Memory Writes | Count | Number of writes to flash memory since last update. |

All ExpressLink custom metrics are volatile in nature, as their values are reset to 0 after each periodic update (or set to 1 upon a device reset/reboot for the specific events).

The device defender feature is activated by setting the *Defender* configuration parameter to a value greater than 0 in the configuration dictionary (using the AT\+CONF command).

The Defender parameter value is used to indicate the number of seconds between successive updates of the Device Defender metrics.

The Defender parameter is non-volatile so that an ExpressLink device resumes sending Device Defender metrics at the rate to which it was configured after any reset (soft command or hardware).

Examples:

```
AT+CONF Defender=0    # Device Defender metrics are disabled
```

NOTE: This is the initialized value after a factory reset (see [Table 2 - Configuration Dictionary Persistent Keys](elpg-configuration-dictionary.md#elpg-table2)).

```
AT+CONF Defender=60      # Device Defender metrics will be sent every minute
AT+CONF Defender=3600    # Device Defender metrics will be sent every hour
```

### 8.1.1 DEFENDER: {not implemented in this version}
<a name="elpg-defender-command"></a>

The DEFENDER command is reserved for use with the AWS IoT Device defender service.

## 8.2 AWS IoT Device Shadow
<a name="elpg-device-shadow"></a>

### 8.2.1 SHADOW: {not implemented in this version}
<a name="elpg-shadow-command"></a>

The SHADOW command is reserved for the support of the Device Shadow service.

## 8.3 AWS IoT JOBS
<a name="elpg-iot-jobs"></a>

### 8.3.1 JOB: {not implemented in this version}
<a name="elpg-job-command"></a>

The JOB command is reserved for the support of the AWS IoT Jobs service.
