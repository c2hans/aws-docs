---
source_url: https://docs.aws.amazon.com/medialive/latest/apireference/inputdevices-inputdeviceid.html
---

# Input devices: device ID
<a name="inputdevices-inputdeviceid"></a>

## URI
<a name="inputdevices-inputdeviceid-url"></a>

`/prod/inputDevices/{{inputDeviceId}}`

## HTTP methods
<a name="inputdevices-inputdeviceid-http-methods"></a>

### GET
<a name="inputdevices-inputdeviceidget"></a>

**Operation ID:** `DescribeInputDevice`

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{inputDeviceId}} | String | True |  |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | InputDevice | 200 response |
| 400 | InvalidRequest | 400 response |
| 403 | AccessDenied | 403 response |
| 404 | ResourceNotFound | 404 response |
| 429 | LimitExceeded | 429 response |
| 500 | InternalServiceError | 500 response |
| 502 | BadGatewayException | 502 response |
| 504 | GatewayTimeoutException | 504 response |

### PUT
<a name="inputdevices-inputdeviceidput"></a>

**Operation ID:** `UpdateInputDevice`

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{inputDeviceId}} | String | True |  |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | InputDevice | 200 response |
| 400 | InvalidRequest | 400 response |
| 403 | AccessDenied | 403 response |
| 404 | ResourceNotFound | 404 response |
| 422 | InputDeviceConfigurationValidationError | 422 response |
| 429 | LimitExceeded | 429 response |
| 500 | InternalServiceError | 500 response |
| 502 | BadGatewayException | 502 response |
| 504 | GatewayTimeoutException | 504 response |

## Schemas
<a name="inputdevices-inputdeviceid-schemas"></a>

### Request bodies
<a name="inputdevices-inputdeviceid-request-examples"></a>

#### PUT schema
<a name="inputdevices-inputdeviceid-request-body-put-example"></a>

```
{
  "availabilityZone": "string",
  "hdDeviceSettings": {
    "configuredInput": enum,
    "maxBitrate": integer
  },
  "name": "string",
  "uhdDeviceSettings": {
    "configuredInput": enum,
    "maxBitrate": integer
  }
}
```

### Response bodies
<a name="inputdevices-inputdeviceid-response-examples"></a>

#### InputDevice schema
<a name="inputdevices-inputdeviceid-response-body-inputdevice-example"></a>

```
{
  "arn": "string",
  "availabilityZone": "string",
  "connectionState": enum,
  "deviceSettingsSyncState": enum,
  "deviceUpdateStatus": enum,
  "hdDeviceSettings": {
    "activeInput": enum,
    "configuredInput": enum,
    "deviceState": enum,
    "framerate": number,
    "height": integer,
    "maxBitrate": integer,
    "scanType": enum,
    "width": integer
  },
  "id": "string",
  "macAddress": "string",
  "name": "string",
  "networkSettings": {
    "dnsAddresses": [
      "string"
    ],
    "gateway": "string",
    "ipAddress": "string",
    "ipScheme": enum,
    "subnetMask": "string"
  },
  "serialNumber": "string",
  "type": enum,
  "uhdDeviceSettings": {
    "activeInput": enum,
    "configuredInput": enum,
    "deviceState": enum,
    "framerate": number,
    "height": integer,
    "maxBitrate": integer,
    "scanType": enum,
    "width": integer
  }
}
```

#### InvalidRequest schema
<a name="inputdevices-inputdeviceid-response-body-invalidrequest-example"></a>

```
{
  "message": "string"
}
```

#### AccessDenied schema
<a name="inputdevices-inputdeviceid-response-body-accessdenied-example"></a>

```
{
  "message": "string"
}
```

#### ResourceNotFound schema
<a name="inputdevices-inputdeviceid-response-body-resourcenotfound-example"></a>

```
{
  "message": "string"
}
```

#### InputDeviceConfigurationValidationError schema
<a name="inputdevices-inputdeviceid-response-body-inputdeviceconfigurationvalidationerror-example"></a>

