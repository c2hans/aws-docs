---
source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_ConfigurationBundleRef.html
---

# ConfigurationBundleRef
<a name="API_ConfigurationBundleRef"></a>

A reference to a specific version of a configuration bundle.

## Contents
<a name="API_ConfigurationBundleRef_Contents"></a>

 ** bundleArn **   <a name="BedrockAgentCore-Type-ConfigurationBundleRef-bundleArn"></a>
The Amazon Resource Name (ARN) of the configuration bundle.
Type: String
Pattern: `arn:aws[a-zA-Z-]*:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:configuration-bundle/[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`
Required: Yes

 ** bundleVersion **   <a name="BedrockAgentCore-Type-ConfigurationBundleRef-bundleVersion"></a>
The version of the configuration bundle.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

## See Also
<a name="API_ConfigurationBundleRef_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/ConfigurationBundleRef)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/ConfigurationBundleRef)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/ConfigurationBundleRef)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock AgentCore Data Plane. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock-agentcore` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
