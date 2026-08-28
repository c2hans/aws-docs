---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_MetadataConfigurationForReranking.html
---

# MetadataConfigurationForReranking
<a name="API_agent_MetadataConfigurationForReranking"></a>

Specifies how metadata fields should be handled during the reranking process.

## Contents
<a name="API_agent_MetadataConfigurationForReranking_Contents"></a>

 ** selectionMode **   <a name="bedrock-Type-agent_MetadataConfigurationForReranking-selectionMode"></a>
The mode for selecting metadata fields for reranking.
Type: String
Valid Values: `SELECTIVE | ALL`
Required: Yes

 ** selectiveModeConfiguration **   <a name="bedrock-Type-agent_MetadataConfigurationForReranking-selectiveModeConfiguration"></a>
The configuration for selective metadata field inclusion or exclusion during reranking.
Type: [RerankingMetadataSelectiveModeConfiguration](API_agent_RerankingMetadataSelectiveModeConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## See Also
<a name="API_agent_MetadataConfigurationForReranking_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/MetadataConfigurationForReranking)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/MetadataConfigurationForReranking)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/MetadataConfigurationForReranking)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