```
{
  "message": "string",
  "validationErrors": [
    {
      "elementPath": "string",
      "errorMessage": "string"
    }
  ]
}
```

#### LimitExceeded schema
<a name="inputdevices-inputdeviceid-response-body-limitexceeded-example"></a>

```
{
  "message": "string"
}
```

#### InternalServiceError schema
<a name="inputdevices-inputdeviceid-response-body-internalserviceerror-example"></a>

```
{
  "message": "string"
}
```

#### BadGatewayException schema
<a name="inputdevices-inputdeviceid-response-body-badgatewayexception-example"></a>

```
{
  "message": "string"
}
```

#### GatewayTimeoutException schema
<a name="inputdevices-inputdeviceid-response-body-gatewaytimeoutexception-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="inputdevices-inputdeviceid-properties"></a>

### AccessDenied
<a name="inputdevices-inputdeviceid-model-accessdenied"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### BadGatewayException
<a name="inputdevices-inputdeviceid-model-badgatewayexception"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### DeviceSettingsSyncState
<a name="inputdevices-inputdeviceid-model-devicesettingssyncstate"></a>

The status of the action to synchronize the device configuration. If you change the configuration of the input device (for example, the maximum bitrate), MediaLive sends the new data to the device. The device might not update itself immediately. SYNCED means the device has updated its configuration. SYNCING means that it has not updated its configuration.
+ `SYNCED`
+ `SYNCING`

### DeviceUpdateStatus
<a name="inputdevices-inputdeviceid-model-deviceupdatestatus"></a>

The status of software on the input device.
+ `UP_TO_DATE`
+ `NOT_UP_TO_DATE`
+ `UPDATING`

### GatewayTimeoutException
<a name="inputdevices-inputdeviceid-model-gatewaytimeoutexception"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### InputDevice
<a name="inputdevices-inputdeviceid-model-inputdevice"></a>

