---
source_url: https://docs.aws.amazon.com/inspector/v1/APIReference/API_AgentPreview.html
---

# AgentPreview
<a name="API_AgentPreview"></a>

Used as a response element in the [PreviewAgents](API_PreviewAgents.md) action.

## Contents
<a name="API_AgentPreview_Contents"></a>

 ** agentId **   <a name="Inspector-Type-AgentPreview-agentId"></a>
The ID of the EC2 instance where the agent is installed.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** agentHealth **   <a name="Inspector-Type-AgentPreview-agentHealth"></a>
The health status of the Amazon Inspector Classic Agent.
Type: String
Valid Values: `HEALTHY | UNHEALTHY | UNKNOWN`
Required: No

 ** agentVersion **   <a name="Inspector-Type-AgentPreview-agentVersion"></a>
The version of the Amazon Inspector Classic Agent.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** autoScalingGroup **   <a name="Inspector-Type-AgentPreview-autoScalingGroup"></a>
The Auto Scaling group for the EC2 instance where the agent is installed.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** hostname **   <a name="Inspector-Type-AgentPreview-hostname"></a>
The hostname of the EC2 instance on which the Amazon Inspector Classic Agent is installed.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** ipv4Address **   <a name="Inspector-Type-AgentPreview-ipv4Address"></a>
The IP address of the EC2 instance on which the Amazon Inspector Classic Agent is installed.
Type: String
Length Constraints: Minimum length of 7. Maximum length of 15.
Required: No

 ** kernelVersion **   <a name="Inspector-Type-AgentPreview-kernelVersion"></a>
The kernel version of the operating system running on the EC2 instance on which the Amazon Inspector Classic Agent is installed.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** operatingSystem **   <a name="Inspector-Type-AgentPreview-operatingSystem"></a>
The operating system running on the EC2 instance on which the Amazon Inspector Classic Agent is installed.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## See Also
<a name="API_AgentPreview_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector-2016-02-16/AgentPreview)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector-2016-02-16/AgentPreview)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector-2016-02-16/AgentPreview)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Inspector Classic. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
