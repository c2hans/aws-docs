---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsElasticsearchDomainEncryptionAtRestOptions.html
---

# AwsElasticsearchDomainEncryptionAtRestOptions
<a name="API_AwsElasticsearchDomainEncryptionAtRestOptions"></a>

Details about the configuration for encryption at rest.

## Contents
<a name="API_AwsElasticsearchDomainEncryptionAtRestOptions_Contents"></a>

 ** Enabled **   <a name="securityhub-Type-AwsElasticsearchDomainEncryptionAtRestOptions-Enabled"></a>
Whether encryption at rest is enabled.
Type: Boolean
Required: No

 ** KmsKeyId **   <a name="securityhub-Type-AwsElasticsearchDomainEncryptionAtRestOptions-KmsKeyId"></a>
The AWS KMS key ID. Takes the form `1a2a3a4-1a2a-3a4a-5a6a-1a2a3a4a5a6a`.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsElasticsearchDomainEncryptionAtRestOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsElasticsearchDomainEncryptionAtRestOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsElasticsearchDomainEncryptionAtRestOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsElasticsearchDomainEncryptionAtRestOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
