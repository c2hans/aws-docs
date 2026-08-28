---
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_TargetTrafficSplitEntry.html
---

# TargetTrafficSplitEntry
<a name="API_TargetTrafficSplitEntry"></a>

An entry in a target traffic split configuration.

## Contents
<a name="API_TargetTrafficSplitEntry_Contents"></a>

 ** name **   <a name="bedrockagentcorecontrol-Type-TargetTrafficSplitEntry-name"></a>
The name of this traffic split variant.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9]([a-zA-Z0-9-]{0,62}[a-zA-Z0-9])?`
Required: Yes

 ** targetName **   <a name="bedrockagentcorecontrol-Type-TargetTrafficSplitEntry-targetName"></a>
The name of the target to route traffic to.
Type: String
Pattern: `([0-9a-zA-Z][-]?){1,100}`
Required: Yes

 ** weight **   <a name="bedrockagentcorecontrol-Type-TargetTrafficSplitEntry-weight"></a>
The percentage of traffic to route to this variant.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 99.
Required: Yes

 ** description **   <a name="bedrockagentcorecontrol-Type-TargetTrafficSplitEntry-description"></a>
The description of this traffic split variant.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Required: No

 ** metadata **   <a name="bedrockagentcorecontrol-Type-TargetTrafficSplitEntry-metadata"></a>
Key-value metadata associated with this traffic split variant.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 25 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## See Also
<a name="API_TargetTrafficSplitEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/TargetTrafficSplitEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/TargetTrafficSplitEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/TargetTrafficSplitEntry)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock AgentCore Control Plane. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock-agentcore-control` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
