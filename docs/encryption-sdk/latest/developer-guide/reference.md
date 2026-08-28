---
source_url: https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/reference.html
---

# AWS Encryption SDK reference
<a name="reference"></a>

|  |
| --- |
| The information on this page is a reference for building your own encryption library that is compatible with the AWS Encryption SDK. If you are not building your own compatible encryption library, you likely do not need this information.<br />To use the AWS Encryption SDK in one of the supported programming languages, see [Programming languages](programming-languages.md).<br />For the specification that defines the elements of a proper AWS Encryption SDK implementation, see the [AWS Encryption SDK Specification](https://github.com/awslabs/aws-encryption-sdk-specification/) in GitHub. |

The AWS Encryption SDK uses the [supported algorithms](supported-algorithms.md) to return a single data structure or *message* that contains encrypted data and the corresponding encrypted data keys. The following topics explain the algorithms and the data structure. Use this information to build libraries that can read and write ciphertexts that are compatible with this SDK.

**Topics**
+ [Message format reference](message-format.md)
+ [Message format examples](message-format-examples.md)
+ [Body AAD reference](body-aad-reference.md)
+ [Algorithms reference](algorithms-reference.md)
+ [Initialization vector reference](IV-reference.md)
+ [AWS KMS Hierarchical keyring technical details](hierarchical-keyring-details.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Encryption SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query encryption-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
