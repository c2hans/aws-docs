---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_SlackBidirectionalConfiguration.html
---

# SlackBidirectionalConfiguration
<a name="API_SlackBidirectionalConfiguration"></a>

Configuration for bidirectional Slack communication.

## Contents
<a name="API_SlackBidirectionalConfiguration_Contents"></a>

 ** roleArn **   <a name="devopsagent-Type-SlackBidirectionalConfiguration-roleArn"></a>
IAM role ARN that AWS DevOps Agent assumes to exchange messages with your Slack workspace on behalf of this association.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `arn:(aws|aws-cn|aws-us-gov):iam::\d{12}:role/[a-zA-Z0-9+=,.@_/-]+`
Required: Yes

 ** enabled **   <a name="devopsagent-Type-SlackBidirectionalConfiguration-enabled"></a>
Whether bidirectional communication is enabled for this association. When you set this value to true, you can mention the agent in a configured Slack channel and it responds in that channel. When you omit this value or set it to false, the agent ignores mentions and only sends notifications.
Type: Boolean
Required: No

## See Also
<a name="API_SlackBidirectionalConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/SlackBidirectionalConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/SlackBidirectionalConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/SlackBidirectionalConfiguration)
