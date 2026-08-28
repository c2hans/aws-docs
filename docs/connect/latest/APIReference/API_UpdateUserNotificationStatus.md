---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_UpdateUserNotificationStatus.html
---

# UpdateUserNotificationStatus
<a name="API_UpdateUserNotificationStatus"></a>

Updates the status of a notification for a specific user, such as marking it as read or hidden. Users can only update notification status for notifications that have been sent to them. READ status deprioritizes the notification and greys it out, while HIDDEN status removes it from the notification widget.

## Request Syntax
<a name="API_UpdateUserNotificationStatus_RequestSyntax"></a>

```
POST /users/{{InstanceId}}/{{UserId}}/notifications/{{NotificationId}} HTTP/1.1
x-amz-last-modified-time: {{LastModifiedTime}}
x-amz-last-modified-region: {{LastModifiedRegion}}
Content-type: application/json

{
   "Status": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateUserNotificationStatus_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_UpdateUserNotificationStatus_RequestSyntax) **   <a name="connect-UpdateUserNotificationStatus-request-uri-InstanceId"></a>
The identifier of the Amazon Connect instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [LastModifiedRegion](#API_UpdateUserNotificationStatus_RequestSyntax) **   <a name="connect-UpdateUserNotificationStatus-request-LastModifiedRegion"></a>
The AWS Region where the notification status was last modified. Used for cross-region replication.
Pattern: `[a-z]{2}(-[a-z]+){1,2}(-[0-9])?`

 ** [LastModifiedTime](#API_UpdateUserNotificationStatus_RequestSyntax) **   <a name="connect-UpdateUserNotificationStatus-request-LastModifiedTime"></a>
The timestamp when the notification status was last modified. Used for cross-region replication and optimistic locking.

 ** [NotificationId](#API_UpdateUserNotificationStatus_RequestSyntax) **   <a name="connect-UpdateUserNotificationStatus-request-uri-NotificationId"></a>
The unique identifier for the notification.
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** [UserId](#API_UpdateUserNotificationStatus_RequestSyntax) **   <a name="connect-UpdateUserNotificationStatus-request-uri-UserId"></a>
The identifier of the user whose notification status is being updated.
Required: Yes

## Request Body
<a name="API_UpdateUserNotificationStatus_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Status](#API_UpdateUserNotificationStatus_RequestSyntax) **   <a name="connect-UpdateUserNotificationStatus-request-Status"></a>
The new status for the notification. Valid values are READ, UNREAD, and HIDDEN.
Type: String
Valid Values: `READ | UNREAD | HIDDEN`
Required: Yes

## Response Syntax
<a name="API_UpdateUserNotificationStatus_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateUserNotificationStatus_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateUserNotificationStatus_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** InternalServiceException **
Request processing failed because of an error or failure with the service.
 ** Message **
The message.
HTTP Status Code: 500

 ** InvalidParameterException **
One or more of the specified parameters are not valid.
 ** Message **
The message about the parameters.
HTTP Status Code: 400

 ** InvalidRequestException **
The request is not valid.
 ** Message **
The message about the request.
 ** Reason **
Reason why the request was invalid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_UpdateUserNotificationStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/UpdateUserNotificationStatus)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/UpdateUserNotificationStatus)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/UpdateUserNotificationStatus)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/UpdateUserNotificationStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/UpdateUserNotificationStatus)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/UpdateUserNotificationStatus)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/UpdateUserNotificationStatus)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/UpdateUserNotificationStatus)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/UpdateUserNotificationStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/UpdateUserNotificationStatus)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
