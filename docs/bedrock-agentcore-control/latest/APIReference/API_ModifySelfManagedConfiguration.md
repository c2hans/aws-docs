---
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_ModifySelfManagedConfiguration.html
---

# ModifySelfManagedConfiguration
<a name="API_ModifySelfManagedConfiguration"></a>

The configuration for updating the self-managed memory strategy.

## Contents
<a name="API_ModifySelfManagedConfiguration_Contents"></a>

 ** historicalContextWindowSize **   <a name="bedrockagentcorecontrol-Type-ModifySelfManagedConfiguration-historicalContextWindowSize"></a>
The updated number of historical messages to include in processing context.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 50.
Required: No

 ** invocationConfiguration **   <a name="bedrockagentcorecontrol-Type-ModifySelfManagedConfiguration-invocationConfiguration"></a>
The updated configuration to invoke self-managed memory processing pipeline.
Type: [ModifyInvocationConfigurationInput](API_ModifyInvocationConfigurationInput.md) object
Required: No

 ** triggerConditions **   <a name="bedrockagentcorecontrol-Type-ModifySelfManagedConfiguration-triggerConditions"></a>
The updated list of conditions that trigger memory processing.
Type: Array of [TriggerConditionInput](API_TriggerConditionInput.md) objects
Array Members: Minimum number of 1 item.
Required: No

## See Also
<a name="API_ModifySelfManagedConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/ModifySelfManagedConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/ModifySelfManagedConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/ModifySelfManagedConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock AgentCore Control Plane. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock-agentcore-control` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
