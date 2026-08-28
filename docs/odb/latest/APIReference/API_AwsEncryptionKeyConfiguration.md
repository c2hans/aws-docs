---
source_url: https://docs.aws.amazon.com/odb/latest/APIReference/API_AwsEncryptionKeyConfiguration.html
---

# AwsEncryptionKeyConfiguration
<a name="API_AwsEncryptionKeyConfiguration"></a>

The configuration of the AWS Key Management Service (KMS) encryption key used for an Autonomous Database.

## Contents
<a name="API_AwsEncryptionKeyConfiguration_Contents"></a>

 ** externalIdType **   <a name="odb-Type-AwsEncryptionKeyConfiguration-externalIdType"></a>
The type of external identifier associated with the encryption key.
Type: String
Valid Values: `database_ocid | compartment_ocid | tenant_ocid`
Required: No

 ** iamRoleArn **   <a name="odb-Type-AwsEncryptionKeyConfiguration-iamRoleArn"></a>
The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that grants access to the KMS key.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:(?:aws|aws-cn|aws-us-gov|aws-iso-{0,1}[a-z]{0,1}):iam::[0-9]{12}:role/.+`
Required: No

 ** kmsKeyId **   <a name="odb-Type-AwsEncryptionKeyConfiguration-kmsKeyId"></a>
The identifier or ARN of the AWS KMS key used for encryption.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[a-zA-Z0-9_:./-]+`
Required: No

## See Also
<a name="API_AwsEncryptionKeyConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/odb-2024-08-20/AwsEncryptionKeyConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/odb-2024-08-20/AwsEncryptionKeyConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/odb-2024-08-20/AwsEncryptionKeyConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Oracle Database@AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query odb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
