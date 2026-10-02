---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_CreateNotification.html
---

# CreateNotification
<a name="API_CreateNotification"></a>

Creates a new notification to be delivered to specified recipients. Notifications can include localized content with links, and an optional expiration time. Recipients can be specified as individual user ARNs or instance ARNs to target all users in an instance.

## Request Syntax
<a name="API_CreateNotification_RequestSyntax"></a>

```
PUT /notifications/{{InstanceId}} HTTP/1.1
Content-type: application/json

{
   "ClientToken": "{{string}}",
   "Content": {
      "{{string}}" : "{{string}}"
   },
   "ExpiresAt": {{number}},
   "PredefinedNotificationId": "{{string}}",
   "Priority": "{{string}}",
   "Recipients": [ "{{string}}" ],
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateNotification_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_CreateNotification_RequestSyntax) **   <a name="connect-CreateNotification-request-uri-InstanceId"></a>
The identifier of the Amazon Connect instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Request Body
<a name="API_CreateNotification_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ClientToken](#API_CreateNotification_RequestSyntax) **   <a name="connect-CreateNotification-request-ClientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the AWS SDK populates this field. For more information about idempotency, see [Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/).
Type: String
Length Constraints: Maximum length of 500.
Required: No

 ** [Content](#API_CreateNotification_RequestSyntax) **   <a name="connect-CreateNotification-request-Content"></a>
The localized content of the notification. A map where keys are locale codes and values are the notification text in that locale. Content supports links. Maximum 250 characters per locale.
Type: String to string map
Valid Keys: `en_US | de_DE | es_ES | fr_FR | id_ID | it_IT | ja_JP | ko_KR | pt_BR | zh_CN | zh_TW`
Value Length Constraints: Minimum length of 0. Maximum length of 3000.
Required: Yes

 ** [ExpiresAt](#API_CreateNotification_RequestSyntax) **   <a name="connect-CreateNotification-request-ExpiresAt"></a>
The timestamp when the notification should expire and no longer be displayed to users. If not specified, defaults to one week from creation.
Type: Timestamp
Required: No

 ** [PredefinedNotificationId](#API_CreateNotification_RequestSyntax) **   <a name="connect-CreateNotification-request-PredefinedNotificationId"></a>
 *This parameter has been deprecated.*
The unique identifier for a notification.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** [Priority](#API_CreateNotification_RequestSyntax) **   <a name="connect-CreateNotification-request-Priority"></a>
The priority level of the notification. Valid values are HIGH and LOW. High priority notifications are displayed above low priority notifications.
Type: String
Valid Values: `HIGH | LOW`
Required: No

 ** [Recipients](#API_CreateNotification_RequestSyntax) **   <a name="connect-CreateNotification-request-Recipients"></a>
A list of Amazon Resource Names (ARNs) identifying the recipients of the notification. Can include user ARNs or instance ARNs to target all users in an instance. Maximum of 200 recipients.
Type: Array of strings
Array Members: Maximum number of 200 items.
Required: Yes

 ** [Tags](#API_CreateNotification_RequestSyntax) **   <a name="connect-CreateNotification-request-Tags"></a>
The tags used to organize, track, or control access for this resource. For example, `{ "Tags": {"key1":"value1", "key2":"value2"} }`.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[\p{L}\p{Z}\p{N}_.:/=+\-@]*$`
Value Length Constraints: Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateNotification_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NotificationArn": "string",
   "NotificationId": "string"
}
```

## Response Elements
<a name="API_CreateNotification_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NotificationArn](#API_CreateNotification_ResponseSyntax) **   <a name="connect-CreateNotification-response-NotificationArn"></a>
The Amazon Resource Name (ARN) of the created notification.
Type: String

 ** [NotificationId](#API_CreateNotification_ResponseSyntax) **   <a name="connect-CreateNotification-response-NotificationId"></a>
The unique identifier assigned to the created notification.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

## Errors
<a name="API_CreateNotification_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** DuplicateResourceException **
A resource with the specified name already exists.
HTTP Status Code: 409

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
<a name="API_CreateNotification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/CreateNotification)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/CreateNotification)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/CreateNotification)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/CreateNotification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/CreateNotification)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/CreateNotification)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/CreateNotification)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/CreateNotification)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/CreateNotification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/CreateNotification)
