---
source_url: https://docs.aws.amazon.com/notifications/latest/APIReference/API_GetManagedNotificationConfiguration.html
---

# GetManagedNotificationConfiguration
<a name="API_GetManagedNotificationConfiguration"></a>

Returns a specified `ManagedNotificationConfiguration`.

## Request Syntax
<a name="API_GetManagedNotificationConfiguration_RequestSyntax"></a>

```
GET /managed-notification-configurations/{{arn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetManagedNotificationConfiguration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [arn](#API_GetManagedNotificationConfiguration_RequestSyntax) **   <a name="Notifications-GetManagedNotificationConfiguration-request-uri-arn"></a>
The Amazon Resource Name (ARN) of the `ManagedNotificationConfiguration` to return.
Pattern: `arn:[-.a-z0-9]{1,63}:notifications::[0-9]{12}:managed-notification-configuration/category/[a-zA-Z0-9\-]{3,64}/sub-category/[a-zA-Z0-9\-]{3,64}`
Required: Yes

## Request Body
<a name="API_GetManagedNotificationConfiguration_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetManagedNotificationConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "arn": "string",
   "category": "string",
   "description": "string",
   "name": "string",
   "subCategory": "string"
}
```

## Response Elements
<a name="API_GetManagedNotificationConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_GetManagedNotificationConfiguration_ResponseSyntax) **   <a name="Notifications-GetManagedNotificationConfiguration-response-arn"></a>
The ARN of the `ManagedNotificationConfiguration` resource.
Type: String
Pattern: `arn:[-.a-z0-9]{1,63}:notifications::[0-9]{12}:managed-notification-configuration/category/[a-zA-Z0-9\-]{3,64}/sub-category/[a-zA-Z0-9\-]{3,64}`

 ** [category](#API_GetManagedNotificationConfiguration_ResponseSyntax) **   <a name="Notifications-GetManagedNotificationConfiguration-response-category"></a>
The category of the `ManagedNotificationConfiguration`.
Type: String

 ** [description](#API_GetManagedNotificationConfiguration_ResponseSyntax) **   <a name="Notifications-GetManagedNotificationConfiguration-response-description"></a>
The description of the `ManagedNotificationConfiguration`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[^\u0001-\u001F\u007F-\u009F]*`

 ** [name](#API_GetManagedNotificationConfiguration_ResponseSyntax) **   <a name="Notifications-GetManagedNotificationConfiguration-response-name"></a>
The name of the `ManagedNotificationConfiguration`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9\-]+`

 ** [subCategory](#API_GetManagedNotificationConfiguration_ResponseSyntax) **   <a name="Notifications-GetManagedNotificationConfiguration-response-subCategory"></a>
The subCategory of the `ManagedNotificationConfiguration`.
Type: String

## Errors
<a name="API_GetManagedNotificationConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
Unexpected error during processing of request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Request references a resource which does not exist.
 ** resourceId **
The ID of the resource that wasn't found.
HTTP Status Code: 404

 ** ThrottlingException **
Request was denied due to request throttling.
 ** quotaCode **
Identifies the quota that is being throttled.
 ** retryAfterSeconds **
The number of seconds a client should wait before retrying the request.
 ** serviceCode **
Identifies the service being throttled.
HTTP Status Code: 429

 ** ValidationException **
This exception is thrown when the notification event fails validation.
 ** fieldList **
The list of input fields that are invalid.
 ** reason **
The reason why your input is considered invalid.
HTTP Status Code: 400

## See Also
<a name="API_GetManagedNotificationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/notifications-2018-05-10/GetManagedNotificationConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/notifications-2018-05-10/GetManagedNotificationConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/notifications-2018-05-10/GetManagedNotificationConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/notifications-2018-05-10/GetManagedNotificationConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/notifications-2018-05-10/GetManagedNotificationConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/notifications-2018-05-10/GetManagedNotificationConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/notifications-2018-05-10/GetManagedNotificationConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/notifications-2018-05-10/GetManagedNotificationConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/notifications-2018-05-10/GetManagedNotificationConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/notifications-2018-05-10/GetManagedNotificationConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS User Notifications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query notifications` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
