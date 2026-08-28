---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsAmazonMqBrokerEncryptionOptionsDetails.html
---

# AwsAmazonMqBrokerEncryptionOptionsDetails
<a name="API_AwsAmazonMqBrokerEncryptionOptionsDetails"></a>

 Provides details about broker encryption options.

## Contents
<a name="API_AwsAmazonMqBrokerEncryptionOptionsDetails_Contents"></a>

 ** KmsKeyId **   <a name="securityhub-Type-AwsAmazonMqBrokerEncryptionOptionsDetails-KmsKeyId"></a>
 The AWS KMS key that’s used to encrypt your data at rest. If not provided, Amazon MQ will use a default KMS key to encrypt your data.
Type: String
Pattern: `.*\S.*`
Required: No

 ** UseAwsOwnedKey **   <a name="securityhub-Type-AwsAmazonMqBrokerEncryptionOptionsDetails-UseAwsOwnedKey"></a>
 Specifies that an AWS KMS key should be used for at-rest encryption. Set to `true` by default if no value is provided (for example, for RabbitMQ brokers).
Type: Boolean
Required: No

## See Also
<a name="API_AwsAmazonMqBrokerEncryptionOptionsDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsAmazonMqBrokerEncryptionOptionsDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsAmazonMqBrokerEncryptionOptionsDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsAmazonMqBrokerEncryptionOptionsDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
