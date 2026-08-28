---
source_url: https://docs.aws.amazon.com/cloudwatchinvestigations/latest/APIReference/API_EncryptionConfiguration.html
---

# EncryptionConfiguration
<a name="API_EncryptionConfiguration"></a>

Use this structure to specify a customer managed AWS KMS key to use to encrypt investigation data.

## Contents
<a name="API_EncryptionConfiguration_Contents"></a>

 ** kmsKeyId **   <a name="cloudwatchinvestigations-Type-EncryptionConfiguration-kmsKeyId"></a>
If the investigation group uses a customer managed key for encryption, this field displays the ID of that key.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `arn:.*`
Required: No

 ** type **   <a name="cloudwatchinvestigations-Type-EncryptionConfiguration-type"></a>
Displays whether investigation data is encrypted by a customer managed key or an AWS owned key.
Type: String
Valid Values: `AWS_OWNED_KEY | CUSTOMER_MANAGED_KMS_KEY`
Required: No

## See Also
<a name="API_EncryptionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/aiops-2018-05-10/EncryptionConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/aiops-2018-05-10/EncryptionConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/aiops-2018-05-10/EncryptionConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for CloudWatch investigations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudwatchinvestigations` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
