---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_CreateFlow.html
---

# CreateFlow
<a name="API_CreateFlow"></a>

 Creates a new flow. The request must include one source. The request optionally can include outputs (up to 50) and entitlements (up to 50).

## Request Syntax
<a name="API_CreateFlow_RequestSyntax"></a>

```
POST /v1/flows HTTP/1.1
Content-type: application/json

{
   "availabilityZone": "{{string}}",
   "encodingConfig": {
      "encodingProfile": "{{string}}",
      "videoMaxBitrate": {{number}}
   },
   "entitlements": [
      {
         "dataTransferSubscriberFeePercent": {{number}},
         "description": "{{string}}",
         "encryption": {
            "algorithm": "{{string}}",
            "constantInitializationVector": "{{string}}",
            "deviceId": "{{string}}",
            "keyType": "{{string}}",
            "region": "{{string}}",
            "resourceId": "{{string}}",
            "roleArn": "{{string}}",
            "secretArn": "{{string}}",
            "url": "{{string}}"
         },
         "entitlementStatus": "{{string}}",
         "entitlementTags": {
            "{{string}}" : "{{string}}"
         },
         "name": "{{string}}",
         "subscribers": [ "{{string}}" ]
      }
   ],
   "flowSize": "{{string}}",
   "flowTags": {
      "{{string}}" : "{{string}}"
   },
   "maintenance": {
      "maintenanceDay": "{{string}}",
      "maintenanceStartHour": "{{string}}"
   },
   "mediaStreams": [
      {
         "attributes": {
            "fmtp": {
               "channelOrder": "{{string}}",
               "colorimetry": "{{string}}",
               "exactFramerate": "{{string}}",
               "par": "{{string}}",
               "range": "{{string}}",
               "scanMode": "{{string}}",
               "tcs": "{{string}}"
            },
            "lang": "{{string}}"
         },
         "clockRate": {{number}},
         "description": "{{string}}",
         "mediaStreamId": {{number}},
         "mediaStreamName": "{{string}}",
         "mediaStreamTags": {
            "{{string}}" : "{{string}}"
         },
         "mediaStreamType": "{{string}}",
         "videoFormat": "{{string}}"
      }
   ],
   "name": "{{string}}",
   "ndiConfig": {
      "machineName": "{{string}}",
      "ndiDiscoveryServers": [
         {
            "discoveryServerAddress": "{{string}}",
            "discoveryServerPort": {{number}},
            "vpcInterfaceAdapter": "{{string}}"
         }
      ],
      "ndiState": "{{string}}"
   },
   "outputs": [
      {
         "cidrAllowList": [ "{{string}}" ],
         "description": "{{string}}",
         "destination": "{{string}}",
         "encryption": {
            "algorithm": "{{string}}",
            "constantInitializationVector": "{{string}}",
            "deviceId": "{{string}}",
            "keyType": "{{string}}",
            "region": "{{string}}",
            "resourceId": "{{string}}",
            "roleArn": "{{string}}",
            "secretArn": "{{string}}",
            "url": "{{string}}"
         },
         "maxLatency": {{number}},
         "mediaStreamOutputConfigurations": [
            {
               "destinationConfigurations": [
                  {
                     "destinationIp": "{{string}}",
                     "destinationPort": {{number}},
                     "interface": {
                        "name": "{{string}}"
                     }
                  }
               ],
               "encodingName": "{{string}}",
               "encodingParameters": {
                  "compressionFactor": {{number}},
                  "encoderProfile": "{{string}}"
               },
               "mediaStreamName": "{{string}}"
            }
         ],
         "minLatency": {{number}},
         "name": "{{string}}",
         "ndiOutputTimecodeSource": "{{string}}",
         "ndiProgramName": "{{string}}",
         "ndiSpeedHqQuality": {{number}},
         "outputStatus": "{{string}}",
         "outputTags": {
            "{{string}}" : "{{string}}"
         },
         "port": {{number}},
         "protocol": "{{string}}",
         "remoteId": "{{string}}",
         "routerIntegrationState": "{{string}}",
         "routerIntegrationTransitEncryption": {
            "encryptionKeyConfiguration": { ... },
            "encryptionKeyType": "{{string}}"
         },
         "senderControlPort": {{number}},
         "smoothingLatency": {{number}},
         "streamId": "{{string}}",
         "vpcInterfaceAttachment": {
            "vpcInterfaceName": "{{string}}"
         }
      }
   ],
   "source": {
      "decryption": {
         "algorithm": "{{string}}",
         "constantInitializationVector": "{{string}}",
         "deviceId": "{{string}}",
         "keyType": "{{string}}",
         "region": "{{string}}",
         "resourceId": "{{string}}",
         "roleArn": "{{string}}",
         "secretArn": "{{string}}",
         "url": "{{string}}"
      },
      "description": "{{string}}",
      "entitlementArn": "{{string}}",
      "gatewayBridgeSource": {
         "bridgeArn": "{{string}}",
         "vpcInterfaceAttachment": {
            "vpcInterfaceName": "{{string}}"
         }
      },
      "ingestPort": {{number}},
      "maxBitrate": {{number}},
      "maxLatency": {{number}},
      "maxSyncBuffer": {{number}},
      "mediaStreamSourceConfigurations": [
         {
            "encodingName": "{{string}}",
            "inputConfigurations": [
               {
                  "inputPort": {{number}},
                  "interface": {
                     "name": "{{string}}"
                  }
               }
            ],
            "mediaStreamName": "{{string}}"
         }
      ],
      "minLatency": {{number}},
      "name": "{{string}}",
      "ndiSourceSettings": {
         "sourceName": "{{string}}"
      },
      "protocol": "{{string}}",
      "routerIntegrationState": "{{string}}",
      "routerIntegrationTransitDecryption": {
         "encryptionKeyConfiguration": { ... },
         "encryptionKeyType": "{{string}}"
      },
      "senderControlPort": {{number}},
      "senderIpAddress": "{{string}}",
      "sourceListenerAddress": "{{string}}",
      "sourceListenerPort": {{number}},
      "sourceTags": {
         "{{string}}" : "{{string}}"
      },
      "streamId": "{{string}}",
      "vpcInterfaceName": "{{string}}",
      "whitelistCidr": "{{string}}"
   },
   "sourceFailoverConfig": {
      "failoverMode": "{{string}}",
      "recoveryWindow": {{number}},
      "sourcePriority": {
         "primarySource": "{{string}}"
      },
      "state": "{{string}}"
   },
   "sourceMonitoringConfig": {
      "audioMonitoringSettings": [
         {
            "silentAudio": {
               "state": "{{string}}",
               "thresholdSeconds": {{number}}
            }
         }
      ],
      "contentQualityAnalysisState": "{{string}}",
      "thumbnailState": "{{string}}",
      "videoMonitoringSettings": [
         {
            "blackFrames": {
               "state": "{{string}}",
               "thresholdSeconds": {{number}}
            },
            "frozenFrames": {
               "state": "{{string}}",
               "thresholdSeconds": {{number}}
            }
         }
      ]
   },
   "sources": [
      {
         "decryption": {
            "algorithm": "{{string}}",
            "constantInitializationVector": "{{string}}",
            "deviceId": "{{string}}",
            "keyType": "{{string}}",
            "region": "{{string}}",
            "resourceId": "{{string}}",
            "roleArn": "{{string}}",
            "secretArn": "{{string}}",
            "url": "{{string}}"
         },
         "description": "{{string}}",
         "entitlementArn": "{{string}}",
         "gatewayBridgeSource": {
            "bridgeArn": "{{string}}",
            "vpcInterfaceAttachment": {
               "vpcInterfaceName": "{{string}}"
            }
         },
         "ingestPort": {{number}},
         "maxBitrate": {{number}},
         "maxLatency": {{number}},
         "maxSyncBuffer": {{number}},
         "mediaStreamSourceConfigurations": [
            {
               "encodingName": "{{string}}",
               "inputConfigurations": [
                  {
                     "inputPort": {{number}},
                     "interface": {
                        "name": "{{string}}"
                     }
                  }
               ],
               "mediaStreamName": "{{string}}"
            }
         ],
         "minLatency": {{number}},
         "name": "{{string}}",
         "ndiSourceSettings": {
            "sourceName": "{{string}}"
         },
         "protocol": "{{string}}",
         "routerIntegrationState": "{{string}}",
         "routerIntegrationTransitDecryption": {
            "encryptionKeyConfiguration": { ... },
            "encryptionKeyType": "{{string}}"
         },
         "senderControlPort": {{number}},
         "senderIpAddress": "{{string}}",
         "sourceListenerAddress": "{{string}}",
         "sourceListenerPort": {{number}},
         "sourceTags": {
            "{{string}}" : "{{string}}"
         },
         "streamId": "{{string}}",
         "vpcInterfaceName": "{{string}}",
         "whitelistCidr": "{{string}}"
      }
   ],
   "vpcInterfaces": [
      {
         "name": "{{string}}",
         "networkInterfaceType": "{{string}}",
         "roleArn": "{{string}}",
         "securityGroupIds": [ "{{string}}" ],
         "subnetId": "{{string}}",
         "vpcInterfaceTags": {
            "{{string}}" : "{{string}}"
         }
      }
   ]
}
```

