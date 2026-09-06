---
source_url: https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_UpdateModelManifest.html
---

# UpdateModelManifest
<a name="API_UpdateModelManifest"></a>

**Important**
 AWS IoT FleetWise is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS IoT FleetWise availability change](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/iotfleetwise-availability-change.html).

 Updates a vehicle model (model manifest). If created vehicles are associated with a vehicle model, it can't be updated.

## Request Syntax
<a name="API_UpdateModelManifest_RequestSyntax"></a>

```
{
   "description": "{{string}}",
   "name": "{{string}}",
   "nodesToAdd": [ "{{string}}" ],
   "nodesToRemove": [ "{{string}}" ],
   "status": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateModelManifest_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [description](#API_UpdateModelManifest_RequestSyntax) **   <a name="iotfleetwise-UpdateModelManifest-request-description"></a>
 A brief description of the vehicle model.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: No

 ** [name](#API_UpdateModelManifest_RequestSyntax) **   <a name="iotfleetwise-UpdateModelManifest-request-name"></a>
 The name of the vehicle model to update.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z\d\-_:]+`
Required: Yes

 ** [nodesToAdd](#API_UpdateModelManifest_RequestSyntax) **   <a name="iotfleetwise-UpdateModelManifest-request-nodesToAdd"></a>
 A list of `fullyQualifiedName` of nodes, which are a general abstraction of signals, to add to the vehicle model.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 500 items.
Length Constraints: Minimum length of 1. Maximum length of 150.
Pattern: `[a-zA-Z0-9_.]+`
Required: No

 ** [nodesToRemove](#API_UpdateModelManifest_RequestSyntax) **   <a name="iotfleetwise-UpdateModelManifest-request-nodesToRemove"></a>
 A list of `fullyQualifiedName` of nodes, which are a general abstraction of signals, to remove from the vehicle model.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 500 items.
Length Constraints: Minimum length of 1. Maximum length of 150.
Pattern: `[a-zA-Z0-9_.]+`
Required: No

 ** [status](#API_UpdateModelManifest_RequestSyntax) **   <a name="iotfleetwise-UpdateModelManifest-request-status"></a>
 The state of the vehicle model. If the status is `ACTIVE`, the vehicle model can't be edited. If the status is `DRAFT`, you can edit the vehicle model.
Type: String
Valid Values: `ACTIVE | DRAFT | INVALID | VALIDATING`
Required: No

## Response Syntax
<a name="API_UpdateModelManifest_ResponseSyntax"></a>

```
{
   "arn": "string",
   "name": "string"
}
```

## Response Elements
<a name="API_UpdateModelManifest_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_UpdateModelManifest_ResponseSyntax) **   <a name="iotfleetwise-UpdateModelManifest-response-arn"></a>
 The Amazon Resource Name (ARN) of the updated vehicle model.
Type: String

 ** [name](#API_UpdateModelManifest_ResponseSyntax) **   <a name="iotfleetwise-UpdateModelManifest-response-name"></a>
 The name of the updated vehicle model.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z\d\-_:]+`

## Errors
<a name="API_UpdateModelManifest_Errors"></a>

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
<a name="API_UpdateModelManifest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotfleetwise-2021-06-17/UpdateModelManifest)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotfleetwise-2021-06-17/UpdateModelManifest)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotfleetwise-2021-06-17/UpdateModelManifest)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotfleetwise-2021-06-17/UpdateModelManifest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotfleetwise-2021-06-17/UpdateModelManifest)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotfleetwise-2021-06-17/UpdateModelManifest)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotfleetwise-2021-06-17/UpdateModelManifest)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotfleetwise-2021-06-17/UpdateModelManifest)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iotfleetwise-2021-06-17/UpdateModelManifest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotfleetwise-2021-06-17/UpdateModelManifest)
