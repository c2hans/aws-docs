---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_UpdateFlow.html
---

# UpdateFlow
<a name="API_UpdateFlow"></a>

 Updates an existing flow.

**Note**
 Because `UpdateFlowSources` and `UpdateFlow` are separate operations, you can't change both the source type AND the flow size in a single request.
If you have a `MEDIUM` flow and you want to change the flow source to NDI®:
First, use the `UpdateFlow` operation to upgrade the flow size to `LARGE`.
After that, you can then use the `UpdateFlowSource` operation to configure the NDI source.
If you're switching from an NDI source to a transport stream (TS) source and want to downgrade the flow size:
First, use the `UpdateFlowSource` operation to change the flow source type.
After that, you can then use the `UpdateFlow` operation to downgrade the flow size to `MEDIUM`.

## Request Syntax
<a name="API_UpdateFlow_RequestSyntax"></a>

```
PUT /v1/flows/{{flowArn}} HTTP/1.1
Content-type: application/json

{
   "encodingConfig": {
      "encodingProfile": "{{string}}",
      "videoMaxBitrate": {{number}}
   },
   "flowSize": "{{string}}",
   "maintenance": {
      "maintenanceDay": "{{string}}",
      "maintenanceScheduledDate": "{{string}}",
      "maintenanceStartHour": "{{string}}"
   },
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
   }
}
```

## URI Request Parameters
<a name="API_UpdateFlow_RequestParameters"></a>

The request uses the following URI parameters.

 ** [flowArn](#API_UpdateFlow_RequestSyntax) **   <a name="mediaconnect-UpdateFlow-request-uri-flowArn"></a>
 The Amazon Resource Name (ARN) of the flow that you want to update.
Pattern: `arn:.+:mediaconnect.+:flow:.+`
Required: Yes

## Request Body
<a name="API_UpdateFlow_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [encodingConfig](#API_UpdateFlow_RequestSyntax) **   <a name="mediaconnect-UpdateFlow-request-encodingConfig"></a>
 The encoding configuration to apply to the NDI® source when transcoding it to a transport stream for downstream distribution. You can choose between several predefined encoding profiles based on common use cases.
Type: [EncodingConfig](API_EncodingConfig.md) object
Required: No

 ** [flowSize](#API_UpdateFlow_RequestSyntax) **   <a name="mediaconnect-UpdateFlow-request-flowSize"></a>
 Determines the processing capacity and feature set of the flow.
Type: String
Valid Values: `MEDIUM | LARGE | LARGE_4X`
Required: No

 ** [maintenance](#API_UpdateFlow_RequestSyntax) **   <a name="mediaconnect-UpdateFlow-request-maintenance"></a>
 The maintenance setting of the flow.
Type: [UpdateMaintenance](API_UpdateMaintenance.md) object
Required: No

 ** [ndiConfig](#API_UpdateFlow_RequestSyntax) **   <a name="mediaconnect-UpdateFlow-request-ndiConfig"></a>
 Specifies the configuration settings for a flow's NDI source or output. Required when the flow includes an NDI source or output.
Type: [NdiConfig](API_NdiConfig.md) object
Required: No

 ** [sourceFailoverConfig](#API_UpdateFlow_RequestSyntax) **   <a name="mediaconnect-UpdateFlow-request-sourceFailoverConfig"></a>
 The settings for source failover.
Type: [UpdateFailoverConfig](API_UpdateFailoverConfig.md) object
Required: No

 ** [sourceMonitoringConfig](#API_UpdateFlow_RequestSyntax) **   <a name="mediaconnect-UpdateFlow-request-sourceMonitoringConfig"></a>
 The settings for source monitoring.
Type: [MonitoringConfig](API_MonitoringConfig.md) object
Required: No

## Response Syntax
<a name="API_UpdateFlow_ResponseSyntax"></a>

```
HTTP/1.1 202
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
<a name="API_UpdateFlow_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [flow](#API_UpdateFlow_ResponseSyntax) **   <a name="mediaconnect-UpdateFlow-response-flow"></a>
 The updated flow.
Type: [Flow](API_Flow.md) object

## Errors
<a name="API_UpdateFlow_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message.
HTTP Status Code: 400

 ** ForbiddenException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerErrorException **
The server encountered an internal error and is unable to complete the request.
HTTP Status Code: 500

 ** NotFoundException **
One or more of the resources in the request does not exist in the system.
HTTP Status Code: 404

 ** ServiceUnavailableException **
The service is currently unavailable or busy.
HTTP Status Code: 503

 ** TooManyRequestsException **
The request was denied due to request throttling.
HTTP Status Code: 429

## See Also
<a name="API_UpdateFlow_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mediaconnect-2018-11-14/UpdateFlow)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mediaconnect-2018-11-14/UpdateFlow)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/UpdateFlow)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mediaconnect-2018-11-14/UpdateFlow)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/UpdateFlow)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mediaconnect-2018-11-14/UpdateFlow)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mediaconnect-2018-11-14/UpdateFlow)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mediaconnect-2018-11-14/UpdateFlow)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mediaconnect-2018-11-14/UpdateFlow)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/UpdateFlow)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaConnect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
