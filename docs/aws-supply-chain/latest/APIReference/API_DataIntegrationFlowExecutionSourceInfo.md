---
source_url: https://docs.aws.amazon.com/aws-supply-chain/latest/APIReference/API_DataIntegrationFlowExecutionSourceInfo.html
---

# DataIntegrationFlowExecutionSourceInfo
<a name="API_DataIntegrationFlowExecutionSourceInfo"></a>

The source information of a flow execution.

## Contents
<a name="API_DataIntegrationFlowExecutionSourceInfo_Contents"></a>

 ** sourceType **   <a name="supplychain-Type-DataIntegrationFlowExecutionSourceInfo-sourceType"></a>
The data integration flow execution source type.
Type: String
Valid Values: `S3 | DATASET`
Required: Yes

 ** datasetSource **   <a name="supplychain-Type-DataIntegrationFlowExecutionSourceInfo-datasetSource"></a>
The source details of a flow execution with dataset source.
Type: [DataIntegrationFlowDatasetSource](API_DataIntegrationFlowDatasetSource.md) object
Required: No

 ** s3Source **   <a name="supplychain-Type-DataIntegrationFlowExecutionSourceInfo-s3Source"></a>
The source details of a flow execution with S3 source.
Type: [DataIntegrationFlowS3Source](API_DataIntegrationFlowS3Source.md) object
Required: No

## See Also
<a name="API_DataIntegrationFlowExecutionSourceInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/supplychain-2024-01-01/DataIntegrationFlowExecutionSourceInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/supplychain-2024-01-01/DataIntegrationFlowExecutionSourceInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/supplychain-2024-01-01/DataIntegrationFlowExecutionSourceInfo)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Supply Chain. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-supply-chain` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
