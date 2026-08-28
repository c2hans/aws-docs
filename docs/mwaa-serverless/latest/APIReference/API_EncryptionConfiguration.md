---
source_url: https://docs.aws.amazon.com/mwaa-serverless/latest/APIReference/API_EncryptionConfiguration.html
---

# EncryptionConfiguration
<a name="API_EncryptionConfiguration"></a>

Configuration for encrypting workflow data at rest and in transit. Amazon Managed Workflows for Apache Airflow Serverless provides comprehensive encryption capabilities to protect sensitive workflow data, parameters, and execution logs. When using customer-managed keys, the service integrates with AWS AWS KMS to provide fine-grained access control and audit capabilities. Encryption is applied consistently across the distributed execution environment including task containers, metadata storage, and log streams.

## Contents
<a name="API_EncryptionConfiguration_Contents"></a>

 ** Type **   <a name="mwaaserverless-Type-EncryptionConfiguration-Type"></a>
The type of encryption to use. Values are `AWS_MANAGED_KEY` (AWS manages the encryption key) or `CUSTOMER_MANAGED_KEY` (you provide a KMS key).
Type: String
Valid Values: `AWS_MANAGED_KEY | CUSTOMER_MANAGED_KEY`
Required: Yes

 ** KmsKeyId **   <a name="mwaaserverless-Type-EncryptionConfiguration-KmsKeyId"></a>
The ID or ARN of the AWS KMS key to use for encryption. Required when `Type` is `CUSTOMER_MANAGED_KEY`.
Type: String
Required: No

## See Also
<a name="API_EncryptionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mwaa-serverless-2024-07-26/EncryptionConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mwaa-serverless-2024-07-26/EncryptionConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mwaa-serverless-2024-07-26/EncryptionConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Workflows for Apache Airflow Serverless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mwaa-serverless` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
