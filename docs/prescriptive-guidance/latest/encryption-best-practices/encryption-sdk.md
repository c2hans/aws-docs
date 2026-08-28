---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/encryption-best-practices/encryption-sdk.html
---

# AWS Encryption SDK
<a name="encryption-sdk"></a>

The [AWS Encryption SDK](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/introduction.html) is an open-source, client-side encryption library. It uses industry standards and best practices to support implementation and interoperability in several [programming languages](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/programming-languages.html). AWS Encryption SDK encrypts data by using a secure, authenticated, symmetric key algorithm and offers default implementation that adheres to cryptography best practices. For more information, see [Supported algorithm suites in the AWS Encryption SDK](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/supported-algorithms.html).

One of the key features of the AWS Encryption SDK is support for encrypting data in use. By adopting an encrypt-then-use approach, you can encrypt sensitive data before it is processed by your application logic. This can help protect the data from potential exposure or tampering, even if the application itself is affected by a security event.

Consider the following best practices for this service:
+ Adhere to all of the recommendations in [Best practices for the AWS Encryption SDK](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/best-practices.html).
+ Select one or more wrapping keys to help protect your data keys. For more information, see [Select wrapping keys](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/configure.html#config-keys).
+ Pass the `KeyId`** **parameter to the [ReEncrypt](https://docs.aws.amazon.com/cli/latest/reference/kms/re-encrypt.html) operation to help prevent use of an untrusted KMS key. For more information, see [Improved client-side encryption: Explicit KeyIds and key commitment](https://aws.amazon.com/blogs/security/improved-client-side-encryption-explicit-keyids-and-key-commitment/) (AWS blog post).
+ When using the AWS Encryption SDK with AWS KMS, use local `KeyId` filtering. For more information, see [Improved client-side encryption: Explicit KeyIds and key commitment](https://aws.amazon.com/blogs/security/improved-client-side-encryption-explicit-keyids-and-key-commitment/) (AWS blog post).
+ For applications with large volumes of traffic requiring encryption or decryption, or if your account is exceeding AWS KMS [request quotas](https://docs.aws.amazon.com/kms/latest/developerguide/requests-per-second.html), you can use the [data key caching](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/data-key-caching.html) feature of the AWS Encryption SDK. Note the following best practices for data key caching:
  + Configure [cache security thresholds](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/thresholds.html) to limit how long each cached data key is used and how much data is protected under each data key. For recommendations when configuring these thresholds, see [Setting cache security thresholds](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/thresholds.html).
  + Limit the local cache to the smallest number of data keys necessary to achieve the performance improvements for your specific application use case. For instructions and an example of configuring limits for the local cache, see [Using data key caching: Step-by-step](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/implement-caching.html).

  For more information, see [AWS Encryption SDK: How to Decide if Data Key Caching Is Right for Your Application](https://aws.amazon.com/blogs/security/aws-encryption-sdk-how-to-decide-if-data-key-caching-is-right-for-your-application/) (AWS blog post).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
