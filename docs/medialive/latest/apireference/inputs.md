---
source_url: https://docs.aws.amazon.com/medialive/latest/apireference/inputs.html
---

# Inputs
<a name="inputs"></a>

## URI
<a name="inputs-url"></a>

`/prod/inputs`

## HTTP methods
<a name="inputs-http-methods"></a>

### GET
<a name="inputsget"></a>

**Operation ID:** `ListInputs`

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| nextToken | String | False |  |
| maxResults | String | False |  |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | ListInputsResultModel | 200 response |
| 400 | InvalidRequest | 400 response |
| 403 | AccessDenied | 403 response |
| 429 | LimitExceeded | 429 response |
| 500 | InternalServiceError | 500 response |
| 502 | BadGatewayException | 502 response |
| 504 | GatewayTimeoutException | 504 response |

### POST
<a name="inputspost"></a>

**Operation ID:** `CreateInput`

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 201 | CreateInputResultModel | 201 response |
| 400 | InvalidRequest | 400 response |
| 403 | AccessDenied | 403 response |
| 429 | LimitExceeded | 429 response |
| 500 | InternalServiceError | 500 response |
| 502 | BadGatewayException | 502 response |
| 504 | GatewayTimeoutException | 504 response |

## Schemas
<a name="inputs-schemas"></a>

### Request bodies
<a name="inputs-request-examples"></a>

#### POST schema
<a name="inputs-request-body-post-example"></a>

```
{
  "destinations": [
    {
      "streamName": "string"
    }
  ],
  "inputDevices": [
    {
      "id": "string"
    }
  ],
  "inputSecurityGroups": [
    "string"
  ],
  "mediaConnectFlows": [
    {
      "flowArn": "string"
    }
  ],
  "name": "string",
  "requestId": "string",
  "roleArn": "string",
  "sources": [
    {
      "passwordParam": "string",
      "url": "string",
      "username": "string"
    }
  ],
  "tags": {
  },
  "type": enum,
  "vpc": {
    "securityGroupIds": [
      "string"
    ],
    "subnetIds": [
      "string"
    ]
  }
}
```

### Response bodies
<a name="inputs-response-examples"></a>

#### ListInputsResultModel schema
<a name="inputs-response-body-listinputsresultmodel-example"></a>

```
{
  "inputs": [
    {
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
  ],
  "nextToken": "string"
}
```

#### CreateInputResultModel schema
<a name="inputs-response-body-createinputresultmodel-example"></a>

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
<a name="inputs-response-body-invalidrequest-example"></a>

```
{
  "message": "string"
}
```

#### AccessDenied schema
<a name="inputs-response-body-accessdenied-example"></a>

```
{
  "message": "string"
}
```

#### LimitExceeded schema
<a name="inputs-response-body-limitexceeded-example"></a>

```
{
  "message": "string"
}
```

#### InternalServiceError schema
<a name="inputs-response-body-internalserviceerror-example"></a>

```
{
  "message": "string"
}
```

#### BadGatewayException schema
<a name="inputs-response-body-badgatewayexception-example"></a>

```
{
  "message": "string"
}
```

#### GatewayTimeoutException schema
<a name="inputs-response-body-gatewaytimeoutexception-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="inputs-properties"></a>

