---
source_url: https://docs.aws.amazon.com/medialive/latest/apireference/multiplexes-multiplexid-start.html
---

# Multiplex: start
<a name="multiplexes-multiplexid-start"></a>

## URI
<a name="multiplexes-multiplexid-start-url"></a>

`/prod/multiplexes/{{multiplexId}}/start`

## HTTP methods
<a name="multiplexes-multiplexid-start-http-methods"></a>

### POST
<a name="multiplexes-multiplexid-startpost"></a>

**Operation ID:** `StartMultiplex`

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{multiplexId}} | String | True |  |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 202 | Multiplex | 202 response |
| 400 | InvalidRequest | 400 response |
| 403 | AccessDenied | 403 response |
| 404 | ResourceNotFound | 404 response |
| 409 | ResourceConflict | 409 response |
| 429 | LimitExceeded | 429 response |
| 500 | InternalServiceError | 500 response |
| 502 | BadGatewayException | 502 response |
| 504 | GatewayTimeoutException | 504 response |

## Schemas
<a name="multiplexes-multiplexid-start-schemas"></a>

### Response bodies
<a name="multiplexes-multiplexid-start-response-examples"></a>

#### Multiplex schema
<a name="multiplexes-multiplexid-start-response-body-multiplex-example"></a>

```
{
  "arn": "string",
  "availabilityZones": [
    "string"
  ],
  "destinations": [
    {
      "mediaConnectSettings": {
        "entitlementArn": "string"
      }
    }
  ],
  "id": "string",
  "multiplexSettings": {
    "maximumVideoBufferDelayMilliseconds": integer,
    "transportStreamBitrate": integer,
    "transportStreamId": integer,
    "transportStreamReservedBitrate": integer
  },
  "name": "string",
  "pipelinesRunningCount": integer,
  "programCount": integer,
  "state": enum,
  "tags": {
  }
}
```

#### InvalidRequest schema
<a name="multiplexes-multiplexid-start-response-body-invalidrequest-example"></a>

```
{
  "message": "string"
}
```

#### AccessDenied schema
<a name="multiplexes-multiplexid-start-response-body-accessdenied-example"></a>

```
{
  "message": "string"
}
```

#### ResourceNotFound schema
<a name="multiplexes-multiplexid-start-response-body-resourcenotfound-example"></a>

```
{
  "message": "string"
}
```

#### ResourceConflict schema
<a name="multiplexes-multiplexid-start-response-body-resourceconflict-example"></a>

```
{
  "message": "string"
}
```

#### LimitExceeded schema
<a name="multiplexes-multiplexid-start-response-body-limitexceeded-example"></a>

```
{
  "message": "string"
}
```

#### InternalServiceError schema
<a name="multiplexes-multiplexid-start-response-body-internalserviceerror-example"></a>

```
{
  "message": "string"
}
```

#### BadGatewayException schema
<a name="multiplexes-multiplexid-start-response-body-badgatewayexception-example"></a>

```
{
  "message": "string"
}
```

#### GatewayTimeoutException schema
<a name="multiplexes-multiplexid-start-response-body-gatewaytimeoutexception-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="multiplexes-multiplexid-start-properties"></a>

### AccessDenied
<a name="multiplexes-multiplexid-start-model-accessdenied"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### BadGatewayException
<a name="multiplexes-multiplexid-start-model-badgatewayexception"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### GatewayTimeoutException
<a name="multiplexes-multiplexid-start-model-gatewaytimeoutexception"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### InternalServiceError
<a name="multiplexes-multiplexid-start-model-internalserviceerror"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### InvalidRequest
<a name="multiplexes-multiplexid-start-model-invalidrequest"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### LimitExceeded
<a name="multiplexes-multiplexid-start-model-limitexceeded"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### Multiplex
<a name="multiplexes-multiplexid-start-model-multiplex"></a>

The multiplex object.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| arn | string | False | The unique arn of the multiplex. |
| availabilityZones | Array of type string | False | A list of availability zones for the multiplex. |
| destinations | Array of type [MultiplexOutputDestination](#multiplexes-multiplexid-start-model-multiplexoutputdestination) | False | A list of the multiplex output destinations. |
| id | string | False | The unique id of the multiplex. |
| multiplexSettings | [MultiplexSettings](#multiplexes-multiplexid-start-model-multiplexsettings) | False | Configuration for a multiplex event. |
| name | string | False | The name of the multiplex. |
| pipelinesRunningCount | integer | False | The number of currently healthy pipelines. |
| programCount | integer | False | The number of programs in the multiplex. |
| state | [MultiplexState](#multiplexes-multiplexid-start-model-multiplexstate) | False | The current state of the multiplex. |
| tags | [Tags](#multiplexes-multiplexid-start-model-tags) | False | A collection of key-value pairs. |

### MultiplexMediaConnectOutputDestinationSettings
<a name="multiplexes-multiplexid-start-model-multiplexmediaconnectoutputdestinationsettings"></a>

Multiplex MediaConnect output destination settings.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| entitlementArn | string<br />MinLength: 1 | False | The MediaConnect entitlement ARN available as a Flow source. |

### MultiplexOutputDestination
<a name="multiplexes-multiplexid-start-model-multiplexoutputdestination"></a>

Multiplex output destination settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| mediaConnectSettings | [MultiplexMediaConnectOutputDestinationSettings](#multiplexes-multiplexid-start-model-multiplexmediaconnectoutputdestinationsettings) | False | Multiplex MediaConnect output destination settings. |

### MultiplexSettings
<a name="multiplexes-multiplexid-start-model-multiplexsettings"></a>

Contains configuration for a Multiplex event

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| maximumVideoBufferDelayMilliseconds | integer<br />Minimum: 800<br />Maximum: 3000 | False | Maximum video buffer delay in milliseconds. |
| transportStreamBitrate | integer<br />Minimum: 1000000<br />Maximum: 100000000 | True | Transport stream bit rate. |
| transportStreamId | integer<br />Minimum: 0<br />Maximum: 65535 | True | Transport stream ID. |
| transportStreamReservedBitrate | integer<br />Minimum: 0<br />Maximum: 100000000 | False | Transport stream reserved bit rate. |

### MultiplexState
<a name="multiplexes-multiplexid-start-model-multiplexstate"></a>

The current state of the multiplex.
+ `CREATING`
+ `CREATE_FAILED`
+ `IDLE`
+ `STARTING`
+ `RUNNING`
+ `RECOVERING`
+ `STOPPING`
+ `DELETING`
+ `DELETED`

### ResourceConflict
<a name="multiplexes-multiplexid-start-model-resourceconflict"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### ResourceNotFound
<a name="multiplexes-multiplexid-start-model-resourcenotfound"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### Tags
<a name="multiplexes-multiplexid-start-model-tags"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| `*` | string | False |  |

## See also
<a name="multiplexes-multiplexid-start-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### StartMultiplex
<a name="StartMultiplex-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/medialive-2017-10-14/StartMultiplex)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/medialive-2017-10-14/StartMultiplex)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/medialive-2017-10-14/StartMultiplex)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/medialive-2017-10-14/StartMultiplex)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/medialive-2017-10-14/StartMultiplex)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/medialive-2017-10-14/StartMultiplex)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/medialive-2017-10-14/StartMultiplex)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/medialive-2017-10-14/StartMultiplex)
+ [AWS SDK for Python (Boto3)](/goto/boto3/medialive-2017-10-14/StartMultiplex)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/medialive-2017-10-14/StartMultiplex)
