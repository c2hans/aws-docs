---
source_url: https://docs.aws.amazon.com/notifications/latest/APIReference/API_UpdateNotificationConfiguration.html
---

# UpdateNotificationConfiguration
<a name="API_UpdateNotificationConfiguration"></a>

Updates a `NotificationConfiguration`.

## Request Syntax
<a name="API_UpdateNotificationConfiguration_RequestSyntax"></a>

```
PUT /notification-configurations/{{arn}} HTTP/1.1
Content-type: application/json

{
   "aggregationDuration": "{{string}}",
   "description": "{{string}}",
   "name": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateNotificationConfiguration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [arn](#API_UpdateNotificationConfiguration_RequestSyntax) **   <a name="Notifications-UpdateNotificationConfiguration-request-uri-arn"></a>
The Amazon Resource Name (ARN) used to update the `NotificationConfiguration`.
Pattern: `arn:[a-z-]{3,10}:notifications::[0-9]{12}:configuration/[a-z0-9]{27}`
Required: Yes

## Request Body
<a name="API_UpdateNotificationConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [aggregationDuration](#API_UpdateNotificationConfiguration_RequestSyntax) **   <a name="Notifications-UpdateNotificationConfiguration-request-aggregationDuration"></a>
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

 ** [description](#API_UpdateNotificationConfiguration_RequestSyntax) **   <a name="Notifications-UpdateNotificationConfiguration-request-description"></a>
The description of the `NotificationConfiguration`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[^\u0001-\u001F\u007F-\u009F]*`
Required: No

 ** [name](#API_UpdateNotificationConfiguration_RequestSyntax) **   <a name="Notifications-UpdateNotificationConfiguration-request-name"></a>
The name of the `NotificationConfiguration`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_\-]+`
Required: No

## Response Syntax
<a name="API_UpdateNotificationConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "arn": "string"
}
```

## Response Elements
<a name="API_UpdateNotificationConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_UpdateNotificationConfiguration_ResponseSyntax) **   <a name="Notifications-UpdateNotificationConfiguration-response-arn"></a>
The ARN used to update the `NotificationConfiguration`.
Type: String
Pattern: `arn:[a-z-]{3,10}:notifications::[0-9]{12}:configuration/[a-z0-9]{27}`

## Errors
<a name="API_UpdateNotificationConfiguration_Errors"></a>

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
<a name="API_UpdateNotificationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/notifications-2018-05-10/UpdateNotificationConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/notifications-2018-05-10/UpdateNotificationConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/notifications-2018-05-10/UpdateNotificationConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/notifications-2018-05-10/UpdateNotificationConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/notifications-2018-05-10/UpdateNotificationConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/notifications-2018-05-10/UpdateNotificationConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/notifications-2018-05-10/UpdateNotificationConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/notifications-2018-05-10/UpdateNotificationConfiguration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/notifications-2018-05-10/UpdateNotificationConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/notifications-2018-05-10/UpdateNotificationConfiguration)
