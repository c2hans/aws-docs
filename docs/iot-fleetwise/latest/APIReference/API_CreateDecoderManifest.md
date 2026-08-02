---
source_url: https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_CreateDecoderManifest.html
---

# CreateDecoderManifest
<a name="API_CreateDecoderManifest"></a>

**Important**
 AWS IoT FleetWise is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS IoT FleetWise availability change](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/iotfleetwise-availability-change.html).

Creates the decoder manifest associated with a model manifest. To create a decoder manifest, the following must be true:
+ Every signal decoder has a unique name.
+ Each signal decoder is associated with a network interface.
+ Each network interface has a unique ID.
+ The signal decoders are specified in the model manifest.

## Request Syntax
<a name="API_CreateDecoderManifest_RequestSyntax"></a>

```
{
   "defaultForUnmappedSignals": "{{string}}",
   "description": "{{string}}",
   "modelManifestArn": "{{string}}",
   "name": "{{string}}",
   "networkInterfaces": [
      {
         "canInterface": {
            "name": "{{string}}",
            "protocolName": "{{string}}",
            "protocolVersion": "{{string}}"
         },
         "customDecodingInterface": {
            "name": "{{string}}"
         },
         "interfaceId": "{{string}}",
         "obdInterface": {
            "dtcRequestIntervalSeconds": {{number}},
            "hasTransmissionEcu": {{boolean}},
            "name": "{{string}}",
            "obdStandard": "{{string}}",
            "pidRequestIntervalSeconds": {{number}},
            "requestMessageId": {{number}},
            "useExtendedIds": {{boolean}}
         },
         "type": "{{string}}",
         "vehicleMiddleware": {
            "name": "{{string}}",
            "protocolName": "{{string}}"
         }
      }
   ],
   "signalDecoders": [
      {
         "canSignal": {
            "factor": {{number}},
            "isBigEndian": {{boolean}},
            "isSigned": {{boolean}},
            "length": {{number}},
            "messageId": {{number}},
            "name": "{{string}}",
            "offset": {{number}},
            "signalValueType": "{{string}}",
            "startBit": {{number}}
         },
         "customDecodingSignal": {
            "id": "{{string}}"
         },
         "fullyQualifiedName": "{{string}}",
         "interfaceId": "{{string}}",
         "messageSignal": {
            "structuredMessage": { ... },
            "topicName": "{{string}}"
         },
         "obdSignal": {
            "bitMaskLength": {{number}},
            "bitRightShift": {{number}},
            "byteLength": {{number}},
            "isSigned": {{boolean}},
            "offset": {{number}},
            "pid": {{number}},
            "pidResponseLength": {{number}},
            "scaling": {{number}},
            "serviceMode": {{number}},
            "signalValueType": "{{string}}",
            "startByte": {{number}}
         },
         "type": "{{string}}"
      }
   ],
   "tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateDecoderManifest_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [defaultForUnmappedSignals](#API_CreateDecoderManifest_RequestSyntax) **   <a name="iotfleetwise-CreateDecoderManifest-request-defaultForUnmappedSignals"></a>
Use default decoders for all unmapped signals in the model. You don't need to provide any detailed decoding information.
Type: String
Valid Values: `CUSTOM_DECODING`
Required: No

 ** [description](#API_CreateDecoderManifest_RequestSyntax) **   <a name="iotfleetwise-CreateDecoderManifest-request-description"></a>
A brief description of the decoder manifest.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: No

 ** [modelManifestArn](#API_CreateDecoderManifest_RequestSyntax) **   <a name="iotfleetwise-CreateDecoderManifest-request-modelManifestArn"></a>
 The Amazon Resource Name (ARN) of the vehicle model (model manifest).
Type: String
Pattern: `arn:aws:iotfleetwise:[a-z0-9-]+:[0-9]{12}:model-manifest/[a-zA-Z\d\-_:]{1,100}`
Required: Yes

 ** [name](#API_CreateDecoderManifest_RequestSyntax) **   <a name="iotfleetwise-CreateDecoderManifest-request-name"></a>
 The unique name of the decoder manifest to create.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z\d\-_:]+`
