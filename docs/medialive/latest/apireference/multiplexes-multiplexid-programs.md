---
source_url: https://docs.aws.amazon.com/medialive/latest/apireference/multiplexes-multiplexid-programs.html
---

# Multiplex: list programs
<a name="multiplexes-multiplexid-programs"></a>

## URI
<a name="multiplexes-multiplexid-programs-url"></a>

`/prod/multiplexes/{{multiplexId}}/programs`

## HTTP methods
<a name="multiplexes-multiplexid-programs-http-methods"></a>

### GET
<a name="multiplexes-multiplexid-programsget"></a>

**Operation ID:** `ListMultiplexPrograms`

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{multiplexId}} | String | True |  |

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| nextToken | String | False |  |
| maxResults | String | False |  |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | ListMultiplexProgramsResultModel | 200 response |
| 400 | InvalidRequest | 400 response |
| 403 | AccessDenied | 403 response |
| 404 | ResourceNotFound | 404 response |
| 429 | LimitExceeded | 429 response |
| 500 | InternalServiceError | 500 response |
| 502 | BadGatewayException | 502 response |
| 504 | GatewayTimeoutException | 504 response |

### POST
<a name="multiplexes-multiplexid-programspost"></a>

**Operation ID:** `CreateMultiplexProgram`

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{multiplexId}} | String | True |  |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 201 | CreateMultiplexProgramResultModel | 201 response |
| 400 | InvalidRequest | 400 response |
| 403 | AccessDenied | 403 response |
| 409 | ResourceConflict | 409 response |
| 422 | MultiplexConfigurationValidationError | 422 response |
| 429 | LimitExceeded | 429 response |
| 500 | InternalServiceError | 500 response |
| 502 | BadGatewayException | 502 response |
| 504 | GatewayTimeoutException | 504 response |

## Schemas
<a name="multiplexes-multiplexid-programs-schemas"></a>

### Request bodies
<a name="multiplexes-multiplexid-programs-request-examples"></a>

#### POST schema
<a name="multiplexes-multiplexid-programs-request-body-post-example"></a>

```
{
  "multiplexProgramSettings": {
    "preferredChannelPipeline": enum,
    "programNumber": integer,
    "serviceDescriptor": {
      "providerName": "string",
      "serviceName": "string"
    },
    "videoSettings": {
      "constantBitrate": integer,
      "statmuxSettings": {
        "maximumBitrate": integer,
        "minimumBitrate": integer,
        "priority": integer
      }
    }
  },
  "programName": "string",
  "requestId": "string"
}
```

### Response bodies
<a name="multiplexes-multiplexid-programs-response-examples"></a>

#### ListMultiplexProgramsResultModel schema
<a name="multiplexes-multiplexid-programs-response-body-listmultiplexprogramsresultmodel-example"></a>

```
{
  "multiplexPrograms": [
    {
      "channelId": "string",
      "programName": "string"
    }
  ],
  "nextToken": "string"
}
```

#### CreateMultiplexProgramResultModel schema
<a name="multiplexes-multiplexid-programs-response-body-createmultiplexprogramresultmodel-example"></a>

```
{
  "multiplexProgram": {
    "channelId": "string",
    "multiplexProgramSettings": {
      "preferredChannelPipeline": enum,
      "programNumber": integer,
      "serviceDescriptor": {
        "providerName": "string",
        "serviceName": "string"
      },
      "videoSettings": {
        "constantBitrate": integer,
        "statmuxSettings": {
          "maximumBitrate": integer,
          "minimumBitrate": integer,
          "priority": integer
        }
      }
    },
    "packetIdentifiersMap": {
      "audioPids": [
        integer
      ],
      "dvbSubPids": [
        integer
      ],
      "dvbTeletextPid": integer,
      "etvPlatformPid": integer,
      "etvSignalPid": integer,
      "klvDataPids": [
        integer
      ],
      "pcrPid": integer,
      "pmtPid": integer,
      "privateMetadataPid": integer,
      "scte27Pids": [
        integer
      ],
      "scte35Pid": integer,
      "timedMetadataPid": integer,
      "videoPid": integer
    },
    "pipelineDetails": [
      {
        "activeChannelPipeline": "string",
        "pipelineId": "string"
      }
    ],
    "programName": "string"
  }
}
```

#### InvalidRequest schema
<a name="multiplexes-multiplexid-programs-response-body-invalidrequest-example"></a>

```
{
  "message": "string"
}
```

#### AccessDenied schema
<a name="multiplexes-multiplexid-programs-response-body-accessdenied-example"></a>

```
{
  "message": "string"
}
```

#### ResourceNotFound schema
<a name="multiplexes-multiplexid-programs-response-body-resourcenotfound-example"></a>

```
{
  "message": "string"
}
```

#### ResourceConflict schema
<a name="multiplexes-multiplexid-programs-response-body-resourceconflict-example"></a>

```
{
  "message": "string"
}
```

#### MultiplexConfigurationValidationError schema
<a name="multiplexes-multiplexid-programs-response-body-multiplexconfigurationvalidationerror-example"></a>

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
<a name="multiplexes-multiplexid-programs-response-body-limitexceeded-example"></a>

