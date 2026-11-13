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
  "inputNetworkLocation": enum,
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
  "requestId": "string",
  "roleArn": "string",
  "routerSettings": {
    "destinations": [
      {
        "availabilityZoneName": "string"
      }
    ],
    "encryptionType": enum,
    "secretArn": "string"
  },
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
  },
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

### Algorithm
<a name="inputs-model-algorithm"></a>
+ `AES128`
+ `AES192`
+ `AES256`

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
| inputNetworkLocation | [InputNetworkLocation](#inputs-model-inputnetworklocation) | False | The location of this input. `AWS`, for an input existing in the AWS Cloud, On-Prem for an input in a customer network. |
| inputSecurityGroups | Array of type string | False | A list of security groups referenced by IDs to attach to the input. |
| mediaConnectFlows | Array of type [MediaConnectFlowRequest](#inputs-model-mediaconnectflowrequest) | False | A list of the MediaConnect Flows that you want to use in this input. You can specify as few as one Flow and presently, as many as two. The only requirement is when you have more than one is that each Flow is in a separate Availability Zone as this ensures your EML input is redundant to AZ issues.  |
| multicastSettings | [MulticastSettingsCreateRequest](#inputs-model-multicastsettingscreaterequest) | False | Multicast Input settings. |
| name | string | False | Name of the input. |
| requestId | string | False | Unique identifier of the request to ensure the request is handled exactly once in case of retries.  |
| roleArn | string | False | The Amazon Resource Name (ARN) of the role this input assumes during and after creation. |
| routerSettings | [RouterSettings](#inputs-model-routersettings) | False |  |
| sdiSources | Array of type string | False |  |
| smpte2110ReceiverGroupSettings | [Smpte2110ReceiverGroupSettings](#inputs-model-smpte2110receivergroupsettings) | False | Include this parameter if the input is a SMPTE 2110 input, to identify the stream sources for this input. |
| sources | Array of type [InputSourceRequest](#inputs-model-inputsourcerequest) | False | The source URLs for a PULL-type input. Every PULL type input needs exactly two source URLs for redundancy. Only specify sources for PULL type Inputs. Leave Destinations empty.  |
| srtSettings | [SrtSettingsRequest](#inputs-model-srtsettingsrequest) | False | The settings associated with an SRT input. |
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
| network | string | False | If the push input has an input location of ON-PREM, ID the ID of the attached network. |
| networkRoutes | Array of type [InputRequestDestinationRoute](#inputs-model-inputrequestdestinationroute) | False | If the push input has an input location of ON-PREM it's a requirement to specify what the route of the input is going to be on the customer local network. |
| staticIpAddress | string | False | If the push input has an input location of ON-PREM it's optional to specify what the ip address of the input is going to be on the customer local network. |
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

### InputNetworkLocation
<a name="inputs-model-inputnetworklocation"></a>

With the introduction of MediaLive Anywhere, a MediaLive input can now exist in two different places: AWS or inside an on-premises datacenter. By default all inputs will continue to be AWS inputs.
+ `AWS`
+ `ON_PREMISES`

### InputRequestDestinationRoute
<a name="inputs-model-inputrequestdestinationroute"></a>

A network route configuration.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| cidr | string | False | The CIDR of the route. |
| gateway | string | False | An optional gateway for the route. |

### InputSdpLocation
<a name="inputs-model-inputsdplocation"></a>

The location of the SDP file for one of the SMPTE 2110 streams in a receiver group.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| mediaIndex | integer | False | The index of the media stream in the SDP file for one SMPTE 2110 stream. |
| sdpUrl | string | False | The URL of the SDP file for one SMPTE 2110 stream. |

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
+ `SMPTE_2110_RECEIVER_GROUP`
+ `SDI`
+ `MEDIACONNECT_ROUTER`
+ `SRT_LISTENER`

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

### MulticastSettingsCreateRequest
<a name="inputs-model-multicastsettingscreaterequest"></a>

Settings for a Multicast input. Contains a list of multicast Urls and optional source ip addresses.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| sources | Array of type [MulticastSourceCreateRequest](#inputs-model-multicastsourcecreaterequest) | False |  |

### MulticastSourceCreateRequest
<a name="inputs-model-multicastsourcecreaterequest"></a>

Pair of multicast url and source ip address (optional) that make up a multicast source.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| sourceIp | string | False | This represents the ip address of the device sending the multicast stream. |
| url | string | True | This represents the customer's source URL where multicast stream is pulled from. |

### RouterDestinationSettings
<a name="inputs-model-routerdestinationsettings"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| availabilityZoneName | string | True | Availability Zone for this MediaConnect Router destination. |

### RouterEncryptionType
<a name="inputs-model-routerencryptiontype"></a>

The encryption configuration for a MediaConnect Router input. For the valid values, see the `encryptionType` field in `RouterSettings`.
+ `AUTOMATIC`
+ `SECRETS_MANAGER`

### RouterSettings
<a name="inputs-model-routersettings"></a>

This is the collection of settings that are used during the creation of a MediaConnect router input.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| destinations | Array of type [RouterDestinationSettings](#inputs-model-routerdestinationsettings) | False | Destinations for the input from MediaConnect Router. Provide one for a single-pipeline input and two for a standard input. |
| encryptionType | [RouterEncryptionType](#inputs-model-routerencryptiontype) | False | The encryption configuration for this MediaConnect Router input. Valid values:+ `AUTOMATIC` – MediaLive uses a service-managed secret to encrypt the data in transit.<br />+ `SECRETS_MANAGER` – MediaLive uses the secret that you identify in `secretArn` to encrypt the data in transit. Provide `secretArn` when you choose this value. |
| secretArn | string | False | ARN of the secret used to encrypt this input. |

### Smpte2110ReceiverGroup
<a name="inputs-model-smpte2110receivergroup"></a>

A receiver group is a collection of video, audio, and ancillary streams that you want to group together and attach to one input.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| sdpSettings | [Smpte2110ReceiverGroupSdpSettings](#inputs-model-smpte2110receivergroupsdpsettings) | False | The single Smpte2110ReceiverGroupSdpSettings that identify the video, audio, and ancillary streams for this receiver group. |

### Smpte2110ReceiverGroupSdpSettings
<a name="inputs-model-smpte2110receivergroupsdpsettings"></a>

Information about the SDP files that describe the SMPTE 2110 streams that go into one SMPTE 2110 receiver group.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| ancillarySdps | Array of type [InputSdpLocation](#inputs-model-inputsdplocation) | False | A list of InputSdpLocations. Each item in the list specifies the SDP file and index for one ancillary SMPTE 2110 stream. Each stream encapsulates one captions stream (out of any number you can include) or the single SCTE 35 stream that you can include. |
| audioSdps | Array of type [InputSdpLocation](#inputs-model-inputsdplocation) | False | A list of InputSdpLocations. Each item in the list specifies the SDP file and index for one audio SMPTE 2110 stream. |
| videoSdp | [InputSdpLocation](#inputs-model-inputsdplocation) | False | The InputSdpLocation that specifies the SDP file and index for the single video SMPTE 2110 stream for this 2110 input. |

### Smpte2110ReceiverGroupSettings
<a name="inputs-model-smpte2110receivergroupsettings"></a>

Configures the sources for the SMPTE 2110 Receiver Group input.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| smpte2110ReceiverGroups | Array of type [Smpte2110ReceiverGroup](#inputs-model-smpte2110receivergroup) | False |  |

### SrtCallerDecryptionRequest
<a name="inputs-model-srtcallerdecryptionrequest"></a>

Complete these parameters only if the content is encrypted.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| algorithm | [Algorithm](#inputs-model-algorithm) | False | The algorithm used to encrypt content. |
| passphraseSecretArn | string | False | The ARN for the secret in Secrets Manager. Someone in your organization must create a secret and provide you with its ARN. This secret holds the passphrase that MediaLive will use to decrypt the source content. |

### SrtCallerSourceRequest
<a name="inputs-model-srtcallersourcerequest"></a>

Configures the connection for a source that uses SRT as the connection protocol. In terms of establishing the connection, MediaLive is always the caller and the upstream system is always the listener. In terms of transmission of the source content, MediaLive is always the receiver and the upstream system is always the sender.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| decryption | [SrtCallerDecryptionRequest](#inputs-model-srtcallerdecryptionrequest) | False |  |
| minimumLatency | integer | False | The preferred latency (in milliseconds) for implementing packet loss and recovery. Packet recovery is a key feature of SRT. Obtain this value from the operator at the upstream system. |
| srtListenerAddress | string | False | The IP address at the upstream system (the listener) that MediaLive (the caller) will connect to. |
| srtListenerPort | string | False | The port at the upstream system (the listener) that MediaLive (the caller) will connect to. |
| streamId | string | False | This value is required if the upstream system uses this identifier because without it, the SRT handshake between MediaLive (the caller) and the upstream system (the listener) might fail. |

### SrtListenerDecryptionRequest
<a name="inputs-model-srtlistenerdecryptionrequest"></a>

Decryption settings. If specified, both algorithm and passphraseSecretArn are required.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| algorithm | [Algorithm](#inputs-model-algorithm) | True | Required. The decryption algorithm. |
| passphraseSecretArn | string | True | Required. The ARN for the secret in Secrets Manager that holds the passphrase. |

### SrtListenerSettingsRequest
<a name="inputs-model-srtlistenersettingsrequest"></a>

Configuration for SRT Listener input. Encryption is REQUIRED for all SRT Listener inputs for security reasons. You must provide decryption settings including algorithm and passphrase secret ARN.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| decryption | [SrtListenerDecryptionRequest](#inputs-model-srtlistenerdecryptionrequest) | True |  |
| minimumLatency | integer | True | Required. The preferred latency in milliseconds for packet loss and recovery. Range 120-15000. |
| streamId | string | False | Optional. The stream ID if the upstream system uses this identifier. |

### SrtSettingsRequest
<a name="inputs-model-srtsettingsrequest"></a>

Configures the settings for SRT inputs. Provide either srtCallerSources (for SRT\_CALLER type) OR srtListenerSettings (for SRT\_LISTENER type), not both.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| srtCallerSources | Array of type [SrtCallerSourceRequest](#inputs-model-srtcallersourcerequest) | False |  |
| srtListenerSettings | [SrtListenerSettingsRequest](#inputs-model-srtlistenersettingsrequest) | False |  |

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
+ [AWS SDK for Python (Boto3)](/goto/boto3/medialive-2017-10-14/ListInputs)
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
+ [AWS SDK for Python (Boto3)](/goto/boto3/medialive-2017-10-14/CreateInput)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/medialive-2017-10-14/CreateInput)
