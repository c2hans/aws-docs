---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_UpdateFlowSource.html
---

# UpdateFlowSource
<a name="API_UpdateFlowSource"></a>

 Updates the source of a flow.

**Note**
 Because `UpdateFlowSources` and `UpdateFlow` are separate operations, you can't change both the source type AND the flow size in a single request.
If you have a `MEDIUM` flow and you want to change the flow source to NDI®:
First, use the `UpdateFlow` operation to upgrade the flow size to `LARGE`.
After that, you can then use the `UpdateFlowSource` operation to configure the NDI source.
If you're switching from an NDI source to a transport stream (TS) source and want to downgrade the flow size:
First, use the `UpdateFlowSource` operation to change the flow source type.
After that, you can then use the `UpdateFlow` operation to downgrade the flow size to `MEDIUM`.

## Request Syntax
<a name="API_UpdateFlowSource_RequestSyntax"></a>

```
PUT /v1/flows/{{flowArn}}/source/{{sourceArn}} HTTP/1.1
Content-type: application/json

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
   "streamId": "{{string}}",
   "vpcInterfaceName": "{{string}}",
   "whitelistCidr": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateFlowSource_RequestParameters"></a>

The request uses the following URI parameters.

 ** [flowArn](#API_UpdateFlowSource_RequestSyntax) **   <a name="mediaconnect-UpdateFlowSource-request-uri-flowArn"></a>
 The ARN of the flow that you want to update.
Pattern: `arn:.+:mediaconnect.+:flow:.+`
Required: Yes

 ** [sourceArn](#API_UpdateFlowSource_RequestSyntax) **   <a name="mediaconnect-UpdateFlowSource-request-uri-sourceArn"></a>
The ARN of the source that you want to update.
Pattern: `arn:.+:mediaconnect.+:source:.+`
Required: Yes

## Request Body
<a name="API_UpdateFlowSource_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [decryption](#API_UpdateFlowSource_RequestSyntax) **   <a name="mediaconnect-UpdateFlowSource-request-decryption"></a>
The type of encryption that is used on the content ingested from the source.
Type: [UpdateEncryption](API_UpdateEncryption.md) object
Required: No

 ** [description](#API_UpdateFlowSource_RequestSyntax) **   <a name="mediaconnect-UpdateFlowSource-request-description"></a>
A description of the source. This description is not visible outside of the current AWS account.
Type: String
Required: No

 ** [entitlementArn](#API_UpdateFlowSource_RequestSyntax) **   <a name="mediaconnect-UpdateFlowSource-request-entitlementArn"></a>
The Amazon Resource Name (ARN) of the entitlement that allows you to subscribe to the flow. The entitlement is set by the content originator, and the ARN is generated as part of the originator's flow.
Type: String
Pattern: `arn:.+:mediaconnect.+:entitlement:.+`
Required: No

 ** [gatewayBridgeSource](#API_UpdateFlowSource_RequestSyntax) **   <a name="mediaconnect-UpdateFlowSource-request-gatewayBridgeSource"></a>
The source configuration for cloud flows receiving a stream from a bridge.
Type: [UpdateGatewayBridgeSourceRequest](API_UpdateGatewayBridgeSourceRequest.md) object
Required: No

 ** [ingestPort](#API_UpdateFlowSource_RequestSyntax) **   <a name="mediaconnect-UpdateFlowSource-request-ingestPort"></a>
The port that the flow listens on for incoming content. If the protocol of the source is Zixi, the port must be set to 2088.
Type: Integer
Required: No

 ** [maxBitrate](#API_UpdateFlowSource_RequestSyntax) **   <a name="mediaconnect-UpdateFlowSource-request-maxBitrate"></a>
The maximum bitrate for RIST, RTP, and RTP-FEC streams.
Type: Integer
Required: No

 ** [maxLatency](#API_UpdateFlowSource_RequestSyntax) **   <a name="mediaconnect-UpdateFlowSource-request-maxLatency"></a>
The maximum latency in milliseconds. This parameter applies only to RIST-based and Zixi-based streams.
Type: Integer
Required: No

 ** [maxSyncBuffer](#API_UpdateFlowSource_RequestSyntax) **   <a name="mediaconnect-UpdateFlowSource-request-maxSyncBuffer"></a>
The size of the buffer (in milliseconds) to use to sync incoming source data.
Type: Integer
Required: No

 ** [mediaStreamSourceConfigurations](#API_UpdateFlowSource_RequestSyntax) **   <a name="mediaconnect-UpdateFlowSource-request-mediaStreamSourceConfigurations"></a>
The media stream that is associated with the source, and the parameters for that association.
Type: Array of [MediaStreamSourceConfigurationRequest](API_MediaStreamSourceConfigurationRequest.md) objects
Required: No

 ** [minLatency](#API_UpdateFlowSource_RequestSyntax) **   <a name="mediaconnect-UpdateFlowSource-request-minLatency"></a>
The minimum latency in milliseconds for SRT-based streams. In streams that use the SRT protocol, this value that you set on your MediaConnect source or output represents the minimal potential latency of that connection. The latency of the stream is set to the highest number between the sender’s minimum latency and the receiver’s minimum latency.
Type: Integer
Required: No

 ** [ndiSourceSettings](#API_UpdateFlowSource_RequestSyntax) **   <a name="mediaconnect-UpdateFlowSource-request-ndiSourceSettings"></a>
 The settings for the NDI source. This includes the exact name of the upstream NDI sender that you want to connect to your source.
Type: [NdiSourceSettings](API_NdiSourceSettings.md) object
Required: No

 ** [protocol](#API_UpdateFlowSource_RequestSyntax) **   <a name="mediaconnect-UpdateFlowSource-request-protocol"></a>
The protocol that the source uses to deliver the content to MediaConnect.
 AWS Elemental MediaConnect no longer supports the Fujitsu QoS protocol. This reference is maintained for legacy purposes only.
Type: String
Valid Values: `zixi-push | rtp-fec | rtp | zixi-pull | rist | st2110-jpegxs | cdi | srt-listener | srt-caller | fujitsu-qos | udp | ndi-speed-hq`
Required: No

 ** [routerIntegrationState](#API_UpdateFlowSource_RequestSyntax) **   <a name="mediaconnect-UpdateFlowSource-request-routerIntegrationState"></a>
Indicates whether to enable or disable router integration for this flow source.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** [routerIntegrationTransitDecryption](#API_UpdateFlowSource_RequestSyntax) **   <a name="mediaconnect-UpdateFlowSource-request-routerIntegrationTransitDecryption"></a>
The encryption configuration for the flow source when router integration is enabled.
Type: [FlowTransitEncryption](API_FlowTransitEncryption.md) object
Required: No

 ** [senderControlPort](#API_UpdateFlowSource_RequestSyntax) **   <a name="mediaconnect-UpdateFlowSource-request-senderControlPort"></a>
The port that the flow uses to send outbound requests to initiate connection with the sender.
Type: Integer
Required: No

 ** [senderIpAddress](#API_UpdateFlowSource_RequestSyntax) **   <a name="mediaconnect-UpdateFlowSource-request-senderIpAddress"></a>
The IP address that the flow communicates with to initiate connection with the sender.
Type: String
Required: No

 ** [sourceListenerAddress](#API_UpdateFlowSource_RequestSyntax) **   <a name="mediaconnect-UpdateFlowSource-request-sourceListenerAddress"></a>
The source IP or domain name for SRT-caller protocol.
Type: String
Required: No

 ** [sourceListenerPort](#API_UpdateFlowSource_RequestSyntax) **   <a name="mediaconnect-UpdateFlowSource-request-sourceListenerPort"></a>
Source port for SRT-caller protocol.
Type: Integer
Required: No

 ** [streamId](#API_UpdateFlowSource_RequestSyntax) **   <a name="mediaconnect-UpdateFlowSource-request-streamId"></a>
The stream ID that you want to use for this transport. This parameter applies only to Zixi and SRT caller-based streams.
Type: String
Required: No

 ** [vpcInterfaceName](#API_UpdateFlowSource_RequestSyntax) **   <a name="mediaconnect-UpdateFlowSource-request-vpcInterfaceName"></a>
The name of the VPC interface that you want to send your output to.
Type: String
Required: No

 ** [whitelistCidr](#API_UpdateFlowSource_RequestSyntax) **   <a name="mediaconnect-UpdateFlowSource-request-whitelistCidr"></a>
The range of IP addresses that are allowed to contribute content to your source. Format the IP addresses as a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.
Type: String
Required: No

## Response Syntax
<a name="API_UpdateFlowSource_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "flowArn": "string",
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
   }
}
```

## Response Elements
<a name="API_UpdateFlowSource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [flowArn](#API_UpdateFlowSource_ResponseSyntax) **   <a name="mediaconnect-UpdateFlowSource-response-flowArn"></a>
The ARN of the flow that you updated.
Type: String

 ** [source](#API_UpdateFlowSource_ResponseSyntax) **   <a name="mediaconnect-UpdateFlowSource-response-source"></a>
The details of the sources that are assigned to the flow.
Type: [Source](API_Source.md) object

## Errors
<a name="API_UpdateFlowSource_Errors"></a>

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
<a name="API_UpdateFlowSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mediaconnect-2018-11-14/UpdateFlowSource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mediaconnect-2018-11-14/UpdateFlowSource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/UpdateFlowSource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mediaconnect-2018-11-14/UpdateFlowSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/UpdateFlowSource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mediaconnect-2018-11-14/UpdateFlowSource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mediaconnect-2018-11-14/UpdateFlowSource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mediaconnect-2018-11-14/UpdateFlowSource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mediaconnect-2018-11-14/UpdateFlowSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/UpdateFlowSource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaConnect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
