---
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_LicenseSpecification.html
---

# LicenseSpecification
<a name="API_LicenseSpecification"></a>

A license configuration to associate with the instances.

## Contents
<a name="API_LicenseSpecification_Contents"></a>

 ** licenseConfigurationArn **   <a name="bedrockagentcorecontrol-Type-LicenseSpecification-licenseConfigurationArn"></a>
The Amazon Resource Name (ARN) of the license configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws(-[^:]+)?:license-manager:[a-z0-9-]+:[0-9]{12}:license-configuration:[a-zA-Z0-9_-]+`
Required: Yes

## See Also
<a name="API_LicenseSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/LicenseSpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/LicenseSpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/LicenseSpecification)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock AgentCore Control Plane. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock-agentcore-control` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
