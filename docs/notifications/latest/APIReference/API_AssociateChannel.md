---
source_url: https://docs.aws.amazon.com/notifications/latest/APIReference/API_AssociateChannel.html
---

# AssociateChannel
<a name="API_AssociateChannel"></a>

Associates a delivery [Channel](https://docs.aws.amazon.com/notifications/latest/userguide/managing-delivery-channels.html) with a particular `NotificationConfiguration`. Supported Channels include Amazon Q Developer in chat applications, the AWS Console Mobile Application, and emails (notifications-contacts).

## Request Syntax
<a name="API_AssociateChannel_RequestSyntax"></a>

```
POST /channels/associate/{{arn}} HTTP/1.1
Content-type: application/json

{
   "notificationConfigurationArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_AssociateChannel_RequestParameters"></a>

The request uses the following URI parameters.

 ** [arn](#API_AssociateChannel_RequestSyntax) **   <a name="Notifications-AssociateChannel-request-uri-arn"></a>
The Amazon Resource Name (ARN) of the Channel to associate with the `NotificationConfiguration`.
Supported ARNs include Amazon Q Developer in chat applications, the Console Mobile Application, and notifications-contacts.
Pattern: `arn:[a-z-]{3,10}:(chatbot|consoleapp|notifications-contacts):[a-zA-Z0-9-]*:[0-9]{12}:[a-zA-Z0-9-_.@]+/[a-zA-Z0-9/_.@:-]+`
Required: Yes

## Request Body
<a name="API_AssociateChannel_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [notificationConfigurationArn](#API_AssociateChannel_RequestSyntax) **   <a name="Notifications-AssociateChannel-request-notificationConfigurationArn"></a>
The ARN of the `NotificationConfiguration` to associate with the Channel.
Type: String
Pattern: `arn:[a-z-]{3,10}:notifications::[0-9]{12}:configuration/[a-z0-9]{27}`
Required: Yes

## Response Syntax
<a name="API_AssociateChannel_ResponseSyntax"></a>

```
HTTP/1.1 201
```

## Response Elements
<a name="API_AssociateChannel_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response with an empty HTTP body.

## Errors
<a name="API_AssociateChannel_Errors"></a>

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
<a name="API_AssociateChannel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/notifications-2018-05-10/AssociateChannel)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/notifications-2018-05-10/AssociateChannel)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/notifications-2018-05-10/AssociateChannel)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/notifications-2018-05-10/AssociateChannel)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/notifications-2018-05-10/AssociateChannel)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/notifications-2018-05-10/AssociateChannel)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/notifications-2018-05-10/AssociateChannel)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/notifications-2018-05-10/AssociateChannel)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/notifications-2018-05-10/AssociateChannel)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/notifications-2018-05-10/AssociateChannel)
