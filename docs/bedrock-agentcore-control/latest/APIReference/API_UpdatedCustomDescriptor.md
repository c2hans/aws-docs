---
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_UpdatedCustomDescriptor.html
---

# UpdatedCustomDescriptor
<a name="API_UpdatedCustomDescriptor"></a>

Wrapper for updating a custom descriptor with PATCH semantics. When present, the custom descriptor is replaced with the provided value. When absent, the custom descriptor is left unchanged. To unset, include the wrapper with the value set to null.

## Contents
<a name="API_UpdatedCustomDescriptor_Contents"></a>

 ** optionalValue **   <a name="bedrockagentcorecontrol-Type-UpdatedCustomDescriptor-optionalValue"></a>
The updated custom descriptor value.
Type: [CustomDescriptor](API_CustomDescriptor.md) object
Required: No

## See Also
<a name="API_UpdatedCustomDescriptor_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/UpdatedCustomDescriptor)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/UpdatedCustomDescriptor)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/UpdatedCustomDescriptor)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock AgentCore Control Plane. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock-agentcore-control` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
