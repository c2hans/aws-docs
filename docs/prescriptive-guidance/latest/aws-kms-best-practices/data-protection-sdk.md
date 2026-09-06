---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-kms-best-practices/data-protection-sdk.html
---

# Recommendations for using the AWS Encryption SDK
<a name="data-protection-sdk"></a>

The [AWS Encryption SDK](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/introduction.html) is a powerful tool for implementing client-side encryption in your applications. Libraries are available for Java, JavaScript, C, Python, and other programming languages. It integrates with AWS Key Management Service (AWS KMS). You can also use it as a stand-alone SDK without referencing KMS keys.

Recommended practices for using this tool include carefully considering the requirements of your application. Balance those requirements against risks that can be introduced by certain configurations, such as introducing key caching into your application. For more information about data key caching, see [Data key caching](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/data-key-caching.html) in the AWS Encryption SDK documentation.

Consider the following questions when determining whether to use the AWS Encryption SDK:
+ Is there a requirement for client-side encryption that cannot be met by server-side encryption with services that integrate with AWS KMS?
+ Can you adequately protect the keys that are used to encrypt data client-side, and how will you do that?
+ Are there other, fit-for-purpose encryption libraries that might fit your use case more appropriately? Consider alternative AWS offerings, such as [Amazon S3 client-side encryption](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingClientSideEncryption.html) and the [AWS Database Encryption SDK](https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/what-is-database-encryption-sdk.html).

Find more information about choosing the right service for your use case, see the [AWS Crypto Tools Documentation](https://docs.aws.amazon.com/aws-crypto-tools/).
