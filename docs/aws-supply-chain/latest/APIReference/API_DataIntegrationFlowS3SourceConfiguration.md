---
source_url: https://docs.aws.amazon.com/aws-supply-chain/latest/APIReference/API_DataIntegrationFlowS3SourceConfiguration.html
---

# DataIntegrationFlowS3SourceConfiguration
<a name="API_DataIntegrationFlowS3SourceConfiguration"></a>

The S3 DataIntegrationFlow source configuration parameters.

## Contents
<a name="API_DataIntegrationFlowS3SourceConfiguration_Contents"></a>

 ** bucketName **   <a name="supplychain-Type-DataIntegrationFlowS3SourceConfiguration-bucketName"></a>
The bucketName of the S3 source objects.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `[a-z0-9][a-z0-9.-]*[a-z0-9]`
Required: Yes

 ** prefix **   <a name="supplychain-Type-DataIntegrationFlowS3SourceConfiguration-prefix"></a>
The prefix of the S3 source objects. To trigger data ingestion, S3 files need to be put under `s3://bucketName/prefix/`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 700.
Pattern: `[/A-Za-z0-9._-]+`
Required: Yes

 ** options **   <a name="supplychain-Type-DataIntegrationFlowS3SourceConfiguration-options"></a>
The other options of the S3 DataIntegrationFlow source.
Type: [DataIntegrationFlowS3Options](API_DataIntegrationFlowS3Options.md) object
Required: No

## See Also
<a name="API_DataIntegrationFlowS3SourceConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/supplychain-2024-01-01/DataIntegrationFlowS3SourceConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/supplychain-2024-01-01/DataIntegrationFlowS3SourceConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/supplychain-2024-01-01/DataIntegrationFlowS3SourceConfiguration)
