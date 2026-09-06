---
source_url: https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_ImportDecoderManifest.html
---

# ImportDecoderManifest
<a name="API_ImportDecoderManifest"></a>

**Important**
 AWS IoT FleetWise is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS IoT FleetWise availability change](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/iotfleetwise-availability-change.html).

Imports new signal decoders into an existing decoder manifest using the CAN DBC files from your local device. The CAN signal name must be unique and not repeated across CAN message definitions in the .dbc file.

## Request Syntax
<a name="API_ImportDecoderManifest_RequestSyntax"></a>

```
{
   "name": "{{string}}",
   "networkFileDefinitions": [
      { ... }
   ]
}
```

## Request Parameters
<a name="API_ImportDecoderManifest_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [name](#API_ImportDecoderManifest_RequestSyntax) **   <a name="iotfleetwise-ImportDecoderManifest-request-name"></a>
 The name of the decoder manifest to import.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z\d\-_:]+`
Required: Yes

 ** [networkFileDefinitions](#API_ImportDecoderManifest_RequestSyntax) **   <a name="iotfleetwise-ImportDecoderManifest-request-networkFileDefinitions"></a>
 The file to load into an AWS account.
Type: Array of [NetworkFileDefinition](API_NetworkFileDefinition.md) objects
Required: Yes

## Response Syntax
<a name="API_ImportDecoderManifest_ResponseSyntax"></a>

```
{
   "arn": "string",
   "name": "string"
}
```

## Response Elements
<a name="API_ImportDecoderManifest_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_ImportDecoderManifest_ResponseSyntax) **   <a name="iotfleetwise-ImportDecoderManifest-response-arn"></a>
 The Amazon Resource Name (ARN) of the decoder manifest that was imported.
Type: String

 ** [name](#API_ImportDecoderManifest_ResponseSyntax) **   <a name="iotfleetwise-ImportDecoderManifest-response-name"></a>
 The name of the imported decoder manifest.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z\d\-_:]+`

## Errors
<a name="API_ImportDecoderManifest_Errors"></a>

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

 ** InvalidSignalsException **
The request couldn't be completed because it contains signals that aren't valid.
 ** invalidSignals **
The signals which caused the exception.
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
<a name="API_ImportDecoderManifest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotfleetwise-2021-06-17/ImportDecoderManifest)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotfleetwise-2021-06-17/ImportDecoderManifest)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotfleetwise-2021-06-17/ImportDecoderManifest)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotfleetwise-2021-06-17/ImportDecoderManifest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotfleetwise-2021-06-17/ImportDecoderManifest)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotfleetwise-2021-06-17/ImportDecoderManifest)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotfleetwise-2021-06-17/ImportDecoderManifest)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotfleetwise-2021-06-17/ImportDecoderManifest)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iotfleetwise-2021-06-17/ImportDecoderManifest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotfleetwise-2021-06-17/ImportDecoderManifest)