```
{
  "message": "string"
}
```

#### InternalServiceError schema
<a name="multiplexes-multiplexid-programs-response-body-internalserviceerror-example"></a>

```
{
  "message": "string"
}
```

#### BadGatewayException schema
<a name="multiplexes-multiplexid-programs-response-body-badgatewayexception-example"></a>

```
{
  "message": "string"
}
```

#### GatewayTimeoutException schema
<a name="multiplexes-multiplexid-programs-response-body-gatewaytimeoutexception-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="multiplexes-multiplexid-programs-properties"></a>

### AccessDenied
<a name="multiplexes-multiplexid-programs-model-accessdenied"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### BadGatewayException
<a name="multiplexes-multiplexid-programs-model-badgatewayexception"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### CreateMultiplexProgram
<a name="multiplexes-multiplexid-programs-model-createmultiplexprogram"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| multiplexProgramSettings | [MultiplexProgramSettings](#multiplexes-multiplexid-programs-model-multiplexprogramsettings) | True | The settings for this multiplex program. |
| programName | string | True | Name of multiplex program. |
| requestId | string | True | Unique request ID. This prevents retries from creating multiple resources.  |

### CreateMultiplexProgramResultModel
<a name="multiplexes-multiplexid-programs-model-createmultiplexprogramresultmodel"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| multiplexProgram | [MultiplexProgram](#multiplexes-multiplexid-programs-model-multiplexprogram) | False | The newly created multiplex program. |

### GatewayTimeoutException
<a name="multiplexes-multiplexid-programs-model-gatewaytimeoutexception"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### InternalServiceError
<a name="multiplexes-multiplexid-programs-model-internalserviceerror"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### InvalidRequest
<a name="multiplexes-multiplexid-programs-model-invalidrequest"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### LimitExceeded
<a name="multiplexes-multiplexid-programs-model-limitexceeded"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### ListMultiplexProgramsResultModel
<a name="multiplexes-multiplexid-programs-model-listmultiplexprogramsresultmodel"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| multiplexPrograms | Array of type [MultiplexProgramSummary](#multiplexes-multiplexid-programs-model-multiplexprogramsummary) | False | List of multiplex programs. |
| nextToken | string | False | Token for the next ListMultiplexProgram request. |

### MultiplexConfigurationValidationError
<a name="multiplexes-multiplexid-programs-model-multiplexconfigurationvalidationerror"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The error message. |
| validationErrors | Array of type [ValidationError](#multiplexes-multiplexid-programs-model-validationerror) | False | A collection of validation error responses. |

### MultiplexProgram
<a name="multiplexes-multiplexid-programs-model-multiplexprogram"></a>

The multiplex program object.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| channelId | string | False | The MediaLive channel associated with the program. |
| multiplexProgramSettings | [MultiplexProgramSettings](#multiplexes-multiplexid-programs-model-multiplexprogramsettings) | False | The settings for this multiplex program. |
| packetIdentifiersMap | [MultiplexProgramPacketIdentifiersMap](#multiplexes-multiplexid-programs-model-multiplexprogrampacketidentifiersmap) | False | The packet identifier map for this multiplex program. |
| pipelineDetails | Array of type [MultiplexProgramPipelineDetail](#multiplexes-multiplexid-programs-model-multiplexprogrampipelinedetail) | False | Contains information about the current sources for the specified program in the specified multiplex. Keep in mind that each multiplex pipeline connects to both pipelines in a given source channel (the channel identified by the program). But only one of those channel pipelines is ever active at one time. |
| programName | string | False | The name of the multiplex program. |

### MultiplexProgramPacketIdentifiersMap
<a name="multiplexes-multiplexid-programs-model-multiplexprogrampacketidentifiersmap"></a>

Packet identifiers map for a given Multiplex program.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| audioPids | Array of type integer | False |  |
| dvbSubPids | Array of type integer | False |  |
| dvbTeletextPid | integer | False |  |
| etvPlatformPid | integer | False |  |
| etvSignalPid | integer | False |  |
| klvDataPids | Array of type integer | False |  |
| pcrPid | integer | False |  |
| pmtPid | integer | False |  |
| privateMetadataPid | integer | False |  |
| scte27Pids | Array of type integer | False |  |
| scte35Pid | integer | False |  |
| timedMetadataPid | integer | False |  |
| videoPid | integer | False |  |

### MultiplexProgramPipelineDetail
<a name="multiplexes-multiplexid-programs-model-multiplexprogrampipelinedetail"></a>

The current source for one of the pipelines in the multiplex.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| activeChannelPipeline | string | False | Identifies the channel pipeline that is currently active for the pipeline (identified by PipelineId) in the multiplex. |
| pipelineId | string | False | Identifies a specific pipeline in the multiplex. |

### MultiplexProgramServiceDescriptor
<a name="multiplexes-multiplexid-programs-model-multiplexprogramservicedescriptor"></a>

Transport stream service descriptor configuration for the Multiplex program.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| providerName | string<br />MaxLength: 256 | True | Name of the provider. |
| serviceName | string<br />MaxLength: 256 | True | Name of the service. |

### MultiplexProgramSettings
<a name="multiplexes-multiplexid-programs-model-multiplexprogramsettings"></a>

Multiplex Program settings configuration.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| preferredChannelPipeline | [PreferredChannelPipeline](#multiplexes-multiplexid-programs-model-preferredchannelpipeline) | False | Indicates which pipeline is preferred by the multiplex for program ingest. |
| programNumber | integer<br />Minimum: 0<br />Maximum: 65535 | True | Unique program number. |
| serviceDescriptor | [MultiplexProgramServiceDescriptor](#multiplexes-multiplexid-programs-model-multiplexprogramservicedescriptor) | False | Transport stream service descriptor configuration for the Multiplex program. |
| videoSettings | [MultiplexVideoSettings](#multiplexes-multiplexid-programs-model-multiplexvideosettings) | False | Program video settings configuration. |

### MultiplexProgramSummary
<a name="multiplexes-multiplexid-programs-model-multiplexprogramsummary"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| channelId | string | False | The MediaLive Channel associated with the program. |
| programName | string | False | The name of the multiplex program. |

### MultiplexStatmuxVideoSettings
<a name="multiplexes-multiplexid-programs-model-multiplexstatmuxvideosettings"></a>

Statmux rate control settings

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| maximumBitrate | integer<br />Minimum: 100000<br />Maximum: 100000000 | False | Maximum statmux bitrate. |
| minimumBitrate | integer<br />Minimum: 100000<br />Maximum: 100000000 | False | Minimum statmux bitrate. |
| priority | integer<br />Minimum: -5<br />Maximum: 5 | False | The purpose of the priority is to use a combination of the\\nmultiplex rate control algorithm and the QVBR capability of the\\nencoder to prioritize the video quality of some channels in a\\nmultiplex over others. Channels that have a higher priority will\\nget higher video quality at the expense of the video quality of\\nother channels in the multiplex with lower priority. |

### MultiplexVideoSettings
<a name="multiplexes-multiplexid-programs-model-multiplexvideosettings"></a>

The video configuration for each program in a multiplex.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| constantBitrate | integer<br />Minimum: 100000<br />Maximum: 100000000 | False | The constant bitrate configuration for the video encode. When this field is defined, StatmuxSettings must be undefined. |
| statmuxSettings | [MultiplexStatmuxVideoSettings](#multiplexes-multiplexid-programs-model-multiplexstatmuxvideosettings) | False | Statmux rate control settings. When this field is defined, ConstantBitrate must be undefined. |

### PreferredChannelPipeline
<a name="multiplexes-multiplexid-programs-model-preferredchannelpipeline"></a>

Indicates which pipeline is preferred by the multiplex for program ingest. If set to \\"PIPELINE\_0\\" or \\"PIPELINE\_1\\" and an unhealthy ingest causes the multiplex to switch to the non-preferred pipeline, it will switch back once that ingest is healthy again. If set to \\"CURRENTLY\_ACTIVE\\", it will not switch back to the other pipeline based on it recovering to a healthy state, it will only switch if the active pipeline becomes unhealthy.
+ `CURRENTLY_ACTIVE`
+ `PIPELINE_0`
+ `PIPELINE_1`

### ResourceConflict
<a name="multiplexes-multiplexid-programs-model-resourceconflict"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### ResourceNotFound
<a name="multiplexes-multiplexid-programs-model-resourcenotfound"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### ValidationError
<a name="multiplexes-multiplexid-programs-model-validationerror"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| elementPath | string | False | Path to the source of the error. |
| errorMessage | string | False | The error message. |

## See also
<a name="multiplexes-multiplexid-programs-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### ListMultiplexPrograms
<a name="ListMultiplexPrograms-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/medialive-2017-10-14/ListMultiplexPrograms)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/medialive-2017-10-14/ListMultiplexPrograms)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/medialive-2017-10-14/ListMultiplexPrograms)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/medialive-2017-10-14/ListMultiplexPrograms)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/medialive-2017-10-14/ListMultiplexPrograms)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/medialive-2017-10-14/ListMultiplexPrograms)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/medialive-2017-10-14/ListMultiplexPrograms)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/medialive-2017-10-14/ListMultiplexPrograms)
+ [AWS SDK for Python (Boto3)](/goto/boto3/medialive-2017-10-14/ListMultiplexPrograms)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/medialive-2017-10-14/ListMultiplexPrograms)

### CreateMultiplexProgram
<a name="CreateMultiplexProgram-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/medialive-2017-10-14/CreateMultiplexProgram)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/medialive-2017-10-14/CreateMultiplexProgram)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/medialive-2017-10-14/CreateMultiplexProgram)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/medialive-2017-10-14/CreateMultiplexProgram)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/medialive-2017-10-14/CreateMultiplexProgram)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/medialive-2017-10-14/CreateMultiplexProgram)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/medialive-2017-10-14/CreateMultiplexProgram)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/medialive-2017-10-14/CreateMultiplexProgram)
+ [AWS SDK for Python (Boto3)](/goto/boto3/medialive-2017-10-14/CreateMultiplexProgram)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/medialive-2017-10-14/CreateMultiplexProgram)