An input device.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| arn | string | False | The unique ARN of the input device. |
| availabilityZone | string | False | The Availability Zone associated with this input device.  |
| connectionState | [InputDeviceConnectionState](#inputdevices-inputdeviceid-model-inputdeviceconnectionstate) | False | The state of the connection between the input device and AWS. |
| deviceSettingsSyncState | [DeviceSettingsSyncState](#inputdevices-inputdeviceid-model-devicesettingssyncstate) | False | The status of the action to synchronize the device configuration. If you change the configuration of the input device (for example, the maximum bitrate), MediaLive sends the new data to the device. The device might not update itself immediately. SYNCED means the device has updated its configuration. SYNCING means that it has not updated its configuration. |
| deviceUpdateStatus | [DeviceUpdateStatus](#inputdevices-inputdeviceid-model-deviceupdatestatus) | False | The status of software on the input device. |
| hdDeviceSettings | [InputDeviceHdSettings](#inputdevices-inputdeviceid-model-inputdevicehdsettings) | False | Settings that describe an input device that is type HD. |
| id | string | False | The unique ID of the input device. |
| macAddress | string | False | The network MAC address of the input device. |
| name | string | False | A name that you specify for the input device. |
| networkSettings | [InputDeviceNetworkSettings](#inputdevices-inputdeviceid-model-inputdevicenetworksettings) | False | The network settings for the input device. |
| serialNumber | string | False | The unique serial number of the input device. |
| type | [InputDeviceType](#inputdevices-inputdeviceid-model-inputdevicetype) | False | The type of the input device. |
| uhdDeviceSettings | [InputDeviceUhdSettings](#inputdevices-inputdeviceid-model-inputdeviceuhdsettings) | False | Settings that describe an input device that is type UHD. |

### InputDeviceActiveInput
<a name="inputdevices-inputdeviceid-model-inputdeviceactiveinput"></a>

The source at the input device that is currently active.
+ `HDMI`
+ `SDI`

### InputDeviceConfigurableSettings
<a name="inputdevices-inputdeviceid-model-inputdeviceconfigurablesettings"></a>

Configurable settings for the input device.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| configuredInput | [InputDeviceConfiguredInput](#inputdevices-inputdeviceid-model-inputdeviceconfiguredinput) | False | The input source that you want to use. If the device has a source connected to only one of its input ports, or if you don't care which source the device sends, specify Auto. If the device has sources connected to both its input ports, and you want to use a specific source, specify the source. |
| maxBitrate | integer | False | The maximum bitrate in bits per second. Set a value here to throttle the bitrate of the source video. |

### InputDeviceConfigurationValidationError
<a name="inputdevices-inputdeviceid-model-inputdeviceconfigurationvalidationerror"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The error message. |
| validationErrors | Array of type [ValidationError](#inputdevices-inputdeviceid-model-validationerror) | False | A collection of validation error responses. |

### InputDeviceConfiguredInput
<a name="inputdevices-inputdeviceid-model-inputdeviceconfiguredinput"></a>

The source to activate (use) from the input device.
+ `AUTO`
+ `HDMI`
+ `SDI`

### InputDeviceConnectionState
<a name="inputdevices-inputdeviceid-model-inputdeviceconnectionstate"></a>

The state of the connection between the input device and AWS.
+ `DISCONNECTED`
+ `CONNECTED`

### InputDeviceHdSettings
<a name="inputdevices-inputdeviceid-model-inputdevicehdsettings"></a>

Settings that describe the active source from the input device, and the video characteristics of that source.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| activeInput | [InputDeviceActiveInput](#inputdevices-inputdeviceid-model-inputdeviceactiveinput) | False | If you specified Auto as the configured input, specifies which of the sources is currently active (SDI or HDMI). |
| configuredInput | [InputDeviceConfiguredInput](#inputdevices-inputdeviceid-model-inputdeviceconfiguredinput) | False | The source at the input device that is currently active. You can specify this source. |
| deviceState | [InputDeviceState](#inputdevices-inputdeviceid-model-inputdevicestate) | False | The state of the input device. |
| framerate | number | False | The frame rate of the video source. |
| height | integer | False | The height of the video source, in pixels. |
| maxBitrate | integer | False | The current maximum bitrate for ingesting this source, in bits per second. You can specify this maximum. |
| scanType | [InputDeviceScanType](#inputdevices-inputdeviceid-model-inputdevicescantype) | False | The scan type of the video source. |
| width | integer | False | The width of the video source, in pixels. |

### InputDeviceIpScheme
<a name="inputdevices-inputdeviceid-model-inputdeviceipscheme"></a>

Specifies whether the input device has been configured (outside of MediaLive) to use a dynamic IP address assignment (DHCP) or a static IP address.
+ `STATIC`
+ `DHCP`

### InputDeviceNetworkSettings
<a name="inputdevices-inputdeviceid-model-inputdevicenetworksettings"></a>

The network settings for the input device.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| dnsAddresses | Array of type string | False | The DNS addresses of the input device. |
| gateway | string | False | The network gateway IP address. |
| ipAddress | string | False | The IP address of the input device. |
| ipScheme | [InputDeviceIpScheme](#inputdevices-inputdeviceid-model-inputdeviceipscheme) | False | Specifies whether the input device has been configured (outside of MediaLive) to use a dynamic IP address assignment (DHCP) or a static IP address. |
| subnetMask | string | False | The subnet mask of the input device. |

### InputDeviceScanType
<a name="inputdevices-inputdeviceid-model-inputdevicescantype"></a>

The scan type of the video source.
+ `INTERLACED`
+ `PROGRESSIVE`

### InputDeviceState
<a name="inputdevices-inputdeviceid-model-inputdevicestate"></a>

The state of the input device.
+ `IDLE`
+ `STREAMING`

### InputDeviceType
<a name="inputdevices-inputdeviceid-model-inputdevicetype"></a>

The type of the input device. For an AWS Elemental Link device that outputs resolutions up to 1080, choose "HD".
+ `HD`
+ `UHD`

### InputDeviceUhdSettings
<a name="inputdevices-inputdeviceid-model-inputdeviceuhdsettings"></a>

Settings that describe the active source from the input device, and the video characteristics of that source.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| activeInput | [InputDeviceActiveInput](#inputdevices-inputdeviceid-model-inputdeviceactiveinput) | False | If you specified Auto as the configured input, specifies which of the sources is currently active (SDI or HDMI). |
| configuredInput | [InputDeviceConfiguredInput](#inputdevices-inputdeviceid-model-inputdeviceconfiguredinput) | False | The source at the input device that is currently active. You can specify this source. |
| deviceState | [InputDeviceState](#inputdevices-inputdeviceid-model-inputdevicestate) | False | The state of the input device. |
| framerate | number | False | The frame rate of the video source. |
| height | integer | False | The height of the video source, in pixels. |
| maxBitrate | integer | False | The current maximum bitrate for ingesting this source, in bits per second. You can specify this maximum. |
| scanType | [InputDeviceScanType](#inputdevices-inputdeviceid-model-inputdevicescantype) | False | The scan type of the video source. |
| width | integer | False | The width of the video source, in pixels. |

### InternalServiceError
<a name="inputdevices-inputdeviceid-model-internalserviceerror"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### InvalidRequest
<a name="inputdevices-inputdeviceid-model-invalidrequest"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### LimitExceeded
<a name="inputdevices-inputdeviceid-model-limitexceeded"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### ResourceNotFound
<a name="inputdevices-inputdeviceid-model-resourcenotfound"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### UpdateInputDevice
<a name="inputdevices-inputdeviceid-model-updateinputdevice"></a>

Updates an input device.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| availabilityZone | string | False | The Availability Zone you want to associate with this input device.  |
| hdDeviceSettings | [InputDeviceConfigurableSettings](#inputdevices-inputdeviceid-model-inputdeviceconfigurablesettings) | False | The settings that you want to apply to the HD input device. |
| name | string | False | The name that you assigned to this input device (not the unique ID). |
| uhdDeviceSettings | [InputDeviceConfigurableSettings](#inputdevices-inputdeviceid-model-inputdeviceconfigurablesettings) | False | The settings that you want to apply to the UHD input device. |

### ValidationError
<a name="inputdevices-inputdeviceid-model-validationerror"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| elementPath | string | False | Path to the source of the error. |
| errorMessage | string | False | The error message. |

## See also
<a name="inputdevices-inputdeviceid-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### DescribeInputDevice
<a name="DescribeInputDevice-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/medialive-2017-10-14/DescribeInputDevice)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/medialive-2017-10-14/DescribeInputDevice)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/medialive-2017-10-14/DescribeInputDevice)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/medialive-2017-10-14/DescribeInputDevice)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/medialive-2017-10-14/DescribeInputDevice)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/medialive-2017-10-14/DescribeInputDevice)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/medialive-2017-10-14/DescribeInputDevice)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/medialive-2017-10-14/DescribeInputDevice)
+ [AWS SDK for Python](/goto/boto3/medialive-2017-10-14/DescribeInputDevice)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/medialive-2017-10-14/DescribeInputDevice)

### UpdateInputDevice
<a name="UpdateInputDevice-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/medialive-2017-10-14/UpdateInputDevice)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/medialive-2017-10-14/UpdateInputDevice)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/medialive-2017-10-14/UpdateInputDevice)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/medialive-2017-10-14/UpdateInputDevice)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/medialive-2017-10-14/UpdateInputDevice)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/medialive-2017-10-14/UpdateInputDevice)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/medialive-2017-10-14/UpdateInputDevice)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/medialive-2017-10-14/UpdateInputDevice)
+ [AWS SDK for Python](/goto/boto3/medialive-2017-10-14/UpdateInputDevice)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/medialive-2017-10-14/UpdateInputDevice)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
