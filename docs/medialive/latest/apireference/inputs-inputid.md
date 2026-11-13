---
source_url: https://docs.aws.amazon.com/medialive/latest/apireference/inputs-inputid.html
---

# Inputs: input ID
<a name="inputs-inputid"></a>

## URI
<a name="inputs-inputid-url"></a>

`/prod/inputs/{{inputId}}`

## HTTP methods
<a name="inputs-inputid-http-methods"></a>

### DELETE
<a name="inputs-inputiddelete"></a>

**Operation ID:** `DeleteInput`

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{inputId}} | String | True |  |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | Empty | 200 response |
| 400 | InvalidRequest | 400 response |
| 403 | AccessDenied | 403 response |
| 404 | ResourceNotFound | 404 response |
| 409 | ResourceConflict | 409 response |
| 429 | LimitExceeded | 429 response |
| 500 | InternalServiceError | 500 response |
| 502 | BadGatewayException | 502 response |
| 504 | GatewayTimeoutException | 504 response |

### GET
<a name="inputs-inputidget"></a>

**Operation ID:** `DescribeInput`

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{inputId}} | String | True |  |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | Input | 200 response |
| 400 | InvalidRequest | 400 response |
| 403 | AccessDenied | 403 response |
| 404 | ResourceNotFound | 404 response |
| 429 | LimitExceeded | 429 response |
| 500 | InternalServiceError | 500 response |
| 502 | BadGatewayException | 502 response |
| 504 | GatewayTimeoutException | 504 response |

### PUT
<a name="inputs-inputidput"></a>

**Operation ID:** `UpdateInput`

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{inputId}} | String | True |  |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | UpdateInputResultModel | 200 response |
| 400 | InvalidRequest | 400 response |
| 403 | AccessDenied | 403 response |
| 404 | ResourceNotFound | 404 response |
| 409 | ResourceConflict | 409 response |
| 500 | InternalServiceError | 500 response |
| 502 | BadGatewayException | 502 response |
| 504 | GatewayTimeoutException | 504 response |

## Schemas
<a name="inputs-inputid-schemas"></a>

### Request bodies
<a name="inputs-inputid-request-examples"></a>

#### PUT schema
<a name="inputs-inputid-request-body-put-example"></a>

```
{
  "destinations": [
    {
      "network": "string",
      "networkRoutes": [
        {
          "cidr": "string",
          "gateway": "string"
        }
      ],
      "staticIpAddress": "string",
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
  "multicastSettings": {
    "sources": [
      {
        "sourceIp": "string",
        "url": "string"
      }
    ]
  },
  "name": "string",
  "roleArn": "string",
  "sdiSources": [
    "string"
  ],
  "smpte2110ReceiverGroupSettings": {
    "smpte2110ReceiverGroups": [
      {
        "sdpSettings": {
          "ancillarySdps": [
            {
              "mediaIndex": integer,
              "sdpUrl": "string"
            }
          ],
          "audioSdps": [
            {
              "mediaIndex": integer,
              "sdpUrl": "string"
            }
          ],
          "videoSdp": {
            "mediaIndex": integer,
            "sdpUrl": "string"
          }
        }
      }
    ]
  },
  "sources": [
    {
      "passwordParam": "string",
      "url": "string",
      "username": "string"
    }
  ],
  "srtSettings": {
    "srtCallerSources": [
      {
        "decryption": {
          "algorithm": enum,
          "passphraseSecretArn": "string"
        },
        "minimumLatency": integer,
        "srtListenerAddress": "string",
        "srtListenerPort": "string",
        "streamId": "string"
      }
    ],
    "srtListenerSettings": {
      "decryption": {
        "algorithm": enum,
        "passphraseSecretArn": "string"
      },
      "minimumLatency": integer,
      "streamId": "string"
    }
  }
}
```

### Response bodies
<a name="inputs-inputid-response-examples"></a>

#### Empty schema
<a name="inputs-inputid-response-body-empty-example"></a>

```
{
}
```

#### Input schema
<a name="inputs-inputid-response-body-input-example"></a>

```
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
```

#### UpdateInputResultModel schema
<a name="inputs-inputid-response-body-updateinputresultmodel-example"></a>

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
<a name="inputs-inputid-response-body-invalidrequest-example"></a>

```
{
  "message": "string"
}
```

#### AccessDenied schema
<a name="inputs-inputid-response-body-accessdenied-example"></a>

```
{
  "message": "string"
}
```

#### ResourceNotFound schema
<a name="inputs-inputid-response-body-resourcenotfound-example"></a>

