---
source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_DatasetDetails.html
---

# DatasetDetails

Identifies the dataset and the version of it that a batch evaluation ran.

## Contents
<a name="API_DatasetDetails_Contents"></a>

 ** datasetId **   <a name="BedrockAgentCore-Type-DatasetDetails-datasetId"></a>
The unique identifier of the dataset.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,110}`
Required: Yes

 ** datasetVersion **   <a name="BedrockAgentCore-Type-DatasetDetails-datasetVersion"></a>
The version of the dataset that the batch evaluation ran. If the request didn't specify a version, this is the latest published version when the batch evaluation started.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 19.
Pattern: `(DRAFT|[0-9]{1,19})`
Required: Yes

## See Also
<a name="API_DatasetDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/DatasetDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/DatasetDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/DatasetDetails)
