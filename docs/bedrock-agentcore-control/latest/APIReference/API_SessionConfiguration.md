---
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_SessionConfiguration.html
---

# SessionConfiguration
<a name="API_SessionConfiguration"></a>

The session configuration for an MCP gateway. This structure defines settings that control session behavior.

## Contents
<a name="API_SessionConfiguration_Contents"></a>

 ** sessionTimeoutInSeconds **   <a name="bedrockagentcorecontrol-Type-SessionConfiguration-sessionTimeoutInSeconds"></a>
The session timeout in seconds. After this timeout, the session expires and subsequent requests to this session will receive an error. The minimum value is 900 seconds (15 minutes), the maximum value is 28800 seconds (8 hours), and the default value is 3600 seconds (1 hour).
Type: Integer
Valid Range: Minimum value of 900. Maximum value of 28800.
Required: No

## See Also
<a name="API_SessionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/SessionConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/SessionConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/SessionConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock AgentCore Control Plane. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock-agentcore-control` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
