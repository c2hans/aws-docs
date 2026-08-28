---
source_url: https://docs.aws.amazon.com/comprehend/latest/APIReference/API_DataSecurityConfig.html
---

# DataSecurityConfig
<a name="API_DataSecurityConfig"></a>

Data security configuration.

## Contents
<a name="API_DataSecurityConfig_Contents"></a>

 ** DataLakeKmsKeyId **   <a name="comprehend-Type-DataSecurityConfig-DataLakeKmsKeyId"></a>
ID for the AWS KMS key that Amazon Comprehend uses to encrypt the data in the data lake.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `^\p{ASCII}+$`
Required: No

 ** ModelKmsKeyId **   <a name="comprehend-Type-DataSecurityConfig-ModelKmsKeyId"></a>
ID for the AWS KMS key that Amazon Comprehend uses to encrypt trained custom models. The ModelKmsKeyId can be either of the following formats:
+ KMS Key ID: `"1234abcd-12ab-34cd-56ef-1234567890ab"`
+ Amazon Resource Name (ARN) of a KMS Key: `"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"`
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `^\p{ASCII}+$`
Required: No

 ** VolumeKmsKeyId **   <a name="comprehend-Type-DataSecurityConfig-VolumeKmsKeyId"></a>
ID for the AWS KMS key that Amazon Comprehend uses to encrypt the volume.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `^\p{ASCII}+$`
Required: No

 ** VpcConfig **   <a name="comprehend-Type-DataSecurityConfig-VpcConfig"></a>
 Configuration parameters for an optional private Virtual Private Cloud (VPC) containing the resources you are using for the job. For more information, see [Amazon VPC](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html).
Type: [VpcConfig](API_VpcConfig.md) object
Required: No

## See Also
<a name="API_DataSecurityConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/comprehend-2017-11-27/DataSecurityConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/comprehend-2017-11-27/DataSecurityConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/comprehend-2017-11-27/DataSecurityConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Comprehend. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query comprehend` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
