---
source_url: https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/examples-crypto.html
---

The AWS SDK for Java 1.x reached end-of-support on December 31, 2025. We recommend that you migrate to the [AWS SDK for Java 2.x](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/home.html) to continue receiving new features, availability improvements, and security updates.

# Use Amazon S3 client-side encryption
<a name="examples-crypto"></a>

Encrypting data using the Amazon S3 encryption client is one way you can provide an additional layer of protection for sensitive information you store in Amazon S3. The examples in this section demonstrate how to create and configure the Amazon S3 encryption client for your application.

If you are new to cryptography, see the [Cryptography Basics](https://docs.aws.amazon.com/kms/latest/developerguide/crypto-intro.html) in the AWS KMS Developer Guide for a basic overview of cryptography terms and algorithms. For information about cryptography support across all AWS SDKs, see [AWS SDK Support for Amazon S3 Client-Side Encryption](http://docs.aws.amazon.com/general/latest/gr/aws_sdk_cryptography.html) in the Amazon Web Services General Reference.

**Note**
These code examples assume that you understand the material in [Using the AWS SDK for Java](basics.md) and have configured default AWS credentials using the information in [Set up AWS Credentials and Region for Development](setup-credentials.md).

If you are using version 1.11.836 or earlier of the AWS SDK for Java, see [Amazon S3 Encryption Client Migration](s3-encryption-migration.md) for information on migrating your applications to later versions. If you cannot migrate, see [this complete example](https://github.com/awsdocs/aws-doc-sdk-examples/blob/master/java/example_code/s3/src/main/java/aws/example/s3/S3Encrypt.java) on GitHub.

Otherwise, if you are using version 1.11.837 or later of the AWS SDK for Java, explore the example topics listed below to use Amazon S3 client-side encryption.

**Topics**
+ [Amazon S3 client-side encryption with client master keys](examples-crypto-masterkey.md)
+ [Amazon S3 client-side encryption with AWS KMS managed keys](examples-crypto-kms.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Java. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-java` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
