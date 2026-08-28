---
source_url: https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_RemovePermission.html
---

# RemovePermission
<a name="API_RemovePermission"></a>

Revokes the permission of another AWS account to be able to put events to the specified event bus. Specify the account to revoke by the `StatementId` value that you associated with the account when you granted it permission with `PutPermission`. You can find the `StatementId` by using [DescribeEventBus](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_DescribeEventBus.html).

## Request Syntax
<a name="API_RemovePermission_RequestSyntax"></a>

```
{
   "EventBusName": "{{string}}",
   "RemoveAllPermissions": {{boolean}},
   "StatementId": "{{string}}"
}
```

## Request Parameters
<a name="API_RemovePermission_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [EventBusName](#API_RemovePermission_RequestSyntax) **   <a name="eventbridge-RemovePermission-request-EventBusName"></a>
The name of the event bus to revoke permissions for. If you omit this, the default event bus is used.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\.\-_A-Za-z0-9]+`
Required: No

 ** [RemoveAllPermissions](#API_RemovePermission_RequestSyntax) **   <a name="eventbridge-RemovePermission-request-RemoveAllPermissions"></a>
Specifies whether to remove all permissions.
Type: Boolean
Required: No

 ** [StatementId](#API_RemovePermission_RequestSyntax) **   <a name="eventbridge-RemovePermission-request-StatementId"></a>
The statement ID corresponding to the account that is no longer allowed to put events to the default event bus.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9-_]+`
Required: No

## Response Elements
<a name="API_RemovePermission_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_RemovePermission_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConcurrentModificationException **
There is concurrent modification on a rule, target, archive, or replay.
HTTP Status Code: 400

 ** InternalException **
This exception occurs due to unexpected causes.
HTTP Status Code: 500

 ** OperationDisabledException **
The operation you are attempting is not available in this region.
HTTP Status Code: 400

 ** ResourceNotFoundException **
An entity that you specified does not exist.
HTTP Status Code: 400

## See Also
<a name="API_RemovePermission_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/eventbridge-2015-10-07/RemovePermission)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/eventbridge-2015-10-07/RemovePermission)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridge-2015-10-07/RemovePermission)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/eventbridge-2015-10-07/RemovePermission)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridge-2015-10-07/RemovePermission)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/eventbridge-2015-10-07/RemovePermission)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/eventbridge-2015-10-07/RemovePermission)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/eventbridge-2015-10-07/RemovePermission)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/eventbridge-2015-10-07/RemovePermission)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridge-2015-10-07/RemovePermission)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EventBridge. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eventbridge` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