## URI Request Parameters
<a name="API_CreateFlow_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateFlow_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [availabilityZone](#API_CreateFlow_RequestSyntax) **   <a name="mediaconnect-CreateFlow-request-availabilityZone"></a>
 The Availability Zone that you want to create the flow in. These options are limited to the Availability Zones within the current AWS Region.
Type: String
Required: No

 ** [encodingConfig](#API_CreateFlow_RequestSyntax) **   <a name="mediaconnect-CreateFlow-request-encodingConfig"></a>
 The encoding configuration to apply to the NDI® source when transcoding it to a transport stream for downstream distribution. You can choose between several predefined encoding profiles based on common use cases.
Type: [EncodingConfig](API_EncodingConfig.md) object
Required: No

 ** [entitlements](#API_CreateFlow_RequestSyntax) **   <a name="mediaconnect-CreateFlow-request-entitlements"></a>
 The entitlements that you want to grant on a flow.
Type: Array of [GrantEntitlementRequest](API_GrantEntitlementRequest.md) objects
Required: No

 ** [flowSize](#API_CreateFlow_RequestSyntax) **   <a name="mediaconnect-CreateFlow-request-flowSize"></a>
 Determines the processing capacity and feature set of the flow. Set this optional parameter to `LARGE` if you want to enable NDI sources or outputs on the flow.
Type: String
Valid Values: `MEDIUM | LARGE | LARGE_4X`
Required: No

 ** [flowTags](#API_CreateFlow_RequestSyntax) **   <a name="mediaconnect-CreateFlow-request-flowTags"></a>
 The key-value pairs that can be used to tag and organize the flow.
Type: String to string map
Required: No

 ** [maintenance](#API_CreateFlow_RequestSyntax) **   <a name="mediaconnect-CreateFlow-request-maintenance"></a>
 The maintenance settings you want to use for the flow.
Type: [AddMaintenance](API_AddMaintenance.md) object
Required: No

 ** [mediaStreams](#API_CreateFlow_RequestSyntax) **   <a name="mediaconnect-CreateFlow-request-mediaStreams"></a>
 The media streams that you want to add to the flow. You can associate these media streams with sources and outputs on the flow.
Type: Array of [AddMediaStreamRequest](API_AddMediaStreamRequest.md) objects
Required: No

 ** [name](#API_CreateFlow_RequestSyntax) **   <a name="mediaconnect-CreateFlow-request-name"></a>
 The name of the flow.
Type: String
Required: Yes

 ** [ndiConfig](#API_CreateFlow_RequestSyntax) **   <a name="mediaconnect-CreateFlow-request-ndiConfig"></a>
 Specifies the configuration settings for a flow's NDI source or output. Required when the flow includes an NDI source or output.
Type: [NdiConfig](API_NdiConfig.md) object
Required: No

 ** [outputs](#API_CreateFlow_RequestSyntax) **   <a name="mediaconnect-CreateFlow-request-outputs"></a>
 The outputs that you want to add to this flow.
Type: Array of [AddOutputRequest](API_AddOutputRequest.md) objects
Required: No

 ** [source](#API_CreateFlow_RequestSyntax) **   <a name="mediaconnect-CreateFlow-request-source"></a>
 The settings for the source that you want to use for the new flow.
Type: [SetSourceRequest](API_SetSourceRequest.md) object
Required: No

 ** [sourceFailoverConfig](#API_CreateFlow_RequestSyntax) **   <a name="mediaconnect-CreateFlow-request-sourceFailoverConfig"></a>
 The settings for source failover.
Type: [FailoverConfig](API_FailoverConfig.md) object
Required: No

 ** [sourceMonitoringConfig](#API_CreateFlow_RequestSyntax) **   <a name="mediaconnect-CreateFlow-request-sourceMonitoringConfig"></a>
 The settings for source monitoring.
Type: [MonitoringConfig](API_MonitoringConfig.md) object
Required: No

 ** [sources](#API_CreateFlow_RequestSyntax) **   <a name="mediaconnect-CreateFlow-request-sources"></a>
The sources that are assigned to the flow.
Type: Array of [SetSourceRequest](API_SetSourceRequest.md) objects
Required: No

 ** [vpcInterfaces](#API_CreateFlow_RequestSyntax) **   <a name="mediaconnect-CreateFlow-request-vpcInterfaces"></a>
 The VPC interfaces you want on the flow.
Type: Array of [VpcInterfaceRequest](API_VpcInterfaceRequest.md) objects
Required: No

## Response Syntax
<a name="API_CreateFlow_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "flow": {
      "availabilityZone": "string",
      "description": "string",
      "egressIp": "string",
      "encodingConfig": {
         "encodingProfile": "string",
         "videoMaxBitrate": number
      },
      "entitlements": [
         {
            "dataTransferSubscriberFeePercent": number,
            "description": "string",
            "encryption": {
               "algorithm": "string",
               "constantInitializationVector": "string",
               "deviceId": "string",
               "keyType": "string",
               "region": "string",
               "resourceId": "string",
               "roleArn": "string",
               "secretArn": "string",
               "url": "string"
            },
            "entitlementArn": "string",
            "entitlementStatus": "string",
            "name": "string",
            "subscribers": [ "string" ]
         }
      ],
      "flowArn": "string",
      "flowSize": "string",
      "maintenance": {
         "maintenanceDay": "string",
         "maintenanceDeadline": "string",
         "maintenanceScheduledDate": "string",
         "maintenanceStartHour": "string"
      },
      "mediaStreams": [
         {
            "attributes": {
               "fmtp": {
                  "channelOrder": "string",
                  "colorimetry": "string",
                  "exactFramerate": "string",
                  "par": "string",
                  "range": "string",
                  "scanMode": "string",
                  "tcs": "string"
               },
               "lang": "string"
            },
            "clockRate": number,
            "description": "string",
            "fmt": number,
            "mediaStreamId": number,
            "mediaStreamName": "string",
            "mediaStreamType": "string",
            "videoFormat": "string"
         }
      ],
      "name": "string",
      "ndiConfig": {
         "machineName": "string",
         "ndiDiscoveryServers": [
            {
               "discoveryServerAddress": "string",
               "discoveryServerPort": number,
               "vpcInterfaceAdapter": "string"
            }
         ],
         "ndiState": "string"
      },
      "outputs": [
         {
            "bridgeArn": "string",
            "bridgePorts": [ number ],
            "connectedRouterInputArn": "string",
            "dataTransferSubscriberFeePercent": number,
            "description": "string",
            "destination": "string",
            "encryption": {
               "algorithm": "string",
               "constantInitializationVector": "string",
               "deviceId": "string",
               "keyType": "string",
               "region": "string",
               "resourceId": "string",
               "roleArn": "string",
               "secretArn": "string",
               "url": "string"
            },
            "entitlementArn": "string",
            "listenerAddress": "string",
            "mediaLiveInputArn": "string",
            "mediaStreamOutputConfigurations": [
               {
                  "destinationConfigurations": [
                     {
                        "destinationIp": "string",
                        "destinationPort": number,
                        "interface": {
                           "name": "string"
                        },
                        "outboundIp": "string"
                     }
                  ],
                  "encodingName": "string",
                  "encodingParameters": {
                     "compressionFactor": number,
                     "encoderProfile": "string"
                  },
                  "mediaStreamName": "string"
               }
            ],
            "name": "string",
            "outputArn": "string",
            "outputStatus": "string",
            "peerIpAddress": "string",
            "port": number,
            "routerIntegrationState": "string",
            "routerIntegrationTransitEncryption": {
               "encryptionKeyConfiguration": { ... },
               "encryptionKeyType": "string"
            },
            "transport": {
               "cidrAllowList": [ "string" ],
               "maxBitrate": number,
               "maxLatency": number,
               "maxSyncBuffer": number,
               "minLatency": number,
               "ndiOutputTimecodeSource": "string",
               "ndiProgramName": "string",
               "ndiSourceSettings": {
                  "sourceName": "string"
               },
               "ndiSpeedHqQuality": number,
               "protocol": "string",
               "remoteId": "string",
               "senderControlPort": number,
               "senderIpAddress": "string",
               "smoothingLatency": number,
               "sourceListenerAddress": "string",
               "sourceListenerPort": number,
               "streamId": "string"
            },
            "vpcInterfaceAttachment": {
               "vpcInterfaceName": "string"
            }
         }
      ],
      "source": {
         "connectedRouterOutputArn": "string",
         "dataTransferSubscriberFeePercent": number,
         "decryption": {
            "algorithm": "string",
            "constantInitializationVector": "string",
            "deviceId": "string",
            "keyType": "string",
            "region": "string",
            "resourceId": "string",
            "roleArn": "string",
            "secretArn": "string",
            "url": "string"
         },
         "description": "string",
         "entitlementArn": "string",
         "gatewayBridgeSource": {
            "bridgeArn": "string",
            "vpcInterfaceAttachment": {
               "vpcInterfaceName": "string"
            }
         },
         "ingestIp": "string",
         "ingestPort": number,
         "mediaStreamSourceConfigurations": [
            {
               "encodingName": "string",
               "inputConfigurations": [
                  {
                     "inputIp": "string",
                     "inputPort": number,
                     "interface": {
                        "name": "string"
                     }
                  }
               ],
               "mediaStreamName": "string"
            }
         ],
         "name": "string",
         "peerIpAddress": "string",
         "routerIntegrationState": "string",
         "routerIntegrationTransitDecryption": {
            "encryptionKeyConfiguration": { ... },
            "encryptionKeyType": "string"
         },
         "senderControlPort": number,
         "senderIpAddress": "string",
         "sourceArn": "string",
         "transport": {
            "cidrAllowList": [ "string" ],
            "maxBitrate": number,
            "maxLatency": number,
            "maxSyncBuffer": number,
            "minLatency": number,
            "ndiOutputTimecodeSource": "string",
            "ndiProgramName": "string",
            "ndiSourceSettings": {
               "sourceName": "string"
            },
            "ndiSpeedHqQuality": number,
            "protocol": "string",
            "remoteId": "string",
            "senderControlPort": number,
            "senderIpAddress": "string",
            "smoothingLatency": number,
            "sourceListenerAddress": "string",
            "sourceListenerPort": number,
            "streamId": "string"
         },
         "vpcInterfaceName": "string",
         "whitelistCidr": "string"
      },
      "sourceFailoverConfig": {
         "failoverMode": "string",
         "recoveryWindow": number,
         "sourcePriority": {
            "primarySource": "string"
         },
         "state": "string"
      },
      "sourceMonitoringConfig": {
         "audioMonitoringSettings": [
            {
               "silentAudio": {
                  "state": "string",
                  "thresholdSeconds": number
               }
            }
         ],
         "contentQualityAnalysisState": "string",
         "thumbnailState": "string",
         "videoMonitoringSettings": [
            {
               "blackFrames": {
                  "state": "string",
                  "thresholdSeconds": number
               },
               "frozenFrames": {
                  "state": "string",
                  "thresholdSeconds": number
               }
            }
         ]
      },
      "sources": [
         {
            "connectedRouterOutputArn": "string",
            "dataTransferSubscriberFeePercent": number,
            "decryption": {
               "algorithm": "string",
               "constantInitializationVector": "string",
               "deviceId": "string",
               "keyType": "string",
               "region": "string",
               "resourceId": "string",
               "roleArn": "string",
               "secretArn": "string",
               "url": "string"
            },
            "description": "string",
            "entitlementArn": "string",
            "gatewayBridgeSource": {
               "bridgeArn": "string",
               "vpcInterfaceAttachment": {
                  "vpcInterfaceName": "string"
               }
            },
            "ingestIp": "string",
            "ingestPort": number,
            "mediaStreamSourceConfigurations": [
               {
                  "encodingName": "string",
                  "inputConfigurations": [
                     {
                        "inputIp": "string",
                        "inputPort": number,
                        "interface": {
                           "name": "string"
                        }
                     }
                  ],
                  "mediaStreamName": "string"
               }
            ],
            "name": "string",
            "peerIpAddress": "string",
            "routerIntegrationState": "string",
            "routerIntegrationTransitDecryption": {
               "encryptionKeyConfiguration": { ... },
               "encryptionKeyType": "string"
            },
            "senderControlPort": number,
            "senderIpAddress": "string",
            "sourceArn": "string",
            "transport": {
               "cidrAllowList": [ "string" ],
               "maxBitrate": number,
               "maxLatency": number,
               "maxSyncBuffer": number,
               "minLatency": number,
               "ndiOutputTimecodeSource": "string",
               "ndiProgramName": "string",
               "ndiSourceSettings": {
                  "sourceName": "string"
               },
               "ndiSpeedHqQuality": number,
               "protocol": "string",
               "remoteId": "string",
               "senderControlPort": number,
               "senderIpAddress": "string",
               "smoothingLatency": number,
               "sourceListenerAddress": "string",
               "sourceListenerPort": number,
               "streamId": "string"
            },
            "vpcInterfaceName": "string",
            "whitelistCidr": "string"
         }
      ],
      "status": "string",
      "vpcInterfaces": [
         {
            "name": "string",
            "networkInterfaceIds": [ "string" ],
            "networkInterfaceType": "string",
            "roleArn": "string",
            "securityGroupIds": [ "string" ],
            "subnetId": "string"
         }
      ]
   }
}
```

## Response Elements
<a name="API_CreateFlow_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [flow](#API_CreateFlow_ResponseSyntax) **   <a name="mediaconnect-CreateFlow-response-flow"></a>
 The flow that you created.
Type: [Flow](API_Flow.md) object

## Errors
<a name="API_CreateFlow_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message.
HTTP Status Code: 400

 ** CreateFlow420Exception **
Exception raised by AWS Elemental MediaConnect when creating the flow. See the error message for the operation for more information on the cause of this exception.
HTTP Status Code: 420

 ** ForbiddenException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerErrorException **
The server encountered an internal error and is unable to complete the request.
HTTP Status Code: 500

 ** ServiceUnavailableException **
The service is currently unavailable or busy.
HTTP Status Code: 503

 ** TooManyRequestsException **
The request was denied due to request throttling.
HTTP Status Code: 429

## See Also
<a name="API_CreateFlow_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mediaconnect-2018-11-14/CreateFlow)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mediaconnect-2018-11-14/CreateFlow)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/CreateFlow)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mediaconnect-2018-11-14/CreateFlow)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/CreateFlow)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mediaconnect-2018-11-14/CreateFlow)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mediaconnect-2018-11-14/CreateFlow)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mediaconnect-2018-11-14/CreateFlow)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mediaconnect-2018-11-14/CreateFlow)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/CreateFlow)
