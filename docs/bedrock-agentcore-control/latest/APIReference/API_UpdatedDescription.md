---
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_UpdatedDescription.html
---

# UpdatedDescription
<a name="API_UpdatedDescription"></a>

Wrapper for updating an optional Description field with PATCH semantics. When present in an update request, the description is replaced with optionalValue. When absent, the description is left unchanged. To unset the description, include the wrapper with optionalValue not specified.

## Contents
<a name="API_UpdatedDescription_Contents"></a>

 ** optionalValue **   <a name="bedrockagentcorecontrol-Type-UpdatedDescription-optionalValue"></a>
Represents an optional value that is used to update the human-readable description of the resource. If not specified, it will clear the current description of the resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

## See Also
<a name="API_UpdatedDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/UpdatedDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/UpdatedDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/UpdatedDescription)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock AgentCore Control Plane. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock-agentcore-control` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
