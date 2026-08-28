---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_CapabilityExtendedResponseConfig.html
---

# CapabilityExtendedResponseConfig
<a name="API_CapabilityExtendedResponseConfig"></a>

The extended configuration returned for a registered capability, including additional details beyond the base configuration.

## Contents
<a name="API_CapabilityExtendedResponseConfig_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** aiConfig **   <a name="opensearchservice-Type-CapabilityExtendedResponseConfig-aiConfig"></a>
Configuration settings for AI-powered capabilities.
Type: [AIConfig](API_AIConfig.md) object
Required: No

## See Also
<a name="API_CapabilityExtendedResponseConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/CapabilityExtendedResponseConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/CapabilityExtendedResponseConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/CapabilityExtendedResponseConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
