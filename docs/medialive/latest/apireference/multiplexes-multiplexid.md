---
source_url: https://docs.aws.amazon.com/medialive/latest/apireference/multiplexes-multiplexid.html
---

# Multiplexes: multiplex ID
<a name="multiplexes-multiplexid"></a>

## URI
<a name="multiplexes-multiplexid-url"></a>

`/prod/multiplexes/{{multiplexId}}`

## HTTP methods
<a name="multiplexes-multiplexid-http-methods"></a>

### DELETE
<a name="multiplexes-multiplexiddelete"></a>

**Operation ID:** `DeleteMultiplex`

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

### GET
<a name="multiplexes-multiplexidget"></a>

**Operation ID:** `DescribeMultiplex`

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{multiplexId}} | String | True |  |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | Multiplex | 200 response |
| 400 | InvalidRequest | 400 response |
| 403 | AccessDenied | 403 response |
| 404 | ResourceNotFound | 404 response |
| 429 | LimitExceeded | 429 response |
| 500 | InternalServiceError | 500 response |
| 502 | BadGatewayException | 502 response |
| 504 | GatewayTimeoutException | 504 response |

### PUT
<a name="multiplexes-multiplexidput"></a>

**Operation ID:** `UpdateMultiplex`

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{multiplexId}} | String | True |  |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | UpdateMultiplexResultModel | 200 response |
| 400 | InvalidRequest | 400 response |
| 403 | AccessDenied | 403 response |
| 404 | ResourceNotFound | 404 response |
| 409 | ResourceConflict | 409 response |
| 422 | MultiplexConfigurationValidationError | 422 response |
| 500 | InternalServiceError | 500 response |
| 502 | BadGatewayException | 502 response |
| 504 | GatewayTimeoutException | 504 response |

## Schemas
<a name="multiplexes-multiplexid-schemas"></a>

### Request bodies
<a name="multiplexes-multiplexid-request-examples"></a>

#### PUT schema
<a name="multiplexes-multiplexid-request-body-put-example"></a>

```
{
  "multiplexSettings": {
    "maximumVideoBufferDelayMilliseconds": integer,
    "transportStreamBitrate": integer,
    "transportStreamId": integer,
    "transportStreamReservedBitrate": integer
  },
  "name": "string"
}
```

### Response bodies
<a name="multiplexes-multiplexid-response-examples"></a>

#### UpdateMultiplexResultModel schema
<a name="multiplexes-multiplexid-response-body-updatemultiplexresultmodel-example"></a>

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

#### Multiplex schema
<a name="multiplexes-multiplexid-response-body-multiplex-example"></a>

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
<a name="multiplexes-multiplexid-response-body-invalidrequest-example"></a>

```
{
  "message": "string"
}
```

#### AccessDenied schema
<a name="multiplexes-multiplexid-response-body-accessdenied-example"></a>

```
{
  "message": "string"
}
```

#### ResourceNotFound schema
<a name="multiplexes-multiplexid-response-body-resourcenotfound-example"></a>

```
{
  "message": "string"
}
```

#### ResourceConflict schema
<a name="multiplexes-multiplexid-response-body-resourceconflict-example"></a>

```
{
  "message": "string"
}
```

#### MultiplexConfigurationValidationError schema
<a name="multiplexes-multiplexid-response-body-multiplexconfigurationvalidationerror-example"></a>

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
<a name="multiplexes-multiplexid-response-body-limitexceeded-example"></a>

```
{
  "message": "string"
}
```

#### InternalServiceError schema
<a name="multiplexes-multiplexid-response-body-internalserviceerror-example"></a>

```
{
  "message": "string"
}
```

#### BadGatewayException schema
<a name="multiplexes-multiplexid-response-body-badgatewayexception-example"></a>

```
{
  "message": "string"
}
```

#### GatewayTimeoutException schema
<a name="multiplexes-multiplexid-response-body-gatewaytimeoutexception-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="multiplexes-multiplexid-properties"></a>

### AccessDenied
<a name="multiplexes-multiplexid-model-accessdenied"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### BadGatewayException
<a name="multiplexes-multiplexid-model-badgatewayexception"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### GatewayTimeoutException
<a name="multiplexes-multiplexid-model-gatewaytimeoutexception"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### InternalServiceError
<a name="multiplexes-multiplexid-model-internalserviceerror"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### InvalidRequest
<a name="multiplexes-multiplexid-model-invalidrequest"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### LimitExceeded
<a name="multiplexes-multiplexid-model-limitexceeded"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### Multiplex
<a name="multiplexes-multiplexid-model-multiplex"></a>

