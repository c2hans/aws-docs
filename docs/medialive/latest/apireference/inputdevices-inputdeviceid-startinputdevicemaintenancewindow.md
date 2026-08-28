---
source_url: https://docs.aws.amazon.com/medialive/latest/apireference/inputdevices-inputdeviceid-startinputdevicemaintenancewindow.html
---

# Input devices: update
<a name="inputdevices-inputdeviceid-startinputdevicemaintenancewindow"></a>

## URI
<a name="inputdevices-inputdeviceid-startinputdevicemaintenancewindow-url"></a>

`/prod/inputDevices/{{inputDeviceId}}/startInputDeviceMaintenanceWindow`

## HTTP methods
<a name="inputdevices-inputdeviceid-startinputdevicemaintenancewindow-http-methods"></a>

### POST
<a name="inputdevices-inputdeviceid-startinputdevicemaintenancewindowpost"></a>

**Operation ID:** `StartInputDeviceMaintenanceWindow`

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
<a name="inputdevices-inputdeviceid-startinputdevicemaintenancewindow-schemas"></a>

### Response bodies
<a name="inputdevices-inputdeviceid-startinputdevicemaintenancewindow-response-examples"></a>

#### InvalidRequest schema
<a name="inputdevices-inputdeviceid-startinputdevicemaintenancewindow-response-body-invalidrequest-example"></a>

```
{
  "message": "string"
}
```

#### AccessDenied schema
<a name="inputdevices-inputdeviceid-startinputdevicemaintenancewindow-response-body-accessdenied-example"></a>

```
{
  "message": "string"
}
```

#### ResourceNotFound schema
<a name="inputdevices-inputdeviceid-startinputdevicemaintenancewindow-response-body-resourcenotfound-example"></a>

```
{
  "message": "string"
}
```

#### ValidationError schema
<a name="inputdevices-inputdeviceid-startinputdevicemaintenancewindow-response-body-validationerror-example"></a>

```
{
  "elementPath": "string",
  "errorMessage": "string"
}
```

#### LimitExceeded schema
<a name="inputdevices-inputdeviceid-startinputdevicemaintenancewindow-response-body-limitexceeded-example"></a>

```
{
  "message": "string"
}
```

#### InternalServiceError schema
<a name="inputdevices-inputdeviceid-startinputdevicemaintenancewindow-response-body-internalserviceerror-example"></a>

```
{
  "message": "string"
}
```

#### BadGatewayException schema
<a name="inputdevices-inputdeviceid-startinputdevicemaintenancewindow-response-body-badgatewayexception-example"></a>

```
{
  "message": "string"
}
```

#### GatewayTimeoutException schema
<a name="inputdevices-inputdeviceid-startinputdevicemaintenancewindow-response-body-gatewaytimeoutexception-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="inputdevices-inputdeviceid-startinputdevicemaintenancewindow-properties"></a>

### AccessDenied
<a name="inputdevices-inputdeviceid-startinputdevicemaintenancewindow-model-accessdenied"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### BadGatewayException
<a name="inputdevices-inputdeviceid-startinputdevicemaintenancewindow-model-badgatewayexception"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### GatewayTimeoutException
<a name="inputdevices-inputdeviceid-startinputdevicemaintenancewindow-model-gatewaytimeoutexception"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### InternalServiceError
<a name="inputdevices-inputdeviceid-startinputdevicemaintenancewindow-model-internalserviceerror"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### InvalidRequest
<a name="inputdevices-inputdeviceid-startinputdevicemaintenancewindow-model-invalidrequest"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### LimitExceeded
<a name="inputdevices-inputdeviceid-startinputdevicemaintenancewindow-model-limitexceeded"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### ResourceNotFound
<a name="inputdevices-inputdeviceid-startinputdevicemaintenancewindow-model-resourcenotfound"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### ValidationError
<a name="inputdevices-inputdeviceid-startinputdevicemaintenancewindow-model-validationerror"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| elementPath | string | False | Path to the source of the error. |
| errorMessage | string | False | The error message. |

## See also
<a name="inputdevices-inputdeviceid-startinputdevicemaintenancewindow-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### StartInputDeviceMaintenanceWindow
<a name="StartInputDeviceMaintenanceWindow-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/medialive-2017-10-14/StartInputDeviceMaintenanceWindow)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/medialive-2017-10-14/StartInputDeviceMaintenanceWindow)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/medialive-2017-10-14/StartInputDeviceMaintenanceWindow)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/medialive-2017-10-14/StartInputDeviceMaintenanceWindow)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/medialive-2017-10-14/StartInputDeviceMaintenanceWindow)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/medialive-2017-10-14/StartInputDeviceMaintenanceWindow)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/medialive-2017-10-14/StartInputDeviceMaintenanceWindow)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/medialive-2017-10-14/StartInputDeviceMaintenanceWindow)
+ [AWS SDK for Python](/goto/boto3/medialive-2017-10-14/StartInputDeviceMaintenanceWindow)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/medialive-2017-10-14/StartInputDeviceMaintenanceWindow)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
