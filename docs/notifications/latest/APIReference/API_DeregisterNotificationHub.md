---
source_url: https://docs.aws.amazon.com/notifications/latest/APIReference/API_DeregisterNotificationHub.html
---

# DeregisterNotificationHub
<a name="API_DeregisterNotificationHub"></a>

Deregisters a `NotificationHub` in the specified Region.

**Note**
You can't deregister the last `NotificationHub` in the account. `NotificationEvents` stored in the deregistered `NotificationHub` are no longer visible. Recreating a new `NotificationHub` in the same Region restores access to those `NotificationEvents`.

## Request Syntax
<a name="API_DeregisterNotificationHub_RequestSyntax"></a>

```
DELETE /notification-hubs/{{notificationHubRegion}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeregisterNotificationHub_RequestParameters"></a>

The request uses the following URI parameters.

 ** [notificationHubRegion](#API_DeregisterNotificationHub_RequestSyntax) **   <a name="Notifications-DeregisterNotificationHub-request-uri-notificationHubRegion"></a>
The `NotificationHub` Region.
Length Constraints: Minimum length of 2. Maximum length of 25.
Pattern: `([a-z]{1,4})-([a-z]{1,15}-)+([0-9])`
Required: Yes

## Request Body
<a name="API_DeregisterNotificationHub_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeregisterNotificationHub_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "notificationHubRegion": "string",
   "statusSummary": {
      "reason": "string",
      "status": "string"
   }
}
```

## Response Elements
<a name="API_DeregisterNotificationHub_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [notificationHubRegion](#API_DeregisterNotificationHub_ResponseSyntax) **   <a name="Notifications-DeregisterNotificationHub-response-notificationHubRegion"></a>
The `NotificationHub` Region.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 25.
Pattern: `([a-z]{1,4})-([a-z]{1,15}-)+([0-9])`

 ** [statusSummary](#API_DeregisterNotificationHub_ResponseSyntax) **   <a name="Notifications-DeregisterNotificationHub-response-statusSummary"></a>
 `NotificationHub` status information.
Type: [NotificationHubStatusSummary](API_NotificationHubStatusSummary.md) object

## Errors
<a name="API_DeregisterNotificationHub_Errors"></a>

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
<a name="API_DeregisterNotificationHub_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/notifications-2018-05-10/DeregisterNotificationHub)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/notifications-2018-05-10/DeregisterNotificationHub)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/notifications-2018-05-10/DeregisterNotificationHub)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/notifications-2018-05-10/DeregisterNotificationHub)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/notifications-2018-05-10/DeregisterNotificationHub)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/notifications-2018-05-10/DeregisterNotificationHub)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/notifications-2018-05-10/DeregisterNotificationHub)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/notifications-2018-05-10/DeregisterNotificationHub)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/notifications-2018-05-10/DeregisterNotificationHub)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/notifications-2018-05-10/DeregisterNotificationHub)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS User Notifications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query notifications` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
