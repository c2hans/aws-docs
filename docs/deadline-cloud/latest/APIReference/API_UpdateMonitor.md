---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_UpdateMonitor.html
---

# UpdateMonitor
<a name="API_UpdateMonitor"></a>

Modifies the settings for a Deadline Cloud monitor. You can modify one or all of the settings when you call `UpdateMonitor`.

## Request Syntax
<a name="API_UpdateMonitor_RequestSyntax"></a>

```
PATCH /2023-10-12/monitors/{{monitorId}} HTTP/1.1
Content-type: application/json

{
   "displayName": "{{string}}",
   "roleArn": "{{string}}",
   "subdomain": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateMonitor_RequestParameters"></a>

The request uses the following URI parameters.

 ** [monitorId](#API_UpdateMonitor_RequestSyntax) **   <a name="deadlinecloud-UpdateMonitor-request-uri-monitorId"></a>
The unique identifier of the monitor to update.
Pattern: `monitor-[0-9a-f]{32}`
Required: Yes

## Request Body
<a name="API_UpdateMonitor_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [displayName](#API_UpdateMonitor_RequestSyntax) **   <a name="deadlinecloud-UpdateMonitor-request-displayName"></a>
The new value to use for the monitor's display name.
This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** [roleArn](#API_UpdateMonitor_RequestSyntax) **   <a name="deadlinecloud-UpdateMonitor-request-roleArn"></a>
The Amazon Resource Name of the new IAM role to use with the monitor.
Type: String
Pattern: `arn:(aws[a-zA-Z-]*):iam::\d{12}:role(/[!-.0-~]+)*/[\w+=,.@-]+`
Required: No

 ** [subdomain](#API_UpdateMonitor_RequestSyntax) **   <a name="deadlinecloud-UpdateMonitor-request-subdomain"></a>
The new value of the subdomain to use when forming the monitor URL.
Type: String
Pattern: `[a-z0-9-]{1,100}`
Required: No

## Response Syntax
<a name="API_UpdateMonitor_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateMonitor_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateMonitor_Errors"></a>

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
<a name="API_UpdateMonitor_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/deadline-2023-10-12/UpdateMonitor)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/deadline-2023-10-12/UpdateMonitor)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/UpdateMonitor)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/deadline-2023-10-12/UpdateMonitor)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/UpdateMonitor)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/deadline-2023-10-12/UpdateMonitor)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/deadline-2023-10-12/UpdateMonitor)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/deadline-2023-10-12/UpdateMonitor)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/deadline-2023-10-12/UpdateMonitor)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/UpdateMonitor)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Deadline Cloud. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query deadline-cloud` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
