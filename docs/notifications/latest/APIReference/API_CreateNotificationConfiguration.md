---
source_url: https://docs.aws.amazon.com/notifications/latest/APIReference/API_CreateNotificationConfiguration.html
---

# CreateNotificationConfiguration
<a name="API_CreateNotificationConfiguration"></a>

Creates a new `NotificationConfiguration`.

## Request Syntax
<a name="API_CreateNotificationConfiguration_RequestSyntax"></a>

```
POST /notification-configurations HTTP/1.1
Content-type: application/json

{
   "aggregationDuration": "{{string}}",
   "description": "{{string}}",
   "name": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateNotificationConfiguration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateNotificationConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [aggregationDuration](#API_CreateNotificationConfiguration_RequestSyntax) **   <a name="Notifications-CreateNotificationConfiguration-request-aggregationDuration"></a>
The aggregation preference of the `NotificationConfiguration`.
+ Values:
  +  `LONG`
    + Aggregate notifications for long periods of time (12 hours).
  +  `SHORT`
    + Aggregate notifications for short periods of time (5 minutes).
  +  `NONE`
    + Don't aggregate notifications.
Type: String
Valid Values: `LONG | SHORT | NONE`
Required: No

 ** [description](#API_CreateNotificationConfiguration_RequestSyntax) **   <a name="Notifications-CreateNotificationConfiguration-request-description"></a>
The description of the `NotificationConfiguration`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[^\u0001-\u001F\u007F-\u009F]*`
Required: Yes

 ** [name](#API_CreateNotificationConfiguration_RequestSyntax) **   <a name="Notifications-CreateNotificationConfiguration-request-name"></a>
The name of the `NotificationConfiguration`. Supports RFC 3986's unreserved characters.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_\-]+`
Required: Yes

 ** [tags](#API_CreateNotificationConfiguration_RequestSyntax) **   <a name="Notifications-CreateNotificationConfiguration-request-tags"></a>
A map of tags assigned to a resource. A tag is a string-to-string map of key-value pairs.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Pattern: `(?!aws:).{1,128}`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateNotificationConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "arn": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_CreateNotificationConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_CreateNotificationConfiguration_ResponseSyntax) **   <a name="Notifications-CreateNotificationConfiguration-response-arn"></a>
The Amazon Resource Name (ARN) of the `NotificationConfiguration`.
Type: String
Pattern: `arn:[a-z-]{3,10}:notifications::[0-9]{12}:configuration/[a-z0-9]{27}`

 ** [status](#API_CreateNotificationConfiguration_ResponseSyntax) **   <a name="Notifications-CreateNotificationConfiguration-response-status"></a>
The current status of this `NotificationConfiguration`.
Type: String
Valid Values: `ACTIVE | PARTIALLY_ACTIVE | INACTIVE | DELETING`

## Errors
<a name="API_CreateNotificationConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
Updating or deleting a resource can cause an inconsistent state.
 ** resourceId **
The resource ID that prompted the conflict error.
HTTP Status Code: 409

 ** InternalServerException **
Unexpected error during processing of request.
HTTP Status Code: 500

 ** ServiceQuotaExceededException **
Request would cause a service quota to be exceeded.
 ** quotaCode **
The code for the service quota in [Service Quotas](https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html).
 ** resourceId **
The ID of the resource that exceeds the service quota.
 ** resourceType **
The type of the resource that exceeds the service quota.
 ** serviceCode **
The code for the service quota exceeded in [Service Quotas](https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html).
HTTP Status Code: 402

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
<a name="API_CreateNotificationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/notifications-2018-05-10/CreateNotificationConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/notifications-2018-05-10/CreateNotificationConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/notifications-2018-05-10/CreateNotificationConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/notifications-2018-05-10/CreateNotificationConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/notifications-2018-05-10/CreateNotificationConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/notifications-2018-05-10/CreateNotificationConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/notifications-2018-05-10/CreateNotificationConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/notifications-2018-05-10/CreateNotificationConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/notifications-2018-05-10/CreateNotificationConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/notifications-2018-05-10/CreateNotificationConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS User Notifications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query notifications` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
