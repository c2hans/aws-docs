---
source_url: https://docs.aws.amazon.com/codestar-notifications/latest/APIReference/API_DeleteTarget.html
---

# DeleteTarget
<a name="API_DeleteTarget"></a>

Deletes a specified target for notifications.

## Request Syntax
<a name="API_DeleteTarget_RequestSyntax"></a>

```
POST /deleteTarget HTTP/1.1
Content-type: application/json

{
   "ForceUnsubscribeAll": {{boolean}},
   "TargetAddress": "{{string}}"
}
```

## URI Request Parameters
<a name="API_DeleteTarget_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DeleteTarget_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ForceUnsubscribeAll](#API_DeleteTarget_RequestSyntax) **   <a name="codestarnotifications-DeleteTarget-request-ForceUnsubscribeAll"></a>
A Boolean value that can be used to delete all associations with this Amazon Q Developer in chat applications topic. The default value is FALSE. If set to TRUE, all associations between that target and every notification rule in your AWS account are deleted.
Type: Boolean
Required: No

 ** [TargetAddress](#API_DeleteTarget_RequestSyntax) **   <a name="codestarnotifications-DeleteTarget-request-TargetAddress"></a>
The Amazon Resource Name (ARN) of the Amazon Q Developer in chat applications topic or Amazon Q Developer in chat applications client to delete.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 320.
Required: Yes

## Response Syntax
<a name="API_DeleteTarget_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeleteTarget_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteTarget_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ValidationException **
One or more parameter values are not valid.
HTTP Status Code: 400

## See Also
<a name="API_DeleteTarget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codestar-notifications-2019-10-15/DeleteTarget)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codestar-notifications-2019-10-15/DeleteTarget)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codestar-notifications-2019-10-15/DeleteTarget)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codestar-notifications-2019-10-15/DeleteTarget)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codestar-notifications-2019-10-15/DeleteTarget)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codestar-notifications-2019-10-15/DeleteTarget)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codestar-notifications-2019-10-15/DeleteTarget)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codestar-notifications-2019-10-15/DeleteTarget)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codestar-notifications-2019-10-15/DeleteTarget)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codestar-notifications-2019-10-15/DeleteTarget)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeStar Notifications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codestar-notifications` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
