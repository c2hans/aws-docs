---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_osis_EncryptionAtRestOptions.html
---

# EncryptionAtRestOptions
<a name="API_osis_EncryptionAtRestOptions"></a>

Options to control how OpenSearch encrypts buffer data.

## Contents
<a name="API_osis_EncryptionAtRestOptions_Contents"></a>

 ** KmsKeyArn **   <a name="opensearchservice-Type-osis_EncryptionAtRestOptions-KmsKeyArn"></a>
The ARN of the KMS key used to encrypt buffer data. By default, data is encrypted using an AWS owned key.
Type: String
Length Constraints: Minimum length of 7. Maximum length of 2048.
Required: Yes

## See Also
<a name="API_osis_EncryptionAtRestOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/osis-2022-01-01/EncryptionAtRestOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/osis-2022-01-01/EncryptionAtRestOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/osis-2022-01-01/EncryptionAtRestOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