### AccessDenied
<a name="inputs-model-accessdenied"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### BadGatewayException
<a name="inputs-model-badgatewayexception"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### CreateInput
<a name="inputs-model-createinput"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| destinations | Array of type [InputDestinationRequest](#inputs-model-inputdestinationrequest) | False | Destination settings for PUSH type inputs. |
| inputDevices | Array of type [InputDeviceSettings](#inputs-model-inputdevicesettings) | False | Settings for the devices. |
| inputSecurityGroups | Array of type string | False | A list of security groups referenced by IDs to attach to the input. |
| mediaConnectFlows | Array of type [MediaConnectFlowRequest](#inputs-model-mediaconnectflowrequest) | False | A list of the MediaConnect Flows that you want to use in this input. You can specify as few as one Flow and presently, as many as two. The only requirement is when you have more than one is that each Flow is in a separate Availability Zone as this ensures your EML input is redundant to AZ issues.  |
| name | string | False | Name of the input. |
| requestId | string | False | Unique identifier of the request to ensure the request is handled exactly once in case of retries.  |
| roleArn | string | False | The Amazon Resource Name (ARN) of the role this input assumes during and after creation. |
| sources | Array of type [InputSourceRequest](#inputs-model-inputsourcerequest) | False | The source URLs for a PULL-type input. Every PULL type input needs exactly two source URLs for redundancy. Only specify sources for PULL type Inputs. Leave Destinations empty.  |
| tags | [Tags](#inputs-model-tags) | False | A collection of key-value pairs. |
| type | [InputType](#inputs-model-inputtype) | False |  |
| vpc | [InputVpcRequest](#inputs-model-inputvpcrequest) | False |  |

### CreateInputResultModel
<a name="inputs-model-createinputresultmodel"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| input | [Input](#inputs-model-input) | False |  |

### GatewayTimeoutException
<a name="inputs-model-gatewaytimeoutexception"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### Input
<a name="inputs-model-input"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| arn | string | False | The Unique ARN of the input (generated, immutable). |
| attachedChannels | Array of type string | False | A list of channel IDs that that input is attached to (currently an input can only be attached to one channel). |
| destinations | Array of type [InputDestination](#inputs-model-inputdestination) | False | A list of the destinations of the input (PUSH-type). |
| id | string | False | Read-only ID for the input. Unique in the AWS account. |
| inputClass | [InputClass](#inputs-model-inputclass) | False | STANDARD - MediaLive expects two sources to be connected to this input. If the channel is also STANDARD, both sources will be ingested. If the channel is SINGLE\_PIPELINE, only the first source will be ingested; the second source will always be ignored, even if the first source fails. SINGLE\_PIPELINE - You can connect only one source to this input. If the ChannelClass is also SINGLE\_PIPELINE, this value is valid. If the ChannelClass is STANDARD, this value is not valid because the channel requires two sources in the input.  |
| inputDevices | Array of type [InputDeviceSettings](#inputs-model-inputdevicesettings) | False | Settings for the input devices. |
| inputPartnerIds | Array of type string | False | A list of IDs for all Inputs which are partners of this one. |
| inputSourceType | [InputSourceType](#inputs-model-inputsourcetype) | False | Certain pull input sources can be dynamic, meaning that they can have their URL's dynamically changes during input switch actions. Presently, this functionality only works with MP4\_FILE and TS\_FILE inputs.  |
| mediaConnectFlows | Array of type [MediaConnectFlow](#inputs-model-mediaconnectflow) | False | A list of MediaConnect Flows for this input. |
| name | string | False | A modifiable ID for the input. |
| roleArn | string | False | The Amazon Resource Name (ARN) of the role this input assumes during and after creation. |
| securityGroups | Array of type string | False | A list of IDs for all the Input Security Groups attached to the input. |
| sources | Array of type [InputSource](#inputs-model-inputsource) | False | A list of the sources of the input (PULL-type). |
| state | [InputState](#inputs-model-inputstate) | False |  |
| tags | [Tags](#inputs-model-tags) | False | A collection of key-value pairs. |
| type | [InputType](#inputs-model-inputtype) | False |  |

### InputClass
<a name="inputs-model-inputclass"></a>

A standard input has two sources and a single pipeline input only has one.
+ `STANDARD`
+ `SINGLE_PIPELINE`

### InputDestination
<a name="inputs-model-inputdestination"></a>

The settings for a PUSH type input.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| ip | string | False | The system-generated static IP address of endpoint. It remains fixed for the lifetime of the input.  |
| port | string | False | The port number for the input. |
| url | string | False | This represents the endpoint that the customer stream will be pushed to.  |
| vpc | [InputDestinationVpc](#inputs-model-inputdestinationvpc) | False |  |

### InputDestinationRequest
<a name="inputs-model-inputdestinationrequest"></a>

Endpoint settings for a PUSH type input.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| streamName | string | False | A unique name for the location the RTMP stream is being pushed to.  |

### InputDestinationVpc
<a name="inputs-model-inputdestinationvpc"></a>

The properties for a VPC type input destination.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| availabilityZone | string | False | The availability zone of the Input destination.  |
| networkInterfaceId | string | False | The network interface ID of the Input destination in the VPC.  |

### InputDeviceSettings
<a name="inputs-model-inputdevicesettings"></a>

Settings for an input device.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| id | string | False | The unique ID for the device. |

### InputSource
<a name="inputs-model-inputsource"></a>

The settings for a PULL type input.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| passwordParam | string | False | The key used to extract the password from EC2 Parameter store. |
| url | string | False | This represents the customer's source URL where stream is pulled from.  |
| username | string | False | The username for the input source. |

### InputSourceRequest
<a name="inputs-model-inputsourcerequest"></a>

Settings for for a PULL type input.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| passwordParam | string | False | The key used to extract the password from EC2 Parameter store. |
| url | string | False | This represents the customer's source URL where stream is pulled from.  |
| username | string | False | The username for the input source. |

### InputSourceType
<a name="inputs-model-inputsourcetype"></a>

There are two types of input sources, static and dynamic. If an input source is dynamic you can change the source url of the input dynamically using an input switch action. Currently, two input types support a dynamic url at this time, MP4\_FILE and TS\_FILE. By default all input sources are static.
+ `STATIC`
+ `DYNAMIC`

### InputState
<a name="inputs-model-inputstate"></a>
+ `CREATING`
+ `DETACHED`
+ `ATTACHED`
+ `DELETING`
+ `DELETED`

### InputType
<a name="inputs-model-inputtype"></a>

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

### InputVpcRequest
<a name="inputs-model-inputvpcrequest"></a>

Settings for a private VPC Input. When this property is specified, the input destination addresses will be created in a VPC rather than with public Internet addresses. This property requires setting the roleArn property on Input creation. Not compatible with the inputSecurityGroups property.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| securityGroupIds | Array of type string | False | A list of up to 5 EC2 VPC security group IDs to attach to the Input VPC network interfaces. Requires subnetIds. If none are specified then the VPC default security group will be used.  |
| subnetIds | Array of type string | True | A list of 2 VPC subnet IDs from the same VPC. Subnet IDs must be mapped to two unique availability zones (AZ).  |

### InternalServiceError
<a name="inputs-model-internalserviceerror"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### InvalidRequest
<a name="inputs-model-invalidrequest"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### LimitExceeded
<a name="inputs-model-limitexceeded"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### ListInputsResultModel
<a name="inputs-model-listinputsresultmodel"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| inputs | Array of type [Input](#inputs-model-input) | False |  |
| nextToken | string | False |  |

### MediaConnectFlow
<a name="inputs-model-mediaconnectflow"></a>

The settings for a MediaConnect Flow.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| flowArn | string | False | The unique ARN of the MediaConnect Flow being used as a source. |

### MediaConnectFlowRequest
<a name="inputs-model-mediaconnectflowrequest"></a>

The settings for a MediaConnect Flow.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| flowArn | string | False | The ARN of the MediaConnect Flow that you want to use as a source. |

### Tags
<a name="inputs-model-tags"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| `*` | string | False |  |

## See also
<a name="inputs-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### ListInputs
<a name="ListInputs-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/medialive-2017-10-14/ListInputs)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/medialive-2017-10-14/ListInputs)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/medialive-2017-10-14/ListInputs)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/medialive-2017-10-14/ListInputs)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/medialive-2017-10-14/ListInputs)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/medialive-2017-10-14/ListInputs)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/medialive-2017-10-14/ListInputs)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/medialive-2017-10-14/ListInputs)
+ [AWS SDK for Python](/goto/boto3/medialive-2017-10-14/ListInputs)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/medialive-2017-10-14/ListInputs)

### CreateInput
<a name="CreateInput-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/medialive-2017-10-14/CreateInput)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/medialive-2017-10-14/CreateInput)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/medialive-2017-10-14/CreateInput)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/medialive-2017-10-14/CreateInput)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/medialive-2017-10-14/CreateInput)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/medialive-2017-10-14/CreateInput)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/medialive-2017-10-14/CreateInput)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/medialive-2017-10-14/CreateInput)
+ [AWS SDK for Python](/goto/boto3/medialive-2017-10-14/CreateInput)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/medialive-2017-10-14/CreateInput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
