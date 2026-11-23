---
source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_DatasetSource.html
---

# DatasetSource

Identifies the dataset and the version of it to run.

## Contents
<a name="API_DatasetSource_Contents"></a>

 ** datasetId **   <a name="BedrockAgentCore-Type-DatasetSource-datasetId"></a>
The unique identifier of the dataset.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,110}`
Required: Yes

 ** datasetVersion **   <a name="BedrockAgentCore-Type-DatasetSource-datasetVersion"></a>
The number of a published version of the dataset. You can't run the `DRAFT` version. If you don't specify a version, the batch evaluation uses the latest published version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 19.
Pattern: `(DRAFT|[0-9]{1,19})`
Required: No

## See Also
<a name="API_DatasetSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/DatasetSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/DatasetSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/DatasetSource)
