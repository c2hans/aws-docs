---
source_url: https://docs.aws.amazon.com/data-exchange/latest/apireference/API_KmsKeyToGrant.html
---

# KmsKeyToGrant
<a name="API_KmsKeyToGrant"></a>

The Amazon Resource Name (ARN) of the AWS KMS key used to encrypt the shared S3 objects.

## Contents
<a name="API_KmsKeyToGrant_Contents"></a>

 ** KmsKeyArn **   <a name="dataexchange-Type-KmsKeyToGrant-KmsKeyArn"></a>
The AWS KMS CMK (Key Management System Customer Managed Key) used to encrypt S3 objects in the shared S3 Bucket. AWS Data exchange will create a KMS grant for each subscriber to allow them to access and decrypt their entitled data that is encrypted using this KMS key specified.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

## See Also
<a name="API_KmsKeyToGrant_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dataexchange-2017-07-25/KmsKeyToGrant)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dataexchange-2017-07-25/KmsKeyToGrant)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dataexchange-2017-07-25/KmsKeyToGrant)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Data Exchange. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query data-exchange` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
