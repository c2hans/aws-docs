---
source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_SecretsManagerLocation.html
---

# SecretsManagerLocation
<a name="API_SecretsManagerLocation"></a>

The AWS Secrets Manager location configuration.

## Contents
<a name="API_SecretsManagerLocation_Contents"></a>

 ** secretArn **   <a name="BedrockAgentCore-Type-SecretsManagerLocation-secretArn"></a>
The ARN of the AWS Secrets Manager secret containing the certificate.
Type: String
Pattern: `arn:aws(-[a-z-]+)?:secretsmanager:[a-z0-9-]+:[0-9]{12}:secret:[a-zA-Z0-9/_+=.@-]+`
Required: Yes

## See Also
<a name="API_SecretsManagerLocation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/SecretsManagerLocation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/SecretsManagerLocation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/SecretsManagerLocation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock AgentCore Data Plane. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock-agentcore` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
