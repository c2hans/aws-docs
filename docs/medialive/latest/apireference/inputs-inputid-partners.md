---
source_url: https://docs.aws.amazon.com/medialive/latest/apireference/inputs-inputid-partners.html
---

# Inputs: partners
<a name="inputs-inputid-partners"></a>

## URI
<a name="inputs-inputid-partners-url"></a>

`/prod/inputs/{{inputId}}/partners`

## HTTP methods
<a name="inputs-inputid-partners-http-methods"></a>

### POST
<a name="inputs-inputid-partnerspost"></a>

**Operation ID:** `CreatePartnerInput`

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{inputId}} | String | True |  |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 201 | CreatePartnerInputResultModel | 201 response |
| 400 | InvalidRequest | 400 response |
| 403 | AccessDenied | 403 response |
| 429 | LimitExceeded | 429 response |
| 500 | InternalServiceError | 500 response |
| 502 | BadGatewayException | 502 response |
| 504 | GatewayTimeoutException | 504 response |

## Schemas
<a name="inputs-inputid-partners-schemas"></a>

### Request bodies
<a name="inputs-inputid-partners-request-examples"></a>

#### POST schema
<a name="inputs-inputid-partners-request-body-post-example"></a>

```
{
  "requestId": "string",
  "tags": {
  }
}
```

### Response bodies
<a name="inputs-inputid-partners-response-examples"></a>

#### CreatePartnerInputResultModel schema
<a name="inputs-inputid-partners-response-body-createpartnerinputresultmodel-example"></a>

```
{
  "input": {
    "arn": "string",
    "attachedChannels": [
      "string"
    ],
    "destinations": [
      {
        "ip": "string",
        "port": "string",
        "url": "string",
        "vpc": {
          "availabilityZone": "string",
          "networkInterfaceId": "string"
        }
      }
    ],
    "id": "string",
    "inputClass": enum,
    "inputDevices": [
      {
        "id": "string"
      }
    ],
    "inputPartnerIds": [
      "string"
    ],
    "inputSourceType": enum,
    "mediaConnectFlows": [
      {
        "flowArn": "string"
      }
    ],
    "name": "string",
    "roleArn": "string",
    "securityGroups": [
      "string"
    ],
    "sources": [
      {
        "passwordParam": "string",
        "url": "string",
        "username": "string"
      }
    ],
    "state": enum,
    "tags": {
    },
    "type": enum
  }
}
```

#### InvalidRequest schema
<a name="inputs-inputid-partners-response-body-invalidrequest-example"></a>

```
{
  "message": "string"
}
```

#### AccessDenied schema
<a name="inputs-inputid-partners-response-body-accessdenied-example"></a>

```
{
  "message": "string"
}
```

#### LimitExceeded schema
<a name="inputs-inputid-partners-response-body-limitexceeded-example"></a>

```
{
  "message": "string"
}
```

#### InternalServiceError schema
<a name="inputs-inputid-partners-response-body-internalserviceerror-example"></a>

```
{
  "message": "string"
}
```

#### BadGatewayException schema
<a name="inputs-inputid-partners-response-body-badgatewayexception-example"></a>

```
{
  "message": "string"
}
```

#### GatewayTimeoutException schema
<a name="inputs-inputid-partners-response-body-gatewaytimeoutexception-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="inputs-inputid-partners-properties"></a>

