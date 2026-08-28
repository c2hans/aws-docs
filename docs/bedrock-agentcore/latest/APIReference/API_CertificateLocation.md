---
source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_CertificateLocation.html
---

# CertificateLocation
<a name="API_CertificateLocation"></a>

The location from which to retrieve a certificate.

## Contents
<a name="API_CertificateLocation_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** secretsManager **   <a name="BedrockAgentCore-Type-CertificateLocation-secretsManager"></a>
The AWS Secrets Manager location of the certificate.
Type: [SecretsManagerLocation](API_SecretsManagerLocation.md) object
Required: No

## See Also
<a name="API_CertificateLocation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/CertificateLocation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/CertificateLocation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/CertificateLocation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock AgentCore Data Plane. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock-agentcore` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
