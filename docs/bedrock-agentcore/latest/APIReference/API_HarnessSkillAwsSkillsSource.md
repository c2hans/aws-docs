---
source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_HarnessSkillAwsSkillsSource.html
---

# HarnessSkillAwsSkillsSource
<a name="API_HarnessSkillAwsSkillsSource"></a>

Passed to show that AWS Skills should be included.

## Contents
<a name="API_HarnessSkillAwsSkillsSource_Contents"></a>

 ** paths **   <a name="BedrockAgentCore-Type-HarnessSkillAwsSkillsSource-paths"></a>
Optionally filter allowed skills with glob syntax, e.g., ['core-skills/\*'].
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `([^*?\[\]]|\*)+`
Required: No

## See Also
<a name="API_HarnessSkillAwsSkillsSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/HarnessSkillAwsSkillsSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/HarnessSkillAwsSkillsSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/HarnessSkillAwsSkillsSource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock AgentCore Data Plane. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock-agentcore` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
