---
source_url: https://docs.aws.amazon.com/codestar-notifications/latest/APIReference/API_DeleteNotificationRule.html
---

# DeleteNotificationRule
<a name="API_DeleteNotificationRule"></a>

Deletes a notification rule for a resource.

## Request Syntax
<a name="API_DeleteNotificationRule_RequestSyntax"></a>

```
POST /deleteNotificationRule HTTP/1.1
Content-type: application/json

{
   "Arn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_DeleteNotificationRule_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DeleteNotificationRule_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Arn](#API_DeleteNotificationRule_RequestSyntax) **   <a name="codestarnotifications-DeleteNotificationRule-request-Arn"></a>
The Amazon Resource Name (ARN) of the notification rule you want to delete.
Type: String
Pattern: `^arn:aws[^:\s]*:codestar-notifications:[^:\s]+:\d{12}:notificationrule\/(.*\S)?$`
Required: Yes

## Response Syntax
<a name="API_DeleteNotificationRule_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Arn": "string"
}
```

## Response Elements
<a name="API_DeleteNotificationRule_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_DeleteNotificationRule_ResponseSyntax) **   <a name="codestarnotifications-DeleteNotificationRule-response-Arn"></a>
The Amazon Resource Name (ARN) of the deleted notification rule.
Type: String
Pattern: `^arn:aws[^:\s]*:codestar-notifications:[^:\s]+:\d{12}:notificationrule\/(.*\S)?$`

## Errors
<a name="API_DeleteNotificationRule_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConcurrentModificationException **
 AWS CodeStar Notifications can't complete the request because the resource is being modified by another process. Wait a few minutes and try again.
HTTP Status Code: 400

 ** LimitExceededException **
One of the AWS CodeStar Notifications limits has been exceeded. Limits apply to accounts, notification rules, notifications, resources, and targets. For more information, see Limits.
HTTP Status Code: 400

 ** ValidationException **
One or more parameter values are not valid.
HTTP Status Code: 400

## See Also
<a name="API_DeleteNotificationRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codestar-notifications-2019-10-15/DeleteNotificationRule)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codestar-notifications-2019-10-15/DeleteNotificationRule)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codestar-notifications-2019-10-15/DeleteNotificationRule)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codestar-notifications-2019-10-15/DeleteNotificationRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codestar-notifications-2019-10-15/DeleteNotificationRule)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codestar-notifications-2019-10-15/DeleteNotificationRule)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codestar-notifications-2019-10-15/DeleteNotificationRule)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codestar-notifications-2019-10-15/DeleteNotificationRule)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codestar-notifications-2019-10-15/DeleteNotificationRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codestar-notifications-2019-10-15/DeleteNotificationRule)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeStar Notifications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codestar-notifications` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
