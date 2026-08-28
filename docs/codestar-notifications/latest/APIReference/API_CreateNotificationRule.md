---
source_url: https://docs.aws.amazon.com/codestar-notifications/latest/APIReference/API_CreateNotificationRule.html
---

# CreateNotificationRule
<a name="API_CreateNotificationRule"></a>

Creates a notification rule for a resource. The rule specifies the events you want notifications about and the targets (such as Amazon Q Developer in chat applications topics or Amazon Q Developer in chat applications clients configured for Slack) where you want to receive them.

## Request Syntax
<a name="API_CreateNotificationRule_RequestSyntax"></a>

```
POST /createNotificationRule HTTP/1.1
Content-type: application/json

{
   "ClientRequestToken": "{{string}}",
   "DetailType": "{{string}}",
   "EventTypeIds": [ "{{string}}" ],
   "Name": "{{string}}",
   "Resource": "{{string}}",
   "Status": "{{string}}",
   "Tags": {
      "{{string}}" : "{{string}}"
   },
   "Targets": [
      {
         "TargetAddress": "{{string}}",
         "TargetType": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_CreateNotificationRule_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateNotificationRule_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ClientRequestToken](#API_CreateNotificationRule_RequestSyntax) **   <a name="codestarnotifications-CreateNotificationRule-request-ClientRequestToken"></a>
A unique, client-generated idempotency token that, when provided in a request, ensures the request cannot be repeated with a changed parameter. If a request with the same parameters is received and a token is included, the request returns information about the initial request that used that token.
The AWS SDKs prepopulate client request tokens. If you are using an AWS SDK, an idempotency token is created for you.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^[\w:/-]+$`
Required: No

 ** [DetailType](#API_CreateNotificationRule_RequestSyntax) **   <a name="codestarnotifications-CreateNotificationRule-request-DetailType"></a>
The level of detail to include in the notifications for this resource. `BASIC` will include only the contents of the event as it would appear in Amazon CloudWatch. `FULL` will include any supplemental information provided by AWS CodeStar Notifications and/or the service for the resource for which the notification is created.
Type: String
Valid Values: `BASIC | FULL`
Required: Yes

 ** [EventTypeIds](#API_CreateNotificationRule_RequestSyntax) **   <a name="codestarnotifications-CreateNotificationRule-request-EventTypeIds"></a>
A list of event types associated with this notification rule. For a list of allowed events, see [EventTypeSummary](API_EventTypeSummary.md).
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 200.
Required: Yes

 ** [Name](#API_CreateNotificationRule_RequestSyntax) **   <a name="codestarnotifications-CreateNotificationRule-request-Name"></a>
The name for the notification rule. Notification rule names must be unique in your AWS account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9\-_ ]+$`
Required: Yes

 ** [Resource](#API_CreateNotificationRule_RequestSyntax) **   <a name="codestarnotifications-CreateNotificationRule-request-Resource"></a>
The Amazon Resource Name (ARN) of the resource to associate with the notification rule. Supported resources include pipelines in AWS CodePipeline, repositories in AWS CodeCommit, and build projects in AWS CodeBuild.
Type: String
Pattern: `^arn:aws[^:\s]*:[^:\s]*:[^:\s]*:[0-9]{12}:[^\s]+$`
Required: Yes

 ** [Status](#API_CreateNotificationRule_RequestSyntax) **   <a name="codestarnotifications-CreateNotificationRule-request-Status"></a>
The status of the notification rule. The default value is `ENABLED`. If the status is set to `DISABLED`, notifications aren't sent for the notification rule.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** [Tags](#API_CreateNotificationRule_RequestSyntax) **   <a name="codestarnotifications-CreateNotificationRule-request-Tags"></a>
A list of tags to apply to this notification rule. Key names cannot start with "`aws`".
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Value Length Constraints: Maximum length of 256.
Value Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

 ** [Targets](#API_CreateNotificationRule_RequestSyntax) **   <a name="codestarnotifications-CreateNotificationRule-request-Targets"></a>
A list of Amazon Resource Names (ARNs) of Amazon Simple Notification Service topics and Amazon Q Developer in chat applications clients to associate with the notification rule.
Type: Array of [Target](API_Target.md) objects
Array Members: Maximum number of 10 items.
Required: Yes

## Response Syntax
<a name="API_CreateNotificationRule_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Arn": "string"
}
```

## Response Elements
<a name="API_CreateNotificationRule_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_CreateNotificationRule_ResponseSyntax) **   <a name="codestarnotifications-CreateNotificationRule-response-Arn"></a>
The Amazon Resource Name (ARN) of the notification rule.
Type: String
Pattern: `^arn:aws[^:\s]*:codestar-notifications:[^:\s]+:\d{12}:notificationrule\/(.*\S)?$`

## Errors
<a name="API_CreateNotificationRule_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
 AWS CodeStar Notifications can't create the notification rule because you do not have sufficient permissions.
HTTP Status Code: 403

 ** ConcurrentModificationException **
 AWS CodeStar Notifications can't complete the request because the resource is being modified by another process. Wait a few minutes and try again.
HTTP Status Code: 400

 ** ConfigurationException **
Some or all of the configuration is incomplete, missing, or not valid.
HTTP Status Code: 400

 ** LimitExceededException **
One of the AWS CodeStar Notifications limits has been exceeded. Limits apply to accounts, notification rules, notifications, resources, and targets. For more information, see Limits.
HTTP Status Code: 400

 ** ResourceAlreadyExistsException **
A resource with the same name or ID already exists. Notification rule names must be unique in your AWS account.
HTTP Status Code: 409

 ** ValidationException **
One or more parameter values are not valid.
HTTP Status Code: 400

## See Also
<a name="API_CreateNotificationRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codestar-notifications-2019-10-15/CreateNotificationRule)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codestar-notifications-2019-10-15/CreateNotificationRule)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codestar-notifications-2019-10-15/CreateNotificationRule)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codestar-notifications-2019-10-15/CreateNotificationRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codestar-notifications-2019-10-15/CreateNotificationRule)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codestar-notifications-2019-10-15/CreateNotificationRule)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codestar-notifications-2019-10-15/CreateNotificationRule)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codestar-notifications-2019-10-15/CreateNotificationRule)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codestar-notifications-2019-10-15/CreateNotificationRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codestar-notifications-2019-10-15/CreateNotificationRule)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeStar Notifications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codestar-notifications` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
