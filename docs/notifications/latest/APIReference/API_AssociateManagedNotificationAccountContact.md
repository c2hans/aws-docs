---
source_url: https://docs.aws.amazon.com/notifications/latest/APIReference/API_AssociateManagedNotificationAccountContact.html
---

# AssociateManagedNotificationAccountContact
<a name="API_AssociateManagedNotificationAccountContact"></a>

Associates an Account Contact with a particular `ManagedNotificationConfiguration`.

## Request Syntax
<a name="API_AssociateManagedNotificationAccountContact_RequestSyntax"></a>

```
PUT /contacts/associate-managed-notification/{{contactIdentifier}} HTTP/1.1
Content-type: application/json

{
   "isSensitiveEventsSubscribed": {{boolean}},
   "managedNotificationConfigurationArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_AssociateManagedNotificationAccountContact_RequestParameters"></a>

The request uses the following URI parameters.

 ** [contactIdentifier](#API_AssociateManagedNotificationAccountContact_RequestSyntax) **   <a name="Notifications-AssociateManagedNotificationAccountContact-request-uri-contactIdentifier"></a>
A unique value of an Account Contact Type to associate with the `ManagedNotificationConfiguration`.
Valid Values: `ACCOUNT_PRIMARY | ACCOUNT_ALTERNATE_BILLING | ACCOUNT_ALTERNATE_OPERATIONS | ACCOUNT_ALTERNATE_SECURITY`
Required: Yes

## Request Body
<a name="API_AssociateManagedNotificationAccountContact_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [isSensitiveEventsSubscribed](#API_AssociateManagedNotificationAccountContact_RequestSyntax) **   <a name="Notifications-AssociateManagedNotificationAccountContact-request-isSensitiveEventsSubscribed"></a>
Specifies whether this contact is subscribed to sensitive events. The `notifications:SubscribeSensitiveEvents` permission controls access to sensitive events. Defaults to false.
Type: Boolean
Required: No

 ** [managedNotificationConfigurationArn](#API_AssociateManagedNotificationAccountContact_RequestSyntax) **   <a name="Notifications-AssociateManagedNotificationAccountContact-request-managedNotificationConfigurationArn"></a>
The Amazon Resource Name (ARN) of the `ManagedNotificationConfiguration` to associate with the Account Contact.
Type: String
Pattern: `arn:[a-z-]{3,10}:notifications::[0-9]{12}:managed-notification-configuration/category/[a-zA-Z0-9\-]{3,64}/sub-category/[a-zA-Z0-9\-]{3,64}`
Required: Yes

## Response Syntax
<a name="API_AssociateManagedNotificationAccountContact_ResponseSyntax"></a>

```
HTTP/1.1 201
```

## Response Elements
<a name="API_AssociateManagedNotificationAccountContact_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response with an empty HTTP body.

## Errors
<a name="API_AssociateManagedNotificationAccountContact_Errors"></a>

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
<a name="API_AssociateManagedNotificationAccountContact_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/notifications-2018-05-10/AssociateManagedNotificationAccountContact)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/notifications-2018-05-10/AssociateManagedNotificationAccountContact)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/notifications-2018-05-10/AssociateManagedNotificationAccountContact)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/notifications-2018-05-10/AssociateManagedNotificationAccountContact)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/notifications-2018-05-10/AssociateManagedNotificationAccountContact)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/notifications-2018-05-10/AssociateManagedNotificationAccountContact)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/notifications-2018-05-10/AssociateManagedNotificationAccountContact)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/notifications-2018-05-10/AssociateManagedNotificationAccountContact)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/notifications-2018-05-10/AssociateManagedNotificationAccountContact)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/notifications-2018-05-10/AssociateManagedNotificationAccountContact)
