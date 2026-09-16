---
source_url: https://docs.aws.amazon.com/medialive/latest/apireference/inputdevices-inputdeviceid-thumbnaildata.html
---

# Input devices: thumbnail data
<a name="inputdevices-inputdeviceid-thumbnaildata"></a>

## URI
<a name="inputdevices-inputdeviceid-thumbnaildata-url"></a>

`/prod/inputDevices/{{inputDeviceId}}/thumbnailData`

## HTTP methods
<a name="inputdevices-inputdeviceid-thumbnaildata-http-methods"></a>

### GET
<a name="inputdevices-inputdeviceid-thumbnaildataget"></a>

**Operation ID:** `DescribeInputDeviceThumbnail`

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{inputDeviceId}} | String | True |  |

**Header parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| Accept | String | True |  |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | ThumbnailData | 200 response |
| 204 | None | 204 response |
| 400 | InvalidRequest | 400 response |
| 403 | AccessDenied | 403 response |
| 404 | ResourceNotFound | 404 response |
| 429 | LimitExceeded | 429 response |
| 500 | InternalServiceError | 500 response |
| 502 | BadGatewayException | 502 response |
| 504 | GatewayTimeoutException | 504 response |

## Schemas
<a name="inputdevices-inputdeviceid-thumbnaildata-schemas"></a>

### Response bodies
<a name="inputdevices-inputdeviceid-thumbnaildata-response-examples"></a>

#### ThumbnailData schema
<a name="inputdevices-inputdeviceid-thumbnaildata-response-body-thumbnaildata-example"></a>

```
{
  "body": "string"
}
```

#### InvalidRequest schema
<a name="inputdevices-inputdeviceid-thumbnaildata-response-body-invalidrequest-example"></a>

```
{
  "message": "string"
}
```

#### AccessDenied schema
<a name="inputdevices-inputdeviceid-thumbnaildata-response-body-accessdenied-example"></a>

```
{
  "message": "string"
}
```

#### ResourceNotFound schema
<a name="inputdevices-inputdeviceid-thumbnaildata-response-body-resourcenotfound-example"></a>

```
{
  "message": "string"
}
```

#### LimitExceeded schema
<a name="inputdevices-inputdeviceid-thumbnaildata-response-body-limitexceeded-example"></a>

```
{
  "message": "string"
}
```

#### InternalServiceError schema
<a name="inputdevices-inputdeviceid-thumbnaildata-response-body-internalserviceerror-example"></a>

```
{
  "message": "string"
}
```

#### BadGatewayException schema
<a name="inputdevices-inputdeviceid-thumbnaildata-response-body-badgatewayexception-example"></a>

```
{
  "message": "string"
}
```

#### GatewayTimeoutException schema
<a name="inputdevices-inputdeviceid-thumbnaildata-response-body-gatewaytimeoutexception-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="inputdevices-inputdeviceid-thumbnaildata-properties"></a>

### AccessDenied
<a name="inputdevices-inputdeviceid-thumbnaildata-model-accessdenied"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### BadGatewayException
<a name="inputdevices-inputdeviceid-thumbnaildata-model-badgatewayexception"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### GatewayTimeoutException
<a name="inputdevices-inputdeviceid-thumbnaildata-model-gatewaytimeoutexception"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### InternalServiceError
<a name="inputdevices-inputdeviceid-thumbnaildata-model-internalserviceerror"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### InvalidRequest
<a name="inputdevices-inputdeviceid-thumbnaildata-model-invalidrequest"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### LimitExceeded
<a name="inputdevices-inputdeviceid-thumbnaildata-model-limitexceeded"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### ResourceNotFound
<a name="inputdevices-inputdeviceid-thumbnaildata-model-resourcenotfound"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### ThumbnailData
<a name="inputdevices-inputdeviceid-thumbnaildata-model-thumbnaildata"></a>

The binary data for the thumbnail that the Link device has most recently sent to MediaLive.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| body | string<br />Format: byte | False | The binary data for the thumbnail that the Link device has most recently sent to MediaLive. |

## See also
<a name="inputdevices-inputdeviceid-thumbnaildata-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### DescribeInputDeviceThumbnail
<a name="DescribeInputDeviceThumbnail-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/medialive-2017-10-14/DescribeInputDeviceThumbnail)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/medialive-2017-10-14/DescribeInputDeviceThumbnail)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/medialive-2017-10-14/DescribeInputDeviceThumbnail)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/medialive-2017-10-14/DescribeInputDeviceThumbnail)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/medialive-2017-10-14/DescribeInputDeviceThumbnail)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/medialive-2017-10-14/DescribeInputDeviceThumbnail)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/medialive-2017-10-14/DescribeInputDeviceThumbnail)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/medialive-2017-10-14/DescribeInputDeviceThumbnail)
+ [AWS SDK for Python (Boto3)](/goto/boto3/medialive-2017-10-14/DescribeInputDeviceThumbnail)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/medialive-2017-10-14/DescribeInputDeviceThumbnail)
