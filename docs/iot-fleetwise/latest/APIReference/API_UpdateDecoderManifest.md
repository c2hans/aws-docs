---
source_url: https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_UpdateDecoderManifest.html
---

# UpdateDecoderManifest
<a name="API_UpdateDecoderManifest"></a>

**Important**
 AWS IoT FleetWise is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS IoT FleetWise availability change](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/iotfleetwise-availability-change.html).

 Updates a decoder manifest.

A decoder manifest can only be updated when the status is `DRAFT`. Only `ACTIVE` decoder manifests can be associated with vehicles.

## Request Syntax
<a name="API_UpdateDecoderManifest_RequestSyntax"></a>

```
{
   "defaultForUnmappedSignals": "{{string}}",
   "description": "{{string}}",
   "name": "{{string}}",
   "networkInterfacesToAdd": [
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
   "networkInterfacesToRemove": [ "{{string}}" ],
   "networkInterfacesToUpdate": [
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
   "signalDecodersToAdd": [
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
   "signalDecodersToRemove": [ "{{string}}" ],
   "signalDecodersToUpdate": [
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
   "status": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateDecoderManifest_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [defaultForUnmappedSignals](#API_UpdateDecoderManifest_RequestSyntax) **   <a name="iotfleetwise-UpdateDecoderManifest-request-defaultForUnmappedSignals"></a>
Use default decoders for all unmapped signals in the model. You don't need to provide any detailed decoding information.
Type: String
Valid Values: `CUSTOM_DECODING`
Required: No

 ** [description](#API_UpdateDecoderManifest_RequestSyntax) **   <a name="iotfleetwise-UpdateDecoderManifest-request-description"></a>
 A brief description of the decoder manifest to update.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: No

 ** [name](#API_UpdateDecoderManifest_RequestSyntax) **   <a name="iotfleetwise-UpdateDecoderManifest-request-name"></a>
 The name of the decoder manifest to update.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z\d\-_:]+`
Required: Yes

 ** [networkInterfacesToAdd](#API_UpdateDecoderManifest_RequestSyntax) **   <a name="iotfleetwise-UpdateDecoderManifest-request-networkInterfacesToAdd"></a>
 A list of information about the network interfaces to add to the decoder manifest.
Type: Array of [NetworkInterface](API_NetworkInterface.md) objects
Array Members: Minimum number of 1 item. Maximum number of 500 items.
Required: No

 ** [networkInterfacesToRemove](#API_UpdateDecoderManifest_RequestSyntax) **   <a name="iotfleetwise-UpdateDecoderManifest-request-networkInterfacesToRemove"></a>
 A list of network interfaces to remove from the decoder manifest.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 500 items.
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `[-a-zA-Z0-9_.]+`
Required: No

 ** [networkInterfacesToUpdate](#API_UpdateDecoderManifest_RequestSyntax) **   <a name="iotfleetwise-UpdateDecoderManifest-request-networkInterfacesToUpdate"></a>
 A list of information about the network interfaces to update in the decoder manifest.
Type: Array of [NetworkInterface](API_NetworkInterface.md) objects
Array Members: Minimum number of 1 item. Maximum number of 500 items.
Required: No

 ** [signalDecodersToAdd](#API_UpdateDecoderManifest_RequestSyntax) **   <a name="iotfleetwise-UpdateDecoderManifest-request-signalDecodersToAdd"></a>
 A list of information about decoding additional signals to add to the decoder manifest.
Type: Array of [SignalDecoder](API_SignalDecoder.md) objects
Array Members: Minimum number of 1 item. Maximum number of 500 items.
Required: No

 ** [signalDecodersToRemove](#API_UpdateDecoderManifest_RequestSyntax) **   <a name="iotfleetwise-UpdateDecoderManifest-request-signalDecodersToRemove"></a>
 A list of signal decoders to remove from the decoder manifest.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 500 items.
Length Constraints: Minimum length of 1. Maximum length of 150.
Pattern: `[a-zA-Z0-9_.]+`
Required: No

 ** [signalDecodersToUpdate](#API_UpdateDecoderManifest_RequestSyntax) **   <a name="iotfleetwise-UpdateDecoderManifest-request-signalDecodersToUpdate"></a>
 A list of updated information about decoding signals to update in the decoder manifest.
Type: Array of [SignalDecoder](API_SignalDecoder.md) objects
Array Members: Minimum number of 1 item. Maximum number of 500 items.
Required: No

 ** [status](#API_UpdateDecoderManifest_RequestSyntax) **   <a name="iotfleetwise-UpdateDecoderManifest-request-status"></a>
 The state of the decoder manifest. If the status is `ACTIVE`, the decoder manifest can't be edited. If the status is `DRAFT`, you can edit the decoder manifest.
Type: String
Valid Values: `ACTIVE | DRAFT | INVALID | VALIDATING`
Required: No

## Response Syntax
<a name="API_UpdateDecoderManifest_ResponseSyntax"></a>

```
{
   "arn": "string",
   "name": "string"
}
```

## Response Elements
<a name="API_UpdateDecoderManifest_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_UpdateDecoderManifest_ResponseSyntax) **   <a name="iotfleetwise-UpdateDecoderManifest-response-arn"></a>
 The Amazon Resource Name (ARN) of the updated decoder manifest.
Type: String

 ** [name](#API_UpdateDecoderManifest_ResponseSyntax) **   <a name="iotfleetwise-UpdateDecoderManifest-response-name"></a>
 The name of the updated decoder manifest.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z\d\-_:]+`

## Errors
<a name="API_UpdateDecoderManifest_Errors"></a>

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
<a name="API_UpdateDecoderManifest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotfleetwise-2021-06-17/UpdateDecoderManifest)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotfleetwise-2021-06-17/UpdateDecoderManifest)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotfleetwise-2021-06-17/UpdateDecoderManifest)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotfleetwise-2021-06-17/UpdateDecoderManifest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotfleetwise-2021-06-17/UpdateDecoderManifest)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotfleetwise-2021-06-17/UpdateDecoderManifest)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotfleetwise-2021-06-17/UpdateDecoderManifest)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotfleetwise-2021-06-17/UpdateDecoderManifest)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iotfleetwise-2021-06-17/UpdateDecoderManifest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotfleetwise-2021-06-17/UpdateDecoderManifest)
