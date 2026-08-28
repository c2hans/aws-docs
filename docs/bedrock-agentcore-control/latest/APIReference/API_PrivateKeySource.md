---
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_PrivateKeySource.html
---

# PrivateKeySource
<a name="API_PrivateKeySource"></a>

Contains the private key source configuration for a JWT client assertion.

## Contents
<a name="API_PrivateKeySource_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** kmsKeySource **   <a name="bedrockagentcorecontrol-Type-PrivateKeySource-kmsKeySource"></a>
The AWS KMS key source for the JWT client assertion.
Type: [KmsKeySourceType](API_KmsKeySourceType.md) object
Required: No

## See Also
<a name="API_PrivateKeySource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/PrivateKeySource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/PrivateKeySource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/PrivateKeySource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock AgentCore Control Plane. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock-agentcore-control` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
