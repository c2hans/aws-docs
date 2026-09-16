---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_DescribeFlow.html
---

# DescribeFlow
<a name="API_DescribeFlow"></a>

 Displays the details of a flow. The response includes the flow Amazon Resource Name (ARN), name, and Availability Zone, as well as details about the source, outputs, and entitlements.

## Request Syntax
<a name="API_DescribeFlow_RequestSyntax"></a>

```
GET /v1/flows/{{flowArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeFlow_RequestParameters"></a>

The request uses the following URI parameters.

 ** [flowArn](#API_DescribeFlow_RequestSyntax) **   <a name="mediaconnect-DescribeFlow-request-uri-flowArn"></a>
 The ARN of the flow that you want to describe.
Pattern: `arn:.+:mediaconnect.+:flow:.+`
Required: Yes

## Request Body
<a name="API_DescribeFlow_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeFlow_ResponseSyntax"></a>

```
HTTP/1.1 200
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
   },
   "messages": {
      "errors": [ "string" ]
   }
}
```

## Response Elements
<a name="API_DescribeFlow_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [flow](#API_DescribeFlow_ResponseSyntax) **   <a name="mediaconnect-DescribeFlow-response-flow"></a>
The flow that you requested a description of.
Type: [Flow](API_Flow.md) object

 ** [messages](#API_DescribeFlow_ResponseSyntax) **   <a name="mediaconnect-DescribeFlow-response-messages"></a>
 Any errors that apply currently to the flow. If there are no errors, MediaConnect will not include this field in the response.
Type: [Messages](API_Messages.md) object

## Errors
<a name="API_DescribeFlow_Errors"></a>

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
<a name="API_DescribeFlow_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mediaconnect-2018-11-14/DescribeFlow)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mediaconnect-2018-11-14/DescribeFlow)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/DescribeFlow)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mediaconnect-2018-11-14/DescribeFlow)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/DescribeFlow)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mediaconnect-2018-11-14/DescribeFlow)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mediaconnect-2018-11-14/DescribeFlow)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mediaconnect-2018-11-14/DescribeFlow)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/mediaconnect-2018-11-14/DescribeFlow)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/DescribeFlow)
