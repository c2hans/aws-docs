---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_UpdateFarm.html
---

# UpdateFarm
<a name="API_UpdateFarm"></a>

Updates a farm.

## Request Syntax
<a name="API_UpdateFarm_RequestSyntax"></a>

```
PATCH /2023-10-12/farms/{{farmId}} HTTP/1.1
Content-type: application/json

{
   "costScaleFactor": {{number}},
   "description": "{{string}}",
   "displayName": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateFarm_RequestParameters"></a>

The request uses the following URI parameters.

 ** [farmId](#API_UpdateFarm_RequestSyntax) **   <a name="deadlinecloud-UpdateFarm-request-uri-farmId"></a>
The farm ID to update.
Pattern: `farm-[0-9a-f]{32}`
Required: Yes

## Request Body
<a name="API_UpdateFarm_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [costScaleFactor](#API_UpdateFarm_RequestSyntax) **   <a name="deadlinecloud-UpdateFarm-request-costScaleFactor"></a>
A multiplier applied to the farm's calculated costs for usage data and budget tracking. A value less than 1 represents a discount, a value greater than 1 represents a premium, and a value of 1 represents no adjustment.
Type: Float
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

 ** [description](#API_UpdateFarm_RequestSyntax) **   <a name="deadlinecloud-UpdateFarm-request-description"></a>
The description of the farm to update.
This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.
Required: No

 ** [displayName](#API_UpdateFarm_RequestSyntax) **   <a name="deadlinecloud-UpdateFarm-request-displayName"></a>
The display name of the farm to update.
This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

## Response Syntax
<a name="API_UpdateFarm_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateFarm_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateFarm_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have permission to perform the action.
 ** context **
Information about the resources in use when the exception was thrown.
HTTP Status Code: 403

 ** InternalServerErrorException **
Deadline Cloud can't process your request right now. Try again later.
 ** retryAfterSeconds **
The number of seconds a client should wait before retrying the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The requested resource can't be found.
 ** context **
Information about the resources in use when the exception was thrown.
 ** resourceId **
The identifier of the resource that couldn't be found.
 ** resourceType **
The type of the resource that couldn't be found.
HTTP Status Code: 404

 ** ThrottlingException **
Your request exceeded a request rate quota.
 ** context **
Information about the resources in use when the exception was thrown.
 ** quotaCode **
Identifies the quota that is being throttled.
 ** retryAfterSeconds **
The number of seconds a client should wait before retrying the request.
 ** serviceCode **
Identifies the service that is being throttled.
HTTP Status Code: 429

 ** ValidationException **
The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.
 ** context **
Information about the resources in use when the exception was thrown.
 ** fieldList **
A list of fields that failed validation.
 ** reason **
The reason that the request failed validation.
HTTP Status Code: 400

## See Also
<a name="API_UpdateFarm_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/deadline-2023-10-12/UpdateFarm)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/deadline-2023-10-12/UpdateFarm)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/UpdateFarm)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/deadline-2023-10-12/UpdateFarm)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/UpdateFarm)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/deadline-2023-10-12/UpdateFarm)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/deadline-2023-10-12/UpdateFarm)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/deadline-2023-10-12/UpdateFarm)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/deadline-2023-10-12/UpdateFarm)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/UpdateFarm)