Required: Yes

 ** [networkInterfaces](#API_CreateDecoderManifest_RequestSyntax) **   <a name="iotfleetwise-CreateDecoderManifest-request-networkInterfaces"></a>
 A list of information about available network interfaces.
Type: Array of [NetworkInterface](API_NetworkInterface.md) objects
Array Members: Minimum number of 1 item. Maximum number of 500 items.
Required: No

 ** [signalDecoders](#API_CreateDecoderManifest_RequestSyntax) **   <a name="iotfleetwise-CreateDecoderManifest-request-signalDecoders"></a>
 A list of information about signal decoders.
Type: Array of [SignalDecoder](API_SignalDecoder.md) objects
Array Members: Minimum number of 1 item. Maximum number of 500 items.
Required: No

 ** [tags](#API_CreateDecoderManifest_RequestSyntax) **   <a name="iotfleetwise-CreateDecoderManifest-request-tags"></a>
Metadata that can be used to manage the decoder manifest.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

## Response Syntax
<a name="API_CreateDecoderManifest_ResponseSyntax"></a>

```
{
   "arn": "string",
   "name": "string"
}
```

## Response Elements
<a name="API_CreateDecoderManifest_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_CreateDecoderManifest_ResponseSyntax) **   <a name="iotfleetwise-CreateDecoderManifest-response-arn"></a>
 The ARN of the created decoder manifest.
Type: String

 ** [name](#API_CreateDecoderManifest_ResponseSyntax) **   <a name="iotfleetwise-CreateDecoderManifest-response-name"></a>
 The name of the created decoder manifest.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z\d\-_:]+`

## Errors
<a name="API_CreateDecoderManifest_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient permission to perform this action.
HTTP Status Code: 400

 ** ConflictException **
The request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.
 ** resource **
The resource on which there are conflicting operations.
 ** resourceType **
The type of resource on which there are conflicting operations..
HTTP Status Code: 400

 ** DecoderManifestValidationException **
The request couldn't be completed because it contains signal decoders with one or more validation errors.
 ** invalidNetworkInterfaces **
The request couldn't be completed because of invalid network interfaces in the request.
 ** invalidSignals **
The request couldn't be completed because of invalid signals in the request.
HTTP Status Code: 400

 ** InternalServerException **
The request couldn't be completed because the server temporarily failed.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the command.
HTTP Status Code: 500

 ** LimitExceededException **
A service quota was exceeded.
 ** resourceId **
The identifier of the resource that was exceeded.
 ** resourceType **
The type of resource that was exceeded.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The resource wasn't found.
 ** resourceId **
The identifier of the resource that wasn't found.
 ** resourceType **
The type of resource that wasn't found.
HTTP Status Code: 400

 ** ThrottlingException **
The request couldn't be completed due to throttling.
 ** quotaCode **
The quota identifier of the applied throttling rules for this request.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the command.
 ** serviceCode **
The code for the service that couldn't be completed due to throttling.
HTTP Status Code: 400

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
 ** fieldList **
The list of fields that fail to satisfy the constraints specified by an AWS service.
 ** reason **
The reason the input failed to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_CreateDecoderManifest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotfleetwise-2021-06-17/CreateDecoderManifest)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotfleetwise-2021-06-17/CreateDecoderManifest)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotfleetwise-2021-06-17/CreateDecoderManifest)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotfleetwise-2021-06-17/CreateDecoderManifest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotfleetwise-2021-06-17/CreateDecoderManifest)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotfleetwise-2021-06-17/CreateDecoderManifest)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotfleetwise-2021-06-17/CreateDecoderManifest)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotfleetwise-2021-06-17/CreateDecoderManifest)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iotfleetwise-2021-06-17/CreateDecoderManifest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotfleetwise-2021-06-17/CreateDecoderManifest)
