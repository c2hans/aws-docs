---
source_url: https://docs.aws.amazon.com/supportapp/latest/APIReference/API_UpdateSlackChannelConfiguration.html
---

# UpdateSlackChannelConfiguration
<a name="API_UpdateSlackChannelConfiguration"></a>

Updates the configuration for a Slack channel, such as case update notifications.

## Request Syntax
<a name="API_UpdateSlackChannelConfiguration_RequestSyntax"></a>

```
POST /control/update-slack-channel-configuration HTTP/1.1
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
<a name="API_UpdateSlackChannelConfiguration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateSlackChannelConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [channelId](#API_UpdateSlackChannelConfiguration_RequestSyntax) **   <a name="supportapp-UpdateSlackChannelConfiguration-request-channelId"></a>
The channel ID in Slack. This ID identifies a channel within a Slack workspace.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `\S+`
Required: Yes

 ** [channelName](#API_UpdateSlackChannelConfiguration_RequestSyntax) **   <a name="supportapp-UpdateSlackChannelConfiguration-request-channelName"></a>
The Slack channel name that you want to update.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `.+`
Required: No

 ** [channelRoleArn](#API_UpdateSlackChannelConfiguration_RequestSyntax) **   <a name="supportapp-UpdateSlackChannelConfiguration-request-channelRoleArn"></a>
The Amazon Resource Name (ARN) of an IAM role that you want to use to perform operations on AWS services. For more information, see [Managing access to the Support App](https://docs.aws.amazon.com/awssupport/latest/user/support-app-permissions.html) in the * AWS Support User Guide*.
Type: String
Length Constraints: Minimum length of 31. Maximum length of 2048.
Pattern: `arn:aws:iam::[0-9]{12}:role/(.+)`
Required: No

 ** [notifyOnAddCorrespondenceToCase](#API_UpdateSlackChannelConfiguration_RequestSyntax) **   <a name="supportapp-UpdateSlackChannelConfiguration-request-notifyOnAddCorrespondenceToCase"></a>
Whether you want to get notified when a support case has a new correspondence.
Type: Boolean
Required: No

 ** [notifyOnCaseSeverity](#API_UpdateSlackChannelConfiguration_RequestSyntax) **   <a name="supportapp-UpdateSlackChannelConfiguration-request-notifyOnCaseSeverity"></a>
The case severity for a support case that you want to receive notifications.
If you specify `high` or `all`, at least one of the following parameters must be `true`:
+  `notifyOnAddCorrespondenceToCase`
+  `notifyOnCreateOrReopenCase`
+  `notifyOnResolveCase`
If you specify `none`, any of the following parameters that you specify in your request must be `false`:
+  `notifyOnAddCorrespondenceToCase`
+  `notifyOnCreateOrReopenCase`
+  `notifyOnResolveCase`
If you don't specify these parameters in your request, the Support App uses the current values by default.
Type: String
Valid Values: `none | all | high`
Required: No

 ** [notifyOnCreateOrReopenCase](#API_UpdateSlackChannelConfiguration_RequestSyntax) **   <a name="supportapp-UpdateSlackChannelConfiguration-request-notifyOnCreateOrReopenCase"></a>
Whether you want to get notified when a support case is created or reopened.
Type: Boolean
Required: No

 ** [notifyOnResolveCase](#API_UpdateSlackChannelConfiguration_RequestSyntax) **   <a name="supportapp-UpdateSlackChannelConfiguration-request-notifyOnResolveCase"></a>
Whether you want to get notified when a support case is resolved.
Type: Boolean
Required: No

 ** [teamId](#API_UpdateSlackChannelConfiguration_RequestSyntax) **   <a name="supportapp-UpdateSlackChannelConfiguration-request-teamId"></a>
The team ID in Slack. This ID uniquely identifies a Slack workspace, such as `T012ABCDEFG`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `\S+`
Required: Yes

## Response Syntax
<a name="API_UpdateSlackChannelConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "channelId": "string",
   "channelName": "string",
   "channelRoleArn": "string",
   "notifyOnAddCorrespondenceToCase": boolean,
   "notifyOnCaseSeverity": "string",
   "notifyOnCreateOrReopenCase": boolean,
   "notifyOnResolveCase": boolean,
   "teamId": "string"
}
```

