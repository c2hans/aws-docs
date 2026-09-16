---
source_url: https://docs.aws.amazon.com/notifications/latest/APIReference/API_RegisterNotificationHub.html
---

# RegisterNotificationHub
<a name="API_RegisterNotificationHub"></a>

Registers a `NotificationHub` in the specified Region.

There is a maximum of one `NotificationHub` per Region. You can have a maximum of 3 `NotificationHub` resources at a time.

## Request Syntax
<a name="API_RegisterNotificationHub_RequestSyntax"></a>

```
POST /notification-hubs HTTP/1.1
Content-type: application/json

{
   "notificationHubRegion": "{{string}}"
}
```

## URI Request Parameters
<a name="API_RegisterNotificationHub_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_RegisterNotificationHub_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [notificationHubRegion](#API_RegisterNotificationHub_RequestSyntax) **   <a name="Notifications-RegisterNotificationHub-request-notificationHubRegion"></a>
The Region of the `NotificationHub`.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 25.
Pattern: `([a-z]{1,4})-([a-z]{1,15}-)+([0-9])`
Required: Yes

## Response Syntax
<a name="API_RegisterNotificationHub_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "creationTime": "string",
   "lastActivationTime": "string",
   "notificationHubRegion": "string",
   "statusSummary": {
      "reason": "string",
      "status": "string"
   }
}
```

## Response Elements
<a name="API_RegisterNotificationHub_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [creationTime](#API_RegisterNotificationHub_ResponseSyntax) **   <a name="Notifications-RegisterNotificationHub-response-creationTime"></a>
The date the resource was created.
Type: Timestamp

 ** [lastActivationTime](#API_RegisterNotificationHub_ResponseSyntax) **   <a name="Notifications-RegisterNotificationHub-response-lastActivationTime"></a>
The date the resource was last activated.
Type: Timestamp

 ** [notificationHubRegion](#API_RegisterNotificationHub_ResponseSyntax) **   <a name="Notifications-RegisterNotificationHub-response-notificationHubRegion"></a>
The Region of the `NotificationHub`.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 25.
Pattern: `([a-z]{1,4})-([a-z]{1,15}-)+([0-9])`

 ** [statusSummary](#API_RegisterNotificationHub_ResponseSyntax) **   <a name="Notifications-RegisterNotificationHub-response-statusSummary"></a>
Provides additional information about the current `NotificationHub` status information.
Type: [NotificationHubStatusSummary](API_NotificationHubStatusSummary.md) object

## Errors
<a name="API_RegisterNotificationHub_Errors"></a>

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
<a name="API_RegisterNotificationHub_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/notifications-2018-05-10/RegisterNotificationHub)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/notifications-2018-05-10/RegisterNotificationHub)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/notifications-2018-05-10/RegisterNotificationHub)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/notifications-2018-05-10/RegisterNotificationHub)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/notifications-2018-05-10/RegisterNotificationHub)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/notifications-2018-05-10/RegisterNotificationHub)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/notifications-2018-05-10/RegisterNotificationHub)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/notifications-2018-05-10/RegisterNotificationHub)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/notifications-2018-05-10/RegisterNotificationHub)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/notifications-2018-05-10/RegisterNotificationHub)
