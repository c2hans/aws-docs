---
source_url: https://docs.aws.amazon.com/medialive/latest/apireference/claimdevice.html
---

# Input devices: claim device
<a name="claimdevice"></a>

## URI
<a name="claimdevice-url"></a>

`/prod/claimDevice`

## HTTP methods
<a name="claimdevice-http-methods"></a>

### POST
<a name="claimdevicepost"></a>

**Operation ID:** `ClaimDevice`

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
<a name="claimdevice-schemas"></a>

### Request bodies
<a name="claimdevice-request-examples"></a>

#### POST schema
<a name="claimdevice-request-body-post-example"></a>

```
{
  "id": "string"
}
```

### Response bodies
<a name="claimdevice-response-examples"></a>

#### InvalidRequest schema
<a name="claimdevice-response-body-invalidrequest-example"></a>

```
{
  "message": "string"
}
```

#### AccessDenied schema
<a name="claimdevice-response-body-accessdenied-example"></a>

```
{
  "message": "string"
}
```

#### ResourceNotFound schema
<a name="claimdevice-response-body-resourcenotfound-example"></a>

```
{
  "message": "string"
}
```

#### ValidationError schema
<a name="claimdevice-response-body-validationerror-example"></a>

```
{
  "elementPath": "string",
  "errorMessage": "string"
}
```

#### LimitExceeded schema
<a name="claimdevice-response-body-limitexceeded-example"></a>

```
{
  "message": "string"
}
```

#### InternalServiceError schema
<a name="claimdevice-response-body-internalserviceerror-example"></a>

```
{
  "message": "string"
}
```

#### BadGatewayException schema
<a name="claimdevice-response-body-badgatewayexception-example"></a>

```
{
  "message": "string"
}
```

#### GatewayTimeoutException schema
<a name="claimdevice-response-body-gatewaytimeoutexception-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="claimdevice-properties"></a>

### AccessDenied
<a name="claimdevice-model-accessdenied"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### BadGatewayException
<a name="claimdevice-model-badgatewayexception"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### ClaimDeviceRequest
<a name="claimdevice-model-claimdevicerequest"></a>

Request to claim an AWS Elemental device that you have purchased from a third-party vendor.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| id | string | False | The id of the device you want to claim. |

### GatewayTimeoutException
<a name="claimdevice-model-gatewaytimeoutexception"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### InternalServiceError
<a name="claimdevice-model-internalserviceerror"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### InvalidRequest
<a name="claimdevice-model-invalidrequest"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### LimitExceeded
<a name="claimdevice-model-limitexceeded"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### ResourceNotFound
<a name="claimdevice-model-resourcenotfound"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### ValidationError
<a name="claimdevice-model-validationerror"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| elementPath | string | False | Path to the source of the error. |
| errorMessage | string | False | The error message. |

## See also
<a name="claimdevice-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### ClaimDevice
<a name="ClaimDevice-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/medialive-2017-10-14/ClaimDevice)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/medialive-2017-10-14/ClaimDevice)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/medialive-2017-10-14/ClaimDevice)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/medialive-2017-10-14/ClaimDevice)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/medialive-2017-10-14/ClaimDevice)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/medialive-2017-10-14/ClaimDevice)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/medialive-2017-10-14/ClaimDevice)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/medialive-2017-10-14/ClaimDevice)
+ [AWS SDK for Python](/goto/boto3/medialive-2017-10-14/ClaimDevice)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/medialive-2017-10-14/ClaimDevice)
