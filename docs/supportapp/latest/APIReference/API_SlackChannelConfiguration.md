---
source_url: https://docs.aws.amazon.com/supportapp/latest/APIReference/API_SlackChannelConfiguration.html
---

# SlackChannelConfiguration
<a name="API_SlackChannelConfiguration"></a>

The configuration for a Slack channel that you added for your AWS account.

## Contents
<a name="API_SlackChannelConfiguration_Contents"></a>

 ** channelId **   <a name="supportapp-Type-SlackChannelConfiguration-channelId"></a>
The channel ID in Slack. This ID identifies a channel within a Slack workspace.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `\S+`
Required: Yes

 ** teamId **   <a name="supportapp-Type-SlackChannelConfiguration-teamId"></a>
The team ID in Slack. This ID uniquely identifies a Slack workspace, such as `T012ABCDEFG`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `\S+`
Required: Yes

 ** channelName **   <a name="supportapp-Type-SlackChannelConfiguration-channelName"></a>
The name of the Slack channel that you configured with the Support App for your AWS account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `.+`
Required: No

 ** channelRoleArn **   <a name="supportapp-Type-SlackChannelConfiguration-channelRoleArn"></a>
The Amazon Resource Name (ARN) of an IAM role that you want to use to perform operations on AWS services. For more information, see [Managing access to the Support App](https://docs.aws.amazon.com/awssupport/latest/user/support-app-permissions.html) in the * AWS Support User Guide*.
Type: String
Length Constraints: Minimum length of 31. Maximum length of 2048.
Pattern: `arn:aws:iam::[0-9]{12}:role/(.+)`
Required: No

 ** notifyOnAddCorrespondenceToCase **   <a name="supportapp-Type-SlackChannelConfiguration-notifyOnAddCorrespondenceToCase"></a>
Whether you want to get notified when a support case has a new correspondence.
Type: Boolean
Required: No

 ** notifyOnCaseSeverity **   <a name="supportapp-Type-SlackChannelConfiguration-notifyOnCaseSeverity"></a>
The case severity for a support case that you want to receive notifications.
Type: String
Valid Values: `none | all | high`
Required: No

 ** notifyOnCreateOrReopenCase **   <a name="supportapp-Type-SlackChannelConfiguration-notifyOnCreateOrReopenCase"></a>
Whether you want to get notified when a support case is created or reopened.
Type: Boolean
Required: No

 ** notifyOnResolveCase **   <a name="supportapp-Type-SlackChannelConfiguration-notifyOnResolveCase"></a>
Whether you want to get notified when a support case is resolved.
Type: Boolean
Required: No

## See Also
<a name="API_SlackChannelConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/support-app-2021-08-20/SlackChannelConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/support-app-2021-08-20/SlackChannelConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/support-app-2021-08-20/SlackChannelConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Support App in Slack. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query supportapp` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
