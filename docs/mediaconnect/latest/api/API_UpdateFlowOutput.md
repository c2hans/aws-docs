---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_UpdateFlowOutput.html
---

# UpdateFlowOutput
<a name="API_UpdateFlowOutput"></a>

 Updates an existing flow output.

## Request Syntax
<a name="API_UpdateFlowOutput_RequestSyntax"></a>

```
PUT /v1/flows/{{flowArn}}/outputs/{{outputArn}} HTTP/1.1
Content-type: application/json

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
   "ndiOutputTimecodeSource": "{{string}}",
   "ndiProgramName": "{{string}}",
   "ndiSpeedHqQuality": {{number}},
   "outputStatus": "{{string}}",
   "port": {{number}},
   "protocol": "{{string}}",
   "remoteId": "{{string}}",
   "routerIntegrationState": "{{string}}",
   "routerIntegrationTransitEncryption": {
      "encryptionKeyConfiguration": { ... },
      "encryptionKeyType": "{{string}}"
   },
   "senderControlPort": {{number}},
   "senderIpAddress": "{{string}}",
   "smoothingLatency": {{number}},
   "streamId": "{{string}}",
   "vpcInterfaceAttachment": {
      "vpcInterfaceName": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_UpdateFlowOutput_RequestParameters"></a>

The request uses the following URI parameters.

 ** [flowArn](#API_UpdateFlowOutput_RequestSyntax) **   <a name="mediaconnect-UpdateFlowOutput-request-uri-flowArn"></a>
 The Amazon Resource Name (ARN) of the flow that is associated with the output that you want to update.
Pattern: `arn:.+:mediaconnect.+:flow:.+`
Required: Yes

 ** [outputArn](#API_UpdateFlowOutput_RequestSyntax) **   <a name="mediaconnect-UpdateFlowOutput-request-uri-outputArn"></a>
 The ARN of the output that you want to update.
Pattern: `arn:.+:mediaconnect.+:output:.+`
Required: Yes

## Request Body
<a name="API_UpdateFlowOutput_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [cidrAllowList](#API_UpdateFlowOutput_RequestSyntax) **   <a name="mediaconnect-UpdateFlowOutput-request-cidrAllowList"></a>
 The range of IP addresses that should be allowed to initiate output requests to this flow. These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.
Type: Array of strings
Required: No

 ** [description](#API_UpdateFlowOutput_RequestSyntax) **   <a name="mediaconnect-UpdateFlowOutput-request-description"></a>
 A description of the output. This description appears only on the MediaConnect console and will not be seen by the end user.
Type: String
Required: No

 ** [destination](#API_UpdateFlowOutput_RequestSyntax) **   <a name="mediaconnect-UpdateFlowOutput-request-destination"></a>
 The IP address where you want to send the output.
Type: String
Required: No

 ** [encryption](#API_UpdateFlowOutput_RequestSyntax) **   <a name="mediaconnect-UpdateFlowOutput-request-encryption"></a>
 The type of key used for the encryption. If no `keyType` is provided, the service will use the default setting (static-key). Allowable encryption types: static-key.
Type: [UpdateEncryption](API_UpdateEncryption.md) object
Required: No

 ** [maxLatency](#API_UpdateFlowOutput_RequestSyntax) **   <a name="mediaconnect-UpdateFlowOutput-request-maxLatency"></a>
 The maximum latency in milliseconds. This parameter applies only to RIST-based and Zixi-based streams.
Type: Integer
Required: No

 ** [mediaStreamOutputConfigurations](#API_UpdateFlowOutput_RequestSyntax) **   <a name="mediaconnect-UpdateFlowOutput-request-mediaStreamOutputConfigurations"></a>
 The media streams that are associated with the output, and the parameters for those associations.
Type: Array of [MediaStreamOutputConfigurationRequest](API_MediaStreamOutputConfigurationRequest.md) objects
Required: No

 ** [minLatency](#API_UpdateFlowOutput_RequestSyntax) **   <a name="mediaconnect-UpdateFlowOutput-request-minLatency"></a>
 The minimum latency in milliseconds for SRT-based streams. In streams that use the SRT protocol, this value that you set on your MediaConnect source or output represents the minimal potential latency of that connection. The latency of the stream is set to the highest number between the sender’s minimum latency and the receiver’s minimum latency.
Type: Integer
Required: No

 ** [ndiOutputTimecodeSource](#API_UpdateFlowOutput_RequestSyntax) **   <a name="mediaconnect-UpdateFlowOutput-request-ndiOutputTimecodeSource"></a>
Controls how MediaConnect generates timecodes for NDI output frames. If you don't specify this field, MediaConnect leaves the value unchanged.
+  `EMBEDDED_TIMECODE` - Preserves timecodes from the input transport stream. The timecodes must be embedded in the video stream as SEI timing messages. If no embedded timecode is detected, MediaConnect uses the UTC system time instead.
+  `UTC_SYSTEM_TIME` - Generates timecodes based on the system clock time when each frame is sent.
Type: String
Valid Values: `EMBEDDED_TIMECODE | UTC_SYSTEM_TIME`
Required: No

 ** [ndiProgramName](#API_UpdateFlowOutput_RequestSyntax) **   <a name="mediaconnect-UpdateFlowOutput-request-ndiProgramName"></a>
 A suffix for the name of the NDI® sender that the flow creates. If a custom name isn't specified, MediaConnect uses the output name.
Type: String
Required: No

 ** [ndiSpeedHqQuality](#API_UpdateFlowOutput_RequestSyntax) **   <a name="mediaconnect-UpdateFlowOutput-request-ndiSpeedHqQuality"></a>
A quality setting for the NDI Speed HQ encoder.
Type: Integer
Required: No

 ** [outputStatus](#API_UpdateFlowOutput_RequestSyntax) **   <a name="mediaconnect-UpdateFlowOutput-request-outputStatus"></a>
 An indication of whether the output should transmit data or not. If you don't specify the `outputStatus` field in your request, MediaConnect leaves the value unchanged.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** [port](#API_UpdateFlowOutput_RequestSyntax) **   <a name="mediaconnect-UpdateFlowOutput-request-port"></a>
 The port to use when content is distributed to this output.
Type: Integer
Required: No

 ** [protocol](#API_UpdateFlowOutput_RequestSyntax) **   <a name="mediaconnect-UpdateFlowOutput-request-protocol"></a>
 The protocol to use for the output.
 AWS Elemental MediaConnect no longer supports the Fujitsu QoS protocol. This reference is maintained for legacy purposes only.
Type: String
Valid Values: `zixi-push | rtp-fec | rtp | zixi-pull | rist | st2110-jpegxs | cdi | srt-listener | srt-caller | fujitsu-qos | udp | ndi-speed-hq`
Required: No

 ** [remoteId](#API_UpdateFlowOutput_RequestSyntax) **   <a name="mediaconnect-UpdateFlowOutput-request-remoteId"></a>
 The remote ID for the Zixi-pull stream.
Type: String
Required: No

 ** [routerIntegrationState](#API_UpdateFlowOutput_RequestSyntax) **   <a name="mediaconnect-UpdateFlowOutput-request-routerIntegrationState"></a>
Indicates whether to enable or disable router integration for this flow output.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** [routerIntegrationTransitEncryption](#API_UpdateFlowOutput_RequestSyntax) **   <a name="mediaconnect-UpdateFlowOutput-request-routerIntegrationTransitEncryption"></a>
The configuration that defines how content is encrypted during transit between the MediaConnect router and a MediaConnect flow.
Type: [FlowTransitEncryption](API_FlowTransitEncryption.md) object
Required: No

 ** [senderControlPort](#API_UpdateFlowOutput_RequestSyntax) **   <a name="mediaconnect-UpdateFlowOutput-request-senderControlPort"></a>
 The port that the flow uses to send outbound requests to initiate connection with the sender.
Type: Integer
Required: No

 ** [senderIpAddress](#API_UpdateFlowOutput_RequestSyntax) **   <a name="mediaconnect-UpdateFlowOutput-request-senderIpAddress"></a>
 The IP address that the flow communicates with to initiate connection with the sender.
Type: String
Required: No

 ** [smoothingLatency](#API_UpdateFlowOutput_RequestSyntax) **   <a name="mediaconnect-UpdateFlowOutput-request-smoothingLatency"></a>
 The smoothing latency in milliseconds for RIST, RTP, and RTP-FEC streams.
Type: Integer
Required: No

 ** [streamId](#API_UpdateFlowOutput_RequestSyntax) **   <a name="mediaconnect-UpdateFlowOutput-request-streamId"></a>
 The stream ID that you want to use for this transport. This parameter applies only to Zixi and SRT caller-based streams.
Type: String
Required: No

 ** [vpcInterfaceAttachment](#API_UpdateFlowOutput_RequestSyntax) **   <a name="mediaconnect-UpdateFlowOutput-request-vpcInterfaceAttachment"></a>
 The name of the VPC interface attachment to use for this output.
Type: [VpcInterfaceAttachment](API_VpcInterfaceAttachment.md) object
Required: No

## Response Syntax
<a name="API_UpdateFlowOutput_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "flowArn": "string",
   "output": {
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
}
```

## Response Elements
<a name="API_UpdateFlowOutput_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [flowArn](#API_UpdateFlowOutput_ResponseSyntax) **   <a name="mediaconnect-UpdateFlowOutput-response-flowArn"></a>
 The ARN of the flow that is associated with the updated output.
Type: String

 ** [output](#API_UpdateFlowOutput_ResponseSyntax) **   <a name="mediaconnect-UpdateFlowOutput-response-output"></a>
 The new settings of the output that you updated.
Type: [Output](API_Output.md) object

## Errors
<a name="API_UpdateFlowOutput_Errors"></a>

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
<a name="API_UpdateFlowOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mediaconnect-2018-11-14/UpdateFlowOutput)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mediaconnect-2018-11-14/UpdateFlowOutput)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/UpdateFlowOutput)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mediaconnect-2018-11-14/UpdateFlowOutput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/UpdateFlowOutput)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mediaconnect-2018-11-14/UpdateFlowOutput)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mediaconnect-2018-11-14/UpdateFlowOutput)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mediaconnect-2018-11-14/UpdateFlowOutput)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mediaconnect-2018-11-14/UpdateFlowOutput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/UpdateFlowOutput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaConnect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
