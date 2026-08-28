---
source_url: https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/c-language-installation.html
---

# Installing the AWS Encryption SDK for C
<a name="c-language-installation"></a>

Install the latest version of the AWS Encryption SDK for C.

**Note**
All versions of the AWS Encryption SDK for C earlier than 2.0.0 are in the [end-of-support phase](https://docs.aws.amazon.com/sdkref/latest/guide/maint-policy.html#version-life-cycle).
You can safely update from version 2.0.*x* and later to the latest version of the AWS Encryption SDK for C without any code or data changes. However, [ new security features](about-versions.md#version-2) introduced in version 2.0.*x* are not backward-compatible. To update from versions earlier than 1.7.*x* to version 2.0.*x* and later, you must first update to the latest 1.*x* version of the AWS Encryption SDK for C. For details, see [Migrating your AWS Encryption SDK](migration.md).

You can find detailed instructions for installing and building the AWS Encryption SDK for C in the [README file](https://github.com/aws/aws-encryption-sdk-c/#readme) of the [aws-encryption-sdk-c](https://github.com/aws/aws-encryption-sdk-c/) repository. It includes instructions for building on Amazon Linux, Ubuntu, macOS, and Windows platforms.

Before you begin, decide whether you want to use [AWS KMS keyrings](use-kms-keyring.md) in the AWS Encryption SDK. If you use an AWS KMS keyring, you need to install the AWS SDK for C\+\+. The AWS SDK is required to interact with [AWS Key Management Service](https://docs.aws.amazon.com/kms/latest/developerguide/) (AWS KMS). When you use AWS KMS keyrings, the AWS Encryption SDK uses AWS KMS to generate and protect the encryption keys that protect your data.

You do not need to install the AWS SDK for C\+\+ if you are using another keyring type, such as a raw AES keyring, a raw RSA keyring, or a multi-keyring that doesn't include an AWS KMS keyring. However, when using a raw keyring type, you need to generate and protect your own raw wrapping keys.

If you're having trouble with your installation, [file an issue](https://github.com/aws/aws-encryption-sdk-c/issues) in the `aws-encryption-sdk-c` repository or use any of the feedback links on this page.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Encryption SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query encryption-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