### AccessDenied
<a name="inputs-inputid-partners-model-accessdenied"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### BadGatewayException
<a name="inputs-inputid-partners-model-badgatewayexception"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### CreatePartnerInput
<a name="inputs-inputid-partners-model-createpartnerinput"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| requestId | string | False | Unique identifier of the request to ensure the request is handled exactly once in case of retries.  |
| tags | [Tags](#inputs-inputid-partners-model-tags) | False | A collection of key-value pairs. |

### CreatePartnerInputResultModel
<a name="inputs-inputid-partners-model-createpartnerinputresultmodel"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| input | [Input](#inputs-inputid-partners-model-input) | False |  |

### GatewayTimeoutException
<a name="inputs-inputid-partners-model-gatewaytimeoutexception"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### Input
<a name="inputs-inputid-partners-model-input"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| arn | string | False | The Unique ARN of the input (generated, immutable). |
| attachedChannels | Array of type string | False | A list of channel IDs that that input is attached to (currently an input can only be attached to one channel). |
| destinations | Array of type [InputDestination](#inputs-inputid-partners-model-inputdestination) | False | A list of the destinations of the input (PUSH-type). |
| id | string | False | Read-only ID for the input. Unique in the AWS account. |
| inputClass | [InputClass](#inputs-inputid-partners-model-inputclass) | False | STANDARD - MediaLive expects two sources to be connected to this input. If the channel is also STANDARD, both sources will be ingested. If the channel is SINGLE\_PIPELINE, only the first source will be ingested; the second source will always be ignored, even if the first source fails. SINGLE\_PIPELINE - You can connect only one source to this input. If the ChannelClass is also SINGLE\_PIPELINE, this value is valid. If the ChannelClass is STANDARD, this value is not valid because the channel requires two sources in the input.  |
| inputDevices | Array of type [InputDeviceSettings](#inputs-inputid-partners-model-inputdevicesettings) | False | Settings for the input devices. |
| inputPartnerIds | Array of type string | False | A list of IDs for all Inputs which are partners of this one. |
| inputSourceType | [InputSourceType](#inputs-inputid-partners-model-inputsourcetype) | False | Certain pull input sources can be dynamic, meaning that they can have their URL's dynamically changes during input switch actions. Presently, this functionality only works with MP4\_FILE and TS\_FILE inputs.  |
| mediaConnectFlows | Array of type [MediaConnectFlow](#inputs-inputid-partners-model-mediaconnectflow) | False | A list of MediaConnect Flows for this input. |
| name | string | False | A modifiable ID for the input. |
| roleArn | string | False | The Amazon Resource Name (ARN) of the role this input assumes during and after creation. |
| securityGroups | Array of type string | False | A list of IDs for all the Input Security Groups attached to the input. |
| sources | Array of type [InputSource](#inputs-inputid-partners-model-inputsource) | False | A list of the sources of the input (PULL-type). |
| state | [InputState](#inputs-inputid-partners-model-inputstate) | False |  |
| tags | [Tags](#inputs-inputid-partners-model-tags) | False | A collection of key-value pairs. |
| type | [InputType](#inputs-inputid-partners-model-inputtype) | False |  |

### InputClass
<a name="inputs-inputid-partners-model-inputclass"></a>

A standard input has two sources and a single pipeline input only has one.
+ `STANDARD`
+ `SINGLE_PIPELINE`

### InputDestination
<a name="inputs-inputid-partners-model-inputdestination"></a>

The settings for a PUSH type input.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| ip | string | False | The system-generated static IP address of endpoint. It remains fixed for the lifetime of the input.  |
| port | string | False | The port number for the input. |
| url | string | False | This represents the endpoint that the customer stream will be pushed to.  |
| vpc | [InputDestinationVpc](#inputs-inputid-partners-model-inputdestinationvpc) | False |  |

### InputDestinationVpc
<a name="inputs-inputid-partners-model-inputdestinationvpc"></a>

The properties for a VPC type input destination.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| availabilityZone | string | False | The availability zone of the Input destination.  |
| networkInterfaceId | string | False | The network interface ID of the Input destination in the VPC.  |

### InputDeviceSettings
<a name="inputs-inputid-partners-model-inputdevicesettings"></a>

Settings for an input device.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| id | string | False | The unique ID for the device. |

### InputSource
<a name="inputs-inputid-partners-model-inputsource"></a>

The settings for a PULL type input.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| passwordParam | string | False | The key used to extract the password from EC2 Parameter store. |
| url | string | False | This represents the customer's source URL where stream is pulled from.  |
| username | string | False | The username for the input source. |

### InputSourceType
<a name="inputs-inputid-partners-model-inputsourcetype"></a>

There are two types of input sources, static and dynamic. If an input source is dynamic you can change the source url of the input dynamically using an input switch action. Currently, two input types support a dynamic url at this time, MP4\_FILE and TS\_FILE. By default all input sources are static.
+ `STATIC`
+ `DYNAMIC`

### InputState
<a name="inputs-inputid-partners-model-inputstate"></a>
+ `CREATING`
+ `DETACHED`
+ `ATTACHED`
+ `DELETING`
+ `DELETED`

### InputType
<a name="inputs-inputid-partners-model-inputtype"></a>

The different types of inputs that AWS Elemental MediaLive supports.
+ `UDP_PUSH`
+ `RTP_PUSH`
+ `RTMP_PUSH`
+ `RTMP_PULL`
+ `URL_PULL`
+ `MP4_FILE`
+ `MEDIACONNECT`
+ `MULTICAST`
+ `INPUT_DEVICE`
+ `AWS_CDI`
+ `TS_FILE`
+ `SRT_CALLER`
+ `SDI`

### InternalServiceError
<a name="inputs-inputid-partners-model-internalserviceerror"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### InvalidRequest
<a name="inputs-inputid-partners-model-invalidrequest"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### LimitExceeded
<a name="inputs-inputid-partners-model-limitexceeded"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### MediaConnectFlow
<a name="inputs-inputid-partners-model-mediaconnectflow"></a>

The settings for a MediaConnect Flow.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| flowArn | string | False | The unique ARN of the MediaConnect Flow being used as a source. |

### Tags
<a name="inputs-inputid-partners-model-tags"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| `*` | string | False |  |

## See also
<a name="inputs-inputid-partners-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### CreatePartnerInput
<a name="CreatePartnerInput-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/medialive-2017-10-14/CreatePartnerInput)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/medialive-2017-10-14/CreatePartnerInput)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/medialive-2017-10-14/CreatePartnerInput)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/medialive-2017-10-14/CreatePartnerInput)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/medialive-2017-10-14/CreatePartnerInput)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/medialive-2017-10-14/CreatePartnerInput)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/medialive-2017-10-14/CreatePartnerInput)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/medialive-2017-10-14/CreatePartnerInput)
+ [AWS SDK for Python (Boto3)](/goto/boto3/medialive-2017-10-14/CreatePartnerInput)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/medialive-2017-10-14/CreatePartnerInput)
