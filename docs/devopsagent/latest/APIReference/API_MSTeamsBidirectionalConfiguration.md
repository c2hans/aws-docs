---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_MSTeamsBidirectionalConfiguration.html
---

# MSTeamsBidirectionalConfiguration
<a name="API_MSTeamsBidirectionalConfiguration"></a>

Configuration for bidirectional communication with a Microsoft Teams channel. When enabled, the agent receives and responds to mentions in the configured channel in addition to sending notifications.

## Contents
<a name="API_MSTeamsBidirectionalConfiguration_Contents"></a>

 ** roleArn **   <a name="devopsagent-Type-MSTeamsBidirectionalConfiguration-roleArn"></a>
The Amazon Resource Name (ARN) of the IAM role that the agent assumes to exchange messages with the Microsoft Teams team for this association.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `arn:(aws|aws-cn|aws-us-gov):iam::\d{12}:role/[a-zA-Z0-9+=,.@_/-]+`
Required: Yes

 ** enabled **   <a name="devopsagent-Type-MSTeamsBidirectionalConfiguration-enabled"></a>
Specifies whether bidirectional communication is enabled for this association. If you set this value to `true`, you can mention the agent in the configured Microsoft Teams channel and it responds in that channel. If you omit this parameter or set it to `false`, the agent only sends one-way notifications.
Type: Boolean
Required: No

## See Also
<a name="API_MSTeamsBidirectionalConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/MSTeamsBidirectionalConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/MSTeamsBidirectionalConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/MSTeamsBidirectionalConfiguration)
