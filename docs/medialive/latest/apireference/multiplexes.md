---
source_url: https://docs.aws.amazon.com/medialive/latest/apireference/multiplexes.html
---

# Multiplexes
<a name="multiplexes"></a>

## URI
<a name="multiplexes-url"></a>

`/prod/multiplexes`

## HTTP methods
<a name="multiplexes-http-methods"></a>

### GET
<a name="multiplexesget"></a>

**Operation ID:** `ListMultiplexes`

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| nextToken | String | False |  |
| maxResults | String | False |  |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | ListMultiplexesResultModel | 200 response |
| 400 | InvalidRequest | 400 response |
| 403 | AccessDenied | 403 response |
| 429 | LimitExceeded | 429 response |
| 500 | InternalServiceError | 500 response |
| 502 | BadGatewayException | 502 response |
| 504 | GatewayTimeoutException | 504 response |

### POST
<a name="multiplexespost"></a>

**Operation ID:** `CreateMultiplex`

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 201 | CreateMultiplexResultModel | 201 response |
| 400 | InvalidRequest | 400 response |
| 403 | AccessDenied | 403 response |
| 409 | ResourceConflict | 409 response |
| 422 | MultiplexConfigurationValidationError | 422 response |
| 429 | LimitExceeded | 429 response |
| 500 | InternalServiceError | 500 response |
| 502 | BadGatewayException | 502 response |
| 504 | GatewayTimeoutException | 504 response |

## Schemas
<a name="multiplexes-schemas"></a>

### Request bodies
<a name="multiplexes-request-examples"></a>

#### POST schema
<a name="multiplexes-request-body-post-example"></a>

```
{
  "availabilityZones": [
    "string"
  ],
  "multiplexSettings": {
    "maximumVideoBufferDelayMilliseconds": integer,
    "transportStreamBitrate": integer,
    "transportStreamId": integer,
    "transportStreamReservedBitrate": integer
  },
  "name": "string",
  "requestId": "string",
  "tags": {
  }
}
```

### Response bodies
<a name="multiplexes-response-examples"></a>

#### ListMultiplexesResultModel schema
<a name="multiplexes-response-body-listmultiplexesresultmodel-example"></a>

```
{
  "multiplexes": [
    {
      "arn": "string",
      "availabilityZones": [
        "string"
      ],
      "id": "string",
      "multiplexSettings": {
        "transportStreamBitrate": integer
      },
      "name": "string",
      "pipelinesRunningCount": integer,
      "programCount": integer,
      "state": enum,
      "tags": {
      }
    }
  ],
  "nextToken": "string"
}
```

#### CreateMultiplexResultModel schema
<a name="multiplexes-response-body-createmultiplexresultmodel-example"></a>

```
{
  "multiplex": {
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
}
```

#### InvalidRequest schema
<a name="multiplexes-response-body-invalidrequest-example"></a>

```
{
  "message": "string"
}
```

#### AccessDenied schema
<a name="multiplexes-response-body-accessdenied-example"></a>

```
{
  "message": "string"
}
```

#### ResourceConflict schema
<a name="multiplexes-response-body-resourceconflict-example"></a>

```
{
  "message": "string"
}
```

#### MultiplexConfigurationValidationError schema
<a name="multiplexes-response-body-multiplexconfigurationvalidationerror-example"></a>

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
<a name="multiplexes-response-body-limitexceeded-example"></a>

```
{
  "message": "string"
}
```

#### InternalServiceError schema
<a name="multiplexes-response-body-internalserviceerror-example"></a>

```
{
  "message": "string"
}
```

#### BadGatewayException schema
<a name="multiplexes-response-body-badgatewayexception-example"></a>

```
{
  "message": "string"
}
```

#### GatewayTimeoutException schema
<a name="multiplexes-response-body-gatewaytimeoutexception-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="multiplexes-properties"></a>

