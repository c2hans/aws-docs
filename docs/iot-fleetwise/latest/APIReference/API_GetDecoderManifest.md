---
source_url: https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_GetDecoderManifest.html
---

# GetDecoderManifest
<a name="API_GetDecoderManifest"></a>

**Important**
 AWS IoT FleetWise is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS IoT FleetWise availability change](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/iotfleetwise-availability-change.html).

 Retrieves information about a created decoder manifest.

## Request Syntax
<a name="API_GetDecoderManifest_RequestSyntax"></a>

```
{
   "name": "{{string}}"
}
```

## Request Parameters
<a name="API_GetDecoderManifest_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [name](#API_GetDecoderManifest_RequestSyntax) **   <a name="iotfleetwise-GetDecoderManifest-request-name"></a>
 The name of the decoder manifest to retrieve information about.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z\d\-_:]+`
Required: Yes

## Response Syntax
<a name="API_GetDecoderManifest_ResponseSyntax"></a>

```
{
   "arn": "string",
   "creationTime": number,
   "description": "string",
   "lastModificationTime": number,
   "message": "string",
   "modelManifestArn": "string",
   "name": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_GetDecoderManifest_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_GetDecoderManifest_ResponseSyntax) **   <a name="iotfleetwise-GetDecoderManifest-response-arn"></a>
 The Amazon Resource Name (ARN) of the decoder manifest.
Type: String

 ** [creationTime](#API_GetDecoderManifest_ResponseSyntax) **   <a name="iotfleetwise-GetDecoderManifest-response-creationTime"></a>
 The time the decoder manifest was created in seconds since epoch (January 1, 1970 at midnight UTC time).
Type: Timestamp

 ** [description](#API_GetDecoderManifest_ResponseSyntax) **   <a name="iotfleetwise-GetDecoderManifest-response-description"></a>
 A brief description of the decoder manifest.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\u0000-\u001F\u007F]+`

 ** [lastModificationTime](#API_GetDecoderManifest_ResponseSyntax) **   <a name="iotfleetwise-GetDecoderManifest-response-lastModificationTime"></a>
 The time the decoder manifest was last updated in seconds since epoch (January 1, 1970 at midnight UTC time).
Type: Timestamp

 ** [message](#API_GetDecoderManifest_ResponseSyntax) **   <a name="iotfleetwise-GetDecoderManifest-response-message"></a>
The detailed message for the decoder manifest. When a decoder manifest is in an `INVALID` status, the message contains detailed reason and help information.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\u0000-\u001F\u007F]+`

 ** [modelManifestArn](#API_GetDecoderManifest_ResponseSyntax) **   <a name="iotfleetwise-GetDecoderManifest-response-modelManifestArn"></a>
 The ARN of a vehicle model (model manifest) associated with the decoder manifest.
Type: String

 ** [name](#API_GetDecoderManifest_ResponseSyntax) **   <a name="iotfleetwise-GetDecoderManifest-response-name"></a>
 The name of the decoder manifest.
Type: String

 ** [status](#API_GetDecoderManifest_ResponseSyntax) **   <a name="iotfleetwise-GetDecoderManifest-response-status"></a>
 The state of the decoder manifest. If the status is `ACTIVE`, the decoder manifest can't be edited. If the status is marked `DRAFT`, you can edit the decoder manifest.
Type: String
Valid Values: `ACTIVE | DRAFT | INVALID | VALIDATING`

## Errors
<a name="API_GetDecoderManifest_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient permission to perform this action.
HTTP Status Code: 400

 ** InternalServerException **
The request couldn't be completed because the server temporarily failed.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the command.
HTTP Status Code: 500

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
<a name="API_GetDecoderManifest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotfleetwise-2021-06-17/GetDecoderManifest)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotfleetwise-2021-06-17/GetDecoderManifest)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotfleetwise-2021-06-17/GetDecoderManifest)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotfleetwise-2021-06-17/GetDecoderManifest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotfleetwise-2021-06-17/GetDecoderManifest)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotfleetwise-2021-06-17/GetDecoderManifest)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotfleetwise-2021-06-17/GetDecoderManifest)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotfleetwise-2021-06-17/GetDecoderManifest)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iotfleetwise-2021-06-17/GetDecoderManifest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotfleetwise-2021-06-17/GetDecoderManifest)
