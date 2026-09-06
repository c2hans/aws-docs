---
source_url: https://docs.aws.amazon.com/medialive/latest/apireference/inputdevices.html
---

# Input devices
<a name="inputdevices"></a>

## URI
<a name="inputdevices-url"></a>

`/prod/inputDevices`

## HTTP methods
<a name="inputdevices-http-methods"></a>

### GET
<a name="inputdevicesget"></a>

**Operation ID:** `ListInputDevices`

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| nextToken | String | False |  |
| maxResults | String | False |  |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | ListInputDevicesResultModel | 200 response |
| 400 | InvalidRequest | 400 response |
| 403 | AccessDenied | 403 response |
| 429 | LimitExceeded | 429 response |
| 500 | InternalServiceError | 500 response |
| 502 | BadGatewayException | 502 response |
| 504 | GatewayTimeoutException | 504 response |

## Schemas
<a name="inputdevices-schemas"></a>

### Response bodies
<a name="inputdevices-response-examples"></a>

#### ListInputDevicesResultModel schema
<a name="inputdevices-response-body-listinputdevicesresultmodel-example"></a>

```
{
  "inputDevices": [
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
  ],
  "nextToken": "string"
}
```

#### InvalidRequest schema
<a name="inputdevices-response-body-invalidrequest-example"></a>

```
{
  "message": "string"
}
```

#### AccessDenied schema
<a name="inputdevices-response-body-accessdenied-example"></a>

```
{
  "message": "string"
}
```

#### LimitExceeded schema
<a name="inputdevices-response-body-limitexceeded-example"></a>

```
{
  "message": "string"
}
```

#### InternalServiceError schema
<a name="inputdevices-response-body-internalserviceerror-example"></a>

```
{
  "message": "string"
}
```

#### BadGatewayException schema
<a name="inputdevices-response-body-badgatewayexception-example"></a>

```
{
  "message": "string"
}
```

#### GatewayTimeoutException schema
<a name="inputdevices-response-body-gatewaytimeoutexception-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="inputdevices-properties"></a>

### AccessDenied
<a name="inputdevices-model-accessdenied"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### BadGatewayException
<a name="inputdevices-model-badgatewayexception"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### DeviceSettingsSyncState
<a name="inputdevices-model-devicesettingssyncstate"></a>

The status of the action to synchronize the device configuration. If you change the configuration of the input device (for example, the maximum bitrate), MediaLive sends the new data to the device. The device might not update itself immediately. SYNCED means the device has updated its configuration. SYNCING means that it has not updated its configuration.
+ `SYNCED`
+ `SYNCING`

### DeviceUpdateStatus
<a name="inputdevices-model-deviceupdatestatus"></a>

The status of software on the input device.
+ `UP_TO_DATE`
+ `NOT_UP_TO_DATE`
+ `UPDATING`

### GatewayTimeoutException
<a name="inputdevices-model-gatewaytimeoutexception"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### InputDeviceActiveInput
<a name="inputdevices-model-inputdeviceactiveinput"></a>

The source at the input device that is currently active.
+ `HDMI`
+ `SDI`

### InputDeviceConfiguredInput
<a name="inputdevices-model-inputdeviceconfiguredinput"></a>

The source to activate (use) from the input device.
+ `AUTO`
+ `HDMI`
+ `SDI`

### InputDeviceConnectionState
<a name="inputdevices-model-inputdeviceconnectionstate"></a>

The state of the connection between the input device and AWS.
+ `DISCONNECTED`
+ `CONNECTED`

### InputDeviceHdSettings
<a name="inputdevices-model-inputdevicehdsettings"></a>

