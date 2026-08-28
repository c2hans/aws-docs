---
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_NamespaceKeyEntry.html
---

# NamespaceKeyEntry
<a name="API_NamespaceKeyEntry"></a>

A namespace variable key definition with optional `NamespaceKeyValidation` rules.

## Contents
<a name="API_NamespaceKeyEntry_Contents"></a>

 ** key **   <a name="bedrockagentcorecontrol-Type-NamespaceKeyEntry-key"></a>
The namespace variable key name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `(?!memoryStrategyId$|actorId$|sessionId$)[a-z][a-z0-9]*`
Required: Yes

 ** validation **   <a name="bedrockagentcorecontrol-Type-NamespaceKeyEntry-validation"></a>
The validation rules that constrain values for this namespace variable at runtime (`CreateEvent` API).
Type: [NamespaceKeyValidation](API_NamespaceKeyValidation.md) object
Required: No

## See Also
<a name="API_NamespaceKeyEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/NamespaceKeyEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/NamespaceKeyEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/NamespaceKeyEntry)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock AgentCore Control Plane. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock-agentcore-control` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