```
{
  "message": "string"
}
```

#### ResourceConflict schema
<a name="inputs-inputid-response-body-resourceconflict-example"></a>

```
{
  "message": "string"
}
```

#### LimitExceeded schema
<a name="inputs-inputid-response-body-limitexceeded-example"></a>

```
{
  "message": "string"
}
```

#### InternalServiceError schema
<a name="inputs-inputid-response-body-internalserviceerror-example"></a>

```
{
  "message": "string"
}
```

#### BadGatewayException schema
<a name="inputs-inputid-response-body-badgatewayexception-example"></a>

```
{
  "message": "string"
}
```

#### GatewayTimeoutException schema
<a name="inputs-inputid-response-body-gatewaytimeoutexception-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="inputs-inputid-properties"></a>

### AccessDenied
<a name="inputs-inputid-model-accessdenied"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### Algorithm
<a name="inputs-inputid-model-algorithm"></a>
+ `AES128`
+ `AES192`
+ `AES256`

### BadGatewayException
<a name="inputs-inputid-model-badgatewayexception"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### Empty
<a name="inputs-inputid-model-empty"></a>

### GatewayTimeoutException
<a name="inputs-inputid-model-gatewaytimeoutexception"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### Input
<a name="inputs-inputid-model-input"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| arn | string | False | The Unique ARN of the input (generated, immutable). |
| attachedChannels | Array of type string | False | A list of channel IDs that that input is attached to (currently an input can only be attached to one channel). |
| destinations | Array of type [InputDestination](#inputs-inputid-model-inputdestination) | False | A list of the destinations of the input (PUSH-type). |
| id | string | False | Read-only ID for the input. Unique in the AWS account. |
| inputClass | [InputClass](#inputs-inputid-model-inputclass) | False | STANDARD - MediaLive expects two sources to be connected to this input. If the channel is also STANDARD, both sources will be ingested. If the channel is SINGLE\_PIPELINE, only the first source will be ingested; the second source will always be ignored, even if the first source fails. SINGLE\_PIPELINE - You can connect only one source to this input. If the ChannelClass is also SINGLE\_PIPELINE, this value is valid. If the ChannelClass is STANDARD, this value is not valid because the channel requires two sources in the input.  |
| inputDevices | Array of type [InputDeviceSettings](#inputs-inputid-model-inputdevicesettings) | False | Settings for the input devices. |
| inputPartnerIds | Array of type string | False | A list of IDs for all Inputs which are partners of this one. |
| inputSourceType | [InputSourceType](#inputs-inputid-model-inputsourcetype) | False | Certain pull input sources can be dynamic, meaning that they can have their URL's dynamically changes during input switch actions. Presently, this functionality only works with MP4\_FILE and TS\_FILE inputs.  |
| mediaConnectFlows | Array of type [MediaConnectFlow](#inputs-inputid-model-mediaconnectflow) | False | A list of MediaConnect Flows for this input. |
| name | string | False | A modifiable ID for the input. |
| roleArn | string | False | The Amazon Resource Name (ARN) of the role this input assumes during and after creation. |
| securityGroups | Array of type string | False | A list of IDs for all the Input Security Groups attached to the input. |
| sources | Array of type [InputSource](#inputs-inputid-model-inputsource) | False | A list of the sources of the input (PULL-type). |
| state | [InputState](#inputs-inputid-model-inputstate) | False |  |
| tags | [Tags](#inputs-inputid-model-tags) | False | A collection of key-value pairs. |
| type | [InputType](#inputs-inputid-model-inputtype) | False |  |

### InputClass
<a name="inputs-inputid-model-inputclass"></a>

A standard input has two sources and a single pipeline input only has one.
+ `STANDARD`
+ `SINGLE_PIPELINE`

### InputDestination
<a name="inputs-inputid-model-inputdestination"></a>

The settings for a PUSH type input.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| ip | string | False | The system-generated static IP address of endpoint. It remains fixed for the lifetime of the input.  |
| port | string | False | The port number for the input. |
| url | string | False | This represents the endpoint that the customer stream will be pushed to.  |
| vpc | [InputDestinationVpc](#inputs-inputid-model-inputdestinationvpc) | False |  |

### InputDestinationRequest
<a name="inputs-inputid-model-inputdestinationrequest"></a>

Endpoint settings for a PUSH type input.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| network | string | False | If the push input has an input location of ON-PREM, ID the ID of the attached network. |
| networkRoutes | Array of type [InputRequestDestinationRoute](#inputs-inputid-model-inputrequestdestinationroute) | False | If the push input has an input location of ON-PREM it's a requirement to specify what the route of the input is going to be on the customer local network. |
| staticIpAddress | string | False | If the push input has an input location of ON-PREM it's optional to specify what the ip address of the input is going to be on the customer local network. |
| streamName | string | False | A unique name for the location the RTMP stream is being pushed to.  |

### InputDestinationVpc
<a name="inputs-inputid-model-inputdestinationvpc"></a>

The properties for a VPC type input destination.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| availabilityZone | string | False | The availability zone of the Input destination.  |
| networkInterfaceId | string | False | The network interface ID of the Input destination in the VPC.  |

### InputDeviceRequest
<a name="inputs-inputid-model-inputdevicerequest"></a>

Settings for an input device.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| id | string | False | The unique ID for the device. |

### InputDeviceSettings
<a name="inputs-inputid-model-inputdevicesettings"></a>

Settings for an input device.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| id | string | False | The unique ID for the device. |

### InputRequestDestinationRoute
<a name="inputs-inputid-model-inputrequestdestinationroute"></a>

A network route configuration.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| cidr | string | False | The CIDR of the route. |
| gateway | string | False | An optional gateway for the route. |

### InputSdpLocation
<a name="inputs-inputid-model-inputsdplocation"></a>

The location of the SDP file for one of the SMPTE 2110 streams in a receiver group.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| mediaIndex | integer | False | The index of the media stream in the SDP file for one SMPTE 2110 stream. |
| sdpUrl | string | False | The URL of the SDP file for one SMPTE 2110 stream. |

### InputSource
<a name="inputs-inputid-model-inputsource"></a>

The settings for a PULL type input.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| passwordParam | string | False | The key used to extract the password from EC2 Parameter store. |
| url | string | False | This represents the customer's source URL where stream is pulled from.  |
| username | string | False | The username for the input source. |

### InputSourceRequest
<a name="inputs-inputid-model-inputsourcerequest"></a>

Settings for for a PULL type input.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| passwordParam | string | False | The key used to extract the password from EC2 Parameter store. |
| url | string | False | This represents the customer's source URL where stream is pulled from.  |
| username | string | False | The username for the input source. |

### InputSourceType
<a name="inputs-inputid-model-inputsourcetype"></a>

There are two types of input sources, static and dynamic. If an input source is dynamic you can change the source url of the input dynamically using an input switch action. Currently, two input types support a dynamic url at this time, MP4\_FILE and TS\_FILE. By default all input sources are static.
+ `STATIC`
+ `DYNAMIC`

### InputState
<a name="inputs-inputid-model-inputstate"></a>
+ `CREATING`
+ `DETACHED`
+ `ATTACHED`
+ `DELETING`
+ `DELETED`

### InputType
<a name="inputs-inputid-model-inputtype"></a>

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
+ `SMPTE_2110_RECEIVER_GROUP`
+ `SDI`
+ `MEDIACONNECT_ROUTER`
+ `SRT_LISTENER`

### InternalServiceError
<a name="inputs-inputid-model-internalserviceerror"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### InvalidRequest
<a name="inputs-inputid-model-invalidrequest"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### LimitExceeded
<a name="inputs-inputid-model-limitexceeded"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### MediaConnectFlow
<a name="inputs-inputid-model-mediaconnectflow"></a>

The settings for a MediaConnect Flow.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| flowArn | string | False | The unique ARN of the MediaConnect Flow being used as a source. |

### MediaConnectFlowRequest
<a name="inputs-inputid-model-mediaconnectflowrequest"></a>

The settings for a MediaConnect Flow.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| flowArn | string | False | The ARN of the MediaConnect Flow that you want to use as a source. |

### MulticastSettingsUpdateRequest
<a name="inputs-inputid-model-multicastsettingsupdaterequest"></a>

Settings for a Multicast input. Contains a list of multicast Urls and optional source ip addresses.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| sources | Array of type [MulticastSourceUpdateRequest](#inputs-inputid-model-multicastsourceupdaterequest) | False |  |

### MulticastSourceUpdateRequest
<a name="inputs-inputid-model-multicastsourceupdaterequest"></a>

Pair of multicast url and source ip address (optional) that make up a multicast source.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| sourceIp | string | False | This represents the ip address of the device sending the multicast stream. |
| url | string | True | This represents the customer's source URL where multicast stream is pulled from. |

### ResourceConflict
<a name="inputs-inputid-model-resourceconflict"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### ResourceNotFound
<a name="inputs-inputid-model-resourcenotfound"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### Smpte2110ReceiverGroup
<a name="inputs-inputid-model-smpte2110receivergroup"></a>

A receiver group is a collection of video, audio, and ancillary streams that you want to group together and attach to one input.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| sdpSettings | [Smpte2110ReceiverGroupSdpSettings](#inputs-inputid-model-smpte2110receivergroupsdpsettings) | False | The single Smpte2110ReceiverGroupSdpSettings that identify the video, audio, and ancillary streams for this receiver group. |

### Smpte2110ReceiverGroupSdpSettings
<a name="inputs-inputid-model-smpte2110receivergroupsdpsettings"></a>

Information about the SDP files that describe the SMPTE 2110 streams that go into one SMPTE 2110 receiver group.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| ancillarySdps | Array of type [InputSdpLocation](#inputs-inputid-model-inputsdplocation) | False | A list of InputSdpLocations. Each item in the list specifies the SDP file and index for one ancillary SMPTE 2110 stream. Each stream encapsulates one captions stream (out of any number you can include) or the single SCTE 35 stream that you can include. |
| audioSdps | Array of type [InputSdpLocation](#inputs-inputid-model-inputsdplocation) | False | A list of InputSdpLocations. Each item in the list specifies the SDP file and index for one audio SMPTE 2110 stream. |
| videoSdp | [InputSdpLocation](#inputs-inputid-model-inputsdplocation) | False | The InputSdpLocation that specifies the SDP file and index for the single video SMPTE 2110 stream for this 2110 input. |

### Smpte2110ReceiverGroupSettings
<a name="inputs-inputid-model-smpte2110receivergroupsettings"></a>

Configures the sources for the SMPTE 2110 Receiver Group input.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| smpte2110ReceiverGroups | Array of type [Smpte2110ReceiverGroup](#inputs-inputid-model-smpte2110receivergroup) | False |  |

### SrtCallerDecryptionRequest
<a name="inputs-inputid-model-srtcallerdecryptionrequest"></a>

Complete these parameters only if the content is encrypted.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| algorithm | [Algorithm](#inputs-inputid-model-algorithm) | False | The algorithm used to encrypt content. |
| passphraseSecretArn | string | False | The ARN for the secret in Secrets Manager. Someone in your organization must create a secret and provide you with its ARN. This secret holds the passphrase that MediaLive will use to decrypt the source content. |

### SrtCallerSourceRequest
<a name="inputs-inputid-model-srtcallersourcerequest"></a>

Configures the connection for a source that uses SRT as the connection protocol. In terms of establishing the connection, MediaLive is always the caller and the upstream system is always the listener. In terms of transmission of the source content, MediaLive is always the receiver and the upstream system is always the sender.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| decryption | [SrtCallerDecryptionRequest](#inputs-inputid-model-srtcallerdecryptionrequest) | False |  |
| minimumLatency | integer | False | The preferred latency (in milliseconds) for implementing packet loss and recovery. Packet recovery is a key feature of SRT. Obtain this value from the operator at the upstream system. |
| srtListenerAddress | string | False | The IP address at the upstream system (the listener) that MediaLive (the caller) will connect to. |
| srtListenerPort | string | False | The port at the upstream system (the listener) that MediaLive (the caller) will connect to. |
| streamId | string | False | This value is required if the upstream system uses this identifier because without it, the SRT handshake between MediaLive (the caller) and the upstream system (the listener) might fail. |

### SrtListenerDecryptionRequest
<a name="inputs-inputid-model-srtlistenerdecryptionrequest"></a>

Decryption settings. If specified, both algorithm and passphraseSecretArn are required.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| algorithm | [Algorithm](#inputs-inputid-model-algorithm) | True | Required. The decryption algorithm. |
| passphraseSecretArn | string | True | Required. The ARN for the secret in Secrets Manager that holds the passphrase. |

### SrtListenerSettingsRequest
<a name="inputs-inputid-model-srtlistenersettingsrequest"></a>

Configuration for SRT Listener input. Encryption is REQUIRED for all SRT Listener inputs for security reasons. You must provide decryption settings including algorithm and passphrase secret ARN.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| decryption | [SrtListenerDecryptionRequest](#inputs-inputid-model-srtlistenerdecryptionrequest) | True |  |
| minimumLatency | integer | True | Required. The preferred latency in milliseconds for packet loss and recovery. Range 120-15000. |
| streamId | string | False | Optional. The stream ID if the upstream system uses this identifier. |

### SrtSettingsRequest
<a name="inputs-inputid-model-srtsettingsrequest"></a>

Configures the settings for SRT inputs. Provide either srtCallerSources (for SRT\_CALLER type) OR srtListenerSettings (for SRT\_LISTENER type), not both.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| srtCallerSources | Array of type [SrtCallerSourceRequest](#inputs-inputid-model-srtcallersourcerequest) | False |  |
| srtListenerSettings | [SrtListenerSettingsRequest](#inputs-inputid-model-srtlistenersettingsrequest) | False |  |

### Tags
<a name="inputs-inputid-model-tags"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| `*` | string | False |  |

### UpdateInput
<a name="inputs-inputid-model-updateinput"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| destinations | Array of type [InputDestinationRequest](#inputs-inputid-model-inputdestinationrequest) | False | Destination settings for PUSH type inputs. |
| inputDevices | Array of type [InputDeviceRequest](#inputs-inputid-model-inputdevicerequest) | False | Settings for the devices. |
| inputSecurityGroups | Array of type string | False | A list of security groups referenced by IDs to attach to the input. |
| mediaConnectFlows | Array of type [MediaConnectFlowRequest](#inputs-inputid-model-mediaconnectflowrequest) | False | A list of the MediaConnect Flow ARNs that you want to use as the source of the input. You can specify as few as one Flow and presently, as many as two. The only requirement is when you have more than one is that each Flow is in a separate Availability Zone as this ensures your EML input is redundant to AZ issues.  |
| multicastSettings | [MulticastSettingsUpdateRequest](#inputs-inputid-model-multicastsettingsupdaterequest) | False | Multicast Input settings. |
| name | string | False | Name of the input. |
| roleArn | string | False | The Amazon Resource Name (ARN) of the role this input assumes during and after creation. |
| sdiSources | Array of type string | False |  |
| smpte2110ReceiverGroupSettings | [Smpte2110ReceiverGroupSettings](#inputs-inputid-model-smpte2110receivergroupsettings) | False | Include this parameter if the input is a SMPTE 2110 input, to identify the stream sources for this input. |
| sources | Array of type [InputSourceRequest](#inputs-inputid-model-inputsourcerequest) | False | The source URLs for a PULL-type input. Every PULL type input needs exactly two source URLs for redundancy. Only specify sources for PULL type Inputs. Leave Destinations empty.  |
| srtSettings | [SrtSettingsRequest](#inputs-inputid-model-srtsettingsrequest) | False | The settings associated with an SRT input. |

### UpdateInputResultModel
<a name="inputs-inputid-model-updateinputresultmodel"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| input | [Input](#inputs-inputid-model-input) | False |  |

## See also
<a name="inputs-inputid-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### DeleteInput
<a name="DeleteInput-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/medialive-2017-10-14/DeleteInput)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/medialive-2017-10-14/DeleteInput)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/medialive-2017-10-14/DeleteInput)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/medialive-2017-10-14/DeleteInput)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/medialive-2017-10-14/DeleteInput)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/medialive-2017-10-14/DeleteInput)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/medialive-2017-10-14/DeleteInput)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/medialive-2017-10-14/DeleteInput)
+ [AWS SDK for Python (Boto3)](/goto/boto3/medialive-2017-10-14/DeleteInput)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/medialive-2017-10-14/DeleteInput)

### DescribeInput
<a name="DescribeInput-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/medialive-2017-10-14/DescribeInput)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/medialive-2017-10-14/DescribeInput)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/medialive-2017-10-14/DescribeInput)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/medialive-2017-10-14/DescribeInput)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/medialive-2017-10-14/DescribeInput)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/medialive-2017-10-14/DescribeInput)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/medialive-2017-10-14/DescribeInput)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/medialive-2017-10-14/DescribeInput)
+ [AWS SDK for Python (Boto3)](/goto/boto3/medialive-2017-10-14/DescribeInput)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/medialive-2017-10-14/DescribeInput)

### UpdateInput
<a name="UpdateInput-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/medialive-2017-10-14/UpdateInput)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/medialive-2017-10-14/UpdateInput)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/medialive-2017-10-14/UpdateInput)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/medialive-2017-10-14/UpdateInput)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/medialive-2017-10-14/UpdateInput)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/medialive-2017-10-14/UpdateInput)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/medialive-2017-10-14/UpdateInput)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/medialive-2017-10-14/UpdateInput)
+ [AWS SDK for Python (Boto3)](/goto/boto3/medialive-2017-10-14/UpdateInput)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/medialive-2017-10-14/UpdateInput)
