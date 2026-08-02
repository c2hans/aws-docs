---
source_url: https://docs.aws.amazon.com/notifications/latest/APIReference/API_GetNotificationConfiguration.html
---

# GetNotificationConfiguration
<a name="API_GetNotificationConfiguration"></a>

Returns a specified `NotificationConfiguration`.

## Request Syntax
<a name="API_GetNotificationConfiguration_RequestSyntax"></a>

```
GET /notification-configurations/{{arn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetNotificationConfiguration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [arn](#API_GetNotificationConfiguration_RequestSyntax) **   <a name="Notifications-GetNotificationConfiguration-request-uri-arn"></a>
The Amazon Resource Name (ARN) of the `NotificationConfiguration` to return.
Pattern: `arn:[a-z-]{3,10}:notifications::[0-9]{12}:configuration/[a-z0-9]{27}`
Required: Yes

## Request Body
<a name="API_GetNotificationConfiguration_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetNotificationConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "aggregationDuration": "string",
   "arn": "string",
   "creationTime": "string",
   "description": "string",
   "name": "string",
   "status": "string",
   "subtype": "string"
}
```

## Response Elements
<a name="API_GetNotificationConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [aggregationDuration](#API_GetNotificationConfiguration_ResponseSyntax) **   <a name="Notifications-GetNotificationConfiguration-response-aggregationDuration"></a>
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

 ** [arn](#API_GetNotificationConfiguration_ResponseSyntax) **   <a name="Notifications-GetNotificationConfiguration-response-arn"></a>
The ARN of the resource.
Type: String
Pattern: `arn:[a-z-]{3,10}:notifications::[0-9]{12}:configuration/[a-z0-9]{27}`

 ** [creationTime](#API_GetNotificationConfiguration_ResponseSyntax) **   <a name="Notifications-GetNotificationConfiguration-response-creationTime"></a>
The creation time of the `NotificationConfiguration`.
Type: Timestamp

 ** [description](#API_GetNotificationConfiguration_ResponseSyntax) **   <a name="Notifications-GetNotificationConfiguration-response-description"></a>
The description of the `NotificationConfiguration`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[^\u0001-\u001F\u007F-\u009F]*`

 ** [name](#API_GetNotificationConfiguration_ResponseSyntax) **   <a name="Notifications-GetNotificationConfiguration-response-name"></a>
The name of the `NotificationConfiguration`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_\-]+`

 ** [status](#API_GetNotificationConfiguration_ResponseSyntax) **   <a name="Notifications-GetNotificationConfiguration-response-status"></a>
The status of this `NotificationConfiguration`.
Type: String
Valid Values: `ACTIVE | PARTIALLY_ACTIVE | INACTIVE | DELETING`

 ** [subtype](#API_GetNotificationConfiguration_ResponseSyntax) **   <a name="Notifications-GetNotificationConfiguration-response-subtype"></a>
The subtype of the notification configuration returned in the response.
Type: String
Valid Values: `ACCOUNT | ADMIN_MANAGED`

## Errors
<a name="API_GetNotificationConfiguration_Errors"></a>

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
<a name="API_GetNotificationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/notifications-2018-05-10/GetNotificationConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/notifications-2018-05-10/GetNotificationConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/notifications-2018-05-10/GetNotificationConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/notifications-2018-05-10/GetNotificationConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/notifications-2018-05-10/GetNotificationConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/notifications-2018-05-10/GetNotificationConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/notifications-2018-05-10/GetNotificationConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/notifications-2018-05-10/GetNotificationConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/notifications-2018-05-10/GetNotificationConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/notifications-2018-05-10/GetNotificationConfiguration)
