---
source_url: https://docs.aws.amazon.com/medialive/latest/apireference/inputdevices-inputdeviceid-reboot.html
---

# Input devices: reboot
<a name="inputdevices-inputdeviceid-reboot"></a>

## URI
<a name="inputdevices-inputdeviceid-reboot-url"></a>

`/prod/inputDevices/{{inputDeviceId}}/reboot`

## HTTP methods
<a name="inputdevices-inputdeviceid-reboot-http-methods"></a>

### POST
<a name="inputdevices-inputdeviceid-rebootpost"></a>

**Operation ID:** `RebootInputDevice`

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{inputDeviceId}} | String | True |  |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | 200 response |
| 400 | InvalidRequest | 400 response |
| 403 | AccessDenied | 403 response |
| 404 | ResourceNotFound | 404 response |
| 422 | ValidationError | 422 response |
| 429 | LimitExceeded | 429 response |
| 500 | InternalServiceError | 500 response |
| 502 | BadGatewayException | 502 response |
| 504 | GatewayTimeoutException | 504 response |

## Schemas
<a name="inputdevices-inputdeviceid-reboot-schemas"></a>

### Request bodies
<a name="inputdevices-inputdeviceid-reboot-request-examples"></a>

#### POST schema
<a name="inputdevices-inputdeviceid-reboot-request-body-post-example"></a>

```
{
  "force": enum
}
```

### Response bodies
<a name="inputdevices-inputdeviceid-reboot-response-examples"></a>

#### InvalidRequest schema
<a name="inputdevices-inputdeviceid-reboot-response-body-invalidrequest-example"></a>

```
{
  "message": "string"
}
```

#### AccessDenied schema
<a name="inputdevices-inputdeviceid-reboot-response-body-accessdenied-example"></a>

```
{
  "message": "string"
}
```

#### ResourceNotFound schema
<a name="inputdevices-inputdeviceid-reboot-response-body-resourcenotfound-example"></a>

```
{
  "message": "string"
}
```

#### ValidationError schema
<a name="inputdevices-inputdeviceid-reboot-response-body-validationerror-example"></a>

```
{
  "elementPath": "string",
  "errorMessage": "string"
}
```

#### LimitExceeded schema
<a name="inputdevices-inputdeviceid-reboot-response-body-limitexceeded-example"></a>

```
{
  "message": "string"
}
```

#### InternalServiceError schema
<a name="inputdevices-inputdeviceid-reboot-response-body-internalserviceerror-example"></a>

```
{
  "message": "string"
}
```

#### BadGatewayException schema
<a name="inputdevices-inputdeviceid-reboot-response-body-badgatewayexception-example"></a>

```
{
  "message": "string"
}
```

#### GatewayTimeoutException schema
<a name="inputdevices-inputdeviceid-reboot-response-body-gatewaytimeoutexception-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="inputdevices-inputdeviceid-reboot-properties"></a>

### AccessDenied
<a name="inputdevices-inputdeviceid-reboot-model-accessdenied"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### BadGatewayException
<a name="inputdevices-inputdeviceid-reboot-model-badgatewayexception"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### GatewayTimeoutException
<a name="inputdevices-inputdeviceid-reboot-model-gatewaytimeoutexception"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### InternalServiceError
<a name="inputdevices-inputdeviceid-reboot-model-internalserviceerror"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### InvalidRequest
<a name="inputdevices-inputdeviceid-reboot-model-invalidrequest"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### LimitExceeded
<a name="inputdevices-inputdeviceid-reboot-model-limitexceeded"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### RebootInputDevice
<a name="inputdevices-inputdeviceid-reboot-model-rebootinputdevice"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| force | [RebootInputDeviceForce](#inputdevices-inputdeviceid-reboot-model-rebootinputdeviceforce) | False | Force a reboot of an input device. If the device is streaming, it will stop streaming and begin rebooting within a few seconds of sending the command. If the device was streaming prior to the reboot, the device will resume streaming when the reboot completes. |

### RebootInputDeviceForce
<a name="inputdevices-inputdeviceid-reboot-model-rebootinputdeviceforce"></a>

Whether or not to force reboot the input device.
+ `NO`
+ `YES`

### ResourceNotFound
<a name="inputdevices-inputdeviceid-reboot-model-resourcenotfound"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### ValidationError
<a name="inputdevices-inputdeviceid-reboot-model-validationerror"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| elementPath | string | False | Path to the source of the error. |
| errorMessage | string | False | The error message. |

## See also
<a name="inputdevices-inputdeviceid-reboot-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### RebootInputDevice
<a name="RebootInputDevice-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/medialive-2017-10-14/RebootInputDevice)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/medialive-2017-10-14/RebootInputDevice)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/medialive-2017-10-14/RebootInputDevice)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/medialive-2017-10-14/RebootInputDevice)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/medialive-2017-10-14/RebootInputDevice)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/medialive-2017-10-14/RebootInputDevice)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/medialive-2017-10-14/RebootInputDevice)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/medialive-2017-10-14/RebootInputDevice)
+ [AWS SDK for Python](/goto/boto3/medialive-2017-10-14/RebootInputDevice)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/medialive-2017-10-14/RebootInputDevice)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
