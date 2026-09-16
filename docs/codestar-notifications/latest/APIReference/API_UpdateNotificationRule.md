---
source_url: https://docs.aws.amazon.com/codestar-notifications/latest/APIReference/API_UpdateNotificationRule.html
---

# UpdateNotificationRule
<a name="API_UpdateNotificationRule"></a>

Updates a notification rule for a resource. You can change the events that trigger the notification rule, the status of the rule, and the targets that receive the notifications.

**Note**
To add or remove tags for a notification rule, you must use [TagResource](API_TagResource.md) and [UntagResource](API_UntagResource.md).

## Request Syntax
<a name="API_UpdateNotificationRule_RequestSyntax"></a>

```
POST /updateNotificationRule HTTP/1.1
Content-type: application/json

{
   "Arn": "{{string}}",
   "DetailType": "{{string}}",
   "EventTypeIds": [ "{{string}}" ],
   "Name": "{{string}}",
   "Status": "{{string}}",
   "Targets": [
      {
         "TargetAddress": "{{string}}",
         "TargetType": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_UpdateNotificationRule_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateNotificationRule_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Arn](#API_UpdateNotificationRule_RequestSyntax) **   <a name="codestarnotifications-UpdateNotificationRule-request-Arn"></a>
The Amazon Resource Name (ARN) of the notification rule.
Type: String
Pattern: `^arn:aws[^:\s]*:codestar-notifications:[^:\s]+:\d{12}:notificationrule\/(.*\S)?$`
Required: Yes

 ** [DetailType](#API_UpdateNotificationRule_RequestSyntax) **   <a name="codestarnotifications-UpdateNotificationRule-request-DetailType"></a>
The level of detail to include in the notifications for this resource. BASIC will include only the contents of the event as it would appear in Amazon CloudWatch. FULL will include any supplemental information provided by AWS CodeStar Notifications and/or the service for the resource for which the notification is created.
Type: String
Valid Values: `BASIC | FULL`
Required: No

 ** [EventTypeIds](#API_UpdateNotificationRule_RequestSyntax) **   <a name="codestarnotifications-UpdateNotificationRule-request-EventTypeIds"></a>
A list of event types associated with this notification rule. For a complete list of event types and IDs, see [Notification concepts](https://docs.aws.amazon.com/codestar-notifications/latest/userguide/concepts.html#concepts-api) in the *Developer Tools Console User Guide*.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 200.
Required: No

 ** [Name](#API_UpdateNotificationRule_RequestSyntax) **   <a name="codestarnotifications-UpdateNotificationRule-request-Name"></a>
The name of the notification rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9\-_ ]+$`
Required: No

 ** [Status](#API_UpdateNotificationRule_RequestSyntax) **   <a name="codestarnotifications-UpdateNotificationRule-request-Status"></a>
The status of the notification rule. Valid statuses include enabled (sending notifications) or disabled (not sending notifications).
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** [Targets](#API_UpdateNotificationRule_RequestSyntax) **   <a name="codestarnotifications-UpdateNotificationRule-request-Targets"></a>
The address and type of the targets to receive notifications from this notification rule.
Type: Array of [Target](API_Target.md) objects
Array Members: Maximum number of 10 items.
Required: No

## Response Syntax
<a name="API_UpdateNotificationRule_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateNotificationRule_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateNotificationRule_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConfigurationException **
Some or all of the configuration is incomplete, missing, or not valid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
 AWS CodeStar Notifications can't find a resource that matches the provided ARN.
HTTP Status Code: 404

 ** ValidationException **
One or more parameter values are not valid.
HTTP Status Code: 400

## See Also
<a name="API_UpdateNotificationRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codestar-notifications-2019-10-15/UpdateNotificationRule)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codestar-notifications-2019-10-15/UpdateNotificationRule)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codestar-notifications-2019-10-15/UpdateNotificationRule)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codestar-notifications-2019-10-15/UpdateNotificationRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codestar-notifications-2019-10-15/UpdateNotificationRule)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codestar-notifications-2019-10-15/UpdateNotificationRule)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codestar-notifications-2019-10-15/UpdateNotificationRule)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codestar-notifications-2019-10-15/UpdateNotificationRule)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/codestar-notifications-2019-10-15/UpdateNotificationRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codestar-notifications-2019-10-15/UpdateNotificationRule)
