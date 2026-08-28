---
source_url: https://docs.aws.amazon.com/healthlake/latest/APIReference/API_KmsEncryptionConfig.html
---

# KmsEncryptionConfig
<a name="API_KmsEncryptionConfig"></a>

The customer-managed-key (CMK) used when creating a data store. If a customer-owned key is not specified, an AWS-owned key is used for encryption.

## Contents
<a name="API_KmsEncryptionConfig_Contents"></a>

 ** CmkType **   <a name="HealthLake-Type-KmsEncryptionConfig-CmkType"></a>
The type of customer-managed-key (CMK) used for encryption.
Type: String
Valid Values: `CUSTOMER_MANAGED_KMS_KEY | AWS_OWNED_KMS_KEY`
Required: Yes

 ** KmsKeyId **   <a name="HealthLake-Type-KmsEncryptionConfig-KmsKeyId"></a>
The Key Management Service (AWS KMS) encryption key id/alias used to encrypt the data store contents at rest.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 400.
Pattern: `(arn:aws((-us-gov)|(-iso)|(-iso-b)|(-cn))?:kms:)?([a-z]{2}-[a-z]+(-[a-z]+)?-\d:)?(\d{12}:)?(((key/)?[a-zA-Z0-9-_]+)|(alias/[a-zA-Z0-9:/_-]+))`
Required: No

## See Also
<a name="API_KmsEncryptionConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/healthlake-2017-07-01/KmsEncryptionConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/healthlake-2017-07-01/KmsEncryptionConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/healthlake-2017-07-01/KmsEncryptionConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS HealthLake. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query healthlake` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
