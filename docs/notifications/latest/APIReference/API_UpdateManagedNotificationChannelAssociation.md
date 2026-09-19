---
source_url: https://docs.aws.amazon.com/notifications/latest/APIReference/API_UpdateManagedNotificationChannelAssociation.html
---

# UpdateManagedNotificationChannelAssociation
<a name="API_UpdateManagedNotificationChannelAssociation"></a>

Updates the `isSensitiveEventsSubscribed` property of a particular ManagedNotification channel association.

## Request Syntax
<a name="API_UpdateManagedNotificationChannelAssociation_RequestSyntax"></a>

```
PUT /channels/update-managed-notification-channel-association HTTP/1.1
Content-type: application/json

{
   "channelIdentifier": "{{string}}",
   "isSensitiveEventsSubscribed": {{boolean}},
   "managedNotificationConfigurationArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateManagedNotificationChannelAssociation_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateManagedNotificationChannelAssociation_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [channelIdentifier](#API_UpdateManagedNotificationChannelAssociation_RequestSyntax) **   <a name="Notifications-UpdateManagedNotificationChannelAssociation-request-channelIdentifier"></a>
The identifier of the channel association to update. You can specify one of the following:
+ An Account contact identifier.
+ A Channel ARN.
Type: String
Pattern: `(ACCOUNT_PRIMARY|ACCOUNT_ALTERNATE_BILLING|ACCOUNT_ALTERNATE_OPERATIONS|ACCOUNT_ALTERNATE_SECURITY|arn:[a-z-]{3,10}:(chatbot|consoleapp|notifications-contacts):[a-zA-Z0-9-]*:[0-9]{12}:[a-zA-Z0-9-_.@]+/[a-zA-Z0-9/_.@:-]+)`
Required: Yes

 ** [isSensitiveEventsSubscribed](#API_UpdateManagedNotificationChannelAssociation_RequestSyntax) **   <a name="Notifications-UpdateManagedNotificationChannelAssociation-request-isSensitiveEventsSubscribed"></a>
Specifies whether the association is subscribed to sensitive events. The `notifications:SubscribeSensitiveEvents` permission controls access to sensitive events.
Type: Boolean
Required: No

 ** [managedNotificationConfigurationArn](#API_UpdateManagedNotificationChannelAssociation_RequestSyntax) **   <a name="Notifications-UpdateManagedNotificationChannelAssociation-request-managedNotificationConfigurationArn"></a>
The Amazon Resource Name (ARN) of the `ManagedNotificationConfiguration` whose Channel association property you want to update.
Type: String
Pattern: `arn:[a-z-]{3,10}:notifications::[0-9]{12}:managed-notification-configuration/category/[a-zA-Z0-9\-]{3,64}/sub-category/[a-zA-Z0-9\-]{3,64}`
Required: Yes

## Response Syntax
<a name="API_UpdateManagedNotificationChannelAssociation_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateManagedNotificationChannelAssociation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateManagedNotificationChannelAssociation_Errors"></a>

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
<a name="API_UpdateManagedNotificationChannelAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/notifications-2018-05-10/UpdateManagedNotificationChannelAssociation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/notifications-2018-05-10/UpdateManagedNotificationChannelAssociation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/notifications-2018-05-10/UpdateManagedNotificationChannelAssociation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/notifications-2018-05-10/UpdateManagedNotificationChannelAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/notifications-2018-05-10/UpdateManagedNotificationChannelAssociation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/notifications-2018-05-10/UpdateManagedNotificationChannelAssociation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/notifications-2018-05-10/UpdateManagedNotificationChannelAssociation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/notifications-2018-05-10/UpdateManagedNotificationChannelAssociation)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/notifications-2018-05-10/UpdateManagedNotificationChannelAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/notifications-2018-05-10/UpdateManagedNotificationChannelAssociation)
