---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_CapabilityBaseRequestConfig.html
---

# CapabilityBaseRequestConfig
<a name="API_CapabilityBaseRequestConfig"></a>

The base configuration for registering a capability. Contains capability-specific configuration such as AI settings.

## Contents
<a name="API_CapabilityBaseRequestConfig_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** aiConfig **   <a name="opensearchservice-Type-CapabilityBaseRequestConfig-aiConfig"></a>
Configuration settings for AI-powered capabilities.
Type: [AIConfig](API_AIConfig.md) object
Required: No

## See Also
<a name="API_CapabilityBaseRequestConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/CapabilityBaseRequestConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/CapabilityBaseRequestConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/CapabilityBaseRequestConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
