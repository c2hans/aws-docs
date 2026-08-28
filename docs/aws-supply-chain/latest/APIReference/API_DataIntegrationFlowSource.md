---
source_url: https://docs.aws.amazon.com/aws-supply-chain/latest/APIReference/API_DataIntegrationFlowSource.html
---

# DataIntegrationFlowSource
<a name="API_DataIntegrationFlowSource"></a>

The DataIntegrationFlow source parameters.

## Contents
<a name="API_DataIntegrationFlowSource_Contents"></a>

 ** sourceName **   <a name="supplychain-Type-DataIntegrationFlowSource-sourceName"></a>
The DataIntegrationFlow source name that can be used as table alias in SQL transformation query.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9_]+`
Required: Yes

 ** sourceType **   <a name="supplychain-Type-DataIntegrationFlowSource-sourceType"></a>
The DataIntegrationFlow source type.
Type: String
Valid Values: `S3 | DATASET`
Required: Yes

 ** datasetSource **   <a name="supplychain-Type-DataIntegrationFlowSource-datasetSource"></a>
The dataset DataIntegrationFlow source.
Type: [DataIntegrationFlowDatasetSourceConfiguration](API_DataIntegrationFlowDatasetSourceConfiguration.md) object
Required: No

 ** s3Source **   <a name="supplychain-Type-DataIntegrationFlowSource-s3Source"></a>
The S3 DataIntegrationFlow source.
Type: [DataIntegrationFlowS3SourceConfiguration](API_DataIntegrationFlowS3SourceConfiguration.md) object
Required: No

## See Also
<a name="API_DataIntegrationFlowSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/supplychain-2024-01-01/DataIntegrationFlowSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/supplychain-2024-01-01/DataIntegrationFlowSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/supplychain-2024-01-01/DataIntegrationFlowSource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Supply Chain. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-supply-chain` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