## Response Elements
<a name="API_UpdateSlackChannelConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [channelId](#API_UpdateSlackChannelConfiguration_ResponseSyntax) **   <a name="supportapp-UpdateSlackChannelConfiguration-response-channelId"></a>
The channel ID in Slack. This ID identifies a channel within a Slack workspace.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `\S+`

 ** [channelName](#API_UpdateSlackChannelConfiguration_ResponseSyntax) **   <a name="supportapp-UpdateSlackChannelConfiguration-response-channelName"></a>
The name of the Slack channel that you configure for the Support App.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `.+`

 ** [channelRoleArn](#API_UpdateSlackChannelConfiguration_ResponseSyntax) **   <a name="supportapp-UpdateSlackChannelConfiguration-response-channelRoleArn"></a>
The Amazon Resource Name (ARN) of an IAM role that you want to use to perform operations on AWS services. For more information, see [Managing access to the Support App](https://docs.aws.amazon.com/awssupport/latest/user/support-app-permissions.html) in the * AWS Support User Guide*.
Type: String
Length Constraints: Minimum length of 31. Maximum length of 2048.
Pattern: `arn:aws:iam::[0-9]{12}:role/(.+)`

 ** [notifyOnAddCorrespondenceToCase](#API_UpdateSlackChannelConfiguration_ResponseSyntax) **   <a name="supportapp-UpdateSlackChannelConfiguration-response-notifyOnAddCorrespondenceToCase"></a>
Whether you want to get notified when a support case has a new correspondence.
Type: Boolean

 ** [notifyOnCaseSeverity](#API_UpdateSlackChannelConfiguration_ResponseSyntax) **   <a name="supportapp-UpdateSlackChannelConfiguration-response-notifyOnCaseSeverity"></a>
The case severity for a support case that you want to receive notifications.
Type: String
Valid Values: `none | all | high`

 ** [notifyOnCreateOrReopenCase](#API_UpdateSlackChannelConfiguration_ResponseSyntax) **   <a name="supportapp-UpdateSlackChannelConfiguration-response-notifyOnCreateOrReopenCase"></a>
Whether you want to get notified when a support case is created or reopened.
Type: Boolean

 ** [notifyOnResolveCase](#API_UpdateSlackChannelConfiguration_ResponseSyntax) **   <a name="supportapp-UpdateSlackChannelConfiguration-response-notifyOnResolveCase"></a>
Whether you want to get notified when a support case is resolved.
Type: Boolean

 ** [teamId](#API_UpdateSlackChannelConfiguration_ResponseSyntax) **   <a name="supportapp-UpdateSlackChannelConfiguration-response-teamId"></a>
The team ID in Slack. This ID uniquely identifies a Slack workspace, such as `T012ABCDEFG`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `\S+`

## Errors
<a name="API_UpdateSlackChannelConfiguration_Errors"></a>

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

 ** ResourceNotFoundException **
The specified resource is missing or doesn't exist, such as an account alias, Slack channel configuration, or Slack workspace configuration.
HTTP Status Code: 404

 ** ValidationException **
Your request input doesn't meet the constraints that the Support App specifies.
HTTP Status Code: 400

## See Also
<a name="API_UpdateSlackChannelConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/support-app-2021-08-20/UpdateSlackChannelConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/support-app-2021-08-20/UpdateSlackChannelConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/support-app-2021-08-20/UpdateSlackChannelConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/support-app-2021-08-20/UpdateSlackChannelConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/support-app-2021-08-20/UpdateSlackChannelConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/support-app-2021-08-20/UpdateSlackChannelConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/support-app-2021-08-20/UpdateSlackChannelConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/support-app-2021-08-20/UpdateSlackChannelConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/support-app-2021-08-20/UpdateSlackChannelConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/support-app-2021-08-20/UpdateSlackChannelConfiguration)
