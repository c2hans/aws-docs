---
source_url: https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/getting-started.html
---

# Using the AWS Encryption SDK with AWS KMS
<a name="getting-started"></a>

To use the AWS Encryption SDK, you need to configure [keyrings](concepts.md#keyring) or [master key providers](concepts.md#master-key-provider) with wrapping keys. If you don't have a key infrastructure, we recommend using [AWS Key Management Service (AWS KMS)](https://aws.amazon.com/kms/). Many of the code examples in the AWS Encryption SDK require an [AWS KMS key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#master_keys).

To interact with AWS KMS, the AWS Encryption SDK requires the AWS SDK for your preferred programming language. The AWS Encryption SDK client library works with the AWS SDKs to support master keys stored in AWS KMS.

**To prepare to use the AWS Encryption SDK with AWS KMS**

1. Create an AWS account. To learn how, see [How do I create and activate a new Amazon Web Services account?](https://aws.amazon.com/premiumsupport/knowledge-center/create-and-activate-aws-account/) in the AWS Knowledge Center.

1. Create a symmetric encryption AWS KMS key. For help, see [Creating Keys](https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html) in the *AWS Key Management Service Developer Guide*.
**Tip**
To use the AWS KMS key programmatically, you will need the key ID or Amazon Resource Name (ARN) of the AWS KMS key. For help finding the ID or ARN of an AWS KMS key, see [Finding the Key ID and ARN](https://docs.aws.amazon.com/kms/latest/developerguide/viewing-keys.html#find-cmk-id-arn) in the *AWS Key Management Service Developer Guide*.

1. Generate an access key ID and security access key. You can use either the access key ID and secret access key for an IAM user or you can use the AWS Security Token Service to create a new session with temporary security credentials that include an access key ID, secret access key, and session token. As a security best practice, we recommend that you use temporary credentials instead of the long-term credentials associated with your IAM user or AWS (root) user accounts.

   To create an IAM user with an access key, see [Creating IAM Users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html#id_users_create_console) in the *IAM User Guide*.

   To generate temporary security credentials, see [Requesting temporary security credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_request.html) in the *IAM User Guide*.

1. Set your AWS credentials using the instructions in the [AWS SDK for Java](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/setup-credentials.html), [AWS SDK for JavaScript](https://docs.aws.amazon.com/sdk-for-javascript/latest/developer-guide/setting-credentials.html), [AWS SDK for Python (Boto)](https://docs.aws.amazon.com/boto3/latest/#configuration) or [AWS SDK for C\+\+](https://docs.aws.amazon.com/sdk-for-cpp/latest/developer-guide/credentials.html) (for C), and the access key ID and secret access key that you generated in step 3. If you generated temporary credentials, you will also need to specify the session token.

   This procedure allows AWS SDKs to sign requests to AWS for you. Code samples in the AWS Encryption SDK that interact with AWS KMS assume that you have completed this step.

1. Download and install the AWS Encryption SDK. To learn how, see the installation instructions for the [programming language](programming-languages.md) that you want to use.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Encryption SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query encryption-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
