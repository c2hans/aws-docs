---
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_UpdatedDescriptors.html
---

# UpdatedDescriptors
<a name="API_UpdatedDescriptors"></a>

Wrapper for updating an optional descriptors field with PATCH semantics. When present with a value, individual descriptors can be updated. When present with a null value, all descriptors are unset. When absent, descriptors are left unchanged.

## Contents
<a name="API_UpdatedDescriptors_Contents"></a>

 ** optionalValue **   <a name="bedrockagentcorecontrol-Type-UpdatedDescriptors-optionalValue"></a>
The updated descriptors value. Contains per-descriptor-type wrappers that are each independently updatable.
Type: [UpdatedDescriptorsUnion](API_UpdatedDescriptorsUnion.md) object
Required: No

## See Also
<a name="API_UpdatedDescriptors_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/UpdatedDescriptors)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/UpdatedDescriptors)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/UpdatedDescriptors)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock AgentCore Control Plane. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock-agentcore-control` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
