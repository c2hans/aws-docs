---
source_url: https://docs.aws.amazon.com/aws-supply-chain/latest/APIReference/API_DataIntegrationFlowS3Source.html
---

# DataIntegrationFlowS3Source
<a name="API_DataIntegrationFlowS3Source"></a>

The details of a flow execution with S3 source.

## Contents
<a name="API_DataIntegrationFlowS3Source_Contents"></a>

 ** bucketName **   <a name="supplychain-Type-DataIntegrationFlowS3Source-bucketName"></a>
The S3 bucket name of the S3 source.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `[a-z0-9][a-z0-9.-]*[a-z0-9]`
Required: Yes

 ** key **   <a name="supplychain-Type-DataIntegrationFlowS3Source-key"></a>
The S3 object key of the S3 source.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[/A-Za-z0-9._:*()'!=?&+;@-]+`
Required: Yes

## See Also
<a name="API_DataIntegrationFlowS3Source_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/supplychain-2024-01-01/DataIntegrationFlowS3Source)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/supplychain-2024-01-01/DataIntegrationFlowS3Source)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/supplychain-2024-01-01/DataIntegrationFlowS3Source)