The multiplex object.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| arn | string | False | The unique arn of the multiplex. |
| availabilityZones | Array of type string | False | A list of availability zones for the multiplex. |
| destinations | Array of type [MultiplexOutputDestination](#multiplexes-multiplexid-model-multiplexoutputdestination) | False | A list of the multiplex output destinations. |
| id | string | False | The unique id of the multiplex. |
| multiplexSettings | [MultiplexSettings](#multiplexes-multiplexid-model-multiplexsettings) | False | Configuration for a multiplex event. |
| name | string | False | The name of the multiplex. |
| pipelinesRunningCount | integer | False | The number of currently healthy pipelines. |
| programCount | integer | False | The number of programs in the multiplex. |
| state | [MultiplexState](#multiplexes-multiplexid-model-multiplexstate) | False | The current state of the multiplex. |
| tags | [Tags](#multiplexes-multiplexid-model-tags) | False | A collection of key-value pairs. |

### MultiplexConfigurationValidationError
<a name="multiplexes-multiplexid-model-multiplexconfigurationvalidationerror"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The error message. |
| validationErrors | Array of type [ValidationError](#multiplexes-multiplexid-model-validationerror) | False | A collection of validation error responses. |

### MultiplexMediaConnectOutputDestinationSettings
<a name="multiplexes-multiplexid-model-multiplexmediaconnectoutputdestinationsettings"></a>

Multiplex MediaConnect output destination settings.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| entitlementArn | string<br />MinLength: 1 | False | The MediaConnect entitlement ARN available as a Flow source. |

### MultiplexOutputDestination
<a name="multiplexes-multiplexid-model-multiplexoutputdestination"></a>

Multiplex output destination settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| mediaConnectSettings | [MultiplexMediaConnectOutputDestinationSettings](#multiplexes-multiplexid-model-multiplexmediaconnectoutputdestinationsettings) | False | Multiplex MediaConnect output destination settings. |

### MultiplexSettings
<a name="multiplexes-multiplexid-model-multiplexsettings"></a>

Contains configuration for a Multiplex event

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| maximumVideoBufferDelayMilliseconds | integer<br />Minimum: 800<br />Maximum: 3000 | False | Maximum video buffer delay in milliseconds. |
| transportStreamBitrate | integer<br />Minimum: 1000000<br />Maximum: 100000000 | True | Transport stream bit rate. |
| transportStreamId | integer<br />Minimum: 0<br />Maximum: 65535 | True | Transport stream ID. |
| transportStreamReservedBitrate | integer<br />Minimum: 0<br />Maximum: 100000000 | False | Transport stream reserved bit rate. |

### MultiplexState
<a name="multiplexes-multiplexid-model-multiplexstate"></a>

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
<a name="multiplexes-multiplexid-model-resourceconflict"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### ResourceNotFound
<a name="multiplexes-multiplexid-model-resourcenotfound"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### Tags
<a name="multiplexes-multiplexid-model-tags"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| `*` | string | False |  |

### UpdateMultiplex
<a name="multiplexes-multiplexid-model-updatemultiplex"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| multiplexSettings | [MultiplexSettings](#multiplexes-multiplexid-model-multiplexsettings) | False | The new settings for a multiplex. |
| name | string | False | Name of the multiplex. |

### UpdateMultiplexResultModel
<a name="multiplexes-multiplexid-model-updatemultiplexresultmodel"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| multiplex | [Multiplex](#multiplexes-multiplexid-model-multiplex) | False | The updated multiplex. |

### ValidationError
<a name="multiplexes-multiplexid-model-validationerror"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| elementPath | string | False | Path to the source of the error. |
| errorMessage | string | False | The error message. |

## See also
<a name="multiplexes-multiplexid-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### DeleteMultiplex
<a name="DeleteMultiplex-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/medialive-2017-10-14/DeleteMultiplex)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/medialive-2017-10-14/DeleteMultiplex)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/medialive-2017-10-14/DeleteMultiplex)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/medialive-2017-10-14/DeleteMultiplex)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/medialive-2017-10-14/DeleteMultiplex)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/medialive-2017-10-14/DeleteMultiplex)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/medialive-2017-10-14/DeleteMultiplex)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/medialive-2017-10-14/DeleteMultiplex)
+ [AWS SDK for Python](/goto/boto3/medialive-2017-10-14/DeleteMultiplex)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/medialive-2017-10-14/DeleteMultiplex)

### DescribeMultiplex
<a name="DescribeMultiplex-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/medialive-2017-10-14/DescribeMultiplex)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/medialive-2017-10-14/DescribeMultiplex)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/medialive-2017-10-14/DescribeMultiplex)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/medialive-2017-10-14/DescribeMultiplex)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/medialive-2017-10-14/DescribeMultiplex)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/medialive-2017-10-14/DescribeMultiplex)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/medialive-2017-10-14/DescribeMultiplex)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/medialive-2017-10-14/DescribeMultiplex)
+ [AWS SDK for Python](/goto/boto3/medialive-2017-10-14/DescribeMultiplex)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/medialive-2017-10-14/DescribeMultiplex)

### UpdateMultiplex
<a name="UpdateMultiplex-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/medialive-2017-10-14/UpdateMultiplex)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/medialive-2017-10-14/UpdateMultiplex)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/medialive-2017-10-14/UpdateMultiplex)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/medialive-2017-10-14/UpdateMultiplex)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/medialive-2017-10-14/UpdateMultiplex)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/medialive-2017-10-14/UpdateMultiplex)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/medialive-2017-10-14/UpdateMultiplex)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/medialive-2017-10-14/UpdateMultiplex)
+ [AWS SDK for Python](/goto/boto3/medialive-2017-10-14/UpdateMultiplex)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/medialive-2017-10-14/UpdateMultiplex)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
