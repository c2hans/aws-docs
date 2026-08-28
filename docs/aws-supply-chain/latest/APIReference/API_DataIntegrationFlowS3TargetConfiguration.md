---
source_url: https://docs.aws.amazon.com/aws-supply-chain/latest/APIReference/API_DataIntegrationFlowS3TargetConfiguration.html
---

# DataIntegrationFlowS3TargetConfiguration
<a name="API_DataIntegrationFlowS3TargetConfiguration"></a>

The S3 DataIntegrationFlow target configuration parameters.

## Contents
<a name="API_DataIntegrationFlowS3TargetConfiguration_Contents"></a>

 ** bucketName **   <a name="supplychain-Type-DataIntegrationFlowS3TargetConfiguration-bucketName"></a>
The bucketName of the S3 target objects.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `[a-z0-9][a-z0-9.-]*[a-z0-9]`
Required: Yes

 ** prefix **   <a name="supplychain-Type-DataIntegrationFlowS3TargetConfiguration-prefix"></a>
The prefix of the S3 target objects.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 700.
Pattern: `[/A-Za-z0-9._-]+`
Required: Yes

 ** options **   <a name="supplychain-Type-DataIntegrationFlowS3TargetConfiguration-options"></a>
The S3 DataIntegrationFlow target options.
Type: [DataIntegrationFlowS3Options](API_DataIntegrationFlowS3Options.md) object
Required: No

## See Also
<a name="API_DataIntegrationFlowS3TargetConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/supplychain-2024-01-01/DataIntegrationFlowS3TargetConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/supplychain-2024-01-01/DataIntegrationFlowS3TargetConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/supplychain-2024-01-01/DataIntegrationFlowS3TargetConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Supply Chain. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-supply-chain` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