Settings that describe the active source from the input device, and the video characteristics of that source.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| activeInput | [InputDeviceActiveInput](#inputdevices-model-inputdeviceactiveinput) | False | If you specified Auto as the configured input, specifies which of the sources is currently active (SDI or HDMI). |
| configuredInput | [InputDeviceConfiguredInput](#inputdevices-model-inputdeviceconfiguredinput) | False | The source at the input device that is currently active. You can specify this source. |
| deviceState | [InputDeviceState](#inputdevices-model-inputdevicestate) | False | The state of the input device. |
| framerate | number | False | The frame rate of the video source. |
| height | integer | False | The height of the video source, in pixels. |
| maxBitrate | integer | False | The current maximum bitrate for ingesting this source, in bits per second. You can specify this maximum. |
| scanType | [InputDeviceScanType](#inputdevices-model-inputdevicescantype) | False | The scan type of the video source. |
| width | integer | False | The width of the video source, in pixels. |

### InputDeviceIpScheme
<a name="inputdevices-model-inputdeviceipscheme"></a>

Specifies whether the input device has been configured (outside of MediaLive) to use a dynamic IP address assignment (DHCP) or a static IP address.
+ `STATIC`
+ `DHCP`

### InputDeviceNetworkSettings
<a name="inputdevices-model-inputdevicenetworksettings"></a>

The network settings for the input device.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| dnsAddresses | Array of type string | False | The DNS addresses of the input device. |
| gateway | string | False | The network gateway IP address. |
| ipAddress | string | False | The IP address of the input device. |
| ipScheme | [InputDeviceIpScheme](#inputdevices-model-inputdeviceipscheme) | False | Specifies whether the input device has been configured (outside of MediaLive) to use a dynamic IP address assignment (DHCP) or a static IP address. |
| subnetMask | string | False | The subnet mask of the input device. |

### InputDeviceScanType
<a name="inputdevices-model-inputdevicescantype"></a>

The scan type of the video source.
+ `INTERLACED`
+ `PROGRESSIVE`

### InputDeviceState
<a name="inputdevices-model-inputdevicestate"></a>

The state of the input device.
+ `IDLE`
+ `STREAMING`

### InputDeviceSummary
<a name="inputdevices-model-inputdevicesummary"></a>

Details of the input device.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| arn | string | False | The unique ARN of the input device. |
| availabilityZone | string | False | The Availability Zone associated with this input device. |
| connectionState | [InputDeviceConnectionState](#inputdevices-model-inputdeviceconnectionstate) | False | The state of the connection between the input device and AWS. |
| deviceSettingsSyncState | [DeviceSettingsSyncState](#inputdevices-model-devicesettingssyncstate) | False | The status of the action to synchronize the device configuration. If you change the configuration of the input device (for example, the maximum bitrate), MediaLive sends the new data to the device. The device might not update itself immediately. SYNCED means the device has updated its configuration. SYNCING means that it has not updated its configuration. |
| deviceUpdateStatus | [DeviceUpdateStatus](#inputdevices-model-deviceupdatestatus) | False | The status of software on the input device. |
| hdDeviceSettings | [InputDeviceHdSettings](#inputdevices-model-inputdevicehdsettings) | False | Settings that describe an input device that is type HD. |
| id | string | False | The unique ID of the input device. |
| macAddress | string | False | The network MAC address of the input device. |
| name | string | False | A name that you specify for the input device. |
| networkSettings | [InputDeviceNetworkSettings](#inputdevices-model-inputdevicenetworksettings) | False | Network settings for the input device. |
| serialNumber | string | False | The unique serial number of the input device. |
| type | [InputDeviceType](#inputdevices-model-inputdevicetype) | False | The type of the input device. |
| uhdDeviceSettings | [InputDeviceUhdSettings](#inputdevices-model-inputdeviceuhdsettings) | False | Settings that describe an input device that is type UHD. |

### InputDeviceType
<a name="inputdevices-model-inputdevicetype"></a>

The type of the input device. For an AWS Elemental Link device that outputs resolutions up to 1080, choose "HD".
+ `HD`
+ `UHD`

### InputDeviceUhdSettings
<a name="inputdevices-model-inputdeviceuhdsettings"></a>

Settings that describe the active source from the input device, and the video characteristics of that source.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| activeInput | [InputDeviceActiveInput](#inputdevices-model-inputdeviceactiveinput) | False | If you specified Auto as the configured input, specifies which of the sources is currently active (SDI or HDMI). |
| configuredInput | [InputDeviceConfiguredInput](#inputdevices-model-inputdeviceconfiguredinput) | False | The source at the input device that is currently active. You can specify this source. |
| deviceState | [InputDeviceState](#inputdevices-model-inputdevicestate) | False | The state of the input device. |
| framerate | number | False | The frame rate of the video source. |
| height | integer | False | The height of the video source, in pixels. |
| maxBitrate | integer | False | The current maximum bitrate for ingesting this source, in bits per second. You can specify this maximum. |
| scanType | [InputDeviceScanType](#inputdevices-model-inputdevicescantype) | False | The scan type of the video source. |
| width | integer | False | The width of the video source, in pixels. |

### InternalServiceError
<a name="inputdevices-model-internalserviceerror"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### InvalidRequest
<a name="inputdevices-model-invalidrequest"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### LimitExceeded
<a name="inputdevices-model-limitexceeded"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### ListInputDevicesResultModel
<a name="inputdevices-model-listinputdevicesresultmodel"></a>

The list of input devices owned by the AWS account.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| inputDevices | Array of type [InputDeviceSummary](#inputdevices-model-inputdevicesummary) | False | The list of input devices. |
| nextToken | string | False | A token to get additional list results. |

## See also
<a name="inputdevices-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### ListInputDevices
<a name="ListInputDevices-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/medialive-2017-10-14/ListInputDevices)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/medialive-2017-10-14/ListInputDevices)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/medialive-2017-10-14/ListInputDevices)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/medialive-2017-10-14/ListInputDevices)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/medialive-2017-10-14/ListInputDevices)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/medialive-2017-10-14/ListInputDevices)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/medialive-2017-10-14/ListInputDevices)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/medialive-2017-10-14/ListInputDevices)
+ [AWS SDK for Python](/goto/boto3/medialive-2017-10-14/ListInputDevices)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/medialive-2017-10-14/ListInputDevices)
