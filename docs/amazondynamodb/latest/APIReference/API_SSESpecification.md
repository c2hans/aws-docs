---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_SSESpecification.html
---

# SSESpecification
<a name="API_SSESpecification"></a>

Represents the settings used to enable server-side encryption.

## Contents
<a name="API_SSESpecification_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Enabled **   <a name="DDB-Type-SSESpecification-Enabled"></a>
Indicates whether server-side encryption is done using an AWS managed key or an AWS owned key. If enabled (true), server-side encryption type is set to `KMS` and an AWS managed key is used (AWS KMS charges apply). If disabled (false) or not specified, server-side encryption is set to AWS owned key.
Type: Boolean
Required: No

 ** KMSMasterKeyId **   <a name="DDB-Type-SSESpecification-KMSMasterKeyId"></a>
The AWS KMS key that should be used for the AWS KMS encryption. To specify a key, use its key ID, Amazon Resource Name (ARN), alias name, or alias ARN. Note that you should only provide this parameter if the key is different from the default DynamoDB key `alias/aws/dynamodb`.
Type: String
Required: No

 ** SSEType **   <a name="DDB-Type-SSESpecification-SSEType"></a>
Server-side encryption type. The only supported value is:
+  `KMS` - Server-side encryption that uses AWS Key Management Service. The key is stored in your account and is managed by AWS KMS (AWS KMS charges apply).
Type: String
Valid Values: `AES256 | KMS`
Required: No

## See Also
<a name="API_SSESpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/SSESpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/SSESpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/SSESpecification)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DynamoDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazondynamodb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
