---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_AddFlowOutputs.html
---

# AddFlowOutputs
<a name="API_AddFlowOutputs"></a>

 Adds outputs to an existing flow. You can create up to 50 outputs per flow.

## Request Syntax
<a name="API_AddFlowOutputs_RequestSyntax"></a>

```
POST /v1/flows/{{flowArn}}/outputs HTTP/1.1
Content-type: application/json

{
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
   ]
}
```

## URI Request Parameters
<a name="API_AddFlowOutputs_RequestParameters"></a>

The request uses the following URI parameters.

 ** [flowArn](#API_AddFlowOutputs_RequestSyntax) **   <a name="mediaconnect-AddFlowOutputs-request-uri-flowArn"></a>
 The Amazon Resource Name (ARN) of the flow that you want to add outputs to.
Pattern: `arn:.+:mediaconnect.+:flow:.+`
Required: Yes

## Request Body
<a name="API_AddFlowOutputs_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [outputs](#API_AddFlowOutputs_RequestSyntax) **   <a name="mediaconnect-AddFlowOutputs-request-outputs"></a>
 A list of outputs that you want to add to the flow.
Type: Array of [AddOutputRequest](API_AddOutputRequest.md) objects
Required: Yes

## Response Syntax
<a name="API_AddFlowOutputs_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "flowArn": "string",
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
   ]
}
```

## Response Elements
<a name="API_AddFlowOutputs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [flowArn](#API_AddFlowOutputs_ResponseSyntax) **   <a name="mediaconnect-AddFlowOutputs-response-flowArn"></a>
 The ARN of the flow that these outputs were added to.
Type: String

 ** [outputs](#API_AddFlowOutputs_ResponseSyntax) **   <a name="mediaconnect-AddFlowOutputs-response-outputs"></a>
 The details of the newly added outputs.
Type: Array of [Output](API_Output.md) objects

## Errors
<a name="API_AddFlowOutputs_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AddFlowOutputs420Exception **
Exception raised by AWS Elemental MediaConnect when adding the flow output. See the error message for the operation for more information on the cause of this exception.
HTTP Status Code: 420

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
<a name="API_AddFlowOutputs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mediaconnect-2018-11-14/AddFlowOutputs)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mediaconnect-2018-11-14/AddFlowOutputs)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/AddFlowOutputs)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mediaconnect-2018-11-14/AddFlowOutputs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/AddFlowOutputs)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mediaconnect-2018-11-14/AddFlowOutputs)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mediaconnect-2018-11-14/AddFlowOutputs)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mediaconnect-2018-11-14/AddFlowOutputs)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mediaconnect-2018-11-14/AddFlowOutputs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/AddFlowOutputs)
