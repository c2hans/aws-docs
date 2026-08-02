---
source_url: https://docs.aws.amazon.com/notifications/latest/APIReference/API_DeleteNotificationConfiguration.html
---

# DeleteNotificationConfiguration
<a name="API_DeleteNotificationConfiguration"></a>

Deletes a `NotificationConfiguration`.

## Request Syntax
<a name="API_DeleteNotificationConfiguration_RequestSyntax"></a>

```
DELETE /notification-configurations/{{arn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteNotificationConfiguration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [arn](#API_DeleteNotificationConfiguration_RequestSyntax) **   <a name="Notifications-DeleteNotificationConfiguration-request-uri-arn"></a>
The Amazon Resource Name (ARN) of the `NotificationConfiguration` to delete.
Pattern: `arn:[a-z-]{3,10}:notifications::[0-9]{12}:configuration/[a-z0-9]{27}`
Required: Yes

## Request Body
<a name="API_DeleteNotificationConfiguration_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteNotificationConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeleteNotificationConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteNotificationConfiguration_Errors"></a>

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
<a name="API_DeleteNotificationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/notifications-2018-05-10/DeleteNotificationConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/notifications-2018-05-10/DeleteNotificationConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/notifications-2018-05-10/DeleteNotificationConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/notifications-2018-05-10/DeleteNotificationConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/notifications-2018-05-10/DeleteNotificationConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/notifications-2018-05-10/DeleteNotificationConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/notifications-2018-05-10/DeleteNotificationConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/notifications-2018-05-10/DeleteNotificationConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/notifications-2018-05-10/DeleteNotificationConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/notifications-2018-05-10/DeleteNotificationConfiguration)
