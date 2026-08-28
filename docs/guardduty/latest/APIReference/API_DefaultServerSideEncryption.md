---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_DefaultServerSideEncryption.html
---

# DefaultServerSideEncryption
<a name="API_DefaultServerSideEncryption"></a>

Contains information on the server side encryption method used in the S3 bucket. See [S3 Server-Side Encryption](https://docs.aws.amazon.com/AmazonS3/latest/dev/serv-side-encryption.html) for more information.

## Contents
<a name="API_DefaultServerSideEncryption_Contents"></a>

 ** encryptionType **   <a name="guardduty-Type-DefaultServerSideEncryption-encryptionType"></a>
The type of encryption used for objects within the S3 bucket.
Type: String
Required: No

 ** kmsMasterKeyArn **   <a name="guardduty-Type-DefaultServerSideEncryption-kmsMasterKeyArn"></a>
The Amazon Resource Name (ARN) of the KMS encryption key. Only available if the bucket `EncryptionType` is `aws:kms`.
Type: String
Required: No

## See Also
<a name="API_DefaultServerSideEncryption_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/DefaultServerSideEncryption)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/DefaultServerSideEncryption)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/DefaultServerSideEncryption)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GuardDuty. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guardduty` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
