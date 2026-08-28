---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_RedshiftProvisionedConfiguration.html
---

# RedshiftProvisionedConfiguration
<a name="API_agent_RedshiftProvisionedConfiguration"></a>

Contains configurations for a provisioned Amazon Redshift query engine.

## Contents
<a name="API_agent_RedshiftProvisionedConfiguration_Contents"></a>

 ** authConfiguration **   <a name="bedrock-Type-agent_RedshiftProvisionedConfiguration-authConfiguration"></a>
Specifies configurations for authentication to Amazon Redshift.
Type: [RedshiftProvisionedAuthConfiguration](API_agent_RedshiftProvisionedAuthConfiguration.md) object
Required: Yes

 ** clusterIdentifier **   <a name="bedrock-Type-agent_RedshiftProvisionedConfiguration-clusterIdentifier"></a>
The ID of the Amazon Redshift cluster.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Required: Yes

## See Also
<a name="API_agent_RedshiftProvisionedConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/RedshiftProvisionedConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/RedshiftProvisionedConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/RedshiftProvisionedConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