### AccessDenied
<a name="multiplexes-model-accessdenied"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### BadGatewayException
<a name="multiplexes-model-badgatewayexception"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### CreateMultiplex
<a name="multiplexes-model-createmultiplex"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| availabilityZones | Array of type string | True | A list of availability zones for the multiplex. You must specify exactly two. |
| multiplexSettings | [MultiplexSettings](#multiplexes-model-multiplexsettings) | True | Configuration for a multiplex event. |
| name | string | True | Name of multiplex. |
| requestId | string | True | Unique request ID. This prevents retries from creating multiple resources.  |
| tags | [Tags](#multiplexes-model-tags) | False | A collection of key-value pairs. |

### CreateMultiplexResultModel
<a name="multiplexes-model-createmultiplexresultmodel"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| multiplex | [Multiplex](#multiplexes-model-multiplex) | False | The newly created multiplex. |

### GatewayTimeoutException
<a name="multiplexes-model-gatewaytimeoutexception"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### InternalServiceError
<a name="multiplexes-model-internalserviceerror"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### InvalidRequest
<a name="multiplexes-model-invalidrequest"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### LimitExceeded
<a name="multiplexes-model-limitexceeded"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### ListMultiplexesResultModel
<a name="multiplexes-model-listmultiplexesresultmodel"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| multiplexes | Array of type [MultiplexSummary](#multiplexes-model-multiplexsummary) | False | List of multiplexes. |
| nextToken | string | False | Token for the next ListMultiplexes request. |

### Multiplex
<a name="multiplexes-model-multiplex"></a>

The multiplex object.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| arn | string | False | The unique arn of the multiplex. |
| availabilityZones | Array of type string | False | A list of availability zones for the multiplex. |
| destinations | Array of type [MultiplexOutputDestination](#multiplexes-model-multiplexoutputdestination) | False | A list of the multiplex output destinations. |
| id | string | False | The unique id of the multiplex. |
| multiplexSettings | [MultiplexSettings](#multiplexes-model-multiplexsettings) | False | Configuration for a multiplex event. |
| name | string | False | The name of the multiplex. |
| pipelinesRunningCount | integer | False | The number of currently healthy pipelines. |
| programCount | integer | False | The number of programs in the multiplex. |
| state | [MultiplexState](#multiplexes-model-multiplexstate) | False | The current state of the multiplex. |
| tags | [Tags](#multiplexes-model-tags) | False | A collection of key-value pairs. |

### MultiplexConfigurationValidationError
<a name="multiplexes-model-multiplexconfigurationvalidationerror"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The error message. |
| validationErrors | Array of type [ValidationError](#multiplexes-model-validationerror) | False | A collection of validation error responses. |

### MultiplexMediaConnectOutputDestinationSettings
<a name="multiplexes-model-multiplexmediaconnectoutputdestinationsettings"></a>

Multiplex MediaConnect output destination settings.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| entitlementArn | string<br />MinLength: 1 | False | The MediaConnect entitlement ARN available as a Flow source. |

### MultiplexOutputDestination
<a name="multiplexes-model-multiplexoutputdestination"></a>

Multiplex output destination settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| mediaConnectSettings | [MultiplexMediaConnectOutputDestinationSettings](#multiplexes-model-multiplexmediaconnectoutputdestinationsettings) | False | Multiplex MediaConnect output destination settings. |

### MultiplexSettings
<a name="multiplexes-model-multiplexsettings"></a>

Contains configuration for a Multiplex event

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| maximumVideoBufferDelayMilliseconds | integer<br />Minimum: 800<br />Maximum: 3000 | False | Maximum video buffer delay in milliseconds. |
| transportStreamBitrate | integer<br />Minimum: 1000000<br />Maximum: 100000000 | True | Transport stream bit rate. |
| transportStreamId | integer<br />Minimum: 0<br />Maximum: 65535 | True | Transport stream ID. |
| transportStreamReservedBitrate | integer<br />Minimum: 0<br />Maximum: 100000000 | False | Transport stream reserved bit rate. |

### MultiplexSettingsSummary
<a name="multiplexes-model-multiplexsettingssummary"></a>

Contains summary configuration for a Multiplex event.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| transportStreamBitrate | integer<br />Minimum: 1000000<br />Maximum: 100000000 | False | Transport stream bit rate. |

### MultiplexState
<a name="multiplexes-model-multiplexstate"></a>

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

### MultiplexSummary
<a name="multiplexes-model-multiplexsummary"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| arn | string | False | The unique arn of the multiplex. |
| availabilityZones | Array of type string | False | A list of availability zones for the multiplex. |
| id | string | False | The unique id of the multiplex. |
| multiplexSettings | [MultiplexSettingsSummary](#multiplexes-model-multiplexsettingssummary) | False | Configuration for a multiplex event. |
| name | string | False | The name of the multiplex. |
| pipelinesRunningCount | integer | False | The number of currently healthy pipelines. |
| programCount | integer | False | The number of programs in the multiplex. |
| state | [MultiplexState](#multiplexes-model-multiplexstate) | False | The current state of the multiplex. |
| tags | [Tags](#multiplexes-model-tags) | False | A collection of key-value pairs. |

### ResourceConflict
<a name="multiplexes-model-resourceconflict"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### Tags
<a name="multiplexes-model-tags"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| `*` | string | False |  |

### ValidationError
<a name="multiplexes-model-validationerror"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| elementPath | string | False | Path to the source of the error. |
| errorMessage | string | False | The error message. |

## See also
<a name="multiplexes-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### ListMultiplexes
<a name="ListMultiplexes-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/medialive-2017-10-14/ListMultiplexes)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/medialive-2017-10-14/ListMultiplexes)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/medialive-2017-10-14/ListMultiplexes)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/medialive-2017-10-14/ListMultiplexes)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/medialive-2017-10-14/ListMultiplexes)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/medialive-2017-10-14/ListMultiplexes)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/medialive-2017-10-14/ListMultiplexes)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/medialive-2017-10-14/ListMultiplexes)
+ [AWS SDK for Python](/goto/boto3/medialive-2017-10-14/ListMultiplexes)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/medialive-2017-10-14/ListMultiplexes)

### CreateMultiplex
<a name="CreateMultiplex-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/medialive-2017-10-14/CreateMultiplex)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/medialive-2017-10-14/CreateMultiplex)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/medialive-2017-10-14/CreateMultiplex)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/medialive-2017-10-14/CreateMultiplex)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/medialive-2017-10-14/CreateMultiplex)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/medialive-2017-10-14/CreateMultiplex)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/medialive-2017-10-14/CreateMultiplex)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/medialive-2017-10-14/CreateMultiplex)
+ [AWS SDK for Python](/goto/boto3/medialive-2017-10-14/CreateMultiplex)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/medialive-2017-10-14/CreateMultiplex)
