---
source_url: https://docs.aws.amazon.com/medialive/latest/apireference/inputdevices-inputdeviceid-transfer.html
---

# Input devices: transfer device
<a name="inputdevices-inputdeviceid-transfer"></a>

## URI
<a name="inputdevices-inputdeviceid-transfer-url"></a>

`/prod/inputDevices/{{inputDeviceId}}/transfer`

## HTTP methods
<a name="inputdevices-inputdeviceid-transfer-http-methods"></a>

### POST
<a name="inputdevices-inputdeviceid-transferpost"></a>

**Operation ID:** `TransferInputDevice`

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
| 409 | ResourceConflict | 409 response |
| 422 | ValidationError | 422 response |
| 429 | LimitExceeded | 429 response |
| 500 | InternalServiceError | 500 response |
| 502 | BadGatewayException | 502 response |
| 504 | GatewayTimeoutException | 504 response |

## Schemas
<a name="inputdevices-inputdeviceid-transfer-schemas"></a>

### Request bodies
<a name="inputdevices-inputdeviceid-transfer-request-examples"></a>

#### POST schema
<a name="inputdevices-inputdeviceid-transfer-request-body-post-example"></a>

```
{
  "targetCustomerId": "string",
  "targetRegion": "string",
  "transferMessage": "string"
}
```

### Response bodies
<a name="inputdevices-inputdeviceid-transfer-response-examples"></a>

#### InvalidRequest schema
<a name="inputdevices-inputdeviceid-transfer-response-body-invalidrequest-example"></a>

```
{
  "message": "string"
}
```

#### AccessDenied schema
<a name="inputdevices-inputdeviceid-transfer-response-body-accessdenied-example"></a>

```
{
  "message": "string"
}
```

#### ResourceNotFound schema
<a name="inputdevices-inputdeviceid-transfer-response-body-resourcenotfound-example"></a>

```
{
  "message": "string"
}
```

#### ResourceConflict schema
<a name="inputdevices-inputdeviceid-transfer-response-body-resourceconflict-example"></a>

```
{
  "message": "string"
}
```

#### ValidationError schema
<a name="inputdevices-inputdeviceid-transfer-response-body-validationerror-example"></a>

```
{
  "elementPath": "string",
  "errorMessage": "string"
}
```

#### LimitExceeded schema
<a name="inputdevices-inputdeviceid-transfer-response-body-limitexceeded-example"></a>

```
{
  "message": "string"
}
```

#### InternalServiceError schema
<a name="inputdevices-inputdeviceid-transfer-response-body-internalserviceerror-example"></a>

```
{
  "message": "string"
}
```

#### BadGatewayException schema
<a name="inputdevices-inputdeviceid-transfer-response-body-badgatewayexception-example"></a>

```
{
  "message": "string"
}
```

#### GatewayTimeoutException schema
<a name="inputdevices-inputdeviceid-transfer-response-body-gatewaytimeoutexception-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="inputdevices-inputdeviceid-transfer-properties"></a>

### AccessDenied
<a name="inputdevices-inputdeviceid-transfer-model-accessdenied"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### BadGatewayException
<a name="inputdevices-inputdeviceid-transfer-model-badgatewayexception"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### GatewayTimeoutException
<a name="inputdevices-inputdeviceid-transfer-model-gatewaytimeoutexception"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### InternalServiceError
<a name="inputdevices-inputdeviceid-transfer-model-internalserviceerror"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### InvalidRequest
<a name="inputdevices-inputdeviceid-transfer-model-invalidrequest"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### LimitExceeded
<a name="inputdevices-inputdeviceid-transfer-model-limitexceeded"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### ResourceConflict
<a name="inputdevices-inputdeviceid-transfer-model-resourceconflict"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### ResourceNotFound
<a name="inputdevices-inputdeviceid-transfer-model-resourcenotfound"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### TransferInputDevice
<a name="inputdevices-inputdeviceid-transfer-model-transferinputdevice"></a>

The transfer details of the input device.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| targetCustomerId | string | False | The AWS account ID (12 digits) for the recipient of the device transfer. |
| targetRegion | string | False | The target AWS Region to transfer the device. |
| transferMessage | string | False | An optional message for the recipient. Maximum 280 characters. |

### ValidationError
<a name="inputdevices-inputdeviceid-transfer-model-validationerror"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| elementPath | string | False | Path to the source of the error. |
| errorMessage | string | False | The error message. |

## See also
<a name="inputdevices-inputdeviceid-transfer-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### TransferInputDevice
<a name="TransferInputDevice-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/medialive-2017-10-14/TransferInputDevice)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/medialive-2017-10-14/TransferInputDevice)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/medialive-2017-10-14/TransferInputDevice)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/medialive-2017-10-14/TransferInputDevice)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/medialive-2017-10-14/TransferInputDevice)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/medialive-2017-10-14/TransferInputDevice)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/medialive-2017-10-14/TransferInputDevice)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/medialive-2017-10-14/TransferInputDevice)
+ [AWS SDK for Python (Boto3)](/goto/boto3/medialive-2017-10-14/TransferInputDevice)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/medialive-2017-10-14/TransferInputDevice)
