---
source_url: https://docs.aws.amazon.com/ground-station/latest/APIReference/API_AgentDetails.html
---

# AgentDetails
<a name="API_AgentDetails"></a>

Detailed information about the agent.

## Contents
<a name="API_AgentDetails_Contents"></a>

 ** agentVersion **   <a name="groundstation-Type-AgentDetails-agentVersion"></a>
Current agent version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `(0|[1-9]\d*)(\.(0|[1-9]\d*))*`
Required: Yes

 ** componentVersions **   <a name="groundstation-Type-AgentDetails-componentVersions"></a>
List of versions being used by agent components.
Type: Array of [ComponentVersion](API_ComponentVersion.md) objects
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Required: Yes

 ** instanceId **   <a name="groundstation-Type-AgentDetails-instanceId"></a>
ID of EC2 instance agent is running on.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 64.
Pattern: `[a-z0-9-]{10,64}`
Required: Yes

 ** instanceType **   <a name="groundstation-Type-AgentDetails-instanceType"></a>
Type of EC2 instance agent is running on.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-z0-9.-]{1,64}`
Required: Yes

 ** agentCpuCores **   <a name="groundstation-Type-AgentDetails-agentCpuCores"></a>
List of CPU cores reserved for the agent.
Type: Array of integers
Array Members: Minimum number of 0 items. Maximum number of 256 items.
Required: No

 ** reservedCpuCores **   <a name="groundstation-Type-AgentDetails-reservedCpuCores"></a>
This field should not be used. Use agentCpuCores instead.
List of CPU cores reserved for processes other than the agent running on the EC2 instance.
Type: Array of integers
Array Members: Minimum number of 0 items. Maximum number of 256 items.
Required: No

## See Also
<a name="API_AgentDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/groundstation-2019-05-23/AgentDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/groundstation-2019-05-23/AgentDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/groundstation-2019-05-23/AgentDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Ground Station. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ground-station` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
