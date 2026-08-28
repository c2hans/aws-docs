---
source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_ProxyCredentials.html
---

# ProxyCredentials
<a name="API_ProxyCredentials"></a>

Union type representing different proxy authentication methods. Currently supports HTTP Basic Authentication (username and password).

## Contents
<a name="API_ProxyCredentials_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** basicAuth **   <a name="BedrockAgentCore-Type-ProxyCredentials-basicAuth"></a>
HTTP Basic Authentication credentials (username and password) stored in AWS Secrets Manager.
Type: [BasicAuth](API_BasicAuth.md) object
Required: No

## See Also
<a name="API_ProxyCredentials_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/ProxyCredentials)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/ProxyCredentials)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/ProxyCredentials)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock AgentCore Data Plane. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock-agentcore` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
