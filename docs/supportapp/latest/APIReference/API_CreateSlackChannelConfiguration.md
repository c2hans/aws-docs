---
source_url: https://docs.aws.amazon.com/supportapp/latest/APIReference/API_CreateSlackChannelConfiguration.html
---

# CreateSlackChannelConfiguration
<a name="API_CreateSlackChannelConfiguration"></a>

Creates a Slack channel configuration for your AWS account.

**Note**
You can add up to 5 Slack workspaces for your account.
You can add up to 20 Slack channels for your account.

A Slack channel can have up to 100 AWS accounts. This means that only 100 accounts can add the same Slack channel to the Support App. We recommend that you only add the accounts that you need to manage support cases for your organization. This can reduce the notifications about case updates that you receive in the Slack channel.

**Note**
We recommend that you choose a private Slack channel so that only members in that channel have read and write access to your support cases. Anyone in your Slack channel can create, update, or resolve support cases for your account. Users require an invitation to join private channels.

## Request Syntax
<a name="API_CreateSlackChannelConfiguration_RequestSyntax"></a>

```
POST /control/create-slack-channel-configuration HTTP/1.1
Content-type: application/json

{
   "channelId": "{{string}}",
   "channelName": "{{string}}",
   "channelRoleArn": "{{string}}",
   "notifyOnAddCorrespondenceToCase": {{boolean}},
   "notifyOnCaseSeverity": "{{string}}",
   "notifyOnCreateOrReopenCase": {{boolean}},
   "notifyOnResolveCase": {{boolean}},
   "teamId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateSlackChannelConfiguration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateSlackChannelConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [channelId](#API_CreateSlackChannelConfiguration_RequestSyntax) **   <a name="supportapp-CreateSlackChannelConfiguration-request-channelId"></a>
The channel ID in Slack. This ID identifies a channel within a Slack workspace.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `\S+`
Required: Yes

 ** [channelName](#API_CreateSlackChannelConfiguration_RequestSyntax) **   <a name="supportapp-CreateSlackChannelConfiguration-request-channelName"></a>
The name of the Slack channel that you configure for the Support App.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `.+`
Required: No

 ** [channelRoleArn](#API_CreateSlackChannelConfiguration_RequestSyntax) **   <a name="supportapp-CreateSlackChannelConfiguration-request-channelRoleArn"></a>
The Amazon Resource Name (ARN) of an IAM role that you want to use to perform operations on AWS services. For more information, see [Managing access to the Support App](https://docs.aws.amazon.com/awssupport/latest/user/support-app-permissions.html) in the * AWS Support User Guide*.
Type: String
Length Constraints: Minimum length of 31. Maximum length of 2048.
Pattern: `arn:aws:iam::[0-9]{12}:role/(.+)`
Required: Yes

 ** [notifyOnAddCorrespondenceToCase](#API_CreateSlackChannelConfiguration_RequestSyntax) **   <a name="supportapp-CreateSlackChannelConfiguration-request-notifyOnAddCorrespondenceToCase"></a>
Whether you want to get notified when a support case has a new correspondence.
Type: Boolean
Required: No

 ** [notifyOnCaseSeverity](#API_CreateSlackChannelConfiguration_RequestSyntax) **   <a name="supportapp-CreateSlackChannelConfiguration-request-notifyOnCaseSeverity"></a>
The case severity for a support case that you want to receive notifications.
If you specify `high` or `all`, you must specify `true` for at least one of the following parameters:
+  `notifyOnAddCorrespondenceToCase`
+  `notifyOnCreateOrReopenCase`
+  `notifyOnResolveCase`
If you specify `none`, the following parameters must be null or `false`:
+  `notifyOnAddCorrespondenceToCase`
+  `notifyOnCreateOrReopenCase`
+  `notifyOnResolveCase`
If you don't specify these parameters in your request, they default to `false`.
Type: String
Valid Values: `none | all | high`
Required: Yes

 ** [notifyOnCreateOrReopenCase](#API_CreateSlackChannelConfiguration_RequestSyntax) **   <a name="supportapp-CreateSlackChannelConfiguration-request-notifyOnCreateOrReopenCase"></a>
Whether you want to get notified when a support case is created or reopened.
Type: Boolean
Required: No

 ** [notifyOnResolveCase](#API_CreateSlackChannelConfiguration_RequestSyntax) **   <a name="supportapp-CreateSlackChannelConfiguration-request-notifyOnResolveCase"></a>
Whether you want to get notified when a support case is resolved.
Type: Boolean
Required: No

 ** [teamId](#API_CreateSlackChannelConfiguration_RequestSyntax) **   <a name="supportapp-CreateSlackChannelConfiguration-request-teamId"></a>
The team ID in Slack. This ID uniquely identifies a Slack workspace, such as `T012ABCDEFG`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `\S+`
Required: Yes

## Response Syntax
<a name="API_CreateSlackChannelConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_CreateSlackChannelConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_CreateSlackChannelConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient permission to perform this action.
HTTP Status Code: 403

 ** ConflictException **
Your request has a conflict. For example, you might receive this error if you try the following:
+ Add, update, or delete a Slack channel configuration before you add a Slack workspace to your AWS account.
+ Add a Slack channel configuration that already exists in your AWS account.
+ Delete a Slack channel configuration for a live chat channel.
+ Delete a Slack workspace from your AWS account that has an active live chat channel.
+ Call the `RegisterSlackWorkspaceForOrganization` API from an AWS account that doesn't belong to an organization.
+ Call the `RegisterSlackWorkspaceForOrganization` API from a member account, but the management account hasn't registered that workspace yet for the organization.
HTTP Status Code: 409

 ** InternalServerException **
We can’t process your request right now because of a server issue. Try again later.
HTTP Status Code: 500

 ** ServiceQuotaExceededException **
Your Service Quotas request exceeds the quota for the service. For example, your Service Quotas request to Support App might exceed the maximum number of workspaces or channels per account, or the maximum number of accounts per Slack channel.
HTTP Status Code: 402

 ** ValidationException **
Your request input doesn't meet the constraints that the Support App specifies.
HTTP Status Code: 400

## See Also
<a name="API_CreateSlackChannelConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/support-app-2021-08-20/CreateSlackChannelConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/support-app-2021-08-20/CreateSlackChannelConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/support-app-2021-08-20/CreateSlackChannelConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/support-app-2021-08-20/CreateSlackChannelConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/support-app-2021-08-20/CreateSlackChannelConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/support-app-2021-08-20/CreateSlackChannelConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/support-app-2021-08-20/CreateSlackChannelConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/support-app-2021-08-20/CreateSlackChannelConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/support-app-2021-08-20/CreateSlackChannelConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/support-app-2021-08-20/CreateSlackChannelConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Support App in Slack. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query supportapp` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
