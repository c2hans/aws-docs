---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_UpdateLimit.html
---

# UpdateLimit
<a name="API_UpdateLimit"></a>

Updates the properties of the specified limit.

## Request Syntax
<a name="API_UpdateLimit_RequestSyntax"></a>

```
PATCH /2023-10-12/farms/{{farmId}}/limits/{{limitId}} HTTP/1.1
Content-type: application/json

{
   "description": "{{string}}",
   "displayName": "{{string}}",
   "maxCount": {{number}}
}
```

## URI Request Parameters
<a name="API_UpdateLimit_RequestParameters"></a>

The request uses the following URI parameters.

 ** [farmId](#API_UpdateLimit_RequestSyntax) **   <a name="deadlinecloud-UpdateLimit-request-uri-farmId"></a>
The unique identifier of the farm that contains the limit.
Pattern: `farm-[0-9a-f]{32}`
Required: Yes

 ** [limitId](#API_UpdateLimit_RequestSyntax) **   <a name="deadlinecloud-UpdateLimit-request-uri-limitId"></a>
The unique identifier of the limit to update.
Pattern: `limit-[0-9a-f]{32}`
Required: Yes

## Request Body
<a name="API_UpdateLimit_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [description](#API_UpdateLimit_RequestSyntax) **   <a name="deadlinecloud-UpdateLimit-request-description"></a>
The new description of the limit.
This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.
Required: No

 ** [displayName](#API_UpdateLimit_RequestSyntax) **   <a name="deadlinecloud-UpdateLimit-request-displayName"></a>
The new display name of the limit.
This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** [maxCount](#API_UpdateLimit_RequestSyntax) **   <a name="deadlinecloud-UpdateLimit-request-maxCount"></a>
The maximum number of resources constrained by this limit. When all of the resources are in use, steps that require the limit won't be scheduled until the resource is available.
If more than the new maximum number is currently in use, running jobs finish but no new jobs are started until the number of resources in use is below the new maximum number.
The `maxCount` must not be 0. If the value is -1, there is no restriction on the number of resources that can be acquired for this limit.
Type: Integer
Valid Range: Minimum value of -1. Maximum value of 2147483647.
Required: No

## Response Syntax
<a name="API_UpdateLimit_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateLimit_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateLimit_Errors"></a>

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
<a name="API_UpdateLimit_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/deadline-2023-10-12/UpdateLimit)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/deadline-2023-10-12/UpdateLimit)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/UpdateLimit)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/deadline-2023-10-12/UpdateLimit)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/UpdateLimit)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/deadline-2023-10-12/UpdateLimit)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/deadline-2023-10-12/UpdateLimit)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/deadline-2023-10-12/UpdateLimit)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/deadline-2023-10-12/UpdateLimit)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/UpdateLimit)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Deadline Cloud. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query deadline-cloud` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
